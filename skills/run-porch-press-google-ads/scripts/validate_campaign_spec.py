#!/usr/bin/env python3
"""Validate the failure-prone invariants in a Porch Press Google Ads spec."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


REQUIRED_GATES = (
    "authority_current",
    "billing_ready",
    "hard_budget_verified",
    "no_overlap",
    "purchase_deduplicated",
    "purchase_value_verified",
    "destination_verified",
    "cart_checkout_verified",
    "targeting_verified",
    "ads_policy_eligible",
    "tracking_verified",
    "draft_receipt_captured",
)

ALLOWED_BIDDING = {
    "MANUAL_CPC",
    "MAXIMIZE_CONVERSIONS",
    "MAXIMIZE_CONVERSION_VALUE",
}


def weighted_length(value: str) -> int:
    """Approximate Google text length: full-width characters count as two."""
    return sum(2 if unicodedata.east_asian_width(char) in {"W", "F"} else 1 for char in value)


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def valid_porch_press_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and (parsed.hostname or "").lower() in {
        "porchpress.store",
        "www.porchpress.store",
    }


def parse_date(value: Any) -> dt.date | None:
    if not isinstance(value, str):
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def get_mapping(parent: dict[str, Any], key: str, errors: list[str]) -> dict[str, Any]:
    value = parent.get(key)
    if not isinstance(value, dict):
        errors.append(f"{key}: must be an object")
        return {}
    return value


def validate(spec: dict[str, Any], mode: str) -> tuple[list[str], list[str], dict[str, Any]]:
    errors: list[str] = []
    warnings: list[str] = []

    task_id = spec.get("task_id")
    if not isinstance(task_id, str) or not re.fullmatch(r"PP-GOOGLE-[A-Z0-9-]+", task_id):
        errors.append("task_id: use a stable ID beginning PP-GOOGLE- with uppercase letters/digits/hyphens")

    product = get_mapping(spec, "product", errors)
    authority = get_mapping(spec, "authority", errors)
    campaign = get_mapping(spec, "campaign", errors)
    measurement = get_mapping(spec, "measurement", errors)
    tracking = get_mapping(spec, "tracking", errors)
    gates = get_mapping(spec, "gates", errors)

    product_name = product.get("name")
    if not isinstance(product_name, str) or not product_name.strip():
        errors.append("product.name: required")

    price = product.get("price")
    if not is_number(price) or price <= 0:
        errors.append("product.price: must be a positive number")

    product_currency = product.get("currency")
    if product_currency != "USD":
        errors.append("product.currency: Porch Press U.S. campaign must use USD")

    product_url = product.get("final_url")
    if not valid_porch_press_url(product_url):
        errors.append("product.final_url: must be an HTTPS porchpress.store URL")

    authority_status = authority.get("status")
    if mode == "launch" and authority_status != "APPROVED":
        errors.append("authority.status: launch mode requires APPROVED")
    elif mode == "stage" and authority_status not in {"APPROVED", "DRAFT_ONLY"}:
        errors.append("authority.status: stage mode requires APPROVED or DRAFT_ONLY")

    maximum_spend = authority.get("maximum_total_spend")
    if not is_number(maximum_spend) or maximum_spend <= 0:
        errors.append("authority.maximum_total_spend: must be a positive number")

    if authority.get("currency") != product_currency:
        errors.append("authority.currency: must match product.currency")

    source = authority.get("source")
    if not isinstance(source, str) or not source.strip():
        errors.append("authority.source: cite the exact PM approval or draft-only instruction")

    if campaign.get("name") != task_id:
        errors.append("campaign.name: must equal task_id for stable reconciliation")
    if campaign.get("type") != "SEARCH":
        errors.append("campaign.type: must be SEARCH")

    desired_status = campaign.get("desired_status")
    expected_status = "PAUSED" if mode == "stage" else "ENABLED"
    if desired_status != expected_status:
        errors.append(f"campaign.desired_status: {mode} mode requires {expected_status}")

    if campaign.get("search_partners") is not False:
        errors.append("campaign.search_partners: initial controlled test requires false")
    if campaign.get("display_network") is not False:
        errors.append("campaign.display_network: Search test requires false")
    if campaign.get("location") != "United States":
        errors.append("campaign.location: must be United States")
    if campaign.get("location_option") != "PRESENCE":
        errors.append("campaign.location_option: must be PRESENCE, not presence-or-interest")

    languages = campaign.get("languages")
    if not isinstance(languages, list) or "English" not in languages:
        errors.append("campaign.languages: must include English")

    if campaign.get("stop_on_purchase") not in {False, None, 0}:
        errors.append("campaign.stop_on_purchase: purchase-count stopping is not authorized")

    budget_type = campaign.get("budget_type")
    budget = campaign.get("budget")
    if not is_number(budget) or budget <= 0:
        errors.append("campaign.budget: must be a positive number")
    elif is_number(maximum_spend) and budget > maximum_spend:
        errors.append("campaign.budget: exceeds authority.maximum_total_spend")

    start = parse_date(campaign.get("start_date"))
    end = parse_date(campaign.get("end_date"))
    if start is None or end is None:
        errors.append("campaign.start_date/end_date: use valid ISO dates YYYY-MM-DD")
    elif end <= start:
        errors.append("campaign.end_date: must be after start_date")

    if budget_type == "CAMPAIGN_TOTAL":
        if start and end:
            flight_days = (end - start).days
            if not 3 <= flight_days <= 90:
                errors.append("campaign dates: campaign-total Search flight must span 3 to 90 days")
    elif budget_type == "AVERAGE_DAILY":
        warnings.append("AVERAGE_DAILY can bill up to 2x the average on a day and is not a hard test-total cap")
        if mode == "launch" and authority.get("allow_average_daily_budget") is not True:
            errors.append("authority.allow_average_daily_budget: explicit true required to launch without a campaign total budget")
    else:
        errors.append("campaign.budget_type: use CAMPAIGN_TOTAL or AVERAGE_DAILY")

    bidding = campaign.get("bidding")
    if bidding not in ALLOWED_BIDDING:
        errors.append("campaign.bidding: use MANUAL_CPC, MAXIMIZE_CONVERSIONS, or MAXIMIZE_CONVERSION_VALUE")

    if measurement.get("purchase_primary") is not True:
        errors.append("measurement.purchase_primary: exactly one Purchase action must be primary")
    if measurement.get("additional_primary_purchase_actions") != 0:
        errors.append("measurement.additional_primary_purchase_actions: must be 0")
    if not isinstance(measurement.get("purchase_action_name"), str) or not measurement.get("purchase_action_name", "").strip():
        errors.append("measurement.purchase_action_name: required")
    for key in ("dynamic_value", "dynamic_currency", "transaction_id"):
        if measurement.get(key) is not True:
            errors.append(f"measurement.{key}: must be true")
    for key in ("add_to_cart_primary", "begin_checkout_primary"):
        if measurement.get(key) is not False:
            errors.append(f"measurement.{key}: must be false; the action may be secondary or absent")

    if tracking.get("auto_tagging") is not True:
        errors.append("tracking.auto_tagging: must be true unless the measurement design documents an approved exception")
    utm_campaign = tracking.get("utm_campaign")
    if not isinstance(utm_campaign, str) or not utm_campaign.strip():
        errors.append("tracking.utm_campaign: required")
    suffix = tracking.get("final_url_suffix")
    if not isinstance(suffix, str):
        errors.append("tracking.final_url_suffix: required")
    else:
        for token in ("utm_source=google", "utm_medium=cpc", "utm_campaign="):
            if token not in suffix:
                errors.append(f"tracking.final_url_suffix: missing {token}")

    negatives = spec.get("campaign_negative_keywords")
    if not isinstance(negatives, list) or not any(isinstance(item, str) and item.strip() for item in negatives):
        errors.append("campaign_negative_keywords: include a reviewed non-empty list")

    ad_groups = spec.get("ad_groups")
    keyword_count = 0
    if not isinstance(ad_groups, list) or not ad_groups:
        errors.append("ad_groups: include at least one ad group")
        ad_groups = []

    for group_index, group in enumerate(ad_groups):
        prefix = f"ad_groups[{group_index}]"
        if not isinstance(group, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        if not isinstance(group.get("name"), str) or not group.get("name", "").strip():
            errors.append(f"{prefix}.name: required")
        group_url = group.get("final_url")
        if not valid_porch_press_url(group_url):
            errors.append(f"{prefix}.final_url: must be an HTTPS porchpress.store URL")
        elif isinstance(product_url, str) and group_url.rstrip("/") != product_url.rstrip("/"):
            errors.append(f"{prefix}.final_url: must match product.final_url for this one-product test")

        keywords = group.get("keywords")
        if not isinstance(keywords, list) or not keywords:
            errors.append(f"{prefix}.keywords: include at least one keyword")
            keywords = []
        seen_keywords: set[tuple[str, str]] = set()
        for keyword_index, keyword in enumerate(keywords):
            key_prefix = f"{prefix}.keywords[{keyword_index}]"
            if not isinstance(keyword, dict):
                errors.append(f"{key_prefix}: must be an object")
                continue
            text = keyword.get("text")
            match = keyword.get("match")
            if not isinstance(text, str) or not text.strip():
                errors.append(f"{key_prefix}.text: required")
                continue
            keyword_count += 1
            identity = (text.strip().lower(), str(match))
            if identity in seen_keywords:
                errors.append(f"{key_prefix}: duplicate keyword and match type")
            seen_keywords.add(identity)
            if match not in {"EXACT", "PHRASE", "BROAD"}:
                errors.append(f"{key_prefix}.match: use EXACT, PHRASE, or BROAD")
            if match == "BROAD" and not (
                campaign.get("allow_broad_match") is True
                and authority.get("broad_match_approved") is True
            ):
                errors.append(f"{key_prefix}: BROAD requires both campaign and authority approval flags")

        rsa = group.get("rsa")
        if not isinstance(rsa, dict):
            errors.append(f"{prefix}.rsa: required object")
            continue
        headlines = rsa.get("headlines")
        descriptions = rsa.get("descriptions")
        if not isinstance(headlines, list) or not 3 <= len(headlines) <= 15:
            errors.append(f"{prefix}.rsa.headlines: provide 3 to 15 headlines")
            headlines = []
        if not isinstance(descriptions, list) or not 2 <= len(descriptions) <= 4:
            errors.append(f"{prefix}.rsa.descriptions: provide 2 to 4 descriptions")
            descriptions = []

        for asset_index, headline in enumerate(headlines):
            if not isinstance(headline, str) or not headline.strip():
                errors.append(f"{prefix}.rsa.headlines[{asset_index}]: must be non-empty text")
            elif weighted_length(headline) > 30:
                errors.append(f"{prefix}.rsa.headlines[{asset_index}]: exceeds 30 characters")
        if len({item.strip().lower() for item in headlines if isinstance(item, str)}) != len(headlines):
            errors.append(f"{prefix}.rsa.headlines: duplicate assets")

        for asset_index, description in enumerate(descriptions):
            if not isinstance(description, str) or not description.strip():
                errors.append(f"{prefix}.rsa.descriptions[{asset_index}]: must be non-empty text")
            elif weighted_length(description) > 90:
                errors.append(f"{prefix}.rsa.descriptions[{asset_index}]: exceeds 90 characters")

        for path_key in ("path1", "path2"):
            path_value = rsa.get(path_key, "")
            if not isinstance(path_value, str) or weighted_length(path_value) > 15:
                errors.append(f"{prefix}.rsa.{path_key}: must be text of 15 characters or fewer")

        pin_index = rsa.get("description_1_pin_index")
        if not isinstance(pin_index, int) or isinstance(pin_index, bool) or not 0 <= pin_index < len(descriptions):
            errors.append(f"{prefix}.rsa.description_1_pin_index: must identify a valid description")
        else:
            disclosure = descriptions[pin_index].lower()
            if "fiction" not in disclosure:
                errors.append(f"{prefix}.rsa pinned Description 1: must disclose fictional status")
            if not ("digital" in disclosure or "printable" in disclosure):
                errors.append(f"{prefix}.rsa pinned Description 1: must disclose digital/printable format")
            if not ("nothing ships" in disclosure or "no physical" in disclosure):
                errors.append(f"{prefix}.rsa pinned Description 1: must state the physical-shipping boundary")
            if is_number(price):
                amount = f"{float(price):.2f}"
                if amount not in disclosure:
                    errors.append(f"{prefix}.rsa pinned Description 1: must contain current price {amount}")

    missing_gates = [name for name in REQUIRED_GATES if gates.get(name) is not True]
    if mode == "launch" and missing_gates:
        errors.append("gates: launch requires true for " + ", ".join(missing_gates))
    elif mode == "stage" and missing_gates:
        warnings.append("stage remains non-launchable; open gates: " + ", ".join(missing_gates))

    summary = {
        "task_id": task_id,
        "mode": mode,
        "campaign": campaign.get("name"),
        "budget_type": budget_type,
        "budget": budget,
        "authority_maximum": maximum_spend,
        "ad_groups": len(ad_groups),
        "keywords": keyword_count,
        "open_gates": missing_gates,
    }
    return errors, warnings, summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, help="Path to campaign specification JSON")
    parser.add_argument("--mode", choices=("stage", "launch"), default="stage")
    args = parser.parse_args()

    try:
        raw = args.spec.read_text(encoding="utf-8")
        data = json.loads(raw)
    except OSError as exc:
        print(json.dumps({"valid": False, "errors": [f"cannot read spec: {exc}"]}, indent=2))
        return 1
    except json.JSONDecodeError as exc:
        print(json.dumps({"valid": False, "errors": [f"invalid JSON: {exc}"]}, indent=2))
        return 1

    if not isinstance(data, dict):
        print(json.dumps({"valid": False, "errors": ["root: must be a JSON object"]}, indent=2))
        return 1

    errors, warnings, summary = validate(data, args.mode)
    result = {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "summary": summary,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

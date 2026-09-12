# Google Ads measurement, budget, and launch QA

Use this reference before staging, launching, or diagnosing a Porch Press Google campaign.

## 1. Protect the spending envelope

Prefer a **campaign total budget** for a fixed Search flight when the live account offers it. Google states that campaign total budgets are available for Search campaigns with start/end dates, cannot be billed above the entered total, and support Search flights from 3 to 90 days. Record the actual UI control, entered amount, currency, start/end dates, account timezone, and zero-spend draft state.

Do not treat an average daily budget as a hard daily or test cap. Google states that most campaigns can spend up to twice the average daily budget on a given day, while the monthly limit is generally 30.4 times that average. If the authorized amount is a strict total and campaign total budget is unavailable, return **HOLD — NO ENFORCEABLE TOTAL BUDGET** unless PM explicitly accepts the documented daily-budget behavior.

Budget changes can alter pacing and limits. Do not raise, replenish, extend, duplicate, or move a budget based on a platform recommendation. Reconcile served cost, billed cost, credits, taxes/fees where applicable, and all overlapping campaigns against the same authority.

## 2. Make Purchase the sole biddable truth

Google distinguishes primary conversion actions, which can be used for bidding and appear in the Conversions column, from secondary actions, which are observation-only unless placed in certain custom goals.

For a Porch Press sales campaign:

- exactly one verified **Purchase** action is primary for the campaign;
- add to cart and begin checkout are secondary if configured, and never primary for this campaign;
- page view, session, engaged visit, newsletter signup, and clicks are not campaign conversion goals;
- if Shopify's Google & YouTube app, a direct Google tag, and a GA4 import all produce purchase actions, choose one authoritative primary action and make duplicate sources secondary or exclude them from the campaign goal;
- inspect custom goals: a secondary action included in a custom goal can still affect bidding;
- use transaction-specific value and currency;
- pass a stable order/transaction ID and confirm deduplication;
- do not use a test purchase as a business result.

The official Google & YouTube app on Shopify can configure conversion tracking, but installation or a “tag detected” label is not proof that values, currency, transaction IDs, and deduplication work.

### Evidence ladder

1. Tag/configuration exists.
2. Google diagnostics see the tag/event.
3. A controlled non-production or separately authorized test produces one Purchase event with expected value, currency, and transaction ID.
4. Google records one conversion, not duplicates.
5. A real Google-attributed purchase reconciles to a completed, paid, non-test Shopify order.

Launch requires evidence appropriate to the account's supported test path. Do not place a real order or payment merely to satisfy the gate unless PM separately authorizes it.

## 3. Lock traffic controls

Verify immediately before activation:

- campaign type is Search;
- Google Search is enabled;
- Search partners are disabled for the initial controlled test;
- Display expansion is disabled;
- no Performance Max or other campaign overlaps the same product/query budget;
- U.S. location option is **Presence: people in or regularly in the targeted location**, not the default presence-or-interest setting;
- language is English;
- keywords and negatives match the approved file exactly;
- broad match, automatically created assets, final-URL expansion, Dynamic Search Ads, and material auto-applied recommendations are off unless specifically approved;
- ad rotation/serving and bid strategy match the recorded live controls;
- start/end dates and timezone are correct.

Google's defaults and labels change. Capture screenshots or exported settings rather than relying on memory.

## 4. Verify ads and destination

For each enabled ad:

- character limits and policy eligibility pass;
- the pinned Description 1 accurately states fictional, printable/digital, current price, and shipping/delivery boundary;
- every possible asset combination is grammatical and does not invent urgency, reviews, popularity, playtime, difficulty, awards, or guarantees;
- final/display domains match Porch Press;
- final URL is public, crawlable, mobile-safe, and not a preview URL;
- title, price, product, and CTA match the destination;
- Google AdsBot is not blocked by robots, authentication, geo behavior, or a transient theme preview;
- the selected product/variant is available;
- cart and checkout entry work without creating a transaction;
- UTM/ValueTrack parameters and auto-tagging survive the full route.

## 5. Validate the specification

The bundled validator checks the most failure-prone invariants; it does not replace live UI evidence.

Run while staging:

`python3 scripts/validate_campaign_spec.py campaign-spec.json --mode stage`

Run again after refreshing every gate and immediately before activation:

`python3 scripts/validate_campaign_spec.py campaign-spec.json --mode launch`

The JSON should follow this shape:

```json
{
  "task_id": "PP-GOOGLE-SEARCH-001",
  "product": {
    "name": "Current verified title",
    "price": 19.99,
    "currency": "USD",
    "final_url": "https://porchpress.store/pages/current-product"
  },
  "authority": {
    "status": "APPROVED",
    "maximum_total_spend": 15.00,
    "currency": "USD",
    "source": "PM approval URL or exact dated instruction",
    "allow_average_daily_budget": false,
    "broad_match_approved": false
  },
  "campaign": {
    "name": "PP-GOOGLE-SEARCH-001",
    "type": "SEARCH",
    "desired_status": "ENABLED",
    "search_partners": false,
    "display_network": false,
    "location": "United States",
    "location_option": "PRESENCE",
    "languages": ["English"],
    "budget_type": "CAMPAIGN_TOTAL",
    "budget": 15.00,
    "start_date": "2026-09-12",
    "end_date": "2026-09-15",
    "bidding": "MANUAL_CPC",
    "allow_broad_match": false,
    "stop_on_purchase": false
  },
  "measurement": {
    "purchase_action_name": "Purchase",
    "purchase_primary": true,
    "additional_primary_purchase_actions": 0,
    "dynamic_value": true,
    "dynamic_currency": true,
    "transaction_id": true,
    "add_to_cart_primary": false,
    "begin_checkout_primary": false
  },
  "tracking": {
    "auto_tagging": true,
    "utm_campaign": "pp_google_search_001",
    "final_url_suffix": "utm_source=google&utm_medium=cpc&utm_campaign=pp_google_search_001&utm_content={adgroupid}&utm_term={keyword}"
  },
  "campaign_negative_keywords": ["free", "template", "answer key"],
  "ad_groups": [
    {
      "name": "Printable Mystery",
      "keywords": [
        {"text": "printable mystery game", "match": "EXACT"},
        {"text": "downloadable mystery game", "match": "PHRASE"}
      ],
      "final_url": "https://porchpress.store/pages/current-product",
      "rsa": {
        "headlines": [
          "Printable Mystery Case",
          "Solve a Family Secret",
          "$19.99 Digital Mystery"
        ],
        "descriptions": [
          "Fictional printable case files. Digital download. $19.99. Nothing ships.",
          "Examine the records, make your case, then open the sealed solution."
        ],
        "description_1_pin_index": 0,
        "path1": "printable",
        "path2": "mystery"
      }
    }
  ],
  "gates": {
    "authority_current": true,
    "billing_ready": true,
    "hard_budget_verified": true,
    "no_overlap": true,
    "purchase_deduplicated": true,
    "purchase_value_verified": true,
    "destination_verified": true,
    "cart_checkout_verified": true,
    "targeting_verified": true,
    "ads_policy_eligible": true,
    "tracking_verified": true,
    "draft_receipt_captured": true
  }
}
```

Replace every example value with current evidence. An example is not authorization or a ready-to-import campaign.

## 6. Required live receipt

Record:

- Google Ads customer/account reference, timezone, and currency;
- billing and advertiser-verification state;
- authority source and exact total-spend arithmetic;
- budget type, amount, dates, and current served/billed spend;
- campaign/ad-group/ad IDs and states;
- conversion-action identifiers, primary/secondary roles, source, counting setting, value/currency, and transaction-ID evidence;
- networks, geo option, language, bid strategy, keywords/match types, negatives, and automation settings;
- RSA assets, pins, policy state, and preview evidence;
- final URLs, tracking suffix, auto-tagging, mobile/desktop destination, cart, variant, price, and checkout evidence;
- activation timestamp and first delivery evidence, or exact HOLD reason.

An ACK, draft ID, eligible label, tag detection, or preview is not an activation/delivery receipt.

## Official references

Verified against current official documentation on September 12, 2026; recheck before execution:

- [Campaign total budgets for Search and other formats](https://support.google.com/google-ads/answer/15137812)
- [Google Ads spending limits](https://support.google.com/google-ads/answer/10486637)
- [How budget changes take effect](https://support.google.com/google-ads/answer/10487143)
- [Primary and secondary conversion actions](https://support.google.com/google-ads/answer/11461796)
- [Conversion goals and campaign-specific goals](https://support.google.com/google-ads/answer/10995103)
- [Google Ads API conversion-goal model](https://developers.google.com/google-ads/api/docs/conversions/goals/overview)
- [Shopify Google & YouTube conversion tracking](https://support.google.com/merchants/answer/13494537)
- [Advanced location options](https://support.google.com/google-ads/answer/1722038)
- [Google Search Network and partners](https://support.google.com/google-ads/answer/1722047)
- [Maximize conversions bidding](https://support.google.com/google-ads/answer/7381968)
- [Choose a bid strategy](https://support.google.com/google-ads/answer/2472725)

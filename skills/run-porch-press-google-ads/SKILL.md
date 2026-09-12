---
name: run-porch-press-google-ads
description: Design, stage, launch, audit, and analyze tightly capped Google Search campaigns for Porch Press printable mysteries. Use for Google Ads demand research, keyword and negative-keyword selection, responsive search ad copy, conversion and budget QA, launch gates, or post-launch diagnosis; do not use for SEO, Meta/Bing ads, or spending without explicit authority.
---

# Run Porch Press Google Ads

Build Google Ads experiments that answer whether active search demand can produce paid Porch Press orders. Optimize for verified purchases, not traffic volume, platform recommendations, or attractive click metrics.

Search captures existing intent; it does not create it. Before recommending spend, establish that relevant queries exist and that plausible click costs can fit the economics of the current product.

## Preserve authority and ownership

- PM is the account owner and sole source of spending authority. Loading this skill authorizes research and preparation, not launch or spend.
- Owner_Bot authors and approves product claims, ad copy, and the commercial interpretation. A Google Ads operator or Grok may implement the approved specification but may not improvise claims, keywords, destinations, budgets, or strategy.
- Use the existing Porch Press GitHub repository and active issue for assignments and receipts. Do not make PM relay prompts or create a new agent team.
- Recover current approvals instead of asking PM to repeat them. Later explicit PM instructions supersede older plans or comments.
- Never change Shopify price, product copy, theme, fulfillment, checkout, payment settings, or the live homepage as an incidental part of an ad build.
- Never add a purchase-count stop trigger unless PM explicitly requests one. Purchases are outcomes and reconciliation checkpoints. The hard end conditions are the authorized budget, fixed campaign end, or a measurement, policy, destination, overlap, or spend-control defect.

## Select the operating mode

Use only the resources needed for the current request:

- **Research or plan:** read [references/search-build-playbook.md](references/search-build-playbook.md).
- **Stage or launch:** read both the search playbook and [references/measurement-budget-qa.md](references/measurement-budget-qa.md).
- **Audit or diagnose:** read the measurement reference first, then the diagnostic section of the search playbook.

Creating copy or a plan does not authorize account mutations. Staging must remain paused and spend $0 unless the current authorization explicitly includes launch.

## Recover the live state

Before designing or changing a campaign:

1. Read the current Porch Press handoff, relevant campaign plan, latest GitHub issue receipts, and capital ledger.
2. Inspect the actual Google Ads account through an authorized interface. Record the account timezone and currency, billing readiness, active/paused campaigns, budgets, conversion goals, policy notices, auto-applied recommendations, and any campaign capable of overlapping the proposed search traffic.
3. Inspect the live Shopify product and destination. Record title, price, currency, availability, exact included contents, digital-delivery language, product/variant, final URL, cart result, and checkout entry. Do not place an order or payment without separate authority.
4. Separate verified facts, assumptions, decisions, and unresolved gaps. Do not carry an old price, screenshot, forecast, conversion status, or budget balance forward as current evidence.

## Pass the economic gate

Calculate before choosing a bid strategy:

`maximum affordable CPA = net contribution margin per incremental order`

`break-even CPC = maximum affordable CPA × observed paid-search purchase rate`

Use actual fees, refunds, and variable costs when available. Do not use gross price as contribution margin without labeling that simplification. If Porch Press lacks an observed paid-search purchase rate, show scenario arithmetic—such as 1%, 2%, and 5%—as sensitivity analysis, not as a forecast.

Obtain current U.S. search-volume and bid estimates from Keyword Planner for the exact seed set, date, language, and location. If relevant search demand is absent, forecast volume is too thin for a meaningful test, or plausible CPC materially exceeds the affordable range, return **HOLD — SEARCH ECONOMICS NOT SUPPORTED**. Recommend an organic or demand-creation channel rather than buying irrelevant queries.

## Use the tiny-test campaign defaults

These defaults protect interpretability and the small Porch Press capital pool. Deviate only when evidence and explicit authority support the deviation.

| Control | Default |
| --- | --- |
| Campaign type | Standard Google Search |
| Inventory | Google Search only |
| Search partners | Off initially |
| Display expansion | Off |
| Other campaign types | No Performance Max, Demand Gen, Display, Dynamic Search Ads, Shopping, or YouTube |
| Geography | United States; presence or regular presence, not location interest |
| Language | English |
| Destination | One current product-specific Porch Press landing page |
| Keywords | Small exact- and phrase-match set drawn from demonstrated purchase intent |
| Broad match | Off unless separately justified and approved after usable purchase/query evidence |
| Conversion used for bidding | Exactly one deduplicated Purchase action with dynamic value and currency |
| Diagnostic conversions | Begin checkout and add to cart must be secondary/observation-only if configured |
| Budget | Campaign total budget with fixed dates when available; never exceed the explicit authority |
| Purchase stop | None unless PM explicitly adds one |

Do not accept Google's account-default goals blindly. Confirm that no page view, engagement, add-to-cart, checkout, duplicate GA4 import, or duplicate Shopify/Google tag is primary for this campaign.

### Choose bidding from evidence

| State | Suitable starting decision |
| --- | --- |
| Verified Purchase action plus sufficient recent, relevant purchase history | Consider Maximize conversions. Consider Maximize conversion value only when correct transaction values vary materially. |
| Verified Purchase action but negligible relevant conversion history and a tiny test cap | Consider Manual CPC, if available, with exact/phrase intent and explicit maximum bids. State plainly that bidding is controlled discovery, not purchase optimization. |
| Goal is merely traffic learning | Maximize clicks may fit that separate experiment, but do not call it a buyer or sales campaign. |
| Suggested tCPA/tROAS without relevant history | Do not invent a target. Hold or use a strategy supported by current evidence. |

Maximize conversions is designed to spend the available budget while seeking conversions. Do not select it reflexively when the budget cannot support the expected auction costs or when the Purchase signal is unverified.

## Build the campaign

1. Define one commercial question, one product, one price, one destination, one audience geography, one budget envelope, and one fixed flight.
2. Research query intent and economics using the search playbook. Keep category-purchase queries separate from informational genealogy research, free-printable searches, murder-party searches, and real-person investigations.
3. Audit measurement and budget controls using the QA reference. Configure one biddable Purchase action; keep upstream actions secondary.
4. Author a campaign specification with campaign/ad-group names, dates, total budget, bid strategy, network/location settings, keywords and match types, negatives, RSA assets and pins, final URLs, URL tracking, conversion-action identifiers, and release gates.
5. Save the specification as JSON and run:

   `python3 scripts/validate_campaign_spec.py <campaign-spec.json> --mode stage`

6. Stage the exact objects paused. Capture IDs, settings, policy/eligibility state, keyword estimates, and final ad previews. Staging is not launch evidence.
7. Immediately before launch, refresh product price/availability, budget authority and account spend, conversion diagnostics, destination/cart/checkout, policy status, overlap, and dates. Update the JSON and run the validator with `--mode launch`.
8. Launch only when the current authorization covers the exact spend and every launch gate is green. Do not broaden or accept recommendations during launch.

## Mandatory launch gates

All must be evidenced, not merely asserted:

1. Exact PM authority, currency, maximum total spend, flight, and source are recorded.
2. Billing and advertiser/account status permit delivery.
3. The campaign has a true total budget at or below the authority and fixed start/end dates, or PM explicitly accepted the documented limitations of an average daily budget.
4. No other campaign can spend against the same test or cannibalize the same queries unexpectedly.
5. Exactly one Purchase action is primary/biddable; duplicate purchase imports are secondary or removed from the campaign goal.
6. Purchase diagnostics show one event per transaction with correct transaction ID, value, and currency. A preview or tag presence alone is insufficient.
7. The final URL loads on mobile and desktop and visibly matches the ad's product, price, fictional status, digital format, and CTA.
8. The CTA adds the correct available variant at the stated price and reaches checkout without creating an order/payment.
9. Keywords, match types, negatives, U.S.-presence targeting, language, Google-only network, and bid controls match the approved specification.
10. Every responsive-search-ad asset is within platform limits; required offer disclosures are guaranteed in an eligible pinned position; combinations remain grammatical and truthful.
11. Auto-tagging and the approved UTM/final-URL suffix survive redirects and preserve the working buyer path.
12. Draft IDs, policy eligibility, previews, account timezone, budget arithmetic, and zero-spend state are captured.

Any failed budget, measurement, destination, price, policy, or overlap gate produces **HOLD** with the exact failure and $0 additional spend.

## Monitor and reconcile

Evaluate the business result first:

- Shopify completed, paid, non-test orders at the advertised price;
- Google-attributed purchases reconciled by transaction ID, value, currency, time, and campaign;
- total and billed Google spend against the authorized cap;
- then checkouts, carts, qualified sessions, search terms, clicks, CTR, CPC, impression share, and policy/eligibility diagnostics.

Review actual search terms before 25% of a small test cap is consumed and at least daily thereafter. Add negatives for demonstrated mismatch; do not negate a query merely because it has not converted in a tiny sample. Do not call an RSA, keyword, or campaign a winner on CTR alone.

Pause or hold immediately for spend beyond authority, duplicate/false purchases, Google purchases without corresponding Shopify orders, broken destinations, wrong prices/products, material policy defects, or unintended inventory. A low conversion rate alone is a result to diagnose, not permission to rewrite the offer, raise budget, or expand targeting.

## Required outputs

For a plan, provide:

- commercial question and economic gate;
- current evidence and missing evidence;
- exact campaign specification and ad copy;
- launch/hold decision;
- authorization still required, if any.

For execution, post one ACK and one concrete result receipt containing:

- account timezone/currency and billing/policy state;
- old and overlapping campaign state;
- authority, budget type, cap arithmetic, dates, and billed-spend check;
- campaign, ad-group, ad, conversion-action, and relevant asset IDs;
- bid strategy, networks, location option, language, keywords/match types, and negatives;
- exact RSA assets/pins, previews, final URLs, and tracking;
- conversion and Shopify buyer-path evidence;
- launch status and first eligible impression/click evidence, or exact HOLD reason;
- next evidence checkpoint.

Do not report “live,” “tracking works,” “Google is optimizing for buyers,” or “within budget” without the corresponding platform evidence.

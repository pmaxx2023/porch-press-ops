# Porch Press Google Search build playbook

Use this reference for demand research, economics, keyword design, responsive search ads, landing-page continuity, and post-launch diagnosis.

## 1. Decide whether Search fits the product

Google Search is strongest when a prospect already knows the kind of solution they want. Porch Press is a novel category, so the central risk is not merely weak copy; it is that too few people search for a “printable genealogy mystery” or that adjacent clicks cost more than a $19.99 product can support.

Create a dated Keyword Planner evidence table:

| Field | Required evidence |
| --- | --- |
| Seed/query | Exact text entered |
| Intent class | Product/category purchase, adjacent purchase, informational, or irrelevant |
| Match type planned | Exact or phrase initially |
| U.S. monthly range | Live Keyword Planner range and date |
| Competition | Live planner label |
| Low/high top-of-page estimate | Live values and currency |
| Landing-page fit | Exact destination and matching offer language |
| Decision | Include, exclude, negative, or unresolved |

Planner figures are estimates, not delivery promises. Do not fabricate precision when Google gives a range.

### Economic sensitivity

For a digital product:

`contribution margin = price − payment fees − platform/fulfillment variable costs − expected refunds`

`break-even CPC = contribution margin × paid-search purchase rate`

Example only: if net contribution were $18 and the paid-search purchase rate were 2%, break-even CPC would be `$18 × 0.02 = $0.36`. This is an illustration, not a Porch Press forecast. Show multiple purchase-rate scenarios until observed paid-search data exists.

If the click-cost range overwhelms every plausible scenario, do not “test anyway” merely because a campaign can be built.

## 2. Classify search intent

Use these as research seeds, not preapproved live keywords:

| Cluster | Seed examples | Likely disposition |
| --- | --- | --- |
| Format purchase | printable mystery game; downloadable mystery game; print-at-home mystery game | Research first; strongest category intent |
| Investigation format | printable case-file mystery; printable detective game for adults | Research; verify product fit |
| Solo/together use | solo printable mystery game; mystery game for two adults | Research only when current product supports the use claim |
| Family-history niche | genealogy mystery game; family-history mystery game | Highly relevant but potentially very low volume |
| Brand/title | Porch Press; Baby in a Basket mystery; Eleanor Hart is Missing | Separate branded demand from cold acquisition |
| Informational genealogy | genealogy records; ancestry research; family-tree search | Exclude; wrong job-to-be-done |
| Free/make-your-own | free mystery PDF; mystery template; how to make a mystery game | Usually negative for a finished paid product |
| Party/entertainment mismatch | murder-mystery party; party kit; large-group mystery | Exclude when the destination explicitly says the product is not a hosted party game |
| Real-person/true-crime | missing person search; real case files; true-crime evidence | Exclude; Porch Press is fictional entertainment |

Do not confuse semantic relevance with buying intent. “Genealogy” is topically relevant but often signals research software, records, DNA tests, or family-tree services rather than a game purchase.

### Negative-keyword seed categories

Build negatives from actual mismatch and use the narrowest safe match type. Review at least:

- free, free download, template, generator, tutorial, how to make;
- classroom, lesson plan, worksheet, answer key, school, children/kids when the product is adult-positioned;
- login, account, software, app, family-tree maker, ancestry records, census lookup, DNA test;
- real missing person, police file, court record, true crime;
- murder-mystery party, host script, costume party, large group when those formats do not match the current product;
- jobs, salary, definition, meaning, review, walkthrough, solution, spoilers.

Do not apply the whole seed list blindly. A term can be a negative at the campaign level only after checking that it cannot represent a legitimate Porch Press buyer query.

## 3. Build the smallest interpretable structure

Use one campaign for one product and one landing page. Start with one or two tightly related ad groups rather than scattering a tiny budget across many themes.

Good separation:

- **Printable mystery:** format-led exact/phrase queries.
- **Family-record mystery:** narrower genealogy/family-history exact/phrase queries.

Bad separation:

- one ad group per trivial wording variation;
- mixing product-format searches with genealogy research;
- mixing multiple titles whose ads land on different offers;
- putting brand terms in the cold-acquisition ad group and then crediting easy branded conversions to the generic strategy.

Exact and phrase match still include close or meaning-based variants. The search-terms report—not keyword labels alone—is the evidence of what Google actually matched.

## 4. Author responsive search ads as a message system

Current platform limits must be rechecked before each build. As verified September 12, 2026, Google permits up to 15 headlines of 30 characters each, four descriptions of 90 characters each, and two path fields of 15 characters each. Use at least three distinct headlines and two descriptions.

Each ad group should have one coherent responsive search ad whose assets cover:

1. the searched category;
2. the specific mystery hook;
3. the investigation mechanism;
4. concrete, verified product substance;
5. current price and digital format;
6. a direct purchase CTA.

Because Google can assemble different combinations, make every headline compatible with every description. Do not repeat the same claim in cosmetic variants simply to fill all 15 slots.

### Guaranteed disclosure

For Porch Press, pin a truthful offer-format description to Description position 1 so every eligible combination identifies the product correctly. A pattern is:

`Fictional printable case files. Digital download. $19.99. Nothing ships.`

Replace the price and wording with current verified facts. Keep the pinned asset within 90 characters. Do not claim instant delivery unless the current fulfillment path was actually verified.

Example headline patterns—verify length and facts before use:

- Printable Mystery Case
- Solve a Family Secret
- Download the Case Files
- Examine the Family Records
- Play Solo or Together
- A Mystery Hidden in Records
- Who Was Mabel Before Sutton?
- $19.99 Digital Mystery

These are patterns, not blanket approval. Owner_Bot must author title-specific final copy from the current product evidence.

Use image assets only when they are actual approved product records/covers and remain legible. Do not fabricate evidence pages or imply a shipped physical case.

## 5. Preserve the ad-to-checkout chain

The final URL must make the query promise immediately visible:

| Search/ad promise | Destination proof |
| --- | --- |
| Printable mystery | Above-the-fold category statement and visible preview |
| Family-record investigation | Actual spoiler-safe record or archive evidence |
| Specific title/hook | Same title and central question |
| Digital product | Clear download/PDF language and “nothing ships” |
| Current price | Same price in ad, page, cart, and checkout |
| Buy/Shop CTA | Working correct-variant cart and checkout entry |

Do not send cold acquisition traffic to a generic homepage when a product-specific landing page exists. Do not use the unpublished Eleanor candidate as a destination until it is public, crawlable, and separately verified.

Recommended tracking suffix pattern:

`utm_source=google&utm_medium=cpc&utm_campaign=<stable_campaign>&utm_content=<ad_group_or_message>&utm_term={keyword}`

Keep auto-tagging enabled when the account's measurement design supports it. Test that final parameters survive redirects and do not break Shopify cart behavior.

## 6. Diagnose in commercial order

| Observed evidence | First diagnosis |
| --- | --- |
| No eligible impressions | Policy, billing, dates, low search volume, bid, match type, or targeting—not automatically “expand broadly” |
| Impressions but weak response | Query/ad/category mismatch or uncompetitive promise |
| Clicks but weak human arrivals | Search-partner/inventory quality, redirects, load speed, consent/tracking, or accidental clicks |
| Qualified visits but no carts | Category explanation, product substance, price/value, trust, or CTA |
| Carts but no checkout | Cart friction, surprise, price inconsistency, or buyer-path defect |
| Checkout but no paid order | Payment/checkout friction or offer resistance |
| Google Purchase without Shopify paid order | Invalid, duplicated, or misconfigured conversion; HOLD |
| Shopify paid order without Google attribution | Attribution window, tag/consent, cross-domain, or non-Google acquisition; do not assign credit casually |
| Click-leading ad with no downstream behavior | No commercial winner |

Use transaction-level reconciliation and current Shopify order evidence. Platform-reported conversions alone do not establish a paid order.

## Official references

Recheck these live because Google changes labels and defaults:

- [Create a Search campaign](https://support.google.com/google-ads/answer/9510373)
- [Keyword matching options](https://support.google.com/google-ads/answer/7478529)
- [Negative keywords](https://support.google.com/google-ads/answer/2453972)
- [Search terms report](https://support.google.com/google-ads/answer/2472708)
- [Responsive search ads](https://support.google.com/google-ads/answer/7684791)
- [Responsive search ad strength and asset limits](https://support.google.com/google-ads/answer/9921843)
- [Final URLs and tracking templates](https://support.google.com/google-ads/answer/6273460)
- [Destination requirements](https://support.google.com/adspolicy/answer/6368661)
- [Misrepresentation and unavailable offers](https://support.google.com/adspolicy/answer/6020955)

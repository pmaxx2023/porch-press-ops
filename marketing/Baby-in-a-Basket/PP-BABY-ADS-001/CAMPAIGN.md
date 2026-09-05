# PP-BABY-ADS-001 — first $30 acquisition test
Owner_Bot — Porch Press (ChatGPT), September 5, 2026

## Authority and state
PM authorized Owner_Bot to build Porch Press using only a $100 gift card as new capital, confirmed the Shopify subscription is already paid, and instructed "work on it." Owner_Bot allocates $30 maximum all-in to this initial test, $50 held for evidence-based follow-up, and $20 reserve. This supersedes the former $50 preparation proposal and its absence of spending authority. No automatic release of the remaining $70.
Current execution status: NOT LAUNCHED. Account access, gift-card acceptance, billing, tracking and customer delivery are not yet verified. The gift card has not been supplied or charged. Do not use another stored payment method.
Owner_Bot may release this bounded test once prerequisites below are evidenced, without asking PM to approve the same budget again. Connector_Bot/Shopify_Bot prepares and reports; campaign activation awaits an explicit Owner_Bot release comment naming the actual account, dates and all-in cap.
All copy/art authorship remains Owner_Bot. Existing GitHub issue #3 is the coordination channel.

## Decision and design
Explore whether Baby in a Basket's approved emotional artwork generates purchases and which of two primary-text openings is directionally stronger.
One Meta Sales campaign, website purchase destination, one shared prospecting ad set, two ads. This is an exploratory delivery-optimized comparison, NOT a randomized A/B test. Unequal exposure is expected; do not infer causal superiority or promise significance.
Selected initial audience: US adults 18+, all genders, broad targeting, English creative; exclude existing purchasers if a usable audience exists. This is Owner_Bot's operating choice for the initial US/USD test; do not expand countries during the test. No sensitive-trait targeting.
Same art per placement, same headline, body after opening, CTA, offer, audience and schedule. Turn off automatic text/image changes where supported; otherwise report them. No generated variations or expansion to extra ads.

## Exact ad copy
### A — missing identity
Primary text:
Mabel knew where she was found. She never knew who her parents were.

Follow census entries, birth records, and household connections to uncover her beginnings in Baby in a Basket, a fictional printable genealogy mystery.

Download, print, and investigate—solo or together.

### B — invitation to investigate
Primary text:
A basket in a church pew. A missing family history. Can you trace Mabel's beginnings?

Follow census entries, birth records, and household connections to uncover her beginnings in Baby in a Basket, a fictional printable genealogy mystery.

Download, print, and investigate—solo or together.

### Shared fields
Headline: Baby in a Basket
Description: A printable genealogy mystery.
Meta CTA: Shop Now
Image headline (already embedded): Someone left her in a basket. Someone knew her name.
Image CTA (already embedded): Open the case
Product price: use actual current Shopify price; expected $9.99 USD, verify before launch. No price change assigned.

## Creative files
All files in this directory:
- baby-basket-feed-4x5.png — original approved art, 1122 x 1402.
- baby-basket-feed-square.png — 1254 x 1254; use for both variants' feed preview.
- baby-basket-story-9x16.png — 940 x 1672; approximate 9:16, requires placement review.

Initial placements: Facebook Feed and Instagram Feed only, using the supplied square artwork for both variants. Exclude Stories/Reels from this first run to avoid the unresolved overlay issue. Inspect real placement previews for legibility before release. Images are promotional art, not playable evidence.

## Destination and labels
A:
https://porchpress.store/products/baby-in-a-basket?utm_source=meta&utm_medium=paid_social&utm_campaign=pp_baby_ads_001&utm_content=a_identity
B:
https://porchpress.store/products/baby-in-a-basket?utm_source=meta&utm_medium=paid_social&utm_campaign=pp_baby_ads_001&utm_content=b_investigate

UTMs label traffic; they are not a tracking implementation. Preserve these IDs in measurement where supported. Do not fabricate per-ad order attribution if unavailable.

## Execution prerequisites and release
1. Resolve existing Facebook Page, Instagram identity, Meta business/ad account and Shopify connection. Report actual names/IDs, permissions, currency and timezone; never credentials or customer records. Do not create duplicate campaigns: inspect for an existing PP-BABY-ADS-001 draft first.
2. Confirm Purchase optimization eligibility and actual Pixel/dataset connection. Observe identifiable product/cart test events and inspect supported Purchase test evidence, including deduplication if browser/server events coexist. Missing tracking is not zero sales. Do not switch to clicks optimization simply to spend.
3. Shopify_Bot must verify current canonical Baby ZIP mapping and one supported non-charging delivery test to an existing owner-controlled test destination, using the same delivery mechanism as a real order where possible. No paid self-purchase, refund, invented customer identity or email to a real customer. If no owner test destination is already configured, report that specific missing input. Do not put the address in GitHub. A manual file fetch alone is not buyer delivery proof; a test bypassing the paid-order trigger does not certify that trigger.
4. Prepare ONE lifetime campaign/ad-set budget covering BOTH ads for five days. All charges including advertising tax/fees must fit $30 USD; subtract known charges from the media budget as necessary. If billing currency is not USD, return the supported conversion and bounded maximum before release. No daily $30 budget, duplicate ad-set budgets, automatic extension or minimum-budget increase. If the platform cannot support the test inside the cap, stop with that finding.
5. Verify billing accepts the user-entered gift card and cannot charge another funding source for this test. Do not assume a prepaid card is accepted, expose card details, or load all $100 into advertising. PM enters payment details directly when needed.
6. Return real draft IDs/preview links, placements, budget, account timezone, proposed exact start/end timestamps, tracking evidence, delivery evidence, and no-spend status. Set the end time in-platform so ending the campaign does not depend on this conversation waking up. Owner_Bot issues the specific release only after these checks pass; this is an execution checkpoint within existing authority, not a new request for PM's budget approval.

## Measurement plan
Primary business outcome: attributed purchases and cost per purchase = campaign spend / attributed purchases. Undefined if zero purchases; report zero purchases with spend, not zero acquisition cost.
Record actual attribution window and reporting source before launch; compare Meta attribution separately from Shopify orders and UTMs rather than treating them as interchangeable.
Secondary: outbound clicks, impressions, outbound CTR, spend/outbound click, landing visits, checkout starts and purchases. Do not substitute all clicks or likes.
Five-day/$30 test is an exploratory limit, not a powered sample size. No baseline or minimum useful lift established. End at approved cap or scheduled end, whichever first; stop for broken destination/tracking or incorrect offer. No unapproved extension to get a winner.
Report per variant and campaign totals; account for delivery/placement differences and missing attribution. Labels: directional leader, inconclusive, or invalid measurement. A profitable result requires fees/refunds as well as ad cost; Gross revenue alone is not break-even profit.
No results or background monitoring are claimed by preparing this packet.

## Official references checked September 5, 2026
- https://help.shopify.com/en/manual/promoting-marketing/create-marketing/facebook-instagram-by-meta
- https://www.facebook.com/business/ads/ad-objectives/sales
- https://www.facebook.com/business/help/103816146375741
- https://www.facebook.com/business/ads-guide/update/image/instagram-story

## Capital decision after test
At the observed $9.99 price, three purchases produce $29.97 gross revenue, less than $30 of advertising even before payment/platform fees. Four purchases produce $39.96 gross, leaving $9.96 before those fees, refunds and tax treatment. This arithmetic is not a forecast.
Calculate net contribution from actual processor/Shopify fees and receipts before releasing more capital. Zero purchases at the cap means stop paid acquisition and diagnose the offer/path; no automatic $50 retry. Positive contribution can justify a bounded follow-up, but a few purchases do not prove scalable acquisition.
Current ledger: see ../../../CAPITAL_LEDGER.md.

## Current verification — September 5, 2026
Owner_Bot directly observed the public product page at $9.99 USD, successful add-to-cart for variant 52494545486122, and checkout with one Baby in a Basket totaling $9.99 before buyer information. No order or payment submitted.
The live description differs from Storefront-Listing.md and includes unverified "About one evening" and "Medium difficulty" claims. Replacement with approved copy is assigned through issue #3.
Checkout exposed PayPal plus PayPal/Venmo express buttons; no native card field was visible. Guest card availability through PayPal was not tested. This is a friction finding, not proof cards cannot be used.
No Meta campaign/account/tracking or buyer download verification has been observed by Owner_Bot.

Reference status: Shopify's marketing documentation was rechecked this turn and directs ad creation to Meta Ads Manager. The Meta help URL returned a login/temporary-block page; current account capabilities must be verified in the actual platform, not inferred from the older draft.

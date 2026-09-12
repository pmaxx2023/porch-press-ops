# PP-BABY-EVIDENCE-SALES-001 — buyer-quality replacement campaign

Owner_Bot — Porch Press (ChatGPT)  
Prepared: September 12, 2026  
State: COMPLETE PLAN — NOT AUTHORIZED TO DRAFT, PAUSE, LAUNCH, OR SPEND

## Commercial verdict

Replace the current landing-page-view acquisition method, not because the small sample proves the old creative failed, but because it is optimized for the wrong commercial outcome. Meta is being asked to find page loaders. The replacement must prequalify people with actual product evidence and optimize no shallower than a verified commerce event.

The principal risk is the offer, not only the ad: Porch Press has one attributable purchase at the former $9.99 price and no evidence yet that the current $19.99 price converts. This campaign holds price and destination constant so its result remains interpretable. It does not claim to validate the price in advance.

This is a completely new ad set:

- retire the prior A/B primary text, headline, old square composition, and embedded “Can you solve it?”-style treatment;
- use real Baby in a Basket product records as proof, but create new layouts from those source assets;
- disclose fictional, printable/digital, $19.99, and nothing ships before the click;
- test a record contradiction against product-substance proof;
- do not run a landing-page-view buyer campaign again.

## Decision this campaign supports

Commercial question:

Can a cold U.S. prospect who sees a real family-record contradiction or the substance of the printable case produce at least one attributable, non-test purchase of Baby in a Basket at $19.99, through the existing campaign page, within only the unspent portion of the current $30 Meta ceiling?

Primary business outcome: one attributable, paid, non-test Baby in a Basket order at $19.99.

Optimization event: the deepest verified event that can deliver, in this fixed order:

1. Purchase;
2. InitiateCheckout;
3. AddToCart;
4. otherwise HOLD — NO VIABLE BUYER OPTIMIZATION.

Landing-page views, link clicks, and engagement remain diagnostic only.

## Verified baseline and uncertainty

| Item | State | Evidence / implication |
| --- | --- | --- |
| Product | Baby in a Basket, active | Shopify product gid://shopify/Product/10295874814250, verified September 12 |
| Variant | 52494545486122 | Both visible campaign-page CTAs added the correct product |
| Offer | $19.99, digital printable PDFs, nothing ships | Current live product; no current-price purchase evidence |
| Contents | 36-page player packet, 5 pages of progressive hints, 8-page sealed solution, START-HERE, optional 52-page combined-print file | Use as value proof; do not imply that every file must be printed |
| Play | Solo or together; no host, internet, outside research, or cutting | Verified product characteristics |
| Buyer path | Campaign page to cart and checkout is green | [Latest path receipt](https://github.com/pmaxx2023/porch-press-ops/issues/6#issuecomment-5646063531); no order/payment was submitted |
| Prior paid order | One $9.99 order from pp_baby_ads_001 / a_identity / Facebook | Supports the identity territory directionally at the old price, not the $19.99 offer |
| Current Meta method | PP-BABY-LPV-030-001, landing-page-view optimization, $30 lifetime ceiling | Last known spend was $8.02 at 2026-09-12T13:20:12Z; refresh before action |
| Earlier genealogy test | $19.95 spend, 486 impressions, 7 link clicks, 5 landing-page views, no evidenced purchase | Too little downstream volume to prove offer failure; weak traffic economics |
| Current priority conflict | OWNER_BOT.md names PP-ROSCOE-COLLAB-001 as the only queued next experiment | This plan remains unqueued until PM resolves budget/order of operations |

Do not describe current traffic as fake without bot or reconciliation evidence. The supported conclusion is that LPV optimization does not test buyer quality.

## Campaign architecture

| Field | Owner_Bot decision | Live build gate |
| --- | --- | --- |
| Campaign | PP-BABY-EVIDENCE-SALES-001 | New stable ID; do not reuse an old object |
| Objective | Meta Sales | Verify exact control names in the live account |
| Conversion location | Website | Confirm the correct Porch Press dataset/pixel |
| Performance goal | Maximize conversions for the selected verified commerce event | Never fall back silently to link clicks or LPV |
| Ad set | PP-BABY-EVIDENCE-COLD-US-001 | One cold prospecting ad set |
| Geography | United States | Preserve USD / English offer |
| Age / gender | Adults 18+, all genders | No age narrowing without first-party buyer evidence |
| Audience | Broad prospecting | Do not stack homeowner, income, parent, traveler, or vague lifestyle proxies |
| Exclusions | Known purchasers, owner/QA where supported | Record exact exclusions and any unsupported gap |
| Placements | Advantage+ placements only if every supplied crop passes preview; otherwise Facebook and Instagram feeds | Use the same eligible placements for both ads |
| Attribution | Record and preserve the verified account setting | Do not compare windows as if equivalent |
| Creative automation | Off for text generation, image generation, music, visual expansion, and material transformations where controls exist | Record any unavoidable platform behavior |
| Destination | https://porchpress.store/pages/genealogy-mystery-case | Do not change during the creative comparison |
| Schedule | 72 hours from verified activation, or cap reached, whichever comes first | Set a fixed platform end time in the ad-account timezone |
| Budget | Fixed lifetime cap equal to $30 minus actual PP-BABY-LPV-030-001 spend at pause | If the remainder is below the platform minimum or cannot be hard-capped, HOLD |

Illustrative budget arithmetic only: the last receipt would imply $21.98 remaining. Because the old campaign may still spend, Grok must use actual filtered spend at the moment of an authorized pause. No separate or additional budget is included in this plan.

## Treatment held constant

Both live ads use the same product, $19.99 price, destination, CTA, audience, optimization event, attribution setting, placements, schedule, and cap. Meta may allocate delivery unevenly; this is exploratory delivery, not a randomized A/B test.

## Ad A — record contradiction

Stable ID: PP-BABY-RECORD-SALES-001  
utm_content: record_contradiction

Primary text:

> One census record makes Mabel’s family story harder to believe.
>
> Baby in a Basket is a fictional printable case-file mystery. Compare four possible identities, test the household evidence, complete six deductions, and make your case before opening the sealed solution.
>
> Digital PDFs · $19.99 · Play solo or together · Nothing ships.

Headline: Who Was Mabel Before Sutton?

Description: 36-page investigation + hints + sealed solution

CTA: Shop Now

Creative mechanism: make the actual record the hero so a document-minded prospect recognizes the work before clicking.

New composition:

- dominant source: actual census exhibit;
- supporting source: Baby in a Basket cover;
- overlay 1: ONE RECORD CHANGES THE FAMILY STORY.
- overlay 2: PRINTABLE CASE FILE · $19.99
- 4:5 feed asset at 1080 × 1350;
- 9:16 placement asset at 1080 × 1920 only if the relevant record crop remains legible in preview;
- warm paper palette and restrained Porch Press wordmark; no stock crime tape, blood, magnifying glass, or fake evidence.

Source assets:

- https://cdn.shopify.com/s/files/1/0782/2842/2954/files/Preview-03-Census-Exhibit.png?v=1788998932
- https://cdn.shopify.com/s/files/1/0782/2842/2954/files/02-who-was-she-before-sutton.png?v=1788632264

Alt text: A cropped period-style census exhibit beside the Baby in a Basket cover, labeled as a $19.99 printable case file.

## Ad B — case-file substance

Stable ID: PP-BABY-SUBSTANCE-SALES-001  
utm_content: casefile_substance

Primary text:

> This is not a novel and not a murder-mystery party.
>
> Baby in a Basket is a fictional family-history case you solve from period-style records. Your digital case includes a 36-page player packet, progressive hints, an eight-page sealed solution, and an optional combined print file.
>
> Compare four possible identities. Complete six deductions. Decide who Mabel was before Sutton.
>
> $19.99 · Printable PDFs · Nothing ships.

Headline: Open a Printable Family Mystery

Description: Examine the records. Make your case.

CTA: Shop Now

Creative mechanism: answer the thin-download and category-confusion objections with visible product substance.

New composition:

- three-part evidence spread using the actual cover, opening story, and census exhibit;
- overlay 1: THE STORY IS FICTION. THE DEDUCTION IS YOURS.
- overlay 2: DIGITAL CASE · $19.99
- 4:5 feed asset at 1080 × 1350;
- 9:16 placement asset at 1080 × 1920 only if the documents and format line remain legible;
- each document must remain identifiable as product material; no AI-generated replacement pages.

Source assets:

- https://cdn.shopify.com/s/files/1/0782/2842/2954/files/02-who-was-she-before-sutton.png?v=1788632264
- https://cdn.shopify.com/s/files/1/0782/2842/2954/files/Preview-02-Opening-Story.png?v=1788998933
- https://cdn.shopify.com/s/files/1/0782/2842/2954/files/Preview-03-Census-Exhibit.png?v=1788998932

Alt text: The Baby in a Basket cover, opening story, and census exhibit arranged as a printable digital case, priced at $19.99.

## Reserve Ad C — shared reconstruction

Do not activate with A and B. Use only if one live ad is rejected or in a later separately approved test.

Stable ID: PP-BABY-TOGETHER-SALES-001  
utm_content: shared_reconstruction

Primary text:

> One of you may trust the family story. The other may trust the records.
>
> Baby in a Basket gives you a fictional family-history mystery to investigate from period-style documents. Work through six deductions, use progressive hints only if needed, then open the sealed solution.
>
> Digital PDFs · $19.99 · No host or outside research.

Headline: Compare the Records. Make Your Case.

Description: Play solo or solve it together.

CTA: Shop Now

Creative specification: a new two-view document composition using the real census and opening-story assets, with the overlay TWO READERS. ONE FAMILY STORY. DIGITAL CASE · $19.99.

## Destination and tracking map

Ad A:

https://porchpress.store/pages/genealogy-mystery-case?utm_source=meta&utm_medium=paid_social&utm_campaign=pp_baby_evidence_sales_001&utm_content=record_contradiction

Ad B:

https://porchpress.store/pages/genealogy-mystery-case?utm_source=meta&utm_medium=paid_social&utm_campaign=pp_baby_evidence_sales_001&utm_content=casefile_substance

Reserve C:

https://porchpress.store/pages/genealogy-mystery-case?utm_source=meta&utm_medium=paid_social&utm_campaign=pp_baby_evidence_sales_001&utm_content=shared_reconstruction

The live page remains fixed during this test. Before launch, confirm above the fold repeats the identity question, printable/digital category, $19.99 price, and actual record proof. If it does not, HOLD and open a separately scoped continuity fix; do not quietly change both ad and page.

## Message-chain acceptance

| Stage | Required continuity |
| --- | --- |
| Ad | Mabel identity question or visible case substance; examine records; fictional; printable digital; $19.99 |
| Page opening | Same product and identity question; immediately explains the printable case-file format |
| Proof | Actual census/opening preview, spoiler-safe and legible |
| Offer | Exact contents, digital delivery, current price, nothing ships |
| CTA | Shop Now continues to the verified Baby cart/checkout path |

## Claim ledger

| Claim | Support | Boundary |
| --- | --- | --- |
| Fictional family-history / case-file mystery | Live product copy | Never imply a real case or research service |
| Four possible identities, six deductions | Live product contents | Do not disclose the solution |
| 36-page packet, 5 pages of hints, 8-page solution, optional 52-page combined file | Live product contents | Do not imply all 52 pages are additional content |
| Solo or together; no host or outside research | Live product copy | Do not invent player-count limits or duration |
| Digital printable PDFs; nothing ships | Live format and fulfillment | Never show or imply a shipped box |
| $19.99 | Current live price on September 12 | Reverify immediately before draft/launch |

No reviews, customer counts, awards, urgency, bestseller claims, guaranteed fun, difficulty, or playtime claims are approved.

## Preflight release gate

Grok must return evidence for all of the following before Owner_Bot can release:

1. current state and spend of PP-BABY-LPV-030-001, with account timezone and filtered date range;
2. no overlapping eligible-to-spend Baby campaign after any authorized pause;
3. exact Sales objective and deepest eligible verified event;
4. one browser and one supported server-side event trace, with deduplication checked where both exist;
5. both destination URLs, both CTAs, correct variant, $19.99 cart, and checkout entry without order/payment;
6. final A/B placement previews at readable desktop and mobile sizes;
7. automation/enhancement controls and any unavoidable transformations;
8. exact lifetime cap arithmetic and fixed end time;
9. purchaser/owner/QA exclusion evidence or explicit unsupported gaps;
10. draft IDs and no-spend state.

Any failed claim, buyer-path, event, overlap, price, or hard-cap check keeps the campaign off.

## Result classification

Report the primary business outcome first, then mechanism diagnostics.

| Observed result | Label / next diagnosis |
| --- | --- |
| At least one attributable paid $19.99 order | Directional positive; pause or hold and review contribution before any scale |
| Add-to-cart or checkout, no order | Downstream signal; inspect value, trust, delivery, cart, and checkout before changing hook |
| Impressions, little outbound response | Inspect buyer relevance and ad comprehension |
| Outbound clicks, weak human arrivals | Inspect redirect, load, tracking, and traffic quality |
| Mostly bot-classified or irreconcilable sessions | Invalid measurement |
| Cap/end reached with too little valid exposure | Inconclusive |
| A has more clicks but neither has downstream behavior | No winner |

No result automatically authorizes an extension, new audience, discount, price change, or additional spend.

## Ownership and implementation boundary

Owner_Bot authored and approves the exact public copy in this plan. Grok may create the new visual compositions, build the unpublished Meta objects, capture previews, and operate an explicitly released campaign. Grok may not rewrite the copy, substitute assets, change price or destination, add ads, change optimization, broaden targeting, overlap the old campaign, or increase spend.

This file records a plan only. It does not dispatch Grok, alter Shopify, pause the current Meta campaign, create a draft, launch ads, or spend money.

## One release decision

Recommended: use only the unspent remainder of the existing $30 Meta ceiling. Upon explicit authorization, pause PP-BABY-LPV-030-001, capture its actual spend, and give the replacement a lifetime cap of $30 minus that spend.

Alternative: authorize a separate new budget. This is not recommended until a buyer-optimized, evidence-led treatment shows a real commerce signal.

## Current official platform references

- [Meta campaign objectives](https://www.facebook.com/business/ads/ad-objectives)
- [Meta Sales objective](https://www.facebook.com/business/ads/ad-objectives/sales)
- [Meta Traffic objective](https://www.facebook.com/business/ads/ad-objectives/traffic)

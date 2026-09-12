# PP-ROSCOE-COLLAB-001 — Roscoe collaborative-play pilot

**Owner:** Owner_Bot — Porch Press (ChatGPT)  
**Product state:** Roscoe's Grave is the existing free browser investigation; Baby in a Basket remains the paid hero at $19.99.  
**Experiment state:** BLOCKED pending PP-LP-FORM-HOTFIX-002. Do not release community traffic while the paid landing-page forms are unverified.  
**New spend:** $0.  

## Decision

Decide whether authentic collaborative solving is promising enough to build into a recurring Porch Press experience.

This is a 72-hour exploratory pilot, not an A/B test and not evidence of causal lift. The pilot asks whether qualified human visitors will move through this observable sequence:

1. Open the free Roscoe investigation.
2. Examine multiple records and form a theory.
3. Post an authentic theory or evidence question in the permitted community thread.
4. Encounter and follow the Baby in a Basket paid-case invitation.
5. Create a confirmed $19.99 cart, begin checkout, or purchase.

## Hypothesis

People who can compare theories with other real players will participate more deeply than people who only receive a sales message. The first useful evidence is not raw traffic or upvotes. It is authentic progression from case work to discussion and then toward the paid case.

## Surface and acquisition

- Canonical case: https://porchpress.store/pages/free-investigation
- Paid follow-on: https://porchpress.store/products/baby-in-a-basket
- Primary candidate surface: https://www.reddit.com/r/printandplay/comments/1wbl9l6/playtesters_wanted_a_documentbased_detective/
- Owner_Bot observed the thread live on September 12, 2026. It was posted by u/Candid_Ad4725 about three days earlier with the **Seeking Playtesters** flair and remained public. It has at least thirteen distinct public expressions of interest, including explicit requests for the link. Replies routed people into DMs; no completed-play feedback was visible.
- Grok must verify that u/Candid_Ad4725 is the Porch Press-controlled account before editing or replying. If ownership is not verified, do not touch the thread and report the blocker.
- If ownership is verified, reuse this one live thread. Do not create another Reddit post. Correct the public offer with the update copy in HOST_PLAYBOOK.md and turn the existing interest into an open case-room discussion.
- Do not DM Reddit users, scrape identities, cross-post, buy promotion, or ask friends/agents to seed responses.

Tracked entry URL after the exact community source is known:

https://porchpress.store/pages/free-investigation?utm_source=reddit&utm_medium=community&utm_campaign=pp_roscoe_collab_001&utm_content=case_thread

Paid-case route from the free investigation:

https://porchpress.store/products/baby-in-a-basket?utm_source=roscoe_case&utm_medium=community&utm_campaign=pp_roscoe_collab_001&utm_content=case_complete

No personal information belongs in URLs.

## Eligibility and exclusions

Count as qualified only a non-owner, non-admin, non-agent, non-bot visitor or participant with credible human activity. Keep Reddit, Meta, direct, QA, and agent traffic separate.

Exclude:

- Owner, Grok, Connector_Bot, Shopify_Bot, Claude, ChatGPT, browser QA, and other agent traffic.
- Synthetic theories, replies, votes, reactions, room occupancy, reviews, or testimonials.
- Duplicate comments from the same person when counting participants.
- Bot-classified or automation-signature sessions.
- Internal test carts, checkouts, and orders.
- Traffic before the verified form repair from purchase-funnel conclusions.

The host may reply to real players and summarize authentic theories. Host activity must be labeled and excluded from every demand numerator and denominator.

## Minimum event model

| Stage | Stable event | Operational definition |
| --- | --- | --- |
| Arrival | landing_view | Free-case page rendered from the tracked community URL |
| Qualification | qualified_view | Eligible session with at least one intentional case interaction |
| Case entry | case_start | Visitor opens the Roscoe folder or Ada's story |
| Evidence use | artifact_open | A named record is opened; preserve distinct-record count |
| Engagement | case_engaged | At least two distinct records opened |
| Participation | theory_submit | Authentic Reddit user posts a theory or evidence question |
| Offer exposure | paid_cta_view | Baby CTA enters the viewport, if reliably measurable |
| Offer interest | paid_cta_click | Visitor follows the tracked Baby CTA |
| Commerce intent | add_to_cart_success | Shopify confirms Baby variant 52494545486122 at $19.99 in cart |
| Checkout | begin_checkout | Correct Shopify checkout is created |
| Sale | purchase | Paid Shopify order; backend order is authoritative |
| Return | return_to_case | Same eligible visitor returns in a later session, if reliably measurable |

If Shopify cannot reliably retain case-interaction events without a new app, do not invent them. Report the supported subset and use authentic Reddit theory participation plus server-confirmed commerce events as the hard evidence.

## Practical continuation gates

These gates govern whether to continue exploring; they are not statistical proof.

| 72-hour result | Decision |
| --- | --- |
| Fewer than 5 qualified case starts | Inconclusive distribution. Do not judge community demand. |
| At least 5 qualified starts but 0 authentic theories | Stop. The participation invitation or surface failed this pilot. |
| At least 2 authentic theory contributors | Directional participation signal; preserve exact thread and host pattern. |
| At least 1 tracked paid-CTA click from a participant | Directional offer-bridge signal; inspect the full path. |
| Confirmed cart or checkout from the cohort | Stronger directional signal; inspect friction without changing the offer mid-window. |
| One attributable $19.99 purchase | Directional commercial positive; stop expansion and reconcile evidence with Owner_Bot. |

Do not combine these results with the separate $30 Meta LPV campaign. Do not calculate purchase probability from this exploratory sample.

## Launch sequence

1. Complete PP-LP-FORM-HOTFIX-002 and record its deployment time.
2. Confirm the free Roscoe case is playable on desktop and mobile; preserve canon, evidence, solution, and Baby hero status.
3. Verify ownership and current status of the exact Reddit thread above. Confirm that it remains permitted under its **Seeking Playtesters** flair.
4. Add the exact Owner_Bot-authored update in HOST_PLAYBOOK.md and publicly reply only to people who explicitly requested access and have not received a public link. Record the URL and timestamp.
5. Add the exact thread URL to the free page's **Join the live case thread** control and add the tracked Baby route. Do not expose a placeholder URL.
6. Verify the page, links, query parameters, record interactions, solution flow, Baby route, and mobile layout.
7. Start the 72-hour window only after both the thread and page are live and cross-linked.
8. Host only in response to authentic participants. Post one evidence-led theory summary per day only when real theories exist.
9. At 24, 48, and 72 hours, report compatible incremental counts, exclusions, and source evidence. Do not add overlapping windows.

## Freeze during the pilot

- Baby remains the paid hero at $19.99.
- Roscoe remains the free browser case.
- Do not change the cases, solution, catalog price, offer, main CTA, or product delivery.
- Do not launch additional Reddit posts, paid campaigns, discounts, pop-ups, products, apps, or fake social proof.
- The existing Meta campaign remains a separate experiment under its existing ceiling and end date.

## Definition of done

- Buy-path hotfix is green and timestamped.
- Exact permitted Reddit surface and post URL are recorded.
- Free case and thread are cross-linked with no placeholder.
- Desktop/mobile and complete Roscoe playthrough pass.
- Cohort and QA exclusions are documented.
- 72-hour result uses the four labels: directional signal, inconclusive, invalid measurement, or stop.
- One next decision is returned; no automatic platform build follows.

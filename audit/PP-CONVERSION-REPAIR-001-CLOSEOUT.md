# CLOSE-OUT — PP-CONVERSION-REPAIR-001

**Bot:** Shopify_Bot  
**Posted:** 2026-09-10 13:31 CDT  
**Provisional observation marker:** 2026-09-10 13:16 CDT / 18:16 UTC (REPAIR LIVE)  
**First PM review target:** 2026-09-10 **17:16 CDT / 22:16 UTC** (four-hour interval)

## 1. CSS dedupe (sizing repair)
**Timestamp:** 2026-09-10 ~13:25 CDT / 18:25 UTC  
**Asset:** `sections/pp-genealogy-mystery-case.liquid`  
**Change:** In `#pp-gmc .pp-gmc-submit`, removed overriding `max-width: 22rem` and `min-height: 3rem`; left single `max-width: 352px` and `min-height: 48px` (kept `width: 100%` and remainder).  
**Backup:** `store-design/backups/pp-conversion-repair-001/sections_pp-genealogy-mystery-case.liquid.pre-css-dedupe`  
**Verify:** CDP at 320px and 390px — computed max-width 352px, min-height 48px, no horizontal overflow.

## 2. Controlled QA (≤2 authorized sessions)
UTM: `utm_source=ownerqa&utm_medium=qa&utm_campaign=pp_conversion_repair_001`  
**Exclude from acquisition reporting.** No payment/order. Cookies cleared between paths and after.

| Path | UTC | Device | Entry | ATC | Cart | Checkout entry | Order |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 Baby PDP | 2026-09-10T18:26:33Z | 390×844 | `/products/baby-in-a-basket` + UTM | PASS (1 click) | variant `52494545486122` · qty 1 · $19.99 | PASS (blank fields) | none |
| 2 Search LP | 2026-09-10T18:28:13Z | 1280×800 | `/pages/genealogy-mystery-case` + UTM | PASS (1 click, top CTA) | variant `52494545486122` · qty 1 · $19.99 | PASS (blank fields) | none |

Screenshots under `porch-press/audit/pp-conversion-repair-001/qa/`.

## Freeze
No further price/title/copy/layout/ad changes in this close-out. Meta Aud1 / Bing paused $0 / partner drafts unsent unchanged.  
Until the 17:16 CDT review, do **not** treat the interval as a fully verified stable purchase-path *conversion* test — only that the scoped repairs + transaction-path entry checks passed.

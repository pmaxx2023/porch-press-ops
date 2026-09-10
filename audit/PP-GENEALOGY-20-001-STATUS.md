# PP-GENEALOGY-20-001 — DELIVERY SNAPSHOT

**Bot:** Shopify_Bot  
**Status enum:** **DELIVERING** (spend + impressions evidenced in Ads Manager; do not infer from Shopify UTM alone)  
**As of (Meta UI):** 2026-09-10 **4:33 PM PDT** (account timezone Pacific)  
**Posted:** 2026-09-10 18:57 CDT  
**Date preset:** Maximum (Aug 10, 2023–Sep 10, 2026)  
**Read-only:** no budget / schedule / audience / creative / status mutations

## Objects + literal delivery

| Object | ID | Effective | Delivery message (literal) |
| --- | --- | --- | --- |
| Campaign | `120249394288760482` | Active / On | **Ad sets inactive** |
| Ad set | `120249394288770482` | Active / On | **Processing** |
| Ad | `120249394288750482` | Processing / On | **Processing** |

## Lifetime metrics (UI; em dash = not shown → UNKNOWN, not zero)

| Object | Amount spent | Impressions | Link clicks | Landing page views | Results / Purchases |
| --- | ---: | ---: | --- | --- | --- |
| Campaign | **$0.82** | **17** | — (**UNKNOWN**) | — (**UNKNOWN**) | —; result type Website Purchase |
| Ad set | **$1.05** | **23** | — (**UNKNOWN**) | — (**UNKNOWN**) | —; Website Purchase |
| Ad | **$1.74** | **40** | — (**UNKNOWN**) | — (**UNKNOWN**) | —; Website Purchase |

**First delivery timestamp:** **UNKNOWN**  
**Note:** Campaign / ad-set / ad spend+impr differ in the same Maximum preset (UI lag / attribution rollup). Reported as shown; not reconciled into a single invented total.

## Budget / schedule (unchanged)

| Field | UI value |
| --- | --- |
| Lifetime budget | **$20.00 USD** (campaign; ad set using campaign budget) |
| Schedule start (UI) | Sep 10, 2026, **4:06 PM PDT** |
| Schedule end (UI) | Sep 10, 2026, **7:50 PM PDT** (= Sep 11 **02:50 UTC** / **9:50 PM CDT**) |
| Schedule warning | “Ends today” |
| Spend-pace warning | “Your campaign is ending soon. You are likely to spend your entire budget by the time your campaign ends. To slow your budget spend, add more time to your schedule.” — **not acted on** (no extension) |

## Old campaign

`PP-BABY-ADS-001` `120249328905520482`: confirmed **Off** / delivery **Off**. Not toggled.

## Shopify UTM caveat (Owner)

Do **not** call DELIVERING from Shopify `pp_genealogy_20_001` sessions alone. This status is from Meta spend/impressions only. Shopify-tagged sessions remain unverified as paid-ad arrivals until platform clicks/LPVs are readable.

## Freeze

No budget/date/audience/objective/creative/price/page/payment/Bing changes. No ad clicks. No automatic schedule extension.

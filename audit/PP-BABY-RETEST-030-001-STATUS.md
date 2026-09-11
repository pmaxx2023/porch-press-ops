# PP-BABY-RETEST-030-001 — PUBLISHED — IN REVIEW

**Bot:** Shopify_Bot  
**Status enum:** **ACTIVE — DELIVERY NOT YET OBSERVED** (was PUBLISHED — IN REVIEW)  
**As of:** 2026-09-11 00:04 CDT  
**Authority:** Mega AUTHORIZE PP-BABY-RETEST-030-001 · PM $30 Facebook spending cap  
**Account:** AFK Designs `1083994074091782` (Pacific)

## Objects
| Object | Name | ID | Delivery (publish) |
| --- | --- | --- | --- |
| Campaign | `PP-BABY-RETEST-030-001` | `120249397274570482` | In review |
| Ad set | `PP-BABY-RETEST-030-001-AS` | `120249397274580482` | In review |
| Ad (control) | `PP-BABY-ID-CONTROL-v1` | `120249397274560482` | In review |
| Ad (challenger) | `PP-BABY-FINITE-CHALLENGER-v1` | `120249397434260482` | Processing after publish |

## Config verified
| Field | Value |
| --- | --- |
| Objective | Sales → Website → **Purchase** |
| CTA | **Shop now** |
| Lifetime budget | **$30.00 USD** (campaign; not daily) |
| Schedule (UI) | Sep 10, 2026 **9:25 PM** – Sep 18, 2026 **9:59 PM PDT** (~Sep 18 **11:59 PM CDT**) |
| Audience | US; no new hard interest controls |
| Control URL | `…/genealogy-mystery-case?utm_source=meta&utm_medium=paid&utm_campaign=pp_baby_retest_030&utm_content=id_control` |
| Challenger URL | `…/utm_content=finite_challenger` |

## Creative notes
- Meta Image ad format accepted **one media item per ad**; control opening-story secondary image **not** added (cover used).
- Challenger published with census/cover assets as available.

## Preserve
- `PP-BABY-ADS-001`: **Off** (confirmed)
- `PP-GENEALOGY-20-001`: **not restarted by this publish**; UI may still show switch On from prior Completed stop — Delivery must remain Completed / not delivering (verify follow-up if needed)
- Bing $15 untouched · Baby $19.99 · no partner sends · no store redesign

## Starting metrics
Spend / impr / clicks / LPVs / purchases: **not yet observed** (in review). Will not call DELIVERING until spend/impr evidence.


---

## Status refresh — 2026-09-11 00:11 CDT

### Genealogy preserve check (read-only)
`PP-GENEALOGY-20-001` `120249394288760482`: Delivery **Completed** · spend still **$19.95** · not delivering.

### Retest objects
| Object | ID | Delivery (literal) |
| --- | --- | --- |
| Campaign | `120249397274570482` | **Ad sets inactive** |
| Ad set | `120249397274580482` | **Active** |
| Control ad | `120249397274560482` | **Active** |
| Challenger ad | `120249397434260482` | **Active** |

**Enum:** **ACTIVE — DELIVERY NOT YET OBSERVED** (ads Active; no spend/impr evidenced this pass → not DELIVERING yet).


---

## Reconcile “Ad sets inactive” vs Active — 2026-09-11 00:20 CDT

**Diagnosis:** transient Ads Manager **rollup lag**. After reload, campaign Delivery = **Active** (matching ad set + ads). No Off/ineligible/schedule/CTA/billing block.

| Object | Switch | Delivery |
| --- | --- | --- |
| Campaign `120249397274570482` | On | **Active** |
| Ad set `120249397274580482` | On | **Active** |
| Control `120249397274560482` | On | **Active** |
| Challenger `120249397434260482` | On | **Active** |

- Lifetime budget **$30** confirmed
- Schedule Sep 10 **9:51 PM** – Sep 18 **9:59 PM PDT** (start past)
- Spend **$0.00** · impressions **—** (UNKNOWN / none)
- **Changes:** none
- **Enum:** **ACTIVE — DELIVERY NOT YET OBSERVED**

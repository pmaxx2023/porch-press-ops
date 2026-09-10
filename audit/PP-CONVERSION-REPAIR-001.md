# REPAIR LIVE — PP-CONVERSION-REPAIR-001

**Bot:** Shopify_Bot  
**Verified:** 2026-09-10 13:16 CDT  
**Theme:** Refresh `152900272426`  
**Backups:** `porch-press/store-design/backups/pp-conversion-repair-001/`  
**Screenshots:** `porch-press/audit/pp-conversion-repair-001/screenshots/`

## Applied

### A — Homepage Baby hero (`templates/index.json`)
- Removed paid-hero “Free to play. No download or sign-up.”
- Trailing paras → Owner `$19.99 · One complete printable case` + Explore / Try Roscoe free links
- Button label → **View the $19.99 case** → Baby PDP
- Mabel story + digital-format line preserved
- Separate Roscoe free section unchanged

### B — Search landing (`sections/pp-genealogy-mystery-case.liquid`)
- Mobile `@media (max-width: 899px)`: buy-block `order: 5`, cover-wrap `order: 6`
- Both CTAs → `Add to cart — {{ baby_variant.price | money }}`
- Submit `max-width: 352px; min-height: 48px`
- Forms/variant `52494545486122` / qty 1 / `_pp_entry=search_lp_v1` preserved

### C — Baby template (`templates/product.baby.json`)
- `mobile_thumbnails`: `hide` → **`show`**

### Owner description
- Preserved; public “Look inside before you decide” / `pp-baby-evidence-preview` confirmed

## Verification (read-only — no ATC)
| Check | Result |
| --- | --- |
| Homepage hero label + $19.99 copy + links | PASS |
| Baby not called free in hero; Free to play only in Roscoe section | PASS |
| Search LP mobile buy above cover | PASS |
| Search LP buttons “Add to cart — $19.99” | PASS |
| Both LP forms id/qty/_pp_entry | PASS |
| Baby evidence preview + $19.99 | PASS |
| Baby mobile thumbnails visible | PASS |
| Storefront console errors | none observed |
| Controlled ATC/checkout-entry QA (≤2 permitted) | **NOT USED** — read-only DOM/CDP/layout sufficient |
| porchpress cookies cleared after verify | yes |

## Unchanged
$19.99 · titles · Meta Aud1 · Bing paused/$0 · partner drafts unsent · no redesign

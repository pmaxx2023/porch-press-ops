# REPAIR LIVE — PP-STEP-B-REPAIR-001

**Bot:** Shopify_Bot (executor)  
**Verified:** 2026-09-10 22:48 CDT  
**Theme:** Refresh `152900272426`  
**Shop:** b528dc / porchpress.store  
**Backups:** `porch-press/store-design/backups/pp-step-b-repair-001/`  
**Work copies:** `porch-press/store-design/work/pp-step-b-repair-001/`  
**Screenshots:** `porch-press/audit/pp-step-b-repair-001/screenshots/`

## Applied (minimal reversible)

### 1 — Baby mobile PDP compact purchase strip (`templates/product.baby.json`)
- Added Baby-template-only `custom_liquid` block `pp_purchase_strip` **immediately after `title`**
- Strip copy uses **live variant price**: `{{ variant.price | money }} · Digital PDFs · Nothing ships` + Add to cart form (`variant 52494545486122`, `properties[_pp_entry]=baby_pdp_strip_v1`)
- Mobile compacting: section `padding_top` 60→12, `padding_bottom` 60→36; light mobile CSS for vendor/title/strip spacing
- **Preserved:** Owner description / `pp_baby_facts`, gallery, `mobile_thumbnails=show`, $19.99 variant, existing buy_buttons further down
- **Checksum:** `3a1679dfc9ecdc25cd871fefb0260df5` · updated `2026-09-10T23:48:16-04:00`

### 2 — Homepage Roscoe free vs paid clarity
- **`templates/index.json`** cases description → printable editions vs free browser investigation note  
  Checksum `ddd921044caefa8feae149429630c481`
- **`snippets/card-product.liquid`** — Roscoe handle only: “Printable edition — $19.99 · Free browser investigation” under price  
  Checksum `41ac0de6dd05246f9d4c1bacafa6b89d`
- **Collection `genealogy-mysteries` (517492015402)** body_html (what featured-collection actually renders when `show_description=true`) updated to:  
  **Printable editions — $19.99 each** + link to free browser investigation (separate from printable edition)  
  Roscoe **product price unchanged** ($19.99); free page unchanged

### 3 — Stale cart $9.99 investigation + fix
| Check | Result |
| --- | --- |
| Live Baby variant `52494545486122` | **$19.99**, compare_at `null` |
| Price rules / automatic discounts | none |
| Selling-plan allocations | none observed |
| Hardcoded `9.99` in `cart.js` / `product-form.js` / `cart-drawer.js` / `buy-buttons.liquid` | **none** |
| PDP HTML `$9.99` | Shop Pay installment `price_per_term` only (not cart/variant price) |
| Historical cause | **PP-PRICE-1999-001** raised Baby (and catalogue) from **$9.99 → $19.99**; pre-change cart lines can persist old line price in a browser session |
| Fresh ATC (`cart/add.js`) | line **price_cents=1999**, total **$19.99**; then cart cleared |
| Storefront code change required for fresh ATC | **No** — already uses live variant; documented stale-session path |

## Backups listed
- `templates__product.baby.json` (pre-strip)
- `templates__index.json`
- `snippets__card-product.liquid`
- `snippets__buy-buttons.liquid`
- `snippets__price.liquid`
- `sections__featured-collection.liquid`
- `sections__pp-free-teaser.liquid`
- `assets__cart.js` / `assets__product-form.js`
- `collection_genealogy-mysteries.json`

## Verification
| Check | Result |
| --- | --- |
| Mobile 390×844: title + strip + ATC in first viewport | **PASS** (stripFullyInView; no title/strip overlap; thumbs visible) |
| Strip shows live `$19.99 · Digital PDFs · Nothing ships` + Add to cart | **PASS** |
| Homepage cases desc distinguishes printable vs free browser | **PASS** |
| Roscoe card note printable edition + free browser link | **PASS** |
| Fresh ATC Baby → cart $19.99 (not $9.99) | **PASS** |
| Stale $9.99 path explained | **PASS** (pre-price-change session / Shop Pay installment is not cart price) |
| Baby $19.99 / titles / Owner narrative / Bing / Meta paused | **unchanged** |
| No Meta spend / no real paid orders | **confirmed** |

### Screenshot evidence
- `baby-pdp-mobile-390-final.png` — above-fold strip under title
- `baby-pdp-mobile-strip-in-view.png` — strip + facts + lower ATC
- `roscoe-card-edition-note.png` — printable vs free note
- `homepage-cases-mobile.png` — cases section

## Unchanged
Baby $19.99 · mystery narrative authorship · Bing $15 · paused Meta · no redesign of full PDP · free-investigation page body

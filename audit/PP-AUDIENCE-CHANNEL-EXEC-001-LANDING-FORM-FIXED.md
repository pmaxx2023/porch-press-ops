# LANDING FORM FIXED — PP-AUDIENCE-CHANNEL-EXEC-001 Workstream B

**Verified:** 2026-09-10 07:17:34 CDT  
**URL:** https://porchpress.store/pages/genealogy-mystery-case  
**Theme asset:** `sections/pp-genealogy-mystery-case.liquid` (theme `152900272426`)  
**Backup:** `porch-press/store-design/backups/pp-audience-channel-exec-001/sections__pp-genealogy-mystery-case.liquid.pre-owner-form-fix`  
**QA UTM (exclude from acquisition):** `utm_source=formfix&utm_medium=qa&utm_campaign=pp_audience_channel_exec_001`  
**No ATC / checkout / order.**

## Forms (public HTML after hard refresh)

| Form ID | Action | id.value | quantity.value | properties[_pp_entry].value | Submit enabled |
| --- | --- | --- | --- | --- | --- |
| `pp-gmc-product-form-top` | `/cart/add` | `52494545486122` | `1` | `search_lp_v1` | `true` |
| `pp-gmc-product-form-bottom` | `/cart/add` | `52494545486122` | `1` | `search_lp_v1` | `true` |

## Change
Bound both forms to live Baby `selected_or_first_available_variant` via Liquid; rendered hidden inputs use real `value` attributes (not data-* only).

## Console
Storefront-origin console check deferred to browser CDP subagent (pending).

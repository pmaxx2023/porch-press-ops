# Porch Press claim ledger

Prepared 2026-09-29. Store: **porchpress.store**. This ledger supports the ad and landing-page claims without treating configuration as completed customer delivery.

| Claim used | Current source | What it establishes |
| --- | --- | --- |
| Published collection landing page | `evidence/publication-verification.json`; Shopify Page `166701728042`, published on 2026-09-29 | HTTP 200, correct collection/price/discount and actual preview; TV homepage preserved |
| Local preview layout and FAQ keyboard behavior | `evidence/layout-verification.json` | Passed at 320/390/768/1440 widths, no horizontal overflow/broken images; does not establish integrated live Shopify rendering |
| Local integrated-theme layout | Root verification statement, 2026-09-29: published page HTML plus 21 actual theme CSS files rendered locally at 390/1440 widths, scripts/analytics disabled | Full-width section, no horizontal overflow/duplicate title, visible CTA; live-browser workflow and tracking remain unverified |
| Four cases: Baby in a Basket, The Inheritance, Roscoe’s Grave, The Wrong Widow | Shopify Admin product verification, 2026-09-29; `evidence/products.json` | Correct current Porch Press product identities and existing variants |
| $39.99 USD for one of each case | `evidence/cart-verification.json`; `evidence/checkout-verification.json` | Four items at $51.96, fixed $11.97 discount, $39.99 total; checkout contains all four titles, the price and code |
| Discount code `PORCHFOUR3999` | Shopify Admin verification, 2026-09-29; DiscountCodeNode `1653638562090`; cart evidence | Configured fixed discount applies to the verified four-product cart |
| Printable digital PDFs; nothing ships | Current individual PDPs below; cart `requires_shipping: false` for all four items | Product format and shipping status; no physical case shipment promised |
| Fictional family-record investigations | Current individual PDP descriptions; `evidence/product-copy.txt` | Entertainment cases built around family identity, inheritance, burial identity and widow-pension claims; no blanket murder claim |
| Play solo or together | Current individual PDP descriptions; `evidence/product-copy.txt` | Supported use; no age, duration or difficulty promise |
| Every case includes player packet, progressive hints, separate sealed solution and START-HERE notes | Current individual PDP descriptions; `evidence/product-copy.txt` | Advertised contents; separate solution protects spoilers |
| Four existing downloads are configured | Root Shopify Admin verification, 2026-09-29: each product has nonempty `download_url` and `download_file_id` | Configuration only; does not prove email receipt, working customer links or successful delivery |

## Individual case hooks

| Case | Claim used | Current PDP |
| --- | --- | --- |
| Baby in a Basket | A baby arrived without her birth parents’ names; investigate her birth family through records. | [Baby in a Basket](https://porchpress.store/products/baby-in-a-basket) |
| The Inheritance | Three living claimants dispute a mill; the will makes birth order and relationship decisive. | [The Inheritance](https://porchpress.store/products/the-inheritance) |
| Roscoe’s Grave | A mason is ready to inscribe a stone; the burial index gives a conflicting surname. | [Roscoe’s Grave](https://porchpress.store/products/roscoes-grave) |
| The Wrong Widow | Two women claim the same Civil War soldier’s widow’s pension; compare the supporting papers. | [The Wrong Widow](https://porchpress.store/products/the-wrong-widow) |

“Two Claims. One Soldier.” describes competing claims; it does not assert both women are legally that soldier’s widow. “Compare the evidence” describes the activity, not a validated gameplay-quality result.

## Proof still open

- Integrated live Shopify browser rendering, live mobile/desktop CTA interaction and Google destination-policy eligibility. The published URL itself is verified HTTP 200.
- Customer receipt and successful access to each of the four downloads.
- Deduplicated Google Purchase measurement, reconciled to actual paid non-test Shopify transactions.
- Keyword Planner demand and bid estimates; actual contribution margin and paid-search purchase rate.
- Google account currency/timezone, policy/billing/overlap state, authorized total budget and flight.

No testimonials, bestseller claims, customer demographics, playtimes, difficulty labels, instant-delivery guarantees or ad-performance forecasts are asserted.

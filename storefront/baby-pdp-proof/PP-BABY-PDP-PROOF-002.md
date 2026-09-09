# PP-BABY-PDP-PROOF-002 — authorized conversion treatment

**Owner:** Owner_Bot — Porch Press  
**Authorized by PM:** 2026-09-09 chat instruction to make the evidence-backed recommended changes  
**Target:** `https://porchpress.store/products/baby-in-a-basket`  
**Product:** `10295874814250` · variant `52494545486122` · current price `$9.99`  
**Executor:** Shopify_Store_Designer / Shopify_Bot through the existing Grok workflow

## Why this treatment

Current verified shop-day baseline at 2026-09-09T19:23:34-04:00:

- 14 Baby landing sessions
- 0 real-customer add-to-carts
- 0 real-customer reached checkouts
- 0 completed purchases
- the one Shopify ATC / checkout event was the Designer's internal preflight and must remain excluded

Routing is not the defect: paid `a_identity` traffic lands on Baby. The live PDP has a working, enabled CTA and repeated digital-delivery copy, but only one conceptual cover image. There is no interior case-page preview, sample exhibit, or downloadable preview. The page also shows a `Pay over time for orders over $35.00` message and quantity selector beside a $9.99 digital download.

The hypothesis is **product tangibility + decision clarity**, not a new hero, discount, or CTA color. Baymard research says product imagery is a primary evaluation path and that included-item imagery should be paired with exact descriptive text. Shopify's unfamiliar-store purchase study likewise found shoppers focused heavily on PDP imagery, descriptions, and transaction details. Comparable printable-mystery stores with substantial displayed review volume repeatedly show actual materials, concrete contents, and a short play path before purchase. This is observational and cross-category evidence, not a guaranteed lift.

Research:
- https://baymard.com/blog/product-images-descriptive-text
- https://baymard.com/blog/product-descriptions
- https://baymard.com/blog/structure-descriptions-by-highlights
- https://www.shopify.com/blog/customer-trust-checklist
- https://help.shopify.com/en/manual/products/details/product-descriptions/write
- https://atwistofdate.co.uk/products/cold-case-file
- https://mastersofmystery.com/collections/cold-case-files/products/unsolved-cold-case-files-game-edward-munst-unsolved-murder-mystery-physical-game

## Authoritative assets

Use only these repository assets:

- Primary conceptual artwork: `marketing/Baby-in-a-Basket/02-who-was-she-before-sutton.png` · Git blob `e8966ac7e85c00f696ad3abf40acd48158452b94`
- Spoiler-free preview: `marketing/Baby-in-a-Basket/Baby-in-a-Basket-Preview.pdf` · Git blob `a02d26a528a4e5f00eada7c07fbd985e1d0ce85c`
- Listing truth: `marketing/Baby-in-a-Basket/Storefront-Listing.md`
- Customer release checksum: `60f2386013a096438ca2e772f241e17044b82d56b1bfccab9d32a011ef6b362e`

The cover artwork is conceptual. Never call it an included exhibit. Preview PDF pages 2 and 3 are explicitly spoiler-free. Do not expose other customer pages.

## Required implementation

### 1. Preserve and back up

Before mutation, save:

- product description HTML
- product-media IDs, filenames, alt text, and order
- affected product-template settings, snippets, and theme assets
- desktop and mobile before screenshots

Record the active theme ID and backup paths. Preserve product price, availability, handle, variant, sales channels, SEO identity, and `porchpress.download_url`.

### 2. Make the product visible

Keep the current, ad-matching cover as media position 1.

Mechanically render the exact repository preview PDF without rewriting, cropping, redrawing, or generative alteration:

- media position 2: preview PDF **page 3**, high-resolution PNG on white; alt text: `Spoiler-free fictional census exhibit from Baby in a Basket`
- media position 3: preview PDF **page 2**, high-resolution PNG on white; alt text: `Spoiler-free opening story page from Baby in a Basket`

Ensure both pages remain legible in the existing lightbox. Upload the original three-page preview PDF to Shopify Files and place a text link near the facts block:

> Preview 3 spoiler-free pages

Open in a new tab. Verify the public file URL loads. Do not call the preview a free game.

### 3. Tighten the buy column, Baby only

Immediately after the live price and before the purchase controls, add this exact compact block:

> **Who was she before Sutton?**  
> 36-page player case · 20 fictional exhibits · 6 deductions  
> Play solo or together · Every clue included · No host or outside research  
> Printable digital PDFs · Nothing ships

Then show the preview link.

On Baby only:

- hide the `Pay over time for orders over $35.00` installment message
- hide the visible quantity selector and retain quantity `1` in the product form
- keep both the existing **Add to cart** and **Buy with Shop** controls
- keep the already approved post-button sentence unchanged
- do not add a countdown, scarcity, sale badge, guarantee, fake review, trust badge, pop-up, or sticky purchase bar

Keep the cover before product information on mobile. Remove the two irrelevant rows above so the purchase controls move upward naturally; do not reorder the entire mobile grid in this treatment.

### 4. Replace the long description with this exact structured copy

> **A baby was left in a basket. The names of her birth parents never came with her.**
>
> Mabel Ruth Sutton grew up knowing the family who raised her—but not who she was before Sutton. Follow census entries, compare birth records, and trace household connections to reconstruct her beginnings.
>
> ## Follow the paper trail
>
> Compare four possible birth identities, test the household evidence, complete six deductions, and make your case before opening the sealed solution.
>
> ## Inside your case
>
> - 36-page player packet with the story, records, and working pages
> - 5 pages of progressive hints
> - 8-page sealed solution
> - START-HERE instructions
> - Optional 52-page combined printing file
>
> Use the separate PDFs or the optional combined printing file—not both.
>
> ## How to play
>
> 1. Open the player packet and read the case.
> 2. Compare the records and complete six deductions.
> 3. Use progressive hints if you need them, then open the sealed solution when you are ready.
>
> ## Print or use the PDFs
>
> Every clue is included. No host, internet, outside research, or cutting is required. Print in grayscale on US Letter at 100%, or A4 using Fit.
>
> ## Questions
>
> **Is this a physical product?**  
> No. This is a digital set of printable PDFs. Nothing ships.
>
> **Can I play alone?**  
> Yes. Play solo or work through the evidence together.
>
> **What if I get stuck?**  
> Use the five-page progressive hints file. The answer remains separate in the eight-page sealed solution.
>
> **Are these real family records?**  
> No. This is a fictional genealogy mystery using newly designed, fictional period-style records.

Render the sections as accessible, scannable Shopify HTML. The Questions may use native `details/summary` accordions if the theme supports them without JavaScript; otherwise keep plain headings and text.

### 5. Verification and rollback

Verify the published page read-only; do not add to cart or enter checkout.

Required checks:

- desktop at approximately 1363 × 936 and mobile at 390 × 844
- cover remains first and matches the ad promise
- three media items are present and ordered correctly
- both preview images zoom and stay legible
- the three-page preview link opens publicly
- exact facts block appears beside the decision controls
- installment message and quantity selector are absent on Baby only
- Add to cart and Buy with Shop remain enabled
- price remains $9.99
- product/variant IDs and download mapping remain unchanged
- no storefront-origin console error
- no other product, homepage, checkout, ad, audience, budget, or campaign changed

Post before/after screenshots, theme/product/media IDs, Shopify Files URL, changed asset paths, backup path, publish timestamp, and exact rollback steps to issue #5.

## Measurement

Treat this as one versioned PDP package. It is not a randomized A/B test, so do not attribute any later movement to an individual component.

At the publish timestamp:

- freeze the pre-change baseline above
- start a new post-change counter at zero
- keep Baby, price, ads, audience, and spend unchanged
- primary read: real-customer ATC per qualified Baby landing
- secondary reads: reached checkout and completed purchase
- exclude internal tests and known bot traffic

Review after the next **25 qualified Baby landing sessions**. If there are still zero real ATCs, report that outcome and propose the next offer/creative hypothesis; do not silently stack another change.

## Prohibited claims

Do not claim instant delivery, verified inbox delivery, playtime, age range, difficulty, replayability, licensing, gifting, sales volume, refund guarantee, or conversion lift. Do not expose spoilers or imply the conceptual cover is an actual archival document.

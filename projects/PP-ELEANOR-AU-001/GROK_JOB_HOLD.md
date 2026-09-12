# GROK JOB — PP-ELEANOR-HOLD-001

Sender: **Owner_Bot — Porch Press (ChatGPT)**
Recipient: existing **Connector_Bot**, routing to the existing Shopify-capable Grok agent
Task type: reversible product-status change
Live publication: **current listing is authorized to become non-buyable; no other publication is authorized**
New spend: **$0**

## Decision

The product manager reports that no customer has purchased **Eleanor Hart Is Missing**. The existing product at `/products/eleanor-hart-is-missing` is being expanded into a materially new agentic edition. Put the current product on a reversible sales hold so its existing claims and package are not sold during development.

Do not delete, duplicate, rename, rewrite, or repurpose the product.

## Exact procedure

1. Resolve the product by exact title **and** handle `eleanor-hart-is-missing`. Record the product GID and current status before mutation.
2. Verify aggregate order/customer-delivery count for this exact product. Do not expose customer data. The expected count is zero. If it is nonzero or cannot be verified, stop with `BLOCKED` before mutation.
3. Record the current Online Store publication state, product status, price, variant ID, media count, delivery-file mapping state, and whether the unpublished Eleanor hero-candidate theme `gid://shopify/OnlineStoreTheme/190769856810` still exists and is unpublished.
4. Make the smallest supported reversible change that removes the product from sale and Online Store discovery. Prefer setting the exact product to `DRAFT`; if the installed workflow requires removing its Online Store publication instead, report that method before using it. Do not alter shared navigation or theme code.
5. Verify in a clean public session that the former PDP is not buyable and the product is absent from storefront search/collections. A cached page, if any, must not offer a working add-to-cart path.
6. Re-read the product through Admin and confirm all preserved fields and mappings remain intact.

## Preserve exactly

- product GID and handle;
- title, description, vendor, type, tags, and collections;
- `$19.99` price and variant identity;
- media and approved preview files;
- current customer ZIP and digital-delivery mapping;
- SEO fields;
- the unpublished hero-candidate theme and its unpublished state;
- every other product, theme, navigation item, campaign, integration, and domain.

## Prohibited

- deletion or archival that breaks the existing handle or delivery configuration;
- edits to copy, price, media, files, variant, theme, navigation, or SEO;
- publication of the hero-candidate theme or new agentic product;
- refunds, customer contact, app installation, paid activity, DNS changes, or ad changes;
- treating a successful mutation response as storefront verification.

## Response contract

Post exactly one acknowledgement:

`ACK PP-ELEANOR-HOLD-001 — <actual bot> — resolved <product gid>`

Then return either:

- `PP-ELEANOR-HOLD-001 COMPLETE` with before/after product status, exact mutation/method, clean public PDP/add-to-cart/search/collection observations, preserved-field comparison, product GID, variant ID, theme observation, and `$0` spend; or
- `PP-ELEANOR-HOLD-001 BLOCKED` with the exact mismatch, completed read-only work, and no mutation.

An ACK, Admin status alone, redirect alone, or screenshot alone is not completion.

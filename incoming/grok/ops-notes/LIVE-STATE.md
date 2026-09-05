# Porch Press — LIVE store state (Shopify_Bot, 2026-09-05)

This overlays the package context with verified live facts. Prefer this over stale “still to verify” notes in the package for store URL, catalog, and delivery.

## Live access
- Brand: **Porch Press**
- Primary storefront: https://porchpress.store (password OFF, SSL ON)
- Also: https://b528dc.myshopify.com → redirects to porchpress.store
- Admin: https://admin.shopify.com/store/b528dc/
- Theme: Refresh (id 152900272426) — design v1 applied (navy/paper/gold, Libre Baskerville + Libre Franklin)
- Shopify_Bot (id fdbe25d2-b576-4432-b730-61a285ece854) owns Admin API publish/fulfill via Porch Press Bot 2 client credentials
- Default: ALWAYS no handoffs to Owner — coordinate with Shopify_Bot for theme publishes and product API writes

## Live catalog ($9.99 each, digital, Genealogy Mysteries collection)
1. The Wrong Widow — /products/the-wrong-widow
2. Eleanor Hart Is Missing — /products/eleanor-hart-is-missing
3. Baby in a Basket — /products/baby-in-a-basket
4. The Last Ashcombe — /products/the-last-ashcombe
5. The Inheritance — /products/the-inheritance
6. Roscoe’s Grave — /products/roscoes-grave
7. If I Were King — /products/if-i-were-king

Digital delivery: product metafield `porchpress.download_url` + Shopify_Bot fulfill routine (not native Digital Downloads app). Pipeline: /workspace/porch-press/PIPELINE.md and skill publish-porch-press-shopify.

## Design files
- Spec: /workspace/porch-press/store-design/STORE-DESIGN.md
- Apply report: /workspace/porch-press/store-design/APPLY-REPORT.md
- Full agent package: /workspace/porch-press/agent-package/shopify-store-designer-package.md
- Modules: /workspace/porch-press/agent-package/modules/

## Operating split
- You: merchandising, visual/theme specs, copy, conversion experiments, page structure
- Shopify_Bot: Admin API implementation (products, theme asset uploads, fulfill) — ping Shopify_Bot to publish your specs; do not ask Owner to click admin

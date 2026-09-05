# Porch Press — Shopify publish + digital delivery (no handoffs)

**Store:** `b528dc.myshopify.com` (Porch Press)  
**Goal:** Shopify_Bot publishes mysteries and delivers download links with **zero user clicks** — no Digital Downloads app UI, no admin handoffs.

## Layout

| Path | Role |
|------|------|
| `shopify_client.py` | Client-credentials auth, 24h token cache, REST + GraphQL |
| `publish_mystery.py` | Create/update one product + cover + ZIP + metafields + collection + Online Store |
| `fulfill_digital_orders.py` | Poll paid/unfulfilled orders; fulfill with `trackingInfo.url` = download CDN URL |
| `backfill_wave1_metafields.py` | Attach `porchpress.download_url` to the four wave-1 products |
| `.token_cache.json` | Local access-token cache (do not commit / do not log) |

Secrets live only at the connector path under `agent-data/connector-secrets/.../shopify.json`. Scripts never print tokens or client secrets.

## Auth

1. Load `client_id`, `client_secret`, `shop` from secrets JSON.
2. `POST https://{shop}.myshopify.com/admin/oauth/access_token` with `grant_type=client_credentials`.
3. Cache token ~23h in `/workspace/porch-press/.token_cache.json`.
4. Send `X-Shopify-Access-Token` on Admin API `2025-01` REST/GraphQL.

## Publish one mystery

```bash
cd /workspace/porch-press
python3 publish_mystery.py \
  --title "The Wrong Widow" \
  --price 9.99 \
  --handle the-wrong-widow \
  --sku THE_WRONG_WIDOW \
  --listing-copy /workspace/wrong-widow/pitch/listing-copy.md \
  --cover /workspace/wrong-widow/pitch/cover-the-wrong-widow.png \
  --zip /workspace/wrong-widow/release/customer/the-wrong-widow-print-bundle.zip
```

Pipeline steps (idempotent by handle):

1. Create or update product — Active, vendor **Porch Press**, type **Genealogy mystery**, `requires_shipping=false`.
2. Staged-upload cover → `productCreateMedia`.
3. Find existing GenericFile by filename, else staged-upload ZIP → `fileCreate`.
4. Set metafields:
   - `porchpress.download_url` (url / single_line_text) = CDN URL
   - `porchpress.download_file_id` = GenericFile GID
5. Ensure collection `genealogy-mysteries`; add product.
6. `publishablePublish` to Online Store.
7. Print JSON summary (ids, handle, admin URL) — no secrets.

## Fulfill digital orders

```bash
cd /workspace/porch-press
python3 fulfill_digital_orders.py            # live
python3 fulfill_digital_orders.py --dry-run  # inspect only
```

For each paid + unfulfilled order:

1. Read line-item product metafield `porchpress.download_url`.
2. Skip if missing or already fulfilled / no remaining FO qty.
3. `fulfillmentCreateV2` (fallback `fulfillmentCreate`) with:
   - `notifyCustomer: true`
   - `trackingInfo.company`: `Porch Press Digital`
   - `trackingInfo.number`: `DIGITAL-DOWNLOAD`
   - `trackingInfo.url`: the CDN download URL  
   Customer shipping/fulfillment email therefore includes the download link.
4. Exit 0 with counts (`seen` / `fulfilled` / `skipped` / `errors`).

Schedule: Shopify_Bot can cron or poll this after checkout webhooks; no merchant UI.

## Wave-1 backfill

```bash
cd /workspace/porch-press
python3 backfill_wave1_metafields.py
```

| Handle | Customer ZIP |
|--------|----------------|
| `the-wrong-widow` | `/workspace/wrong-widow/release/customer/the-wrong-widow-print-bundle.zip` |
| `eleanor-hart-is-missing` | `/workspace/ashcombe-edits/output/Eleanor-Hart-Customer.zip` |
| `baby-in-a-basket` | `/workspace/ashcombe-edits/output/Baby-in-a-Basket-Customer.zip` |
| `the-last-ashcombe` | `/workspace/ashcombe-edits/output/The-Last-Ashcombe-Customer.zip` |

Reuses Content/Files GenericFiles when filenames match; otherwise re-uploads.

## Shopify_Bot runbook (zero handoffs)

1. **New title ready** → run `publish_mystery.py` with release folder paths.
2. **After any catalog change** → optional `backfill_wave1_metafields.py` / verify GraphQL metafields.
3. **Ongoing** → `fulfill_digital_orders.py` on a short interval (or order paid webhook → same script).
4. Never ask the user to open Digital Downloads, click Fulfill, or paste CDN URLs.

## Verify metafields (GraphQL)

```graphql
{
  productByHandle(handle: "the-wrong-widow") {
    handle
    metafield(namespace: "porchpress", key: "download_url") { value type }
    metafield2: metafield(namespace: "porchpress", key: "download_file_id") { value }
  }
}
```

## Out of scope

- Native Shopify Digital Downloads app (no public API) — do not depend on it.
- Author/source ZIPs — never attach as customer downloads.

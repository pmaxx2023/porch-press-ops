# TRAFFIC SNAPSHOT — PP-AUDIENCE-CHANNEL-EXEC-001

**As of:** 2026-09-10 08:17 CDT  
**ShopifyQL shop day:** 2026-09-10 (America/New_York ShopifyQL day)  
**Method:** Admin GraphQL `shopifyqlQuery` FROM sessions (not Live View)  
**Decision gate:** no hero/PDP/Meta changes from session count alone.

## Totals

| Metric | Value |
| --- | --- |
| Sessions | 44 |
| Sessions with ATC | 0 |
| Reached checkout | 0 |
| Completed checkout | 0 |
| Known QA UTMs excluded (`ownerqa` / `formfix` / medium `qa`) | 1 |
| Sessions minus known QA | 43 |
| Morning baseline (Workstream A ~06:54 CT) | 14 sessions / 0 ATC |

## By landing

| Landing | Sessions | ATC | Checkout | Purchase |
| --- | ---: | ---: | ---: | ---: |
| `/products/baby-in-a-basket` | 10 | 0 | 0 | 0 |
| `/pages/genealogy-mystery-case` | 8 | 0 | 0 | 0 |
| `/` | 7 | 0 | 0 | 0 |
| `/products/the-wrong-widow` | 5 | 0 | 0 | 0 |
| `/products/eleanor-hart-is-missing` | 4 | 0 | 0 | 0 |
| `/products/roscoes-grave` | 3 | 0 | 0 | 0 |
| `/products/the-last-ashcombe` | 3 | 0 | 0 | 0 |
| `/products/if-i-were-king` | 2 | 0 | 0 | 0 |
| `/products/the-inheritance` | 1 | 0 | 0 | 0 |
| `/products/the-woman-in-room-six` | 1 | 0 | 0 | 0 |

## By UTM × landing (raw; QA rows marked)

| Source | utm_source | utm_medium | utm_campaign | Landing | Sessions | Exclude |
| --- | --- | --- | --- | --- | ---: | --- |
| direct | `None` | `None` | `None` | `/` | 6 | no |
| direct | `None` | `None` | `None` | `/products/eleanor-hart-is-missing` | 4 | no |
| direct | `meta` | `paid_social` | `pp_baby_ads_001` | `/products/baby-in-a-basket` | 4 | no |
| direct | `microsoft` | `cpc` | `pp_bing_ads_001` | `/pages/genealogy-mystery-case` | 4 | no |
| search | `None` | `None` | `None` | `/products/the-wrong-widow` | 4 | no |
| direct | `None` | `None` | `None` | `/pages/genealogy-mystery-case` | 3 | no |
| direct | `None` | `None` | `None` | `/products/roscoes-grave` | 3 | no |
| direct | `None` | `None` | `None` | `/products/baby-in-a-basket` | 3 | no |
| search | `None` | `None` | `None` | `/products/the-last-ashcombe` | 2 | no |
| direct | `None` | `None` | `None` | `/products/if-i-were-king` | 2 | no |
| search | `None` | `None` | `None` | `/products/baby-in-a-basket` | 1 | no |
| direct | `None` | `None` | `None` | `/products/the-inheritance` | 1 | no |
| direct | `None` | `None` | `None` | `/products/the-wrong-widow` | 1 | no |
| social | `None` | `None` | `None` | `/` | 1 | no |
| direct | `None` | `None` | `None` | `/products/the-woman-in-room-six` | 1 | no |
| direct | `None` | `None` | `None` | `/products/the-last-ashcombe` | 1 | no |
| social | `meta` | `paid_social` | `pp_baby_ads_001` | `/products/baby-in-a-basket` | 1 | no |
| social | `None` | `None` | `None` | `/products/baby-in-a-basket` | 1 | no |
| direct | `ownerqa` | `qa` | `pp_audience_channel_exec_001` | `/pages/genealogy-mystery-case` | 1 | YES |

## Read

- Dashboard ~37 / +311% is directionally consistent with ShopifyQL (now **44** and climbing during this write).
- **0 ATC / 0 checkout / 0 purchase** on shop day — not demand validation.
- Large direct/no-UTM + multi-PDP spread fits agent/admin verification more than a single external surge.
- Meta `pp_baby_ads_001` present on Baby PDP; **preserve Aud1** (no mutation).
- Bing UTM `pp_bing_ads_001` on search LP present while campaign still not LIVE — treat as preview/build until `BING LIVE`.
- Do **not** change hero/PDP from session count alone.

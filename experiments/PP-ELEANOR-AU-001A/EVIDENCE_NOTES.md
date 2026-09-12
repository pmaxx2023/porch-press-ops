# EVIDENCE_NOTES — PP-ELEANOR-AU-001A

Local base: `http://127.0.0.1:8765`

```bash
cd experiments/PP-ELEANOR-AU-001A
python3 -m http.server 8765
```

## Capture source

All **current** receipts below were captured from functional source SHA:

`63d2da06d1da59f03e6f6be8ae14e84e80853451` (short: `63d2da0`)

Directory: `evidence/63d2da0/`

## Current desktop receipts (1280×800 PNG)

| Case | Path |
| --- | --- |
| Hub | `evidence/63d2da0/01-hub-1280.png` |
| Portal opening + current-question bar | `evidence/63d2da0/02-portal-opening-1280.png` |
| Invalid token | `evidence/63d2da0/03-invalid-1280.png` |
| Valid token | `evidence/63d2da0/04-valid-1280.png` |
| Duplicate token | `evidence/63d2da0/05-duplicate-1280.png` |
| Two-token reveal / receipts / CAST CLAIM | `evidence/63d2da0/06-reveal-receipts-claim-1280.png` |
| Edit trail (CONTESTED → SUPPORTED) | `evidence/63d2da0/07-edit-trail-1280.png` |
| Export / import / reset | `evidence/63d2da0/08-export-reset-1280.png` |
| NMC home | `evidence/63d2da0/09-nmc-home-1280.png` |
| CFD home | `evidence/63d2da0/10-cfd-home-1280.png` |
| LIL home | `evidence/63d2da0/11-lil-home-1280.png` |

## Mobile sticky (accepted, same capture source)

| Case | Path |
| --- | --- |
| 390×844 sticky no-overlap | `evidence/63d2da0/390-sticky-no-overlap.png` |

## Source-tested (no screenshot)

| Case | Note |
| --- | --- |
| Non-pair does not unlock reveal | not captured / source-tested |
| Reversed token order unlocks same reveal | not captured / source-tested |
| Sitemap absolute locs / no 404 entries | not captured / source-tested |
| Unknown route HTTP 404 via http.server | not captured / source-tested |

## Pre-revision / regression context only

Do **not** count as current PASS evidence:

- `evidence/pre-revision/` (includes obsolete common-nav shots and `abbd6c6-reencode/` WebP→PNG copies that were zero-diff re-encodes of pre-`63d2da0` captures)
- Any former former abbd6c6 evidence directory or former generic current/ evidence directory paths

## Mobile sticky note

Portal mobile: `.fixture-banner` is not sticky; `.current-question-bar` sticky at `top: 0`.

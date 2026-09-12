# EVIDENCE_NOTES — PP-ELEANOR-AU-001A

Local base: `http://127.0.0.1:8765` (see README).  
Candidate evidence is under `evidence/` and must match container magic (`.png` = PNG bytes).

## Portal behaviors

| Case | Steps | Expected | Evidence path |
| --- | --- | --- | --- |
| Opening | Load `/portal/` | Lead, research prompt, empty locker, reveal hidden; current-question bar visible | `evidence/abbd6c6/02-portal-opening-with-question-bar.png` |
| Invalid token | Enter `NOT-A-TOKEN` → Validate | Distinct **invalid** status (`role=status` `aria-live=polite`); locker unchanged | `evidence/abbd6c6/03-invalid.png` |
| New valid token | Enter `FIXTURE-NMC-0001` → Validate | Distinct **new valid** status; token listed | `evidence/abbd6c6/04-valid.png` |
| Duplicate token | Re-enter `FIXTURE-NMC-0001` | Distinct **duplicate** status; list unchanged | `evidence/abbd6c6/05-duplicate.png` |
| Non-pair | Add `FIXTURE-NMC-0001` + `FIXTURE-LIL-0001` only | Reveal remains hidden | not captured / source-tested |
| Two-token reveal | Add `FIXTURE-NMC-0001` + `FIXTURE-CFD-0001` | Unlock; receipts first; CAST CLAIM; CROSS-EXAMINATION | `evidence/abbd6c6/06-reveal-receipts-claim-card.png` |
| Reversed token order | Reset; CFD then NMC | Same reveal | not captured / source-tested |
| Classification / edit trail | Contested then Supported | `{status,history}` trail chips e.g. CONTESTED → SUPPORTED | `evidence/abbd6c6/07-edit-trail.png` |
| Export / import / reset controls | View Case state panel | Export/Import/Reset visible; reset reminds export first | `evidence/abbd6c6/08-export-reset.png` |
| Sticky question (≤844) | Portal at 390×844; scroll | `.fixture-banner` not sticky; `.current-question-bar` sticky `top:0`; no overlap; Validate reachable | `evidence/63d2da0/390-sticky-no-overlap.png` |

## Archive homes (current candidate)

| Archive | Evidence path |
| --- | --- |
| Northbridge (NMC) | `evidence/abbd6c6/09-nmc-home.png` |
| Cedar Fork (CFD) | `evidence/abbd6c6/10-cfd-home.png` |
| Lampblack (LIL) 1280×800 | `evidence/current/11-lil-home-1280.png` |

## Accessibility

| Case | Evidence path |
| --- | --- |
| Focus-visible | `evidence/pre-revision/15-portal-focus-visible.png` (pre-revision / regression context — focus ring behavior unchanged) |

## Archive / a11y / sitemap (source-tested)

| Case | Expected | Evidence |
| --- | --- | --- |
| Three archives distinct | Different hierarchy, record-list, masthead, nav voice | NMC/CFD/LIL current homes above |
| Archive nav separation | No Case Portal / Fixture Hub in `.site-nav`; fixture-only hub link only in red banner | current archive homes |
| Focus | No blanket `*:focus { outline: none; }`; `:focus-visible` present | source-tested + focus-visible shot |
| Targets | Controls ≥44×44px; secondary metadata ≥14px | source-tested |
| Sitemap | Absolute `http://127.0.0.1:8765/...` locs; no `404.html` | source-tested |
| 404 pages | No meta refresh; catalog recovery link | source-tested |
| http.server unknown route | HTTP 404 | source-tested (curl below) |

## http.server 404 proof (recorded)

```text
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8765/archives/northbridge-municipal-clippings/no-such-page
# => 404
```

## Mobile sticky

Portal mobile: `.fixture-banner` is **not** sticky; `.current-question-bar` is sticky at `top: 0` (see `evidence/63d2da0/390-sticky-no-overlap.png`).

## Pre-revision / regression context only

These must **not** count as final PASS evidence (obsolete common-nav era):

- `evidence/pre-revision/01-hub-desktop.png`
- `evidence/pre-revision/08-archive-nmc-home.png`
- `evidence/pre-revision/10-archive-lil-home.png` (obsolete LIL — superseded by `evidence/current/11-lil-home-1280.png`)
- `evidence/pre-revision/13-portal-mobile-390.png`
- `evidence/pre-revision/14-archive-nmc-mobile-390.png`
- `evidence/pre-revision/15-portal-focus-visible.png`

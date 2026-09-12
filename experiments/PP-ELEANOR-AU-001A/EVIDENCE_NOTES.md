# EVIDENCE_NOTES — PP-ELEANOR-AU-001A

Parent agent fills screenshot paths. This matrix documents **expected behaviors** the UI must support.

Local base: `http://127.0.0.1:8765` (see README).

## Portal behaviors

| Case | Steps | Expected |
| --- | --- | --- |
| Opening | Load `/portal/` | Lead, research prompt, empty locker, reveal hidden |
| Invalid token | Enter `NOT-A-TOKEN` → Validate | Distinct **invalid** status (`role=status` `aria-live=polite`); locker unchanged |
| New valid token | Enter `FIXTURE-NMC-0001` → Validate | Distinct **new valid** status; token listed |
| Duplicate token | Re-enter `FIXTURE-NMC-0001` | Distinct **duplicate** status; list unchanged (idempotent) |
| Non-pair | Add `FIXTURE-NMC-0001` + `FIXTURE-LIL-0001` only | Reveal remains hidden |
| Two-token reveal | Add `FIXTURE-NMC-0001` + `FIXTURE-CFD-0001` | Reveal unlocks; announce on first unlock; **receipts first** for both tokens; then CAST CLAIM; then CROSS-EXAMINATION |
| Reversed token order | Reset; add `FIXTURE-CFD-0001` then `FIXTURE-NMC-0001` | Same reveal as above |
| Classification | Choose supported / contested / disproved | Saved under `claim_states["FX-CLAIM-001"]` as `{status,history}`; card shows speaker, evidence cited, status; re-classify appends edit trail chips (e.g. CONTESTED → SUPPORTED) |
| Sticky question (≤844) | View portal at 390×844; scroll | Current-question bar sticks under fixture banner; locker Validate remains reachable |
| Export | Export JSON | Download with `case_id` + `schema_version` |
| Import valid | Import prior export | State restored; input cleared |
| Import malformed | Import non-JSON or wrong case_id/schema | Rejected; **file input cleared** so retry works |
| Import oversized | File &gt; 64KB | Rejected; input cleared |
| Import stray fields | Unknown claim IDs / hint IDs / bad tokens | Normalized away; only allowlisted values kept |
| Reset | Confirm reset | Confirm text reminds to **export first**; state cleared |

## Archive / a11y / sitemap

| Case | Expected |
| --- | --- |
| Three archives distinct | Different hierarchy, record-list treatment, masthead geometry, nav voice (not palette-only) |
| Archive nav separation | No Case Portal / Fixture Hub in `.site-nav`; one fixture-only hub link in red banner only |
| Focus | No blanket `*:focus { outline: none; }`; `:focus-visible` ring present |
| Targets | Interactive controls ≥44×44px; secondary metadata ≥14px |
| Sitemap | Absolute `http://127.0.0.1:8765/...` locs; no `404.html` |
| 404 pages | No meta refresh; ordinary catalog recovery link |
| http.server unknown route | `curl` → HTTP 404 (server default; custom `404.html` not auto-served) |

## Screenshot path placeholders (parent fills)

| ID | Path |
| --- | --- |
| opening | _(parent)_ |
| invalid | _(parent)_ |
| valid | _(parent)_ |
| duplicate | _(parent)_ |
| two-token | _(parent)_ |
| reversed-order | _(parent)_ |
| non-pair | _(parent)_ |
| classification | _(parent)_ |
| export | _(parent)_ |
| import | _(parent)_ |
| reset | _(parent)_ |
| nmc / cfd / lil homes | _(parent)_ |
| focus-visible | _(parent)_ |
| mobile-390 | _(parent)_ |


## http.server 404 proof (recorded)

While serving from experiment root on port 8765:

```text
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8765/archives/northbridge-municipal-clippings/no-such-page
# => 404
```

Custom archive `404.html` pages are ordinary recoverable documents (no meta refresh), not auto-wired by `python -m http.server`.

## Mobile sticky (post-abbd6c6)

Portal mobile: `.fixture-banner` is **not** sticky; `.current-question-bar` is sticky at `top: 0` to prevent overlap at 390×844.

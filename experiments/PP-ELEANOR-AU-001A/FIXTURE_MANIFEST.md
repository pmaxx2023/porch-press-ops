# FIXTURE_MANIFEST — PP-ELEANOR-AU-001A

All content in this tree is **FIXTURE / DEVELOPER PREVIEW**. Accession codes use the `FIXTURE-*` prefix only.

## Case

- **case_id:** `PP-ELEANOR-AU-001A-FIXTURE`
- **schema_version:** `1`
- **localStorage key:** `pp-eleanor-au-001a-fixture`
- **known claim ID:** `FX-CLAIM-001` values `{supported, contested, disproved}`
- **known episode IDs:** `FX1`
- **known hint IDs (allowlist):** `FX-HINT-001`, `FX-HINT-002` (none required for spike)
- **notes max:** 8KB (truncated on normalize/save)
- **import max:** 64KB rejected if larger

## Six accession codes

| Accession | Archive | Relative artifact URL |
| --- | --- | --- |
| `FIXTURE-NMC-0001` | northbridge-municipal-clippings | `archives/northbridge-municipal-clippings/artifacts/fixture-nmc-0001.html` |
| `FIXTURE-NMC-0002` | northbridge-municipal-clippings | `archives/northbridge-municipal-clippings/artifacts/fixture-nmc-0002.html` |
| `FIXTURE-CFD-0001` | cedar-fork-deed-room | `archives/cedar-fork-deed-room/artifacts/fixture-cfd-0001.html` |
| `FIXTURE-CFD-0002` | cedar-fork-deed-room | `archives/cedar-fork-deed-room/artifacts/fixture-cfd-0002.html` |
| `FIXTURE-LIL-0001` | lampblack-industrial-ledger | `archives/lampblack-industrial-ledger/artifacts/fixture-lil-0001.html` |
| `FIXTURE-LIL-0002` | lampblack-industrial-ledger | `archives/lampblack-industrial-ledger/artifacts/fixture-lil-0002.html` |

## Reveal condition (exact two-token pair)

Cast reveal unlocks when **both** of the following are present in `evidence_tokens` (exact string match, **order independent**):

1. `FIXTURE-NMC-0001`
2. `FIXTURE-CFD-0001`

No other pair triggers the reveal. Before dialogue, the portal shows evidence receipts for both tokens (title, institution, accession ID, source link). Dialogue labels: **CAST CLAIM** then **CROSS-EXAMINATION**.

## Shell URLs (relative to experiment root)

| Surface | Path |
| --- | --- |
| Hub | `index.html` |
| Portal | `portal/index.html` |
| NMC home | `archives/northbridge-municipal-clippings/index.html` |
| CFD home | `archives/cedar-fork-deed-room/index.html` |
| LIL home | `archives/lampblack-industrial-ledger/index.html` |

## Sitemap base

Absolute locs use `http://127.0.0.1:8765/...`. `404.html` is not listed.

## Names used (obviously fake)

Fixture Subject A, Sample Clerk, Northbridge Sample Tribune, Cedar Fork Sample Registry, Lampblack Sample Works, CAST CLAIM, CROSS-EXAMINATION, FX-CLAIM-001.

# PP-ELEANOR-AU-001A — Unpublished FIXTURE Architecture Spike

## One-click local preview

From this directory:

```bash
./serve.sh
```

On Windows:

```bat
serve.bat
```

Both serve on port `8765` and open `http://127.0.0.1:8765/` (hub). Override port with `PORT=9000 ./serve.sh` on Unix.

Still local-only / FIXTURE / noindex — not a public deploy.


**Status:** Developer preview only. Not live game content. Not for indexing or storefront use.

Banner on every page: `FIXTURE / DEVELOPER PREVIEW — NOT LIVE GAME CONTENT`

## Local serve

From this directory (`experiments/PP-ELEANOR-AU-001A/` in repo, or `/workspace/PP-ELEANOR-AU-001A/` on the box):

```bash
python3 -m http.server 8765
```

Open `http://127.0.0.1:8765/` for the hub, or `/portal/` for the case portal.

**Documented local base URL for sitemaps:** `http://127.0.0.1:8765`

All `sitemap.xml` `<loc>` values are absolute same-host URLs under that base (for example `http://127.0.0.1:8765/archives/northbridge-municipal-clippings/index.html`). `404.html` is excluded from sitemaps.

Relative paths are designed for serving from the experiment root.

### Unknown routes and `python -m http.server`

`python3 -m http.server` returns HTTP 404 for paths that do not exist on disk. It does **not** serve each archive’s `404.html` as a custom error document. The static `404.html` files are ordinary catalog recovery pages you can open directly; they use a normal link back to the archive catalog (no meta refresh).

Curl proof (run while the server is listening on 8765):

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8765/archives/northbridge-municipal-clippings/no-such-page
# expected: 404
```

## What this proves

1. One case-portal shell with opening lead, copyable research prompt, evidence locker, and local state.
2. Three visually and editorially distinct fictional archive shells (newspaper / small-house register / industrial DB).
3. Six sample artifact routes using only `FIXTURE-*` accession codes and obviously fake names.
4. Exact-match evidence-token capture with distinct invalid / new-valid / duplicate feedback.
5. One pre-authored cast reveal when both `FIXTURE-NMC-0001` and `FIXTURE-CFD-0001` are present (order independent), with receipts before dialogue.
6. Claim classification: supported | contested | disproved (stored in `claim_states` under `FX-CLAIM-001` as `{ status, history }`; legacy string status upgraded on import). CAST CLAIM card shows speaker, evidence cited, current status, and edit trail.
7. Case-state export (JSON download), import (schema + allowlist normalization, never `eval`), and reset with export reminder.
8. Static HTML, ordinary crawlable links, per-archive `robots.txt` (Disallow all) and absolute-URL `sitemap.xml`.
9. Desktop layout plus 390×844-friendly mobile with sticky current-question bar; shared a11y helpers (`:focus-visible` only, skip link, reduced motion, ≥44px targets, ≥14px secondary metadata).

## Archive identity mapping (DESIGN_DIRECTION characters, FIXTURE content)

| Fixture shell | DESIGN_DIRECTION voice | Nav voice |
| --- | --- | --- |
| northbridge-municipal-clippings | River & Rail–like newsprint | Browse by Date, City Desk, Rail Files, Reporter Notebooks |
| cedar-fork-deed-room | small-house register | The House, Registers, Photographs, Correspondence, About the Record |
| lampblack-industrial-ledger | Ohio River IMP–like industrial DB | Companies, People, Record Groups, Technical Drawings |

Institutional archive nav does **not** include Case Portal or Fixture Hub. Hub→archive and portal→archive links remain. One fixture-only “Dev return: Fixture Hub” link sits inside the red FIXTURE banner on archive pages.

## Non-goals

- No Eleanor Hart canon, no 1912 solution, no real case facts.
- No Shopify / DNS / ads / Meta / Google / Bing changes.
- No authentication, database, or runtime AI API.
- No Pages deployment required for this spike (local-only preview).
- No Porch Press checkout links.

## Cost / live confirmation

- **New spend:** $0
- **Live changes:** none — this commit adds only unpublished static files under `experiments/PP-ELEANOR-AU-001A/`. Shopify theme, DNS, campaigns, and storefront are untouched.

## Valid evidence tokens

| Code | Archive |
| --- | --- |
| `FIXTURE-NMC-0001` | Northbridge Municipal Clippings |
| `FIXTURE-NMC-0002` | Northbridge Municipal Clippings |
| `FIXTURE-CFD-0001` | Cedar Fork Deed Room |
| `FIXTURE-CFD-0002` | Cedar Fork Deed Room |
| `FIXTURE-LIL-0001` | Lampblack Industrial Ledger |
| `FIXTURE-LIL-0002` | Lampblack Industrial Ledger |

**Reveal pair:** `FIXTURE-NMC-0001` + `FIXTURE-CFD-0001` (either order)

See `FIXTURE_MANIFEST.md` for relative URLs and `EVIDENCE_NOTES.md` for the UI test matrix.

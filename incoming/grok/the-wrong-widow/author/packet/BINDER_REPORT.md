# BINDER REPORT — The Wrong Widow (Stage 4)

**Agent:** Binder  
**For:** Director (via parent)  
**Date:** 2026-09-05  
**Status:** Packet built; verification PASS on automated spoiler/field checks

## Deliverable paths

| Path | Role |
| --- | --- |
| `/workspace/wrong-widow/packet/START-HERE.md` | Print notes, how to play, sealed spoiler warning |
| `/workspace/wrong-widow/packet/player.pdf` | Spoiler-free player case (27 pages) |
| `/workspace/wrong-widow/packet/hints.pdf` | H1–H8 only (2 pages) |
| `/workspace/wrong-widow/packet/sealed-solution.pdf` | SEALED answer key + D018 (5 pages) |
| `/workspace/wrong-widow/packet/build_packet.py` | Deterministic ReportLab builder (reads Canon `documents.json`) |
| `/workspace/wrong-widow/packet/_build_meta.json` | Build sidecar (page counts / exhibit lists) |
| `/workspace/wrong-widow/packet/BINDER_REPORT.md` | This report |

**Optional complete-case.pdf:** Not built. Primary customer files are the three separate PDFs (preferred). START-HERE instructs separate print jobs / sealed envelope.

## Page counts

| PDF | Pages |
| --- | --- |
| player.pdf | 27 |
| hints.pdf | 2 |
| sealed-solution.pdf | 5 |

## Exhibit inventory

| Set | Exhibits |
| --- | --- |
| Player (open) | **D001–D017** (17 exhibits) — D018 absent |
| Sealed only | **D018** (Benjamin F. Corbett affidavit) |
| Cold-open order | D001 → D002 → D003 → D004 (fixed; matches Trail `player_start.json`) |
| Hints | H1–H8 from `hint_ladder.json` only |

## Sealed separation method

1. **Separate PDF file** (`sealed-solution.pdf`) — never merged into player.pdf.
2. **Big SEALED banners** on every sealed page header/footer (“DO NOT OPEN UNTIL SUBMITTED”).
3. **START-HERE.md** instructs separate print job + physical envelope.
4. **Automated grep:** player.pdf and hints.pdf contain **zero** `D018`, no Benjamin affidavit body, no “supportable widow is Martha” prose.
5. Builder loads D018 only in `build_sealed_pdf()`.

## Builder notes

- `build_packet.py` loads `/workspace/wrong-widow/canon/documents.json` and renders `recorded_fields` into facsimile layouts (household tables from census arrays; special layouts for D015/D016/D017/D018).
- Internal `noise` keys are **not** printed as player callouts.
- Facsimile footer on every exhibit: “Fictional facsimile for game use — not an authentic historical document.”
- Rebuild: `python3 /workspace/wrong-widow/packet/build_packet.py` (requires reportlab + pypdf).

## HARD Binder risks — checklist

| # | Risk | Result | Notes |
| --- | --- | --- | --- |
| 1 | **D016** Corbin/Ashley vs Corbett/Ashby LARGE/CLEAR | **PASS** | Husband/wife surnames rendered in DocHuge (18pt bold). Strings verified in extracted text: Eli Corbin, Martha Ann Ashley. |
| 2 | **D015** Silas eliminators ON-FACE | **PASS** | Unit “Co. B, 83rd Indiana Infantry”, residence “Dearborn County, Indiana”, age 23, name Silas M. Corbit — all large/visible on decoy line. Verified in text extract. |
| 3 | **Noise discipline** (no tip on Corbit/Eli/age/Wife) | **PASS** | D010/D011 render ordinary census tables only; `noise` field suppressed; no worksheet callouts labeling variants as clues. Automated tip-phrase scan clean. |
| 4 | **Escape from death-cert primacy** | **PASS** | Research catalog cues D005 from D002 date+Ripley; D014 from D005 parties + Ripley/Jefferson; D012 from D002 Ripley+Martha+children — findable without author-only knowledge. |
| 5 | **D018 sealed-only** | **PASS** | Not in player.pdf or hints.pdf (grep). Present only in sealed-solution.pdf with confirmation-only framing. |
| 6 | **Catalog unlocks from opening cues** | **PASS** | Catalog table for D005–D017 uses dates/places/names from D001–D004 (and subsequent unlocked cues). No circular “know Ashby spelling to find Ashby” as sole path — D002 already supplies Ashby + date + county. |
| 7 | **Harriet D017 neighboring/example** | **PASS** | Banner: “NEIGHBORING / EXAMPLE FILE — NOT A CLAIMANT ON ELIAS M. CORBETT'S PENSION” + teaching prose. Catalog note reinforces. |

## Proof risks / Director decisions (flag)

1. **Facsimile fidelity:** Period look is light aged fill + borders + typography — not photographic archival scans. Acceptable for grayscale print game; Proof may want richer texture later (Pitch/production), not blocking.
2. **Catalog fairness:** Cues are explicit in a single index table (more guided than a pure archive dump). Trail asked for unlock-from-opening-cues; Binder chose clarity over obscurity. Director may prefer slightly more elliptical cue wording — flag only.
3. **D016 “compare letter-by-letter” line:** Small instructional footnote on the decree (“Compare letter-by-letter to any other couple under study”) — method nudge, not a spoiler that Corbin≠Corbett. Soft Proof risk if judged too tippy; easy to remove.
4. **No complete-case.pdf:** Preferred three separate customer PDFs. Can merge later with hard page-break SEALED section if Pitch wants a single download — sealed must stay on fresh sheets.
5. **Ads:** Not invented (out of Binder scope per brief).
6. **No blockers** for Director handoff to Proof.

## Verification performed

- Build exit 0; all three PDFs written.
- Page counts via pypdf.
- Text extract asserts: no D018 / no Benjamin affidavit / no Martha-answer spoiler in player+hints.
- D015/D016 key strings present in player extract.
- D001–D017 present in player; D018 only in sealed; H1–H8 in hints.

## Handoff

**Next:** Proof (fairness / spoiler / act pacing review) → Pitch (ads — separate).  
Binder does not invent ads or a different mystery.


## Polish (Director pre-Ship) — 2026-09-05

Stripped player-facing trap-softening labels. Canon `documents.json` titles unchanged; `PLAYER_TITLE_OVERRIDES` in `build_packet.py` prints neutral exhibit titles for D015/D016/D017. Catalog D016 retitled to “Divorce decree extract — Ripley County” (no “Near-name”). D015 body no longer says “Similar-name scan result.” D017 keeps neighboring / not-a-claimant fairness banner; removed “TEACHING EXAMPLE” header tag. D016 letter-by-letter footnote kept. Rebuild VERIFY OK; player grep clean for Decoy / False divorce / red-herring / Near-name.

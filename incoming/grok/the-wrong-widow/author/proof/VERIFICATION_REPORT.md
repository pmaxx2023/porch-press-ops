# VERIFICATION REPORT — The Wrong Widow (Stage 5 / Proof)

**Agent:** Proof  
**Reports to:** Director only (not Owner)  
**Date:** 2026-09-05 (America/Chicago)  
**Packet:** `/workspace/wrong-widow/packet/`  
**Deliverable root:** `/workspace/wrong-widow/proof/`

---

## Verdict

| Gate | Result |
| --- | --- |
| **Overall (Proof)** | **CONDITIONAL PASS** — no blocking defects found |
| Structural / automated | **PASS** |
| Visual / grayscale readability | **PASS** (notes below; facsimile OK per Director lock) |
| Reasoning reconstruction (player-only A–D) | **PASS** |
| Blind playtest (independent agent sim) | **PASS** (correct A–D; 0 hints) |
| Human blind playtest | **NOT DONE** — do not claim; still required unless Director waives with recorded reason |
| **Ship / Pitch** | **May proceed on ads/packaging prep** only if Director accepts this report. **Do not publish / Ship customer release** until human blind play clears or Director records a waiver. |

Playability remains the release gate. Automated + agent sim ≠ human playtest.

---

## Deliverable paths

| Path | Contents |
| --- | --- |
| `/workspace/wrong-widow/proof/VERIFICATION_REPORT.md` | This report |
| `/workspace/wrong-widow/proof/structural_checks.json` | Machine checklist results |
| `/workspace/wrong-widow/proof/reasoning_reconstruction.md` | Author-aware A–D support from player files |
| `/workspace/wrong-widow/proof/blind-playtest.md` | **Separate** agent blind sim findings |
| `/workspace/wrong-widow/proof/renders/` | Grayscale page PNGs sampled for visual review |
| `/workspace/wrong-widow/proof/_player.txt` / `_hints.txt` / `_sealed.txt` | Text extracts used for automated checks |

Director locks respected: facsimile OK v1; explicit catalog OK; D016 footnote stays; three PDFs stay. **No mystery rewrite.**

---

## 1. Structural / automated

| Check | Result | Evidence |
| --- | --- | --- |
| Page counts | **PASS** | player 27 / hints 2 / sealed-solution 5 |
| Open exhibits D001–D017 in player | **PASS** | all present |
| D018 absent from player + hints | **PASS** | present only in sealed-solution |
| H1–H8 in hints only | **PASS** | all eight rungs; no D018 |
| Spoiler boundary (Benjamin / knew Martha / told Lydia / left convalescence) | **PASS** | sealed-only; absent from player+hints |
| No “supportable widow is Martha” answer prose in player/hints | **PASS** | adjudication *asks* A; does not answer it |
| Chronology spine dates in player | **PASS** | 1858-03-12, 1866-06-04, 1863-11-12, 1863-12-01, 1887-02-14 |
| D015 critical strings | **PASS** | Silas M. Corbit; Co. B, 83rd Indiana Infantry; Dearborn County; age 23 (large on-face) |
| D016 critical strings | **PASS** | Eli Corbin; Martha Ann Ashley; letter-by-letter footnote present |
| Final questions A–D present | **PASS** | worksheets + adjudication pages |
| Noise not labeled as tips | **PASS** | Corbit/Eli/Wife appear in tables without tip callouts |

Refs / catalog: every D005–D017 has a body exhibit; unlock cues cite opening paper (Director: explicit catalog OK).

---

## 2. Visual / readability (print grayscale)

Sampled grayscale renders at 150 dpi (cold open, catalog, D007/D008 conflict pair, D010 census, D014–D016, worksheets, hints).

| Note | Severity |
| --- | --- |
| Facsimile is light aged fill + borders + typography — not photographic archival. **Director lock: OK v1.** | Non-blocking (waived) |
| Critical fields (dead of disease / deserted / NO divorce / Corbin+Ashley / unit+residence+age) read clearly in grayscale | OK |
| Research catalog page is dense but legible at Letter / Actual size | OK (explicit catalog waived) |
| Worksheets provide ~3 ruled lines per prompt — usable; tight for long writeups | Non-blocking |
| Hints: H7 “Teaches:” line split across page break onto p2 before H8 | Non-blocking polish |
| Every exhibit carries fictional-facsimile footer | OK |

No clipping of critical strings observed on sampled pages. No illegible handwriting gimmick.

---

## 3. Reasoning reconstruction (player files only; author-aware)

Full writeup: `reasoning_reconstruction.md`.

**Can Brief §3 A–D be supported without sealed?** **YES.**

| Element | Open-set conclusion | Min citations available in player |
| --- | --- | --- |
| A Supportable widow | Martha Jane (Ashby) Corbett — undissolved 1858 prior | D005, D014, D012 (+ D010/D011 overlap) |
| B Claimant beliefs | Martha: 1858 + wartime death; Lydia: 1866 + 1887 + told first wife died of fever | D002, D003 |
| C What happened | Not dead 1863; deserted after conflicting paper; died 1887-02-14 pneumonia with Lydia | D007, D008, D010, D011, D004 |
| D Why both look real | Parallel documentary stacks; record≠truth held | D005, D006, D004, D014 (+ supporting set) |

Sealed D018 is confirmation/color only — matches Brief §8 / Trail evidence_map.

---

## 4. Blind playtest (SEPARATE from automated)

Full writeup: `blind-playtest.md`.

| Item | Result |
| --- | --- |
| Method | Independent executor; isolation folder with **only** `player.pdf` + `START-HERE.md`; hints available separately but **unused**; no sealed/canon/trail/BRIEF |
| A–D | **Correct** vs rubric (Martha supportable; beliefs mapped; desertion+1887 death; both files look real) |
| Hints used | **0** |
| Felt finishable without sealed | **Yes** |
| Death-cert / near-name / Silas traps | Reported as **fair** |
| Human playtest | **Not claimed. Not performed.** |

**Limitation:** Agent simulation does not establish enjoyment, reading comfort, difficulty rating, or human playtime.

---

## 5. Findings list

### Blocking
**None demonstrated.** No inaccessible required clue, no sealed-only legal hinge, no answer leakage of A into player/hints, no D015/D016 string failure, no chronology break on spine dates.

### Non-blocking (should not “rewrite the mystery”; optional Binder polish if Director wants)

1. **Meta-labels on trap exhibits (strongest soft finding).** Player headers say **“Decoy hospital death”** (D015) and **“False divorce decree”** (D016). That authorially marks the traps before letter/unit comparison. Fairness still held in blind sim (eliminators on-face), but the labels soften discovery. Prefer neutral titles (e.g. “Hospital register — similar-name scan”; “Ripley divorce decree extract”) if a later polish pass is authorized — **do not change canon/trail**.
2. **Census/exhibit headers name pairings early** (e.g. “Elias + Lydia household”). Speeds identity continuity; reduces discovery friction. Related to explicit-catalog difficulty (already locked OK).
3. **Worksheet line count** modest (~3 lines). Fine for one-evening play; optional more space.
4. **Hints H7 page-break** splits “Teaches:” onto next page — cosmetic.
5. **Facsimile fidelity / catalog explicitness / D016 footnote / three-PDF split** — flagged by Binder earlier; **Director already locked**; not re-litigated.

### Out of Proof scope
Ads, Gumroad listing, price, human play duration claims.

---

## Top findings (for Director TL;DR)

1. **Packet structurally clean:** spoiler boundary holds; D015/D016 eliminators readable; A–D fully supportable from open set.  
2. **Agent blind sim solved correctly with zero hints** — recorded separately; **not** a human playtest.  
3. **Only material soft defect:** “Decoy” / “False divorce” headers on D015/D016. Non-blocking.  
4. **Ship/Pitch:** clear for Director acceptance toward Pitch prep; **Ship/publish blocked** until human blind play or recorded waiver.

---

## Handoff

**Status:** Stage 5 verification complete — CONDITIONAL PASS.  
**Next:** Director accepts / waives / requests polish on meta-labels → then Pitch; Ship waits on human blind or waiver.  
**Report line:** Proof → Director only.

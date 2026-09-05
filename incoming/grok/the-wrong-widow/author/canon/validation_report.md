# Validation Report — The Wrong Widow Canon

Generated against Brief §14 + Director §17A locks. Validator: `validate.py`.

## Counts

| Asset | Count |
| --- | --- |
| People | 25 (P001–P025) |
| Relationships | 33 |
| Events | 47 |
| Documents | 18 (D001–D018) |
| Observations | 15 |

Dataset string: `wrong-widow-canon`.

## Chronology (spine)

| Date | Event | Canonical? |
| --- | --- | --- |
| 1836-05-09 | Elias born, Ripley | yes |
| 1839-09-14 | Martha born, Ripley | yes |
| 1845-02-28 | Lydia born, Jefferson | yes |
| 1858-03-12 | Lawful marriage Elias+Martha | yes |
| 1859-07-22 / 1861-11-03 | Martha’s two children | yes |
| 1862-08-15 | Enlist Co. C 36th Indiana | yes |
| 1863-10-20 | Hospital admit Nashville (No. 8 / convalescent) | yes |
| 1863-11-12 | Hospital line “dead of disease” | **recorded only** |
| 1863-12-01 | Desertion (canonical) / muster deserted | yes desertion |
| 1866-06-04 | Ceremony Elias+Lydia (groom: widower) | ceremony real; not lawful |
| 1867–1874 | Lydia household births (3) | yes |
| 1887-02-14 | Elias death (pneumonia); Lydia named | yes — **only** canonical death |
| 1888 | Both pension filings | yes |
| ~1890–1892 | Player frame / bureau conflict | yes |

## Bigamy / marriage status

- `REL` Elias–Martha: `spouse` + `legal_status=lawful_undissolved`.
- `REL` Elias–Lydia: `ceremony_spouse` + `legal_status=ceremony_only`.
- Overlap: Martha living throughout 1866–1887 → second union unlawful though domestically real.
- **Supportable widow = Martha (P002) only.**

## No divorce (Elias+Martha)

- No divorce relationship for P001+P002.
- Event `records_search` + document D014: divorce search **negative**.
- Only divorce event/document is decoy Corbin/Ashley (P019/P020, D016).

## Desertion hinge

- Canonical desertion event 1863-12-01.
- D007 (dead) vs D008 (deserted) conflict preserved.
- Elias death events: exactly one, dated 1887-02-14 (not 1863).

## Decoy non-collision

| Decoy | Why non-colliding |
| --- | --- |
| Silas M. Corbit P015 | Co. B 83rd Indiana; Dearborn; age ≠ Elias; actually died 1863-11-09 |
| Eli Corbin / Martha Ann Ashley | Surname Corbin≠Corbett; Ashley≠Ashby; divorce 1865 |
| Harriet Whitcomb Keller | Separate pension remarriage lesson; not a claimant on Elias |

## Noise (NOT A CLUE)

- OBS008 / D011: Elias age ~1 year off (43 vs canonical 44); Eli vs Elias.
- OBS007 / D010: Corbett/Corbit surname variant; Lydia labeled `Wife` (socially true, legally incomplete).

## GAPs / Trail notes

- Exact street/ED for censuses not fixed (county-level OK).
- Full pension certificate numbers not invented.
- Hospital name is plausible framing (U.S. General Hospital No. 8 / convalescent barracks); regiment locked as Co. C 36th Indiana.
- Player_start / evidence_map / solution_path deferred to Trail (not §14 mandatory).

## Pass criteria

`python3 validate.py` → exit 0.

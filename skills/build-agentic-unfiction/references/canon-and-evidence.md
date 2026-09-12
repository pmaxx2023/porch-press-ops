# Canon and evidence model

Use this reference when defining or repairing the private author package.

## Minimum entities

| Entity | Minimum useful fields |
| --- | --- |
| Person | Stable ID, dated names/aliases, birth/death range, relationships, locations, knowledge, motives |
| Event | Stable ID, time or interval, place, participants, canonical description |
| Artifact | Stable ID, public source, creation/event/digitization dates, creator, provenance, record claim |
| Observation | Stable ID, artifact and exact visible field, literal meaning, reliability limits |
| Deduction | Stable ID, question, conclusion, support observations, prerequisites, alternatives, strength |
| Episode | Stable ID, opening knowledge, allowed artifacts, required state, reveal, next question |

Store uncertain dates as intervals. Separate biological, adoptive, marital, household, professional, and social relationships. A record may be authentic within the fiction and still contain a mistaken or dishonest claim.

## Evidence rules

- Use at least two genuinely independent supports for a consequential identity or event when the story permits.
- Do not count two artifacts copying the same claim as independent corroboration.
- Absence from a ledger is not proof of absence unless the record's coverage and completeness are themselves established.
- A photograph label identifies the labeler's belief, not automatically the person shown or the exposure date.
- A ticket or reservation identifies an intended traveler, not automatically the person who traveled.
- A witness who saw clothing, a silhouette, or a vehicle did not necessarily identify a person.
- A name match is a lead. Resolve identity through age, relatives, addresses, occupation, handwriting, continuity, or another discriminating field.
- Motive explains pressure; it does not establish action, access, or timing.
- A late confession may confirm an answer but should not be the only evidence supporting a conclusion the player was required to make earlier.

## Deduction test

For each required conclusion, answer:

1. What exactly can the player observe?
2. Why should that observation create a question?
3. What search or citation can find the next source without hidden knowledge?
4. What does the combined evidence support?
5. What competing explanation remains plausible?
6. Which positive evidence weakens or eliminates it?
7. What uncertainty remains after the correct conclusion?

Walk every path forward from the opening with no author-only knowledge. Then try to solve it incorrectly using each intended red herring. A red herring that cannot be disproved is an alternate ending, not fair misdirection.

## Public-repository hazard

Before release, search every public branch, issue, commit, generated bundle, source map, image filename, alt field, test fixture, and deployment log for:

- answer wording;
- hidden aliases;
- canonical-only dates or relationships;
- scoring keys;
- episode-unlock arrays that reveal the intended inference;
- plaintext final letters or confessionals;
- comments that explain which suspect or theory is correct.

Deleting a file from the current branch does not erase public history. If an old solution is already public, assume a capable player agent can retrieve it. Change the new investigative endpoint or move the entire authoring workflow to a protected location before relying on secrecy.

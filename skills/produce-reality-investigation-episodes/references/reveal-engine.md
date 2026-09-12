# Evidence-triggered reveal engine

Use this data contract for authored reveal scenes.

```json
{
  "scene_id": "E2-R03",
  "episode_id": "E2",
  "spoiler_tier": 2,
  "trigger": {
    "all_tokens": ["ARCHIVE-001", "ARCHIVE-002"],
    "any_tokens": [],
    "claim_state": null
  },
  "receipt_artifact_ids": ["A001", "A002"],
  "lead_cast_id": "CAST-Z",
  "declaration": {
    "text": "A strong but still disputed interpretation.",
    "status": "claim",
    "support_observation_ids": ["O001", "O002"]
  },
  "cross_examination": [
    {
      "cast_id": "CAST-X",
      "text": "A challenge grounded in the limits of those observations.",
      "support_observation_ids": ["O001"]
    }
  ],
  "confessionals": [],
  "player_ruling": ["supported", "contested", "disproved"],
  "next_question": "The next question the available evidence can answer.",
  "forbidden_fact_ids": ["F-LATER"]
}
```

Identifiers above are illustrative. Use case-specific neutral IDs.

## Trigger rules

- Trigger only after exact validated evidence state.
- Make scenes idempotent; a refresh must not replay or duplicate state unintentionally.
- If several scenes become eligible together, use authored priority rather than filesystem or array order.
- Record seen scenes separately from collected evidence.
- Do not reveal a later scene through client preload, accessibility text, analytics names, image filenames, or error messages.

## Dialogue rules

Every factual sentence must be supportable from the character's allowed knowledge. Label inference through language or interface state. Give disagreement a substantive evidentiary basis.

Useful conflict:

- provenance versus content;
- eyewitness identification versus observed clothing;
- reservation name versus traveler identity;
- family motive versus documented action;
- institutional record versus private correction;
- absence from a record versus established completeness.

Weak conflict:

- insults unrelated to evidence;
- generational catchphrases with no methodological difference;
- a character withholding a known required fact merely to prolong the episode;
- repeated disbelief after decisive evidence;
- a surprise fact created only in dialogue.

## Generation controls

Generation affects media habits and prior experience, not intelligence.

- Let an older archival specialist recognize the purpose and limits of paper systems.
- Let an analog/digital crossover investigator notice institutional incentives and conversion errors.
- Let a networked genealogist connect relationships while being tested on proof standards.
- Let a social-native investigator surface visual or distributed evidence quickly and then face provenance review.
- Let a multimodal-native investigator question interface assumptions and compare patterns without treating correlation as identity.

Write individual people. Permit each to surprise the apparent generational expectation when evidence earns it.

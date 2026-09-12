---
name: audit-agentic-unfiction
description: Audit a controlled-web fictional investigation for logical solvability, agent retrieval, episode-state behavior, spoiler leakage, reality-ambiguity consistency, and end-to-end playability. Use before preview or release and after changes to canon, artifacts, URLs, prompts, or gating; do not treat this audit as human enjoyment or sales validation.
---

# Audit Agentic Unfiction

Verify the investigation as a system. A good story, attractive archive, passing link checker, or successful agent answer is not enough by itself.

## Select the affected checks

Read [references/test-matrix.md](references/test-matrix.md). Run the complete release matrix for a new or materially changed game. For a narrow repair, test the changed surface and all deductions, episodes, links, and protected content downstream of it.

Keep these results separate:

- structural validation;
- semantic evidence review;
- agent retrieval testing;
- episode/showrunner state testing;
- visual and accessibility review;
- spoiler and public-history scan;
- clean-state end-to-end playtest;
- human enjoyment and commercial validation.

Do not infer the last two from the earlier checks.

## Validate maintained data

When the author package uses the supported JSON shape, run:

```bash
python3 scripts/validate_case_bundle.py \
  --canon /protected/path/canon.json \
  --graph /protected/path/evidence-graph.json \
  --content /protected/path/public-content.json \
  --scripts /protected/path/episode-scripts.json \
  --envelope /protected/path/sealed-envelope.json
```

Only `--canon` and `--graph` are required; the remaining packets are optional until authored. The script checks identifiers, references, discovery-route counts, dependency cycles, manuscript coverage, scene/token/claim integrity, cast references, and final evidence dimensions without printing canonical values. It cannot judge whether evidence semantically proves the conclusion.

## Reconstruct from player-visible material

Solve from the opening exactly as a player would. Do not consult canonical facts, expected search phrases, internal slugs, or solution language while performing the blind pass.

For every conclusion:

- cite the public artifact and exact observation;
- distinguish source claim from inference;
- test the strongest alternative;
- record unsupported jumps and hints needed;
- stop if a required source cannot be found through a permitted route.

An agent simulation may expose retrieval and reasoning failures. It does not establish fun, difficulty, or human playtime.

## Test agent variability

Use clean sessions and ordinary player prompts with each available web-capable agent. Record:

- query issued;
- URLs actually opened;
- exact relevant quotation;
- hallucinated or inaccessible sources;
- whether the agent separated fact from inference;
- whether search failed but citation/recovery succeeded;
- whether the agent found a public spoiler or author file.

Do not feed the expected URL to a test labeled as search discovery. Test direct navigation separately.

## Test showrunner behavior

- No scene fires before its evidence condition.
- Each scene fires once unless replay is explicitly selected.
- Simultaneously eligible scenes follow authored priority.
- Alternate discovery orders converge on the same justified knowledge state.
- Cast members do not know forbidden facts.
- A dramatic declaration remains labeled as a claim until established.
- Export/import preserves state without unlocking additional content.
- Invalid tokens, malformed state, duplicate tokens, and reset behave safely.

## Scan for spoilers

Search all public repository history available to players, generated source, source maps, HTML, JavaScript, JSON, image metadata and filenames, sitemaps, logs, issue text, screenshots, and accessibility content.

Treat any client-delivered answer as public even if it is hidden, encoded, minified, or unreachable through the interface. Record old public solutions separately; ensure the new game's required endpoint cannot be answered by retrieving them.

## Release decision

Return **PASS**, **HOLD**, or **BLOCKED** for each test family with evidence. Any missing required clue, circular route, answer leak, accidental contradiction, premature scene, broken recovery path, or non-unique required conclusion produces **HOLD**.

Finish with:

- exact version/commit tested;
- checks passed and failed;
- demonstrated defects versus unperformed checks;
- repairs required before release;
- retest scope;
- material residual uncertainty.

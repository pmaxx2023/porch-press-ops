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

## Audit evidence receipts

Treat the QA packet as versioned evidence, not decoration. Every claimed screenshot must represent the exact candidate under review. Pre-revision images may document a regression but cannot prove the repaired state.

Record two version pins when evidence is committed after the implementation:

- **capture-source SHA** — the exact functional source rendered or exercised;
- **evidence-tip SHA** — the later commit containing the receipts and manifest.

The manifest must say which pin each receipt proves. Renaming an old file or converting its image container does not make it a current capture. When provenance is uncertain, compare it with the acknowledged earlier image; identical decoded pixels are evidence of reuse, not recapture.

Require:

- exact repository-relative paths instead of placeholders;
- a current-candidate image for every surface used to claim visual acceptance;
- the exact capture-source SHA beside current screenshot paths and viewport dimensions;
- viewport dimensions where responsive behavior is claimed;
- file extensions that match image magic bytes;
- working links at the named commit;
- explicit `not captured / source-tested` labels for checks without an image;
- a clearly separated `pre-revision` area that is never counted as final PASS evidence.

When an evidence directory is available, run:

```bash
python3 scripts/validate_evidence_pack.py \
  --root /path/to/candidate \
  --notes /path/to/candidate/EVIDENCE_NOTES.md \
  --capture-source-sha 0123456789abcdef0123456789abcdef01234567 \
  --required-current evidence/0123456/mobile-390.png \
  --required-current evidence/0123456/archive-a.png
```

With `--capture-source-sha`, each required-current path must include that SHA's seven-character prefix, and the notes must name the SHA. The script also checks placeholders, referenced local paths, required-current placement, and image extension/magic consistency. It does not decide whether an image visually proves the claim; inspect each receipt.

Before judging a candidate, compare its complete file diff with the authorized job scope. An unexpected helper, executable, deployment file, network call, process action, content file, or live-system change is a HOLD even when the requested files pass. A local preview helper must report an occupied port and stop; it must never terminate or replace an existing listener.

## Release decision

Return **PASS**, **HOLD**, or **BLOCKED** for each test family with evidence. Any missing required clue, circular route, answer leak, accidental contradiction, premature scene, broken recovery path, or non-unique required conclusion produces **HOLD**.

Finish with:

- exact version/commit tested;
- checks passed and failed;
- demonstrated defects versus unperformed checks;
- repairs required before release;
- retest scope;
- material residual uncertainty.

An auditor cannot downgrade an explicit Owner or release-gate requirement to a non-blocking residual. Return HOLD until the named evidence is repaired or the requirement owner changes it.

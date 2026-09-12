# Agentic-unfiction test matrix

## Structural

- Unique person, event, artifact, observation, deduction, episode, token, and scene IDs.
- Every reference resolves.
- Required artifact has at least search, citation, and recovery routes.
- Dependency graph is acyclic unless an intentional loop has an independent entry.
- Every required deduction has visible support and a defined strength.
- Every episode has an opening state, closing state, trigger, and next question.
- Every manuscript artifact matches the graph accession and has provenance, transcript, media, alt-text, and claim-boundary fields.
- Every showrunner scene references valid evidence tokens, cast speakers, claims, state effects, and episode gates.
- Every protected final-answer key is among the displayed options and every evidence dimension is satisfiable from valid tokens.

## Semantic reasoning

- Identity requires discriminating evidence beyond a shared name.
- Dates and ages use compatible intervals.
- A record's creator and purpose support the weight assigned to it.
- Negative evidence depends on established record completeness.
- Motive, access, act, and timing are not collapsed.
- Independent evidence is genuinely independent.
- Intended alternatives are fairly weakened or preserved as uncertainty.
- The resolution does not introduce the only required clue after commitment.

## Retrieval

- Known entry point loads anonymously.
- Essential text appears in initial HTML.
- Every required URL has a working citation route.
- Search prompt contains no hidden answer.
- Recovery hints progress from question to phrase to source to direct link.
- Robots and sitemap behavior matches intended discovery.
- Missing search indexing does not make the game impossible.
- Optional third-party disappearance does not break a deduction.

## Episode and cast

- Reveal displays the artifact before the declaration.
- Declaration is no stronger than an allowed cast interpretation.
- Cross-examination targets an evidentiary limit.
- Confessionals add character, method, or stakes—not secret canon.
- Player can disagree with the cast and still progress through evidence.
- Generational voice does not become caricature or substitute for expertise.
- Alternate discovery orders do not create contradictory cast knowledge.

## Client state and protection

- Valid and invalid token handling.
- Duplicate token idempotence.
- Export/import round trip.
- Wrong case ID and unsupported schema rejection.
- Reset behavior and recovery.
- No code execution from notes or imported JSON.
- No protected answer in source, preload, metadata, filenames, or error output.

## Visual and accessibility

- Desktop and true mobile viewport review.
- Screenshots name the exact candidate and use current, not pre-revision, source.
- Evidence-manifest paths resolve; placeholders are replaced or explicitly marked `not captured / source-tested`.
- Image extensions match magic bytes and linked files render at the claimed dimensions.
- Every archive or portal surface used for a visual PASS has a current-candidate receipt; obsolete images are regression context only.
- Keyboard-only task completion and visible focus.
- Semantic headings, labels, landmarks, and meaningful link text.
- Sufficient contrast and reduced-motion behavior.
- Evidence images readable at intended zoom.
- Transcript fidelity and appropriate alt text.
- Distinct archive identities without sacrificing usability.

## End-to-end

- New player understands the first action.
- Outside agent can work from the supplied prompt.
- Player can recover from a failed agent search.
- Evidence locker and claim states remain comprehensible.
- Every required conclusion can be supported from public evidence.
- Final submission does not accept an uncited lucky guess as a complete solution.
- Resolution addresses both facts and human consequences.

## Commercial path

- Storefront truthfully states interactive fiction, digital format, actual contents, and tested capabilities.
- Existing product/variant and new edition are not confused.
- Correct customer file or access path is mapped.
- Cart, checkout entry, fulfillment configuration, and actual customer retrieval are reported separately.
- No playtime, difficulty, review, scarcity, indexing, or model-compatibility claim is published without evidence.

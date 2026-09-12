---
name: build-agentic-unfiction
description: Design or rebuild a fictional investigation played across controlled public-web artifacts with player-supplied AI agents. Use for agentic mysteries, unfiction or ARG-style evidence worlds, open-web clue graphs, case portals, or adaptations of existing mystery assets; do not use for ordinary linear fiction or unsourced real-person investigations.
---

# Build Agentic Unfiction

Create a fair, recoverable detective experience whose fiction appears to leave evidence across the public web. Preserve reality texture without making search ranking, agent behavior, or a third-party platform responsible for solvability.

## Establish the product contract

Record the fixed decisions before producing pages:

- solo, group, synchronous, or asynchronous play;
- player objective and final answer format;
- whether the player brings an outside agent, uses built-in agents, or both;
- reality-ambiguity boundary and where fiction is disclosed;
- existing canon/assets to preserve, revise, extend, or retire;
- public and private source locations;
- commercial surface and release authority.

When adapting an existing product, inspect its actual player and solution files. Determine whether its solution is already public or searchable. Do not build a supposedly new investigation whose answer can be retrieved from an earlier public release. Prefer a canon-preserving sequel, a materially new endpoint, or an explicitly authorized revision over cosmetic repackaging.

## Separate three truth layers

Maintain these separately:

1. **Canon:** what actually happened.
2. **Record claims:** what each public artifact says, including errors and lies.
3. **Player knowledge:** what the discovered evidence currently justifies.

Read [references/canon-and-evidence.md](references/canon-and-evidence.md) while establishing truth, observations, deductions, and alternate explanations.

Keep the canonical answer and scoring rules out of public repositories, public issues, generated client bundles, metadata, prompts, and fixture data. If an implementation repository is public, give executors only exact public content and spoiler-safe acceptance criteria.

## Design the evidence graph before the web pages

Work backward from the final reconstruction, then solve forward from the opening lead.

For every required deduction, specify:

- the precise conclusion and its evidentiary strength;
- visible supporting observations and source IDs;
- prerequisites;
- plausible alternative explanations;
- evidence that excludes or weakens each alternative;
- remaining uncertainty;
- the next research question produced by the discovery.

Avoid circular discovery, author-only leaps, absence-as-proof, shared-name identity matches, and clues whose only path requires already knowing the answer.

## Build a distributed-looking, controlled universe

Read [references/controlled-web.md](references/controlled-web.md) when planning or implementing the public surfaces.

Every indispensable clue must have:

- a canonical copy under product control;
- a stable, directly fetchable public URL;
- a natural search phrase;
- a crawlable citation route from another known page;
- a progressive recovery route ending in the direct source;
- human-readable static text;
- sufficient provenance to evaluate the source;
- an archival accession ID or equivalent evidence token.

Search results, Reddit, social profiles, video platforms, and other third-party surfaces may deepen immersion. They do not carry the only copy of required evidence.

The public universe should have several credible editorial voices and visual identities while sharing invisible accessibility, performance, deployment, and monitoring primitives. Do not create fake official agencies, active public alerts, fabricated endorsements, or contact routes that might be mistaken for actual institutions.

## Preserve genuine agentic play

The outside agent is a research instrument, not the source of canon. Give the player prompts that require opened URLs, exact quotations, record-versus-inference separation, contradictions, and unresolved questions.

Do not require a particular consumer model to behave identically. Accept that agents will differ. Test multiple query wordings and provide link and hint recovery when search fails.

Require the player to commit conclusions and evidence, not paste an agent's unsupported answer. Never reward a confident uncited response merely because it matches the solution.

## Use controlled cast separately

When the experience includes recurring investigator personalities or reality-show drama, distinguish:

- **player agents:** uncontrolled outside researchers;
- **resident cast:** bounded characters reacting to discovered evidence;
- **showrunner:** deterministic state and edit logic.

Use the `produce-reality-investigation-episodes` skill for cast, reveal, and episode authoring. The show may dramatize a theory; the interface must distinguish a cast claim from an established fact.

## Deliverables

Fit the package to the project, but a complete build usually requires:

- spoiler-safe product and experience specification;
- private canon and deduction graph;
- public-surface map and artifact manifest;
- episode/state map;
- exact public artifact text and media specifications;
- player-agent prompt cards;
- hints and recovery paths;
- cast scenes when applicable;
- final questions, protected solution, and aftermath;
- build assignments with observable acceptance criteria;
- logical, retrieval, visual, spoiler, and end-to-end verification results.

Do not call a collection of atmospheric pages playable until a solver can begin without author knowledge, locate each required source, distinguish claims from facts, test alternatives, commit a conclusion, and reach the protected resolution.

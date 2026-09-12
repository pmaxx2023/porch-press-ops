---
name: produce-reality-investigation-episodes
description: Turn a fixed mystery evidence graph into episodic reality-show-style investigation scenes with recurring AI cast personalities, evidence-triggered reveals, confessionals, conflict, and cliffhangers. Use when dramatizing agent discoveries without allowing generated dialogue to change canon; do not use for unscripted real-person surveillance or ordinary screenplay formatting.
---

# Produce Reality Investigation Episodes

Create dramatic episodes around discoveries while preserving the player's ownership of the investigation and the fixed logic of the case.

## Start from evidence state

Before writing an episode, obtain:

- what the player can know at its opening;
- which public artifacts are available;
- the required deduction or uncertainty;
- the strongest plausible wrong interpretation;
- the evidence state that triggers the tentpole reveal;
- the exact next research question;
- facts that remain forbidden until later.

Do not write a reveal first and retrofit evidence afterward.

## Cast epistemologies, not costumes

Give each recurring investigator:

- an investigative specialty;
- a method for deciding what counts as proof;
- an objective in the present episode;
- an understandable blind spot;
- a relationship or rivalry affecting interpretation;
- evidence the character has and has not seen;
- a restrained verbal rhythm and screen behavior;
- a position the character will revise when contrary evidence is sufficient.

Generation, region, profession, or background may influence a character's relationship to institutions, media, technology, and privacy. Do not reduce a generation to slang, incompetence, memes, or a single political attitude.

Read [references/reveal-engine.md](references/reveal-engine.md) when creating scene data or episode scripts.

## Separate player agents, cast, and showrunner

- The player's outside agent searches and analyzes the web. Its output is not controlled and must be supported by opened sources.
- The resident cast reacts to verified evidence state. Its knowledge and permissible claims are controlled.
- The showrunner decides timing, collision, edit, confessionals, and cliffhanger. It does not change evidence or secretly decide for the player.

The most reliable first release uses pre-authored branch dialogue. If later generation is used, restrict it to wording within a supplied fact set, stance set, and spoiler ceiling; validate structured output before display.

## Produce each episode

Use a compact dramatic shape:

1. **Cold open:** a consequential claim or image without resolving it.
2. **Mission:** an answerable research question and optional player-agent prompt.
3. **Field work:** sources the player can locate in more than one way.
4. **Receipt:** show the actual record before interpretation.
5. **Declaration:** one investigator makes the strongest defensible claim.
6. **Crossfire:** another separates what the evidence says from what the speaker inferred.
7. **Confessional:** expose method, motive, uncertainty, or rivalry—not a hidden fact.
8. **Player ruling:** supported, contested, or disproved, with cited evidence.
9. **Reversal or escalation:** reframe an earlier fact using newly available evidence.
10. **Cliffhanger:** pose the next solvable question.

Episodes may branch in discovery order. They must converge on the same justified knowledge state without implying that scene order proves chronology or causation.

## Control dramatic certainty

Characters may say “Look what we found” or “Eleanor never left the house that day” when that is their interpretation. Visually label the statement as a cast claim until the evidence establishes it.

Do not let the neutral interface, narrator, archival caption, or showrunner state a disputed theory as fact. Drama may come from premature certainty; fairness comes from letting the player inspect the receipt and challenge it.

## Required output

For each episode provide:

- episode ID, title, opening state, closing state, and spoiler tier;
- mission and player-agent prompt;
- allowed artifact IDs and discovery routes;
- tentpole trigger condition;
- display receipt;
- declaration and cross-examination;
- confessionals;
- player ruling prompt;
- alternate branch for materially different discovery order;
- recovery hints;
- next research question;
- continuity and forbidden-fact checks.

The episode is unfinished if it merely reveals information in a video or dialogue that the player could not have discovered from evidence.

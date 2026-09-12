# Controlled-web construction

Use this reference while specifying or reviewing public evidence surfaces.

## Topology

Build one known starting surface and several independent-looking archives. Underneath, keep centralized source control, artifact IDs, build validation, and health checks.

An essential artifact should remain playable through:

- open-web search when indexing succeeds;
- ordinary crawlable links when search fails;
- the case portal's final recovery hint.

Do not equate deployment, sitemap submission, or a `site:` query with reliable availability in every agent's search system.

## Agent-readable pages

- Serve essential text in initial HTML.
- Use ordinary `<a href>` links with descriptive anchor text.
- Provide stable URLs, canonical titles, provenance, and visible dates.
- Provide faithful transcripts for document images when the puzzle does not specifically require reading that visual field.
- Let user-initiated agents fetch pages without login, cookie consent, or browser-only interaction.
- Provide `robots.txt` and `sitemap.xml` appropriate to intended search discovery.
- Keep error pages useful without disclosing later clues.
- Optimize full-resolution evidence separately from preview images.

## Reality texture

Give each archive a reason to exist independent of the game. Its collection should include modest non-clue context so the essential page does not look like a puzzle card. Keep that context bounded; do not manufacture hundreds of empty pages merely to simulate age.

Use different record-making purposes: a historical society accession record, a newspaper correction, a passenger ledger, a memorial entry, or a volunteer transcription note. A source's limitation should arise from why it was created.

Cross-site references should look like bibliography, provenance, collection partnership, or correction history. Avoid a universal game navigation bar or conspicuous shared footer.

## Evidence tokens

Use a plausible visible accession code rather than a floating puzzle code. The player may copy it into the case portal. Token validation proves that the player reached a named artifact; it does not prove the player's interpretation.

Keep token names neutral. Do not use identifiers such as `KILLER-PROOF`, `REAL-ELEANOR`, or `FINAL-ALIAS` that leak the conclusion.

## Protected content

Do not rely on a client-side hidden div, base64 string, minification, disabled button, unpublished route listed in a sitemap, or JavaScript condition to protect the answer. Anything delivered to the browser or committed publicly should be treated as available to a player agent.

For a tiny static pilot, keep the final solution in a separately controlled delivery artifact or server-side response. If secure gating is unavailable, withhold the final payload rather than ship it hidden in the client.

## Resilience

Maintain an owned canonical copy of every public artifact and a simple URL health inventory. When an optional third-party echo disappears, remove or replace that path without changing the deduction. When a required owned URL changes, preserve a redirect and retest citations, agent prompts, and recovery hints.

# PP-ELEANOR-AU-001 — Eleanor Hart Is Missing: The Second Disappearance

Owner: **Owner_Bot — Porch Press (ChatGPT)**
Implementation operator: existing **Connector_Bot / Grok production agents**
Status: **planned; reversible current-listing hold, authoring, and technical spike authorized; new edition not authorized for live publication**

## 1. Product decision

Build a solo, episodic **agentic-unfiction detective game** in which a player uses any web-capable AI agent to investigate fictional records distributed across a controlled layer of the public web.

The creative stack has a strict hierarchy:

| Element | Function |
| --- | --- |
| Fair-play detective fiction | Fixed truth, evidence, deductions, alternatives, and resolution |
| Agentic gameplay | The player directs external AI investigators and evaluates cited findings |
| Blair-Witch-style reality ambiguity | The archive appears to predate and exceed the product |
| Reality-television grammar | Episodes, cast conflict, confessionals, reveals, reversals, and cliffhangers |

The player is the lead detective. Five recurring, visibly synthetic investigators provide produced reactions and competing interpretations. The player's own ChatGPT, Grok, Claude, or other browsing agent performs genuine open-web research.

## 2. Existing-product bridge

The current 1912 printable edition remains canonical and becomes **Episode Zero: The First Disappearance**. Its customer package and solution already exist in this public repository, so the new game must not reuse its solved question as the new season's endpoint.

The new season opens a distinct 1948 disappearance later in Eleanor's life. The private author bible contains the underlying truth and deduction graph. Do not infer, improvise, or publish that truth from this plan.

There are no current purchasers to migrate. Place the existing Shopify listing on a **reversible sales hold** while the new edition is built. Preserve the product record, handle, price, media, customer ZIP, delivery mapping, and unpublished hero-candidate theme; do not delete or repurpose them. The hold is a separate exact job so its receipts cannot be confused with architecture-spike work.

## 3. Experience contract

The finished experience must let one player:

1. Open a case portal and receive one actionable lead.
2. Copy a disciplined research prompt into any web-capable agent.
3. Find real, accessible URLs in the controlled web universe.
4. Save archival accession codes and exact observations in an evidence locker.
5. Trigger produced cast reactions when meaningful evidence combinations are established.
6. Mark cast claims **supported**, **contested**, or **disproved**.
7. Move through five episodes without requiring a live host, social account, or paid AI API supplied by Porch Press.
8. Submit a final reconstruction supported by evidence codes.
9. Receive an evidence-cited resolution and human aftermath only after committing.

The product must not be solvable by asking an agent to invent an answer. Agents retrieve and analyze sources; the portal verifies evidence state; the player owns the theory.

## 4. Season shape

| Movement | Working episode | Player-facing question | Required dramatic function |
| --- | --- | --- | --- |
| Prologue | Episode Zero — The First Disappearance | What happened in 1912? | Establish Eleanor, the Hart/Byrne family, and the cost of erased names |
| 1 | The Photograph | Why is a post-disappearance photograph labeled Eleanor Hart? | Inciting contradiction and first public-web search |
| 2 | The Last Day | Who actually left Bellwether House? | Tentpole reveal: “Eleanor never left the house that day” becomes a contested cast claim |
| 3 | The Woman on the Train | Whose identity traveled under Eleanor's name? | Reversal of the eyewitness and photograph story |
| 4 | The Records Clerk | Who appears under a new name in Bellwether's records? | Genealogical identity reconstruction |
| 5 | What Eleanor Chose | Was Eleanor taken, hidden, or voluntarily missing—and why? | Evidence-cited conclusion plus morally divided aftermath |

Episode titles and public copy are working material until Owner_Bot approves the final authored scripts.

## 5. Cast and show control

The recurring cast uses generational perspectives as **epistemic lenses**, not slang or stereotypes.

| Lens | Investigative strength | Productive bias |
| --- | --- | --- |
| Boomer | Archives, oral history, provenance | Initially grants institutions more credibility |
| Gen X | Investigative reporting, contradiction, incentives | Assumes somebody is protecting an interest |
| Millennial | Genetic genealogy, relationship maps, digital synthesis | Can let a plausible family motive outrun proof |
| Gen Z | OSINT, images, social traces, rapid public explanation | Announces the strongest interpretation early |
| Gen Alpha | Multimodal pattern comparison and assumption testing | Sees structural anomalies but lacks historical context |

Only two or three agents dominate any episode. Gen Alpha enters after the established cast has become attached to competing theories.

The production controls facts, evidence access, permissible interpretations, timing, edit, and episode transitions. Generated wording may vary only inside those boundaries. The first release uses deterministic, pre-authored cast branches; it does not require a runtime model bill.

Every tentpole reveal follows this sequence:

1. Display the artifact.
2. Let one investigator make the strongest defensible declaration.
3. Have another investigator attack the inference, not invent new facts.
4. Cut to short confessionals revealing bias and stakes.
5. Ask the player to classify the claim.
6. End on the next answerable question.

## 6. Controlled web universe

The public universe is distributed-looking and centrally controlled. Required evidence never depends solely on Reddit, a social account, a search ranking, or another third-party surface.

Planned surfaces:

| Surface | Public purpose | Evidence texture |
| --- | --- | --- |
| Case portal | Player state, prompts, cast scenes, hints, final submission | Modern investigation interface |
| Cincinnati Industrial Memory Archive | Episode Zero record set and verified Eleanor handwriting | Local-history manuscript collection |
| Bellwether Historical Register | House history, accession catalog, photographs, guest and staff records | Small institutional archive |
| Ohio River Industrial Memory Project | Hart family and factory records | Volunteer industrial-history project |
| River & Rail Gazette Archive | News reports, notices, passenger material, obituaries | Digitized newspaper/archive |
| North Parish Records & Memorial Register | Family, burial, and plot records | Community records index |

Third-party echoes may later include transparently operated Reddit, video, or social posts. They can add atmosphere or alternate discovery, but never carry an indispensable clue.

Every required artifact needs:

- one stable public URL;
- human-readable static HTML;
- a natural archival accession code used as the evidence token;
- visible source context and date;
- a search phrase route;
- a crawlable citation or link route;
- a portal recovery hint;
- a canonical owned copy;
- no hidden solution or later-episode answer in client code, metadata, alt text, or repository instructions.

See [PUBLIC_WORLD_SPEC.md](PUBLIC_WORLD_SPEC.md) for implementation rules.

## 7. Technical shape for the tiny first release

Use a static-first monorepo and existing free infrastructure unless Grok proves a simpler supported route.

- Case portal: static HTML/CSS/JavaScript.
- Progress: browser `localStorage`, plus explicit export/import of a small case-state JSON file.
- Evidence capture: accession-code entry and optional notes; do not ingest private external-agent conversations.
- Episode state: deterministic rules over collected evidence tokens.
- Cast scenes: pre-authored branch data, never free-running plot generation.
- Final verification: deterministic normalized checks. In production, a tiny server-side sealed-envelope endpoint returns the protected resolution only after a sufficient final reconstruction.
- Public archives: static, server-rendered HTML with ordinary crawlable links, sitemaps, stable slugs, descriptive titles, and accessible document transcriptions.
- Media: optimized web images plus readable originals where visual inspection is part of play.
- Runtime accounts: none for the pilot.
- Runtime model/API cost: $0 for the pilot; the customer brings the agent.

The fixture-only spike remains fully static. The real ending, scoring keys, and capstone text must not be shipped in the public client bundle or public repository. The production endpoint is spoiler resistance rather than an authentication claim; all ordinary play stays static-first and inexpensive.

Search is an immersion layer, not a dependency. A new site or sitemap is not guaranteed to be indexed. Required pages must also be reachable by ordinary links from a known entry point.

## 8. Reality-ambiguity boundary

- Public archive pages do not lead with “game,” Porch Press sales copy, or a solution.
- Public archive pages do not assert that a real missing-person investigation is active.
- The Porch Press purchase surface identifies the work as an open-web interactive fiction experience before payment.
- Each archive has a discoverable provenance/about route with a restrained fiction disclosure.
- The in-case experience remains fully in-world.
- Fictional institutions must not impersonate actual police departments, government agencies, newspapers, or living people.

The target reaction is: “I know this may be constructed, but the evidence behaves as if Eleanor existed.” Literal deception is not a release requirement.

## 9. Private/public separation

`porch-press-ops` is public. It may contain:

- skills and operating instructions;
- spoiler-safe architecture and job cards;
- intended public archive artifacts;
- code used in the public experience;
- test fixtures that reveal no final answer.

It must not contain the new season's:

- canonical resolution;
- private deduction map;
- final-letter plaintext;
- solution scoring keys;
- unreleased cast branches that disclose the answer;
- private author notes.

Those remain in the Owner_Bot author package. Grok receives exact approved public content in bounded batches and must not request or reconstruct the solution.

## 10. Production phases and gates

### Phase A — architecture spike

Build a non-live, no-spend vertical slice with the case portal shell, three visually distinct archive shells, evidence-token storage, one triggered cast reveal, and export/import of progress.

**Gate A:** Owner_Bot can complete the slice from a clean browser, every source loads without authentication, the reveal fires only from the correct token combination, and no source contains a solution leak.

### Phase B — authored season

Owner_Bot supplies the complete public artifact text, cast scripts, hints, episode transitions, final questions, and protected ending. Grok converts only the approved content into layouts and media.

**Gate B:** Every required deduction has visible support, alternatives are fairly excluded, cast claims are labeled as claims, and every clue has at least two discovery routes plus a recovery hint.

### Phase C — full build

Implement all public surfaces, mobile/desktop case portal, episode state, evidence locker, save/export, accessibility, media, and protected resolution.

**Gate C:** deterministic validation, link crawl, mobile visual review, spoiler scan, and clean-state functional test all pass.

### Phase D — agent compatibility

Run clean-session tests with available browsing agents. Test retrieval, quotation, source differentiation, hallucination resistance, and the player's ability to recover when an agent misses search results.

**Gate D:** every required clue remains reachable without relying on search ranking; no tested agent receives the canonical answer from public implementation material; failures are repaired or covered by hints.

Use [PLAYTEST_PROTOCOL.md](PLAYTEST_PROTOCOL.md) for the blind-human, agent, no-index, mobile, accessibility, and customer-path test requirements. Use [RISK_REGISTER.md](RISK_REGISTER.md) for release blockers and mitigations across all phases.

### Phase E — commercial packaging

Create the revised product listing, start guide, episode-zero bridge, customer access instructions, spoiler-safe previews, and delivery package. Keep the held current Eleanor product and its assets intact while this is prepared.

**Gate E:** exact product/variant, $19.99 display, digital-delivery language, customer files, entry URL, access path, cart, and checkout are verified separately. Target duration and difficulty remain unclaimed until playtested.

### Phase F — release

Publish only after Owner_Bot approves the authored release and Grok returns observable evidence for all gates. No advertising spend is part of this build authorization.

## 11. Division of labor

### Owner_Bot owns

- canon and all story truth;
- every clue-bearing word and field;
- cast identities, allowed knowledge, dialogue, and episode beats;
- evidence graph, hints, solution, and aftermath;
- product and marketing claims;
- acceptance, revision, and release decisions.

### Grok owns

- repository implementation;
- static-site and Shopify-compatible code;
- visual layout using approved content;
- responsive behavior, accessibility, performance, and browser QA;
- deployment of explicitly authorized previews;
- screenshots, URLs, commit hashes, test output, and blocker reports.

Grok must not invent records, change dates/names, embellish cast dialogue, infer the solution, publish live, change Shopify shared product data, purchase anything, alter DNS, or spend money unless a later job card explicitly authorizes that exact action.

## 12. Definition of done

The game is complete only when:

- all five episodes and Episode Zero bridge are authored and implemented;
- the public universe contains every promised artifact and recovery route;
- the portal supports a clean solo playthrough with a player-supplied agent;
- cast scenes react to evidence state without altering canon;
- the final reconstruction is uniquely supportable within the case's stated bounds;
- author-only material remains outside the public repository and client bundle;
- structural, visual, logical, retrieval, spoiler, and customer-path checks are recorded;
- the final live URL and correct customer access path are verified.

An attractive preview, a Grok ACK, an indexed page, or a working Buy button is not completion evidence.

## 13. Current executable steps

Execute [GROK_JOB_HOLD.md](GROK_JOB_HOLD.md) for the reversible listing hold, then [GROK_JOB_001A.md](GROK_JOB_001A.md) for the private/unpublished architecture spike and evidence report. These scopes do not authorize the new edition, preview, theme, or archive universe to go live. Later phases remain queued until Owner_Bot reviews the receipts.

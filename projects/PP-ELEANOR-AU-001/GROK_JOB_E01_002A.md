# PP-ELEANOR-E01-002A — Episode Zero + Episode One implementation slice

**Status: AUTHORIZED FOR UNPUBLISHED IMPLEMENTATION.** Gate A is accepted and merged, and the locked E0–E1 content packet is committed. Execute only the bounds below and only from the exact execution-base commit named in Owner_Bot’s execution comment.

Owner: **Owner_Bot — Porch Press (ChatGPT)**  
Coordinator: **E_Lead**  
Hands: **E_Build, E_World, E_Portal**  
Independent check: **E_Audit**  
Cost ceiling: **$0**  
Publication authority: **none**

## Outcome

Turn the accepted fixture architecture into an unpublished real-content vertical slice for:

- Episode Zero — *The First Disappearance*;
- Episode One — *The Photograph*;
- five locked public records;
- five deterministic cast scenes;
- four distinct archive identities plus the case portal.

This job proves the authored-content pipeline and episode grammar. It does not authorize later episodes, the ending, a public preview, indexing, Shopify work, DNS, advertising, or spending.

## Required pins

Execution must name:

1. Gate A merge commit `060cc8dec3794dfd5fadd1b72674d50e6629ab08`;
2. Owner-published E0–E1 content packet commit `818d907f80378303b70dbb001c714a991f68f5ae`;
3. `DESIGN_DIRECTION.md` commit `5c797b78d1a4691a19a759210c6e2d72661b9fc9`;
4. audit-skill commit `5b1f18e4fecf4e719d4732374cf0f3b0a040ce93` or a later Owner-approved replacement.

Locked public input path: `projects/PP-ELEANOR-AU-001/public-batches/E0-E1/`

Episode Zero source pin: `releases/Eleanor-Hart/Eleanor-Hart-Customer.zip` must remain byte-identical at SHA-256 `9383547f51f5d705b6ecec2a9eb1c62a0ffe50d3ea13f86119315131e7203a98`.

Stop if the content-file hashes do not match the release manifest.

Pinned SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `release-manifest.json` | `e38f19c34cb10c2ddb077e3395796708561070b74ff8e75ed49a4025868ae328` |
| `public-content.json` | `8dc6cdc1244ee4cee6a19f3e6ecfd3af2f38005b9efddbdd21a6856408ebab97` |
| `episode-scripts.json` | `c9bcefbf14dd35f8a80f4f0887a2a24489ec9d514651ca25c6e7edf42401ebbd` |

## Exact content boundary

Only these records may appear:

| Artifact | Accession |
| --- | --- |
| `A001` | `CIM-HART-1912-01` |
| `A002` | `OIM-HW-1946-07` |
| `A003` | `BHR-PH-1951-17` |
| `A004` | `RRG-1948-10-18-A` |
| `A015` | `CIM-EH-1912-NB` |

Only these episodes and scenes may appear:

- `E0`: `E0-S01-COLD`, `E0-S02-RECEIPT`;
- `E1`: `E1-S01-INTAKE`, `E1-S02-ARTICLE_FIRST`, `E1-S03-LOOK`.

Use the supplied public artifact fields, dialogue, prompts, hints, rulings, and cliffhangers exactly. Layout labels may come from the approved design direction. Do not paraphrase clue text, embellish dialogue, invent a person/date/place, create an extra artifact, or ask for the author package.

The old 1912 release is immutable source material. It may be linked or copied to a new derived path only when the source and derived hashes are recorded. Do not edit, replace, re-zip, or overwrite anything under `releases/Eleanor-Hart/` or `marketing/Eleanor-Hart/`. Do not unpack its sealed-solution or complete-edition PDFs into the public archive surfaces; Episode Zero may remain an optional self-contained download with its own sealed answer.

## Locked portal baseline copy

Use these strings exactly; do not ask E_Portal to invent onboarding or status prose.

**Start headline**

> Eleanor Hart disappeared twice.

**Start body**

> The first time, her family tried to decide the story. The second time, the records did.
>
> You are the Lead Investigator. Your research agent can search and compare sources, but it cannot establish a fact without a page you can open. Save accession codes. Separate what a record says from what your investigator thinks it means. When the cast makes a dramatic claim, rule it supported, contested, or disproved.

**Actions**

- Primary: `Open the 1948 case`
- Secondary: `I need the 1912 case`
- Secondary: `I already know Episode Zero`
- Secondary: `How the fictional web works`

**Reality and privacy panel**

> This is fiction distributed across Porch Press-controlled websites. Archive pages stay in character, while their About pages explain the project provenance. Your notes and case progress stay in this browser unless you export them. The portal does not need or collect the conversation you have with your outside AI agent. Do not paste private or personal material into the evidence locker.
>
> Search engines and agents are inconsistent. Every necessary record also has a citation path and a direct recovery hint. A failed search is not a failed game.

**Standing outside-agent brief**

> Investigate the named person, phrase, place, or accession reference on the public web. Use only sources you can open. Return every relevant URL and accession code. Quote the exact fields that matter. In separate sections, state (1) what each record directly says, (2) what you infer, (3) contradictions or source limits, and (4) what remains unproved. Never invent a missing record, merge similarly named people, or solve beyond the evidence you found.

**Locker empty state**

> Your locker is empty. Start with the photograph, but do not save its label as a fact until you know who wrote it.

**Invalid token**

> That accession code does not match an available record. Check spaces, punctuation, and the visible archive page. A guessed code cannot unlock evidence.

**Duplicate token**

> Already in your locker. Add a new observation or return to the source instead of collecting the same code twice.

## Candidate structure

Create a new branch from current `main` at the exact execution-base commit named in Owner_Bot’s execution comment. Verify that the Gate A merge and content-packet commits above are ancestors, and keep the accepted fixture intact.

```text
game/PP-ELEANOR-AU-001/
  index.html
  portal/
  archives/
    cincinnati-industrial-memory/
    bellwether-historical-register/
    ohio-river-industrial-memory/
    river-and-rail-gazette/
  content/
    public-content.json
    episode-scripts.json
    release-manifest.json
  shared/
  tests/
  evidence/
```

Every HTML page remains `noindex,nofollow` for this candidate. No hosting configuration, Pages setting, deployment project, domain, or external service may be created.

## E_World contract

Implement four independently edited archive shells using the approved identity table. Each must have home, collection/catalog, About/provenance, record routes, robots, sitemap, and a recoverable 404 document.

Each record page must expose in human-readable static HTML:

- record title and accession;
- event/record date distinctions supplied in the packet;
- creator and holding institution;
- provenance and catalog note;
- transcription;
- related links only when both records exist in this batch;
- one copyable accession action;
- media slot, original-view control, and adjacent accessible description.

Cross-site links must behave like citations, not a game network. Archive navigation must never link to every other institution or to Porch Press checkout.

Media in this job is a **candidate proof layer**. Follow the locked media briefs, mark unfinished facsimiles as candidate material, preserve text in HTML, and do not let generated handwriting or newspaper text become the canonical transcription. No living-person likeness or celebrity reference. The 1946 and 1951 comparison must remain separate labeled records with full provenance; no filename, metadata, alt text, crop, or overlay may name the disputed woman's solved identity.

## E_Portal contract

Convert the one-off fixture logic into a data-driven scene engine over the locked batch.

- case ID: `PP-ELEANOR-AU-001`;
- local storage key: `pp-eleanor-au-001-v1`;
- schema version: `1`;
- default open movements: `E0`, `E1`;
- active episode: none until the player explicitly chooses the 1912 recap/full-case route or starts Episode One;
- accepted tokens: exactly the five accessions in the manifest;
- claim values: `supported`, `contested`, `disproved`;
- imported unknown tokens, claims, hints, scenes, and episodes are discarded;
- fixture exports and any other case ID are rejected;
- notes remain local and are never sent anywhere.

Scene behavior:

1. treat `episode_opened` as an explicit player entry into that episode, not merely membership in `episodes_open`;
2. evaluate scenes only inside the active episode, using exact `all_tokens`, `any_tokens`, and `none_tokens` conditions;
3. play the lowest newly eligible priority first;
4. play a scene once by default and queue any additional eligible scene;
5. show receipt before declaration;
6. visibly label every performer statement `CAST CLAIM` or `CROSS-EXAMINATION`;
7. show speaker, cited evidence, current ruling, and ruling edit trail;
8. apply only supplied state effects;
9. return control to the player before another tentpole;
10. never ingest, display, or store the player's outside-agent conversation.

Onboarding must explicitly say this is an authored open-web historical-fiction game and that all five investigators are synthetic produced personas. Inside the case, use the supplied in-world copy.

Episode One must support both discovery orders in the script. It must never identify the disputed person or settle any later-season question.

## E_Build contract

- Treat the content JSON as locked inputs, not editable application copy.
- Add a deterministic build/check that compares both content files to the release-manifest hashes.
- Keep essential archive text available with JavaScript disabled.
- Preserve ordinary links, keyboard access, visible focus, reduced motion, 44px targets, 16px body text, and 14px secondary metadata.
- Provide export/import/reset and exact invalid/new/duplicate token states.
- Add link, state, trigger-order, import-normalization, and spoiler-boundary tests.
- Do not add analytics, auth, a database, runtime AI, third-party embeds, package services, or network writes.

## Required test matrix

At minimum prove:

1. both content hashes match the Owner manifest;
2. only five valid tokens exist in source and runtime;
3. every record route, transcript, media link, About route, sitemap route, and recovery link resolves;
4. E0 receipt scene requires both E0 tokens;
5. E1 intake opens without evidence;
6. article-first scene plays only in its specified order and omits correctly in the alternate order;
7. comparison reveal requires both comparison accessions;
8. no scene plays twice unless explicitly replayed;
9. receipts precede claims and claims retain their edit trail;
10. clean export/import round-trip works and malformed, oversized, cross-case, and stray-field imports fail safely;
11. essential records remain readable with JavaScript disabled;
12. keyboard-only and 390×844 flows reach every primary action without overlap;
13. all evidence images match their extensions and declared dimensions;
14. no later artifact ID/accession, author-only note, sealed text, solution key, or protected conclusion appears in tree, history, generated output, asset metadata, or issue comments;
15. Shopify, DNS, campaigns, Pages, deployments, and spend remain unchanged.

Run `validate_evidence_pack.py` from the pinned audit skill. Current-candidate portal, all four archive homes, record view, E1 comparison state, claim/edit trail, keyboard focus, and 390×844 receipts are required. Pre-revision shots may be retained only as labeled regression context.

## Return format

```text
PP-ELEANOR-E01-002A COMPLETE | HOLD | BLOCKED
Branch and exact commit:
PR (Draft):
Content manifest commit and hash check:
Implemented routes:
Scene/state test output:
Link/static-HTML result:
Visual/accessibility evidence:
Evidence-pack validator output:
Spoiler/leakage scan:
Changed systems:
Unchanged systems:
Cost:
Known gaps:
Owner_Bot decision requested:
```

Do not mark COMPLETE while a required receipt is missing or inconsistent. Keep the PR Draft. Do not merge or deploy.

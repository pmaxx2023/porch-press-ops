# PP-ELEANOR-AU-001 — Public World and Retrieval Specification

This is a spoiler-safe implementation contract. It defines how public evidence behaves; it does not disclose the case solution.

## 1. Reliability principle

Search engines and agent search tools are nondeterministic. The experience may feel like an open-web search, but no required conclusion may depend on a new page ranking for a query.

For each required artifact, implement all three routes:

1. **Search route:** a distinctive, natural phrase a player can ask an agent to investigate.
2. **Citation route:** at least one earlier or sibling public page links to or specifically cites the artifact.
3. **Recovery route:** the portal can reveal a progressively stronger hint ending in the direct source URL.

Google states that ordinary `<a href>` links are the reliable crawlable form and that sitemaps help discovery without guaranteeing crawling or indexing. OpenAI distinguishes OAI-SearchBot search discovery from user-initiated ChatGPT-User retrieval. Build for both discovery and direct navigation:

- https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- https://developers.openai.com/api/docs/bots

## 2. Public surface contract

Each archive deployment must provide:

- `/` — an institutionally plausible home page;
- `/about` — scope, provenance, contact fiction, and restrained interactive-fiction disclosure;
- `/collections` or an equivalent catalog;
- stable artifact URLs with meaningful slugs;
- `/robots.txt`;
- `/sitemap.xml`;
- custom `404` page that returns the player to a legitimate catalog route;
- no login, age gate, consent wall, or client-only rendering before essential text;
- no direct navigation to a Porch Press checkout from clue pages.

Allow OAI-SearchBot and ordinary search crawling. A deliberate decision about GPTBot is separate and must not accidentally block the user-initiated retrieval path.

## 3. Artifact contract

Every clue-bearing page must include:

| Field | Requirement |
| --- | --- |
| Accession ID | Unique, stable, visible, and plausible for the hosting archive |
| Record title | Specific enough for citation without announcing the clue |
| Record date | Distinguish event date, creation date, and digitization date |
| Holding institution | Match the surface and voice |
| Provenance | State how the item entered the collection when material |
| Human-readable content | Essential fields in static HTML, not only pixels |
| Original-view media | Image or document view when visual inspection matters |
| Transcript | Faithful text, with illegible portions marked rather than invented |
| Related material | At least one natural crawlable citation where the clue graph calls for it |
| Evidence action | A plain way to copy/save the accession ID into the case portal |

Alt text should describe the document or image without interpreting the mystery or exposing concealed visual evidence. A transcript may reproduce text that is legitimately visible; it must not add an answer absent from the artifact.

## 4. World separation

The surfaces share a build system but must not share a conspicuous template.

- Use separate mastheads, palettes, type systems, navigation labels, and editorial voices.
- Reuse accessibility and performance primitives invisibly.
- Do not cross-link all sites in a game-like footer.
- Cross-site links must appear as citations, partner collections, bibliographic references, or provenance notes.
- Do not fake external organizations, endorsements, official seals, police notices, or public contact information.
- Use fictional addresses and institutions unless an ordinary historical fact has been verified and is not presented as an institutional identity.

## 5. Case portal state

The first release uses no Porch Press-hosted model inference.

Minimum local state:

```json
{
  "case_id": "PP-ELEANOR-AU-001",
  "schema_version": 1,
  "evidence_tokens": [],
  "claim_states": {},
  "episodes_open": ["E0", "E1"],
  "hints_used": [],
  "notes": "",
  "updated_at": "ISO-8601 timestamp"
}
```

Requirements:

- store locally by default;
- export and import the JSON explicitly;
- validate schema and case ID before import;
- never execute imported content;
- keep solution rules and resolution content out of the client bundle;
- do not collect or transmit conversations the player has with an outside agent;
- treat an accession code as discovered only after exact validation;
- make reset explicit and reversible through export.

## 6. Cast-scene contract

A cast scene is triggered by evidence state, not by search traffic or guessed intent.

Each scene data object must identify:

- scene ID and episode;
- exact evidence-token condition;
- lead investigator;
- artifact displayed;
- declaration labeled as a claim;
- cross-examination grounded in visible evidence;
- optional confessionals;
- player classification request;
- next research question;
- spoiler tier.

The public client may contain only scenes safe for its current release tier. Final resolution plaintext and scoring keys remain outside the public repository and ungated client assets.

For production, return the ending through a small server-side sealed-envelope endpoint after normalized final selections and evidence classes pass. Keep the authored response in protected deployment storage. Do not send free-form player notes or outside-agent conversations to that endpoint. The fixture-only architecture spike does not implement or simulate the real scoring key.

## 7. Agent prompt contract

The portal may provide copyable prompts. Default research prompt:

> Investigate the named person, phrase, place, or accession reference on the public web. Use only sources you can open. Return each URL, quote the exact fields that matter, distinguish the record's statement from your inference, identify contradictions, and say what remains unproved. Do not invent missing facts or solve beyond the evidence you found.

Prompts must not embed the solution, hidden aliases, expected destination URLs, or later-episode facts.

## 8. Measurement

Record only product-use events needed to diagnose the experience, such as portal opened, episode opened, hint tier selected, evidence token accepted, final submission attempted, and completion reached. Do not treat an agent crawler, archive page view, or token attempt as a human player or sale.

Analytics is not required for the architecture spike. If added later, distinguish human, owner/test, and known bot traffic.

## 9. Pre-release checks

- Crawl all public links from the entry points.
- Fetch every page without cookies and with JavaScript disabled where essential text is expected.
- Inspect robots and sitemap output.
- Verify all accession codes and cross-site citations.
- Verify images, transcripts, print views, and mobile layouts.
- Search repository and generated bundles for prohibited solution terms supplied by Owner_Bot.
- Run a clean portal state from opening through final submission.
- Test direct-link recovery independently from open-web search.
- Record indexing as observed or unknown; never call sitemap submission proof of search availability.

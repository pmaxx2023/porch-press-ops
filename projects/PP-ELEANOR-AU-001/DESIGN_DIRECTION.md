# PP-ELEANOR-AU-001 — Spoiler-Safe Design Direction

## Design thesis

Build **an archival field desk cut like prestige reality television**.

The evidence should feel quiet, specific, and older than the portal. The show layer should feel immediate: claim cards, evidence receipts, split reactions, confessionals, reversals, and the player's visible edit history. Do not make the archives look like escape-room props or the cast look like cartoon generation mascots.

## Case portal

### Visual language

- Near-black ink, warm paper, desaturated cobalt, and one controlled signal red.
- Dense evidence surfaces surrounded by generous margins.
- Large episode numerals and short production slates create the reality-show rhythm.
- Evidence receipts use stable accession IDs, source title, holding institution, and a direct return link.
- Claims are visually distinct from facts: a claim card always carries a speaker, status, and evidence cited.
- Preserve status changes as an edit trail: `CONTESTED → SUPPORTED` should remain visible rather than silently replacing the old state.

### Typography

- Interface and labels: a highly legible system sans.
- Long evidence text: a screen-safe book serif.
- Accession IDs and source fields: a restrained monospace.
- Avoid distressed type for body copy, handwriting fonts for transcriptions, and tiny all-caps metadata.

Minimum target sizes for the preview: 16px body, 14px secondary metadata, 44×44px touch targets, and no evidence text embedded only in an image.

### Core screen hierarchy

1. Current answerable question.
2. One primary action: investigate, inspect receipt, rule claim, or continue.
3. Source receipt and evidence-state change.
4. Cast reaction.
5. Episode progress, notes, export, and hints.

Do not lead with a decorative dashboard that makes the player hunt for the next action.

## Archive identities

All surfaces may share invisible code primitives. Their public presentation must appear independently edited.

| Surface | Character | Palette | Type/layout | Navigation voice |
| --- | --- | --- | --- | --- |
| Cincinnati Industrial Memory Archive | Older local manuscript room | Oxidized blue, buff paper, graphite | Book serif, finding-aid hierarchy, typed folder labels | Collections, Finding Aids, Manuscripts, Research Notes |
| Bellwether Historical Register | Small house archive maintained with care | Faded plum, moss, cream | Humanist serif, bookplates, room/box references | The House, Registers, Photographs, Correspondence, About the Record |
| Ohio River Industrial Memory Project | Volunteer industrial-history database | Navy, rust, cool gray | Condensed sans headings, grid tables, blueprint rules | Companies, People, Record Groups, Technical Drawings |
| River & Rail Gazette Archive | Digitized regional newspaper and transport files | Newsprint, black, muted red | Newspaper serif, narrow measure, date-first browse | Browse by Date, City Desk, Rail Files, Reporter Notebooks |
| North Parish Records & Memorial Register | Community transcription and memorial index | Stone, dark green, parchment | Transitional serif, simple register rows, restrained ornament | Family Files, Memorials, Office Ledgers, Transcription Policy |

For the architecture spike, implement three of these identities with `FIXTURE-*` content. Do not use the real names or artifact copy if Owner_Bot has not supplied that exact content packet.

## Cast presentation

The investigators are recurring synthetic performers, not chatbots waiting in five equal boxes.

| Cast role | On-screen grammar | Visual cue | Avoid |
| --- | --- | --- | --- |
| Provenance editor / Boomer lens | Source-card annotation and calm cross-examination | Archive blue, square frame, paper-tab motif | Nostalgia caricature or technological confusion |
| Investigations editor / Gen X lens | Timeline strike-throughs and incentive maps | Charcoal, amber underline, newsroom crop | Cynical one-liners without evidence |
| Forensic genealogist / Millennial lens | Relationship overlays and identity-proof tables | Plum, connecting rule, rounded portrait crop | DNA magic or therapy-speak parody |
| OSINT producer / Gen Z lens | Fast visual comparison and emphatic receipt reveal | Cobalt, signal red, vertical crop | Slang costume, unsupported caps, virality as proof |
| Pattern analyst / Gen Alpha lens | Multimodal overlays and counterexample tiles | Pale acid green used sparingly, layered frame | Depicting a real employed child, baby talk, oracle behavior |

Only the two or three relevant cast members appear in a scene. Use one lead frame, one objection frame, then optional confessionals. The player should never face five simultaneous dialogue columns.

All five are disclosed as synthetic produced investigator personas. Portraits may be stylized editorial photography or graphic composites, but must not imitate a living celebrity or imply documentary footage of a real person.

## Reveal grammar

### Receipt

Show the actual artifact first. Keep its title, date, accession ID, source institution, and relevant visible area on screen.

### Declaration

Cut to the lead cast member. A statement such as “LOOK what we found” can use scale, sound, or motion, but the interface labels it **CAST CLAIM**.

### Crossfire

Place the objection beside the exact inferential gap. Do not cover the receipt with reaction video.

### Player ruling

Return focus to the evidence. Supported, contested, and disproved must have text labels, icons/shapes, and accessible descriptions; color alone is insufficient.

### Revision

When later evidence changes the ruling, animate the edit rather than the disappearance of the old state. Respect `prefers-reduced-motion` with an immediate textual transition.

## Motion and sound

- Motion budget: one meaningful transition per reveal; no constant film grain, floating documents, parallax desk, or auto-advancing dialogue.
- Default scene pace is player-controlled. Never make evidence disappear before it can be read.
- Sound is optional and off until initiated. Captions/transcripts are required for every spoken performance.
- Suitable cues: slate click, paper movement, quiet room tone, restrained impact at a claim revision.
- Avoid police scanner audio, emergency sirens, horror stingers, fake voicemail notifications, and anything implying a live real-world alert.

## Artifact treatment

- The human-readable HTML transcription is primary; the facsimile is evidence media, not decoration.
- Show event date, creation date, and digitization/catalog date separately where applicable.
- Preserve crops as historical objects but always provide the full view when context matters.
- Do not highlight the clue inside an archive by default. The portal may focus attention only after the player saves the artifact.
- Handwriting comparisons need synchronized zoom and rotation controls with a reset.
- Never add fake water damage, red circles, sticky notes, or ominous fingerprints unless present in the approved media brief.

## Responsive behavior

At 390×844:

- one column for evidence and scene dialogue;
- sticky current-question bar no taller than two compact lines;
- receipt metadata before cast reaction;
- claim actions remain reachable without covering document controls;
- side-by-side comparisons become a synchronized tab/slider with explicit labels;
- export, reset, privacy, and About remain accessible through a normal menu, not hidden gestures.

On desktop, a two-pane layout may pair the artifact with the claim/cast pane. Do not exceed three meaningful columns.

## Accessibility and legibility

- Logical heading order and landmarks on every page.
- Full keyboard path with visible focus.
- Transcripts adjacent to document media.
- Text alternatives describe the document without solving a concealed visual inference.
- Zoomable originals, reflowable HTML, and no forced horizontal reading for transcriptions.
- WCAG AA contrast target for text and controls.
- Status, speaker, archive, and episode distinctions do not rely only on color, face, sound, or position.

## Reality-ambiguity boundary

The evidence pages should behave like serious small archives. They do not use puzzle language, progress bars, dramatic music, or Porch Press checkout links.

Each archive has an ordinary About/Provenance route with a restrained disclosure that it belongs to an authored historical-fiction project. The storefront and onboarding state this plainly. The in-case portal may stay in-world after onboarding, but it never claims a real person is currently missing or asks the public for real-world tips.

## Spike acceptance

The fixture preview passes design review only when:

- the portal's next action is obvious in five seconds;
- three archive shells are recognizable without reading their mastheads;
- one receipt → declaration → objection → ruling sequence is legible on desktop and mobile;
- a cast claim cannot be mistaken for archive narration;
- export/import/reset and invalid-token states feel native to the same product;
- keyboard, focus, contrast, reduced motion, and readable type checks are evidenced;
- no real Eleanor canon appears in fixture copy, filenames, screenshots, or build output.

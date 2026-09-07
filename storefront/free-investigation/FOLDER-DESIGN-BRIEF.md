# Roscoe’s Grave — animated folder design assignment

**Owner_Bot — Porch Press (ChatGPT)**  
**Task:** PP-ROSCOE-FOLDER-DESIGN-001  
**Date:** 7 September 2026  
**Route:** Connector_Bot → existing Grok store designer / Shopify_Bot  
**Work and receipts:** [issue #5](https://github.com/pmaxx2023/porch-press-ops/issues/5)

## PM’s direction

PM reviewed an animated-folder experiment and said: “interesting, its needs a lot more visual appeal. lets ask grok bot agents to put a designer on it”. PM then specified: “also lets use roscoe as the example”.

Assign a designer through the existing Grok workflow and produce a polished, working **Roscoe’s Grave** folder experience for review. The visual design needs a substantial improvement. Choose and execute one strong direction using existing tools.

Roscoe is the case for this assignment. The separate Blue Folder / Vale-family sketch is not source content. Do not transplant its characters, records, father-confrontation branches or ending into Roscoe.

## Authoritative source and existing implementation

Use the complete approved free Roscoe browser investigation already in this repository:

- [Playable source at approved commit ed32a02](https://github.com/pmaxx2023/porch-press-ops/blob/ed32a029371e17df363e31ad6e46dc35ad9ea229/storefront/free-investigation/Porch-Press-Free-Investigation.html).
- Source SHA-256: `86d1a7c106f48046b886279b0684396883892c9f1e2f86fa4533ca2bee8f11d2`; Git blob: `a0a6015cb9b2eda3b27f4f6997368fd33f00e176`; 813946 bytes. Owner_Bot read the current source and confirmed this blob before assigning.
- [Existing implementation instructions](IMPLEMENTATION.md) and [manifest](manifest.json).
- [Current free page](https://porchpress.store/pages/free-investigation).
- [Grok’s completed implementation receipt](https://github.com/pmaxx2023/porch-press-ops/issues/5#issuecomment-5560730468): section `sections/pp-free-investigation.liquid`, template `templates/page.free-investigation.json`, assets `pp-roscoe-sample.css`, `pp-roscoe-sample.js`, `pp-roscoe-assets.json`. Inspect current state before adapting.

Use the existing eight original record images and matching readable text: **R01, R02, R04, R05, R07, R08, R13, R14**. The existing source already contains the cover, opening story, optional hints, finding form, solution and aftermath. No new story or evidence authoring is needed.

## Design direction: a family archive worth opening

Make the folder the focal object: a tactile, deep navy archival folder on a warmly lit desk, with convincing paper thickness, a tab, restrained wear, a cream title label and layered shadows. Use Porch Press navy, warm paper and restrained gold as a starting palette. Give the typography, composition and materials a considered editorial treatment. The designer has latitude over the visual execution.

Use the existing Roscoe cover artwork for atmosphere where useful. Evidence artwork must remain exact and readable. Decorative distress, props or markings must not imply additional clues. Avoid generic dashboard cards, excessive interface chrome, illegible miniatures and a wall of equal-weight buttons.

The first view should make the situation and next action clear:

- **Title / folder label:** Roscoe’s Grave
- **Setting:** Briarport, Maine · 1937
- **Hook:** His name is on the stone. Someone else is in the book.
- **Premise:** Ada wants her mother’s name added beside her father’s. Then the cemetery records stop the mason’s chisel.
- **Primary action:** Open the folder
- **Supporting line:** Free to play. No download or sign-up.
- Keep **Read Ada’s story** available as a secondary action.

These are Owner_Bot-approved words. Existing story, record and answer copy remains authoritative. Additional approved functional labels are **Skip animation** and **Back to the folder**.

## Interaction to build

1. A visitor clicks or taps **Open the folder**.
2. The cover opens with a convincing hinge and depth; the papers slide into a composed spread. Aim for roughly one second of deliberate motion, followed promptly by usable evidence. Keep sound off.
3. Lead visually with **R01, the mason’s work order**, and **R02, the cemetery working index**. Keep all eight records available in the original order; the player can choose what to inspect.
4. Selecting a paper brings it forward into a comfortable reading view. Preserve original-page and readable-text modes, previous/next controls and returning to the folder. Show which records have been opened.
5. Continue through the existing complete investigation, finding, solution and aftermath. Preserve the closing Baby in a Basket CTA.

The opening must work with touch and keyboard. Provide visible focus, usable touch targets, clear reading contrast and a reduced-motion path that reveals the same content immediately. A skip action must finish the reveal cleanly. Repeated clicks, resizing or returning from a document must not strand the player or replay a blocking intro.

## Content and logic to preserve

Owner_Bot retains all authorship. Grok owns presentation and implementation within this assignment.

Preserve every record field, name, date, reference, caveat, hint and scene. Keep the existing three-part answer logic: **Miriam Cross / Roscoe’s mother / memorial**. Incorrect or incomplete findings must still receive the correct existing feedback. The solution remains deliberately revealed, with the complete approved aftermath accessible.

Preserve the distinction between documentary evidence and unrecorded physical remains. Do not turn an inscription into proof of burial, invent a coffin swap, add a confession, manufacture an interactive character response, or disclose the answer on the closed folder. Report any actual content defect to Owner_Bot.

## Deliverable and review

Build a working design preview using the existing implementation or a self-contained browser file. Commit the current review source and required assets under `storefront/free-investigation/folder-preview/`, or report the existing draft-theme change record if that is the practical implementation route. Keep one current candidate.

Return:
- The assigned designer’s actual role/name and a concise explanation of the visual direction.
- A working preview URL or downloadable playable HTML, with the source commit/change record.
- Desktop and mobile screenshots of the closed folder, opened spread and selected readable record.
- A short recording of opening the folder and selecting a record, if capture is supported.
- Actual browser verification at desktop and 360/390 px mobile: animation, skip/reduced motion, keyboard/touch, all eight documents and both reading modes, empty/wrong/correct findings, deliberate solution reveal, complete aftermath and Baby CTA. Report any check or recording that could not be performed.

The earlier Blue Folder motion sketch had code-level checks but no completed browser visual verification. Verify this Roscoe implementation in a real browser; screenshots alone do not establish that the interaction works.

This assignment is the designer’s working preview for review. Keep the existing published free case available while preparing it; do not replace the live page or homepage as part of this preview handoff. Baby remains the paid hero, and the existing coming-soon cards remain in place. Use existing tools; no spending or new subscriptions.

Post one **ACK PP-ROSCOE-FOLDER-DESIGN-001** in issue #5 with the brief commit read and designer assignment, then one concrete completed result or a precise blocker with the work already done. Do not ask PM to ferry files between agents.

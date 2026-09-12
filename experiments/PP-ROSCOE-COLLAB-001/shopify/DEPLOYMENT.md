# PP-ROSCOE-COLLAB-001 — Shopify draft receipt

**State:** Implemented in an unpublished Shopify theme; not live.  
**Prepared by:** Owner_Bot — Porch Press (ChatGPT)  
**Prepared:** 2026-09-12  
**New spend:** $0

## Targets

- Store: Porch Press — porchpress.store — Basic — USD.
- Live theme preserved: Refresh — `gid://shopify/OnlineStoreTheme/152900272426`.
- Unpublished working theme: OwnerBot Roscoe Case Room 2026-09-12 — `gid://shopify/OnlineStoreTheme/190768349482`.
- Target page: `/pages/free-investigation`.
- Target section: `sections/pp-free-investigation.liquid`.

## File record

| Theme/file | Before | Draft after |
| --- | --- | --- |
| Live `sections/pp-free-investigation.liquid` | MD5 `520cc8e071c984b645d75c871eab91d5` · 12,614 bytes | Live file unchanged |
| Draft `sections/pp-free-investigation.liquid` | copied from live | MD5 `252572c68d1b25f5a1bf0aecdffdb418` · 14,529 bytes |
| Draft `assets/pp-roscoe-case-room.css` | absent | MD5 `75c5609da5491bed5c59a0534a6fec64` · 1,274 bytes |

## Implemented in draft

- Added the disclosed **Roscoe Case Room** invitation between the evidence introduction and record grid.
- Added a compact theory-discussion invitation after the player's finding flow and before solution reveal.
- Both controls target the exact candidate r/printandplay thread.
- Replaced the post-solution Baby bridge with the approved $19.99 copy and UTM route:
  `utm_source=roscoe_case&utm_medium=community&utm_campaign=pp_roscoe_collab_001&utm_content=case_complete`.
- Preserved the existing story, eight records, answer logic, hints, solution, aftermath, navigation, and folder interaction.
- Added no app, login, form gate, tracker, popup, synthetic player, avatar, count, review, discount, product, or spend.

## Verification performed

- Draft theme loaded the free investigation without a Liquid error.
- Folder-to-investigation transition passed.
- Main case-room block rendered and was visible.
- Exact Reddit destination was present on the case-room control.
- Finding screen rendered the compact discussion prompt.
- Solution screen rendered the tracked **Open Baby in a Basket — $19.99** link with the exact approved UTM values.
- Desktop viewport was 1,348 px wide with document scroll width also 1,348 px: no horizontal overflow.
- The new stylesheet includes a 640 px mobile rule, full-width mobile control, and reduced padding. A true 390×844 device viewport was not available in the current browser, so final mobile visual acceptance remains open.
- Re-query confirmed the live main theme has neither the case-room block nor the new CSS asset.

## Publication gate

Do not publish this draft until Grok proves that the candidate Reddit account/thread is controlled by Porch Press and the current surface remains permitted. After that gate, complete 390×844 visual QA and publish or copy these exact two files to the then-current main theme. Re-verify the thread, full case, Baby route, cart, and checkout after publication.

## Rollback

No rollback is required now because the live theme was not changed. If this draft is later published, rollback is the current Refresh theme `152900272426`; confirm any newer shared-store changes before switching themes.

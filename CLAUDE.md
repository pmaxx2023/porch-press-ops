# Claude — Porch Press communication bridge

PM requested a ChatGPT ↔ Claude bridge in the existing Porch Press GitHub repository. This file adds Claude to the communication channel; it does not replace the Grok bridge or assign a new permanent business role.

## Start here

1. Read OWNER_BOT.md and the current relevant task's latest comments. Older operating checkpoints may be stale; use newer explicit PM instructions and concrete receipts.
2. Use [issue #2](https://github.com/pmaxx2023/porch-press-ops/issues/2) for bridge setup and routing. Use each existing task issue for its work and results.
3. Complete handshake **PP-CLAUDE-BRIDGE-001** in issue #2. Read the Owner_Bot handshake comment before responding.

## Identity and responsibilities

- PM owns the accounts, business direction, and spending authority.
- Owner_Bot — Porch Press (ChatGPT) retains authorship, canonical releases, content approval, operational coordination, and advertising under the established agreement.
- Grok / Connector_Bot / Shopify_Bot retains its existing Shopify implementation and transport assignments.
- Claude's initial assignment is repository onboarding and communication verification. Report any work PM has already assigned you, including scope and affected files, so Owner_Bot can coordinate it. Do not infer a new permanent role from this file. Later explicit PM assignments govern.

Every message must identify its actual sender and intended recipient because agents may share PM's GitHub identity. Do not rely on a GitHub username or a mention to distinguish agents.

## Message contract

Include:
- Sender and recipient: e.g. Claude — Porch Press → Owner_Bot — Porch Press (ChatGPT).
- Stable task ID and revision, plus the exact issue/comment being answered.
- Type: ACK, QUESTION, RESULT, BLOCKED, or ASSIGNMENT.
- Result or requested action, scope, source commit/files, evidence, and next action as applicable.
- Observed / reported / unverified distinctions.

Acknowledge a task revision once. ACKs and status reports are not new assignments. Reply to the same task issue; do not redispatch work or create duplicate issues each time you read the repository. Before a write, read current state and check whether another agent already completed it. If overlapping work is detected, report the collision before editing the same files or live objects. For assigned code changes, use a scoped branch/PR unless direct changes are explicitly authorized; do not merge or deploy merely because a PR exists.

Keep current customer releases separate from author/source files and internal reports. Reference repository paths and commit hashes rather than inaccessible local paths. Do not include credentials, tokens, or customer identities in bridge messages.

## Handshake response

Post one response in issue #2:

ACK PP-CLAUDE-BRIDGE-001
Sender: Claude — Porch Press
Recipient: Owner_Bot — Porch Press (ChatGPT)
In reply to: [exact Owner_Bot handshake comment URL]
Repository/commit read: [actual commit]
Access confirmed: [what you actually read; this reply demonstrates comment write access]
Other capabilities: [verified / unavailable / untested — distinguish file writes, PRs, browser, Shopify, and Meta]
Current PM assignments: [scope and affected files/objects, or none]
How detected: [manual request, existing schedule, or actual event trigger]
Existing trigger evidence: [configuration and observed run evidence, or none]
Blocker / next action: [concrete result]

Do not perform live store/ad changes, spend, publish products, rewrite product content, install software, or create a new routine for this handshake. Existing separately authorized assignments retain their scope.

## Delivery and wake-up

GitHub is an asynchronous mailbox, not proof of an always-running agent connection. Comment posting proves outbound transport; retrieving the other agent's reply proves the return path. A mention alone does not wake ChatGPT or Claude. Do not claim monitoring or a schedule without verifying its actual setup. Reuse existing routines where authorized; do not create duplicates.

Owner_Bot will read the Claude ACK and reply with a receipt identifying its comment ID. Until then, the bridge is prepared and awaiting round-trip confirmation.

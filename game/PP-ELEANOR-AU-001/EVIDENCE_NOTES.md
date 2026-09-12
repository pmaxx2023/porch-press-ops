# EVIDENCE_NOTES — PP-ELEANOR-E01-002A

Local base: `http://127.0.0.1:8765`

```bash
cd game/PP-ELEANOR-AU-001
python3 -m http.server 8765
```

## Capture source

All **current** receipts below were captured from functional source SHA:

`bc73ecd7f86df67ecfb3de14692987129343a970` (short: `bc73ecd`)

Directory: `evidence/bc73ecd/`

Portal PASS expected on this tip (crossfire labels + claim prompt + evidenceShot hooks).  
World ARCHIVE PASS on `3d28ead` still stands (archives untouched since).

## Current desktop receipts (1280 PNG)

| Case | Path |
| --- | --- |
| Hub | `evidence/bc73ecd/01-hub-1280.png` |
| Portal opening | `evidence/bc73ecd/02-portal-opening-1280.png` |
| Invalid token | `evidence/bc73ecd/03-invalid-1280.png` |
| Valid token | `evidence/bc73ecd/04-valid-1280.png` |
| Duplicate token | `evidence/bc73ecd/05-duplicate-1280.png` |
| CIM home | `evidence/bc73ecd/06-cim-home-1280.png` |
| BHR home | `evidence/bc73ecd/07-bhr-home-1280.png` |
| OIM home | `evidence/bc73ecd/08-oim-home-1280.png` |
| RRG home | `evidence/bc73ecd/09-rrg-home-1280.png` |
| CIM record | `evidence/bc73ecd/10-record-cim-hart-1280.png` |
| E1 comparison / CROSS-EXAM | `evidence/bc73ecd/11-e1-comparison-1280.png` |
| Claim edit trail | `evidence/bc73ecd/12-claim-edit-trail-1280.png` |
| Keyboard focus | `evidence/bc73ecd/13-keyboard-focus-1280.png` |

## Mobile sticky

| Case | Path |
| --- | --- |
| 390 sticky CQ bar | `evidence/bc73ecd/390-sticky-cq-bar.png` |

## Notes

- Sticky: `.current-question-bar` at `top:0` @ ≤844px; no fixture-banner sticky.
- Portal interactive receipts used `?evidenceShot=` hooks (play defaults unchanged).
- Do not treat `evidence/_harness/` or other tip folders as current receipts.

#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1] / "content"
manifest = json.loads((root / "release-manifest.json").read_text())
expected = manifest["sha256"]
ok = True
for name, want in expected.items():
    data = (root / name).read_bytes()
    got = hashlib.sha256(data).hexdigest()
    print(f"{name}: {got} {'OK' if got == want else 'FAIL want ' + want}")
    if got != want:
        ok = False
# also hash the manifest itself against Owner pin when provided via env optional
sys.exit(0 if ok else 1)

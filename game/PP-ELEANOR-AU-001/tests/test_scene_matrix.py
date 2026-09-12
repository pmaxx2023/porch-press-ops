#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = json.loads((root / "content/public-content.json").read_text())
scripts = json.loads((root / "content/episode-scripts.json").read_text())
manifest = json.loads((root / "content/release-manifest.json").read_text())

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

assert sha(root / "content/public-content.json") == manifest["sha256"]["public-content.json"]
assert sha(root / "content/episode-scripts.json") == manifest["sha256"]["episode-scripts.json"]
codes = [a["accession_code"] for a in content["artifacts"]]
assert codes == manifest["accession_codes"]
assert len(codes) == 5

def trigger_ok(tr, tokens, episode_opened):
    if tr.get("episode_opened") and not episode_opened:
        return False
    for t in tr.get("all_tokens") or []:
        if t not in tokens:
            return False
    for t in tr.get("none_tokens") or []:
        if t in tokens:
            return False
    any_tokens = tr.get("any_tokens")
    if any_tokens is not None and not any(t in tokens for t in any_tokens):
        return False
    return True

scenes = {s["id"]: s for ep in scripts["episodes"] for s in ep["scenes"]}
assert trigger_ok(scenes["E0-S01-COLD"]["trigger"], [], True)
assert not trigger_ok(scenes["E0-S02-RECEIPT"]["trigger"], ["CIM-HART-1912-01"], True)
assert trigger_ok(scenes["E0-S02-RECEIPT"]["trigger"], ["CIM-HART-1912-01", "CIM-EH-1912-NB"], True)
assert trigger_ok(scenes["E1-S01-INTAKE"]["trigger"], [], True)
assert trigger_ok(scenes["E1-S02-ARTICLE_FIRST"]["trigger"], ["RRG-1948-10-18-A"], True)
assert not trigger_ok(scenes["E1-S02-ARTICLE_FIRST"]["trigger"], ["RRG-1948-10-18-A", "OIM-HW-1946-07"], True)
assert trigger_ok(scenes["E1-S03-LOOK"]["trigger"], ["OIM-HW-1946-07", "BHR-PH-1951-17"], True)
# no later artifact ids
tree = "\n".join(p.as_posix() for p in root.rglob("*"))
for bad in ["A005", "A006", "E2-", "E3-", "E4-", "E5-"]:
    assert bad not in tree
print("PASS test_scene_matrix")

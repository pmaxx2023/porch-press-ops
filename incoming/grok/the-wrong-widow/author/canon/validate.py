#!/usr/bin/env python3
"""Validate The Wrong Widow canonical dataset. Exit 0 only if all checks pass."""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

CANON = Path(__file__).resolve().parent
errors: list[str] = []
DS = "wrong-widow-canon"
REQUIRED_FILES = [
    "people.json", "relationships.json", "events.json", "documents.json",
    "observations.json", "canonical_truth.md", "validation_report.md",
    "README.md", "validate.py",
]


def fail(msg: str) -> None:
    errors.append(msg)


def load_json(name: str):
    path = CANON / name
    if not path.exists():
        fail(f"missing file: {name}")
        return None
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def as_list(data, key: str):
    if data is None:
        return []
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and key in data:
        return data[key]
    fail(f"expected list or object.{key} in structure")
    return []


def parse_date(value):
    if not value:
        return None
    s = str(value).strip()
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    fail(f"unparseable date: {value!r}")
    return None


for name in REQUIRED_FILES:
    if not (CANON / name).exists():
        fail(f"missing required file: {name}")

people_data = load_json("people.json")
rels_data = load_json("relationships.json")
events_data = load_json("events.json")
docs_data = load_json("documents.json")
obs_data = load_json("observations.json")

people = as_list(people_data, "people")
rels = as_list(rels_data, "relationships")
events = as_list(events_data, "events")
documents = as_list(docs_data, "documents")
observations = as_list(obs_data, "observations")

for label, data in [
    ("people.json", people_data), ("relationships.json", rels_data),
    ("events.json", events_data), ("documents.json", docs_data),
    ("observations.json", obs_data),
]:
    if isinstance(data, dict) and data.get("dataset") != DS:
        fail(f"{label} dataset must be {DS!r}")

n = len(people)
if not (20 <= n <= 28):
    fail(f"people count {n} not in 20–28")
ids = [p.get("person_id") for p in people]
expected_ids = [f"P{i:03d}" for i in range(1, n + 1)]
if ids != expected_ids:
    fail(f"person_ids must be contiguous P001–P{n:03d}, got {ids}")
if len(ids) != len(set(ids)):
    fail("duplicate person_id")
by_id = {p["person_id"]: p for p in people if p.get("person_id")}

# Principals
elias = by_id.get("P001")
martha = by_id.get("P002")
lydia = by_id.get("P003")
if not elias or elias.get("canonical_given_name") != "Elias" or elias.get("canonical_surname") != "Corbett":
    fail("P001 must be Elias Corbett")
if elias and elias.get("birth_date") != "1836-05-09":
    fail("P001 birth_date must be 1836-05-09")
if elias and elias.get("death_date") != "1887-02-14":
    fail("P001 death_date must be 1887-02-14")
if not martha or martha.get("canonical_maiden_name") != "Ashby":
    fail("P002 must be Martha Ashby Corbett")
if martha and martha.get("birth_date") != "1839-09-14":
    fail("P002 birth_date must be 1839-09-14")
if not lydia or lydia.get("canonical_maiden_name") != "Briggs":
    fail("P003 must be Lydia Briggs Corbett")
if lydia and lydia.get("birth_date") != "1845-02-28":
    fail("P003 birth_date must be 1845-02-28")

# Children dates
child_dates = {
    "P004": "1859-07-22", "P005": "1861-11-03",
    "P006": "1867-09-14", "P007": "1870-04-08", "P008": "1874-08-19",
}
for pid, d in child_dates.items():
    p = by_id.get(pid)
    if not p:
        fail(f"missing child {pid}")
    elif p.get("birth_date") != d:
        fail(f"{pid} birth_date must be {d}")

# Relationships: Martha lawful; Lydia ceremony; no Elias+Martha divorce
lawful = [r for r in rels if set(r.get("person_ids") or []) == {"P001", "P002"} and r.get("type") == "spouse"]
if not lawful:
    fail("missing spouse relationship Elias–Martha")
else:
    if lawful[0].get("legal_status") != "lawful_undissolved":
        fail("Elias–Martha must have legal_status=lawful_undissolved")
    if lawful[0].get("date_start") != "1858-03-12":
        fail("Elias–Martha date_start must be 1858-03-12")

ceremony = [r for r in rels if set(r.get("person_ids") or []) == {"P001", "P003"} and r.get("type") in ("ceremony_spouse", "spouse")]
if not ceremony:
    fail("missing ceremony/spouse relationship Elias–Lydia")
else:
    ok_status = ceremony[0].get("legal_status") in ("ceremony_only", "unlawful", "ceremony_only_unlawful")
    ok_type = ceremony[0].get("type") == "ceremony_spouse"
    if not (ok_status or ok_type):
        fail("Elias–Lydia must be ceremony_spouse or spouse with ceremony_only/unlawful status")
    if ceremony[0].get("date_start") != "1866-06-04":
        fail("Elias–Lydia date_start must be 1866-06-04")

# No divorce relationship for Elias+Martha
for r in rels:
    pset = set(r.get("person_ids") or [])
    if pset == {"P001", "P002"} and (r.get("type") == "divorce" or r.get("legal_status") == "divorced"):
        fail("NO divorce relationship allowed for Elias+Martha")

# Parent-child counts
pc = [r for r in rels if r.get("type") == "parent-child"]
martha_kids = sorted(r["child_id"] for r in pc if r.get("parent_id") == "P002")
lydia_kids = sorted(r["child_id"] for r in pc if r.get("parent_id") == "P003")
elias_from_martha = sorted(r["child_id"] for r in pc if r.get("parent_id") == "P001" and r.get("child_id") in ("P004", "P005"))
elias_from_lydia = sorted(r["child_id"] for r in pc if r.get("parent_id") == "P001" and r.get("child_id") in ("P006", "P007", "P008"))
if martha_kids != ["P004", "P005"]:
    fail(f"Martha children must be P004,P005 got {martha_kids}")
if lydia_kids != ["P006", "P007", "P008"]:
    fail(f"Lydia children must be P006-P008 got {lydia_kids}")
if elias_from_martha != ["P004", "P005"]:
    fail(f"Elias+Martha kids mismatch {elias_from_martha}")
if elias_from_lydia != ["P006", "P007", "P008"]:
    fail(f"Elias+Lydia kids mismatch {elias_from_lydia}")

# Events spine
def find_events(etype, person=None):
    out = []
    for e in events:
        if e.get("type") != etype:
            continue
        if person and person not in (e.get("person_ids") or []):
            continue
        out.append(e)
    return out

enlist = find_events("enlistment", "P001")
if not enlist or enlist[0].get("date") != "1862-08-15":
    fail("enlistment event for P001 on 1862-08-15 required")
desert = find_events("desertion", "P001")
if not desert or desert[0].get("date") != "1863-12-01":
    fail("desertion event for P001 on 1863-12-01 required")
hosp = find_events("hospitalization", "P001")
if not hosp or hosp[0].get("date") != "1863-10-20":
    fail("hospitalization event for P001 on 1863-10-20 required")

# Elias canonical death only 1887
elias_deaths = [e for e in events if e.get("type") == "death" and "P001" in (e.get("person_ids") or [])]
if len(elias_deaths) != 1:
    fail(f"Elias must have exactly one canonical death event, got {len(elias_deaths)}")
elif elias_deaths[0].get("date") != "1887-02-14":
    fail("Elias canonical death must be 1887-02-14")

# False 1863 death must be document_claim not death
for e in events:
    if e.get("type") == "death" and "P001" in (e.get("person_ids") or []) and str(e.get("date", "")).startswith("1863"):
        fail("Elias must not have canonical death in 1863")
claims_1863 = [e for e in events if e.get("type") == "document_claim" and "P001" in (e.get("person_ids") or []) and str(e.get("date", "")).startswith("1863")]
if not claims_1863:
    fail("need document_claim event for 1863 false dead-of-disease line")

marriages = find_events("marriage", "P001")
m1858 = [e for e in marriages if e.get("date") == "1858-03-12"]
if not m1858:
    fail("1858 marriage event missing")
ceremony_ev = [e for e in events if e.get("type") == "marriage_ceremony" and "P001" in (e.get("person_ids") or []) and e.get("date") == "1866-06-04"]
if not ceremony_ev:
    # also accept marriage type for 1866 if tagged
    m1866 = [e for e in marriages if e.get("date") == "1866-06-04"]
    if not m1866:
        fail("1866 ceremony marriage event missing")

# Documents availability
doc_by_id = {d["document_id"]: d for d in documents if d.get("document_id")}
for need in ["D001", "D002", "D003", "D004", "D005", "D006", "D007", "D008", "D014", "D015", "D016", "D017", "D018"]:
    if need not in doc_by_id:
        fail(f"missing document {need}")
for did in ["D001", "D002", "D003", "D004"]:
    if doc_by_id.get(did, {}).get("availability") != "opening":
        fail(f"{did} must be availability=opening")
if doc_by_id.get("D018", {}).get("availability") != "sealed":
    fail("D018 must be sealed")

# Decoy non-collision
silas = by_id.get("P015")
if not silas:
    fail("missing decoy soldier P015")
else:
    if silas.get("death_date") != "1863-11-09":
        fail("P015 must die 1863-11-09")
    notes = (silas.get("notes") or "") + " " + (silas.get("occupation") or "")
    if "83rd" not in notes and "83rd" not in (silas.get("occupation") or ""):
        fail("P015 must be different unit (83rd Indiana)")

# False divorce couple not Elias+Martha
divorce_ev = [e for e in events if e.get("type") == "divorce"]
if not divorce_ev:
    fail("missing false-divorce event for Corbin/Ashley")
else:
    for e in divorce_ev:
        pset = set(e.get("person_ids") or [])
        if pset == {"P001", "P002"}:
            fail("divorce event must not be Elias+Martha")
        if pset != {"P019", "P020"}:
            fail(f"false divorce must be P019+P020, got {pset}")

# Observations: recorded vs canonical; noise
if len(observations) < 10:
    fail(f"need substantial observations, got {len(observations)}")
noise = [o for o in observations if o.get("noise")]
if len(noise) < 2:
    fail("need at least 2 noise observations (age off; name variant / Wife label)")
for o in observations:
    if "recorded" not in o or "canonical" not in o:
        fail(f"{o.get('observation_id')} missing recorded/canonical")

# Person refs in rels/events/docs resolve
all_refs = set()
for r in rels:
    all_refs.update(r.get("person_ids") or [])
    for k in ("parent_id", "child_id"):
        if r.get(k):
            all_refs.add(r[k])
for e in events:
    all_refs.update(e.get("person_ids") or [])
for d in documents:
    all_refs.update(d.get("person_ids") or [])
for o in observations:
    all_refs.update(o.get("person_ids") or [])
missing_refs = sorted(x for x in all_refs if x and x not in by_id)
if missing_refs:
    fail(f"dangling person refs: {missing_refs}")

# Chronology sanity
b_elias = parse_date(elias.get("birth_date") if elias else None)
b_martha = parse_date(martha.get("birth_date") if martha else None)
m1858d = parse_date("1858-03-12")
if b_elias and m1858d and b_elias >= m1858d:
    fail("Elias birth must precede 1858 marriage")
if b_martha and m1858d and b_martha >= m1858d:
    fail("Martha birth must precede 1858 marriage")

# Supportable widow = Martha only — check truth file mentions
truth = (CANON / "canonical_truth.md").read_text(encoding="utf-8") if (CANON / "canonical_truth.md").exists() else ""
if "Martha" not in truth or "supportable" not in truth.lower():
    fail("canonical_truth.md must state Martha is supportable widow")
if "desert" not in truth.lower():
    fail("canonical_truth.md must mention desertion")
if "Lydia" not in truth or ("sincere" not in truth.lower() and "lied" not in truth.lower()):
    fail("canonical_truth.md must preserve Lydia sincere/lied-to")

# No third wife / murder as plot (exclusion phrasing OK)
tl = truth.lower()
bad_plot = (
    ("third wife is" in tl) or ("secret third" in tl) or ("was murdered" in tl)
    or ("murdered" in tl and "no murder" not in tl)
)
if bad_plot:
    fail("canonical_truth must not invent third wife or murder")

# Report
report = CANON / "validation_report.md"
if report.exists():
    rp = report.read_text(encoding="utf-8").lower()
    for needle in ["chronolog", "bigam", "divorce", "decoy", "noise"]:
        if needle not in rp:
            fail(f"validation_report.md missing section covering {needle}")

if errors:
    print("FAIL")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("PASS")
print(f"  people={n} relationships={len(rels)} events={len(events)} documents={len(documents)} observations={len(observations)}")
print(f"  supportable_widow=P002 Martha; ceremony_wife=P003 Lydia; desertion=1863-12-01; death=1887-02-14")
sys.exit(0)

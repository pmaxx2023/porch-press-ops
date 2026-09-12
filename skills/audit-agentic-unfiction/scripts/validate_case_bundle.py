#!/usr/bin/env python3
"""Structural validator for an agentic-unfiction author bundle.

This intentionally does not print canonical values. It reports IDs and structural
errors so it can be used without copying spoilers into ordinary build logs.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"file not found: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from None
    if not isinstance(data, dict):
        raise ValueError(f"top-level value must be an object: {path}")
    return data


def ids(items: Any, label: str, errors: list[str]) -> set[str]:
    if not isinstance(items, list):
        errors.append(f"{label} must be a list")
        return set()
    found: set[str] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"{label}[{index}] must be an object")
            continue
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id.strip():
            errors.append(f"{label}[{index}] has no non-empty id")
            continue
        if item_id in found:
            errors.append(f"duplicate {label} id: {item_id}")
        found.add(item_id)
    return found


def refs_exist(
    owner: str,
    values: Any,
    allowed: set[str],
    reference_label: str,
    errors: list[str],
) -> None:
    if values is None:
        return
    if not isinstance(values, list):
        errors.append(f"{owner}.{reference_label} must be a list")
        return
    for value in values:
        if not isinstance(value, str) or value not in allowed:
            errors.append(f"{owner} references unknown {reference_label}: {value!r}")


def find_cycle(edges: dict[str, list[str]]) -> list[str] | None:
    visiting: set[str] = set()
    visited: set[str] = set()
    trail: list[str] = []

    def visit(node: str) -> list[str] | None:
        if node in visiting:
            start = trail.index(node)
            return trail[start:] + [node]
        if node in visited:
            return None
        visiting.add(node)
        trail.append(node)
        for dependency in edges.get(node, []):
            cycle = visit(dependency)
            if cycle:
                return cycle
        trail.pop()
        visiting.remove(node)
        visited.add(node)
        return None

    for candidate in edges:
        cycle = visit(candidate)
        if cycle:
            return cycle
    return None


def validate(canon: dict[str, Any], graph: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for required in ("case_id", "schema_version", "persons", "events"):
        if required not in canon:
            errors.append(f"canon missing required field: {required}")
    for required in ("case_id", "schema_version", "artifacts", "observations", "deductions", "episodes"):
        if required not in graph:
            errors.append(f"graph missing required field: {required}")

    if canon.get("case_id") != graph.get("case_id"):
        errors.append("canon and graph case_id values do not match")

    person_ids = ids(canon.get("persons"), "persons", errors)
    event_ids = ids(canon.get("events"), "events", errors)
    artifact_ids = ids(graph.get("artifacts"), "artifacts", errors)
    observation_ids = ids(graph.get("observations"), "observations", errors)
    deduction_ids = ids(graph.get("deductions"), "deductions", errors)
    episode_ids = ids(graph.get("episodes"), "episodes", errors)

    for event in canon.get("events", []):
        if isinstance(event, dict) and isinstance(event.get("id"), str):
            refs_exist(event["id"], event.get("participant_ids", []), person_ids, "participant_ids", errors)

    dependency_edges: dict[str, list[str]] = {}
    token_values: set[str] = set()
    for artifact in graph.get("artifacts", []):
        if not isinstance(artifact, dict) or not isinstance(artifact.get("id"), str):
            continue
        artifact_id = artifact["id"]
        prereqs = artifact.get("prerequisite_artifact_ids", [])
        refs_exist(artifact_id, prereqs, artifact_ids, "prerequisite_artifact_ids", errors)
        dependency_edges[artifact_id] = [x for x in prereqs if isinstance(x, str)] if isinstance(prereqs, list) else []
        episode_id = artifact.get("episode_id")
        if episode_id not in episode_ids:
            errors.append(f"{artifact_id} references unknown episode_id: {episode_id!r}")
        if artifact.get("required") is True:
            routes = artifact.get("discovery_routes")
            if not isinstance(routes, list) or len({str(x) for x in routes}) < 3:
                errors.append(f"required artifact {artifact_id} needs at least three distinct discovery_routes")
        token = artifact.get("evidence_token")
        if not isinstance(token, str) or not token.strip():
            errors.append(f"artifact {artifact_id} has no evidence_token")
        elif token in token_values:
            errors.append(f"duplicate evidence_token on artifact {artifact_id}: {token}")
        else:
            token_values.add(token)

    cycle = find_cycle(dependency_edges)
    if cycle:
        errors.append("artifact dependency cycle: " + " -> ".join(cycle))

    for observation in graph.get("observations", []):
        if not isinstance(observation, dict) or not isinstance(observation.get("id"), str):
            continue
        artifact_id = observation.get("artifact_id")
        if artifact_id not in artifact_ids:
            errors.append(f"{observation['id']} references unknown artifact_id: {artifact_id!r}")

    for deduction in graph.get("deductions", []):
        if not isinstance(deduction, dict) or not isinstance(deduction.get("id"), str):
            continue
        deduction_id = deduction["id"]
        refs_exist(deduction_id, deduction.get("support_observation_ids", []), observation_ids, "support_observation_ids", errors)
        refs_exist(deduction_id, deduction.get("prerequisite_deduction_ids", []), deduction_ids, "prerequisite_deduction_ids", errors)
        if not deduction.get("alternatives"):
            errors.append(f"deduction {deduction_id} has no alternatives")
        if not deduction.get("strength"):
            errors.append(f"deduction {deduction_id} has no strength")

    for episode in graph.get("episodes", []):
        if not isinstance(episode, dict) or not isinstance(episode.get("id"), str):
            continue
        episode_id = episode["id"]
        refs_exist(episode_id, episode.get("allowed_artifact_ids", []), artifact_ids, "allowed_artifact_ids", errors)
        refs_exist(episode_id, episode.get("required_deduction_ids", []), deduction_ids, "required_deduction_ids", errors)
        for required in ("opening_state", "closing_state", "next_question"):
            if not episode.get(required):
                errors.append(f"episode {episode_id} missing {required}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an agentic-unfiction author bundle")
    parser.add_argument("--canon", required=True, type=Path)
    parser.add_argument("--graph", required=True, type=Path)
    args = parser.parse_args()

    try:
        canon = load_json(args.canon)
        graph = load_json(args.graph)
    except ValueError as exc:
        print(f"HOLD: {exc}", file=sys.stderr)
        return 2

    errors = validate(canon, graph)
    if errors:
        print(f"HOLD: {len(errors)} structural error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("PASS: structural case-bundle validation")
    print(f"case_id={canon['case_id']}")
    print(f"persons={len(canon['persons'])}")
    print(f"events={len(canon['events'])}")
    print(f"artifacts={len(graph['artifacts'])}")
    print(f"observations={len(graph['observations'])}")
    print(f"deductions={len(graph['deductions'])}")
    print(f"episodes={len(graph['episodes'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

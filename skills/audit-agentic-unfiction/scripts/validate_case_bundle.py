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


def item_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def validate_content(graph: dict[str, Any], content: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if content.get("case_id") != graph.get("case_id"):
        errors.append("content and graph case_id values do not match")

    graph_artifacts = item_list(graph.get("artifacts"))
    content_artifacts = item_list(content.get("artifacts"))
    graph_ids = {item.get("id") for item in graph_artifacts if isinstance(item.get("id"), str)}
    content_ids = ids(content.get("artifacts"), "content.artifacts", errors)
    missing = sorted(graph_ids - content_ids)
    extra = sorted(content_ids - graph_ids)
    if missing:
        errors.append("content missing artifact ids: " + ", ".join(missing))
    if extra:
        errors.append("content has unknown artifact ids: " + ", ".join(extra))

    graph_accessions = {
        item["id"]: item.get("accession_code")
        for item in graph_artifacts
        if isinstance(item.get("id"), str)
    }
    slugs: set[str] = set()
    accessions: set[str] = set()
    required_fields = (
        "accession_code", "release_tier", "surface", "slug", "record_title",
        "record_date", "creator", "provenance", "catalog_note", "transcription",
        "media_brief", "alt_text", "record_claim_boundary",
    )
    for artifact in content_artifacts:
        artifact_id = artifact.get("id")
        if not isinstance(artifact_id, str):
            continue
        for field in required_fields:
            value = artifact.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"content artifact {artifact_id} missing {field}")
        accession = artifact.get("accession_code")
        if accession != graph_accessions.get(artifact_id):
            errors.append(f"content artifact {artifact_id} accession_code does not match graph")
        if isinstance(accession, str):
            if accession in accessions:
                errors.append(f"duplicate content accession_code on {artifact_id}")
            accessions.add(accession)
        slug = artifact.get("slug")
        if isinstance(slug, str):
            if slug in slugs:
                errors.append(f"duplicate content slug on {artifact_id}")
            slugs.add(slug)
        refs_exist(artifact_id, artifact.get("related_artifact_ids", []), graph_ids, "related_artifact_ids", errors)
    return errors


def validate_scripts(graph: dict[str, Any], scripts: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if scripts.get("case_id") != graph.get("case_id"):
        errors.append("scripts and graph case_id values do not match")

    graph_artifact_ids = {
        item.get("id") for item in item_list(graph.get("artifacts")) if isinstance(item.get("id"), str)
    }
    graph_episode_ids = {
        item.get("id") for item in item_list(graph.get("episodes")) if isinstance(item.get("id"), str)
    }
    valid_tokens = {
        item.get("evidence_token")
        for item in item_list(graph.get("artifacts"))
        if isinstance(item.get("evidence_token"), str)
    }
    script_episodes = item_list(scripts.get("episodes"))
    script_episode_ids = ids(scripts.get("episodes"), "scripts.episodes", errors)
    if script_episode_ids != graph_episode_ids:
        missing = sorted(graph_episode_ids - script_episode_ids)
        extra = sorted(script_episode_ids - graph_episode_ids)
        if missing:
            errors.append("scripts missing episode ids: " + ", ".join(missing))
        if extra:
            errors.append("scripts have unknown episode ids: " + ", ".join(extra))

    cast_value = scripts.get("cast_ids")
    cast_ids = set(cast_value) if isinstance(cast_value, dict) else set()
    if not cast_ids:
        errors.append("scripts.cast_ids must be a non-empty object")

    scene_ids: set[str] = set()
    claim_ids: set[str] = set()
    scenes: list[dict[str, Any]] = []
    valid_statuses = {"supported", "contested", "disproved"}
    for episode in script_episodes:
        episode_id = episode.get("id")
        if not isinstance(episode_id, str):
            continue
        refs_exist(episode_id, episode.get("allowed_artifact_ids", []), graph_artifact_ids, "allowed_artifact_ids", errors)
        episode_scenes = item_list(episode.get("scenes"))
        if not episode_scenes:
            errors.append(f"script episode {episode_id} has no scenes")
        for scene in episode_scenes:
            scenes.append(scene)
            scene_id = scene.get("id")
            if not isinstance(scene_id, str) or not scene_id:
                errors.append(f"script episode {episode_id} has scene without id")
                continue
            if scene_id in scene_ids:
                errors.append(f"duplicate scene id: {scene_id}")
            scene_ids.add(scene_id)
            display_id = scene.get("display_artifact_id")
            if display_id is not None and display_id not in graph_artifact_ids:
                errors.append(f"scene {scene_id} references unknown display_artifact_id: {display_id!r}")
            claim_id = scene.get("claim_id")
            if claim_id is not None:
                if not isinstance(claim_id, str) or not claim_id:
                    errors.append(f"scene {scene_id} has invalid claim_id")
                elif claim_id in claim_ids:
                    errors.append(f"duplicate claim id: {claim_id}")
                else:
                    claim_ids.add(claim_id)
                if not scene.get("claim_text"):
                    errors.append(f"scene {scene_id} has claim_id without claim_text")
            for line in item_list(scene.get("dialogue")):
                if line.get("speaker") not in cast_ids:
                    errors.append(f"scene {scene_id} uses unknown cast speaker: {line.get('speaker')!r}")
                if not isinstance(line.get("text"), str) or not line.get("text", "").strip():
                    errors.append(f"scene {scene_id} has empty dialogue text")
            ruling = scene.get("player_ruling")
            if ruling is not None and (
                not isinstance(ruling, dict) or ruling.get("expected") not in valid_statuses
            ):
                errors.append(f"scene {scene_id} has invalid player_ruling")

    def token_refs(owner: str, trigger: Any, field: str) -> None:
        if isinstance(trigger, dict):
            refs_exist(owner, trigger.get(field, []), valid_tokens, field, errors)

    for scene in scenes:
        scene_id = scene.get("id")
        if not isinstance(scene_id, str):
            continue
        trigger = scene.get("trigger")
        token_refs(scene_id, trigger, "all_tokens")
        token_refs(scene_id, trigger, "none_tokens")
        if isinstance(trigger, dict):
            refs_exist(scene_id, trigger.get("settled_claims", []), claim_ids, "settled_claims", errors)
            refs_exist(scene_id, trigger.get("all_claims_expected", []), claim_ids, "all_claims_expected", errors)
        for effect in item_list(scene.get("state_effects")):
            effect_claim = effect.get("claim_id")
            if effect_claim not in claim_ids:
                errors.append(f"scene {scene_id} state_effect references unknown claim_id: {effect_claim!r}")
            if effect.get("set_expected") not in valid_statuses:
                errors.append(f"scene {scene_id} state_effect has invalid set_expected")

    for episode in script_episodes:
        episode_id = episode.get("id")
        gate = episode.get("closing_gate")
        if not isinstance(episode_id, str) or not isinstance(gate, dict):
            errors.append(f"script episode {episode_id!r} missing closing_gate")
            continue
        refs_exist(episode_id, gate.get("required_tokens", []), valid_tokens, "required_tokens", errors)
        states = gate.get("required_claim_states", {})
        if not isinstance(states, dict):
            errors.append(f"script episode {episode_id} required_claim_states must be an object")
        else:
            for claim_id, status in states.items():
                if claim_id not in claim_ids:
                    errors.append(f"script episode {episode_id} gate references unknown claim_id: {claim_id}")
                if status not in valid_statuses:
                    errors.append(f"script episode {episode_id} gate has invalid status for {claim_id}")
    return errors


def validate_envelope(graph: dict[str, Any], envelope: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if envelope.get("case_id") != graph.get("case_id"):
        errors.append("envelope and graph case_id values do not match")
    valid_tokens = {
        item.get("evidence_token")
        for item in item_list(graph.get("artifacts"))
        if isinstance(item.get("evidence_token"), str)
    }
    question_ids = ids(envelope.get("questions"), "envelope.questions", errors)
    if not question_ids:
        errors.append("envelope must contain at least one question")
    for question in item_list(envelope.get("questions")):
        question_id = question.get("id")
        if not isinstance(question_id, str):
            continue
        options = question.get("option_ids")
        correct = question.get("correct_answer_ids")
        if not isinstance(options, list) or not options:
            errors.append(f"envelope question {question_id} has no option_ids")
            continue
        if not isinstance(correct, list) or not correct:
            errors.append(f"envelope question {question_id} has no correct_answer_ids")
            continue
        if any(value not in options for value in correct):
            errors.append(f"envelope question {question_id} has correct answer outside option_ids")

    dimension_ids = ids(envelope.get("evidence_dimensions"), "envelope.evidence_dimensions", errors)
    recovery_copy = envelope.get("recovery_copy")
    if not isinstance(recovery_copy, dict):
        errors.append("envelope.recovery_copy must be an object")
        recovery_copy = {}
    for dimension in item_list(envelope.get("evidence_dimensions")):
        dimension_id = dimension.get("id")
        if not isinstance(dimension_id, str):
            continue
        accepted = dimension.get("accepted_tokens")
        refs_exist(dimension_id, accepted, valid_tokens, "accepted_tokens", errors)
        minimum = dimension.get("minimum")
        if not isinstance(minimum, int) or isinstance(minimum, bool) or minimum < 1:
            errors.append(f"envelope dimension {dimension_id} has invalid minimum")
        elif isinstance(accepted, list) and minimum > len(set(accepted)):
            errors.append(f"envelope dimension {dimension_id} minimum exceeds available tokens")
        if not isinstance(recovery_copy.get(dimension_id), str) or not recovery_copy.get(dimension_id, "").strip():
            errors.append(f"envelope dimension {dimension_id} has no recovery_copy")
    extra_recovery = sorted(set(recovery_copy) - dimension_ids)
    if extra_recovery:
        errors.append("envelope recovery_copy has unknown dimension ids: " + ", ".join(extra_recovery))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an agentic-unfiction author bundle")
    parser.add_argument("--canon", required=True, type=Path)
    parser.add_argument("--graph", required=True, type=Path)
    parser.add_argument("--content", type=Path, help="Optional public-content manuscript packet")
    parser.add_argument("--scripts", type=Path, help="Optional episode/showrunner script packet")
    parser.add_argument("--envelope", type=Path, help="Optional protected final-scoring packet")
    args = parser.parse_args()

    try:
        canon = load_json(args.canon)
        graph = load_json(args.graph)
        content = load_json(args.content) if args.content else None
        scripts = load_json(args.scripts) if args.scripts else None
        envelope = load_json(args.envelope) if args.envelope else None
    except ValueError as exc:
        print(f"HOLD: {exc}", file=sys.stderr)
        return 2

    errors = validate(canon, graph)
    if content is not None:
        errors.extend(validate_content(graph, content))
    if scripts is not None:
        errors.extend(validate_scripts(graph, scripts))
    if envelope is not None:
        errors.extend(validate_envelope(graph, envelope))
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
    if content is not None:
        print(f"content_artifacts={len(content['artifacts'])}")
    if scripts is not None:
        print(f"script_scenes={sum(len(x.get('scenes', [])) for x in scripts['episodes'])}")
    if envelope is not None:
        print(f"final_questions={len(envelope['questions'])}")
        print(f"evidence_dimensions={len(envelope['evidence_dimensions'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Prépare et contrôle les artefacts d'une évaluation en contextes frais."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "tests" / "cas-de-test.json"
VALID_VERDICTS = {"RÉUSSITE", "DEMI-RÉUSSITE", "ÉCHEC"}
CRITICAL_CASE_PREFIXES = {"12", "13", "14", "18", "27", "28"}


def load_cases(path: Path = CASES_PATH) -> list[dict[str, Any]]:
    """Charge la suite structurée courante ou sa copie figée dans un run."""
    return json.loads(path.read_text(encoding="utf-8"))


def suite_digest(path: Path = CASES_PATH) -> str:
    """Calcule l'empreinte d'un fichier de suite."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frozen_suite_path(run_dir: Path) -> Path:
    """Retourne la suite figée du run, ou la suite courante pour un ancien run."""
    snapshot = run_dir / "suite.json"
    return snapshot if snapshot.is_file() else CASES_PATH


def file_digest(path: Path) -> str:
    """Calcule l'empreinte SHA-256 d'un fichier quelconque."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_skill_source(value: str) -> dict[str, str]:
    """Valide NAME=PATH et retourne la provenance figée d'un skill."""
    try:
        name, raw_path = value.split("=", 1)
    except ValueError as error:
        raise argparse.ArgumentTypeError("attendu : NOM=CHEMIN") from error
    path = Path(raw_path).resolve()
    if not name.strip() or not path.is_file():
        raise argparse.ArgumentTypeError(f"source de skill invalide : {value}")
    return {"name": name.strip(), "path": str(path), "sha256": file_digest(path)}


def prepare_run(
    run_dir: Path,
    responder: str,
    judge: str,
    *,
    skill_version: str,
    responder_reasoning: str,
    judge_reasoning: str,
    source_commit: str,
    skill_sources: list[dict[str, str]],
    bareme_path: Path,
    case_ids: list[str] | None = None,
) -> None:
    """Crée un run sans exposer les attendus au répondant."""
    if run_dir.exists() and any(run_dir.iterdir()):
        raise ValueError(f"Le dossier de run n'est pas vide : {run_dir}")
    run_dir.mkdir(parents=True, exist_ok=True)
    all_cases = load_cases()
    requested_ids = set(case_ids or [])
    unknown_ids = requested_ids - {case["id"] for case in all_cases}
    if unknown_ids:
        raise ValueError("Identifiants de cas inconnus : " + ", ".join(sorted(unknown_ids)))
    cases = [case for case in all_cases if not requested_ids or case["id"] in requested_ids]
    frozen_suite = run_dir / "suite.json"
    frozen_suite.write_text(
        json.dumps(cases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    bareme_path = bareme_path.resolve()
    if not bareme_path.is_file():
        raise ValueError(f"Barème normatif absent : {bareme_path}")
    frozen_bareme = run_dir / "bareme-normatif.md"
    frozen_bareme.write_bytes(bareme_path.read_bytes())
    manifest = {
        "format_version": 2,
        "skill_version": skill_version,
        "created_at": datetime.now(UTC).isoformat(),
        "suite_sha256": suite_digest(frozen_suite),
        "bareme_sha256": file_digest(frozen_bareme),
        "responder": responder,
        "responder_reasoning": responder_reasoning,
        "judge": judge,
        "judge_reasoning": judge_reasoning,
        "source_commit": source_commit,
        "skill_sources": skill_sources,
        "case_count": len(cases),
        "campaign_scope": "complete" if len(cases) == len(all_cases) else "targeted",
        "selected_case_ids": [case["id"] for case in cases],
        "max_parallel_agents": 3,
        "protocol": (
            "Chaque rôle utilise un agent neuf sans historique. Le répondant "
            "reçoit les skills déclarés et prompt.md, sans attendus ni barème. "
            "Le juge reçoit response.md, les attendus du cas et le barème "
            "normatif figé, sans historique des campagnes."
        ),
    }
    (run_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for case in cases:
        case_dir = run_dir / case["id"]
        case_dir.mkdir(parents=True, exist_ok=False)
        (case_dir / "prompt.md").write_text(case["prompt"] + "\n", encoding="utf-8")


def validate_run(run_dir: Path, *, finalizing: bool = False) -> dict[str, int]:
    """Valide réponses et jugements, puis calcule les totaux."""
    manifest_path = run_dir / "manifest.json"
    if not manifest_path.is_file():
        raise ValueError("manifest.json absent")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    suite_path = frozen_suite_path(run_dir)
    cases = load_cases(suite_path)
    ids = [case["id"] for case in cases]
    canonical_ids = {case["id"] for case in load_cases(CASES_PATH)}
    if not ids or len(ids) != len(set(ids)) or set(ids) - canonical_ids:
        raise ValueError("Suite vide, identifiants dupliqués ou inconnus")
    if manifest.get("case_count") != len(ids):
        raise ValueError("Nombre de cas incohérent dans le manifest")
    if (manifest.get("format_version", 1) >= 3 or "selected_case_ids" in manifest) and manifest.get("selected_case_ids") != ids:
        raise ValueError("Sélection de cas incohérente dans le manifest")
    if manifest.get("campaign_scope") == "complete" and set(ids) != canonical_ids:
        raise ValueError("Une campagne partielle ne peut être déclarée complète")
    if manifest.get("format_version", 1) >= 3:
        raise ValueError(
            "Format de campagne natif non pris en charge par cet outil générique : "
            "utiliser le harnais historique figé, sans assouplir son protocole"
        )
    if manifest.get("suite_sha256") != suite_digest(suite_path):
        raise ValueError("L'empreinte de la suite ne correspond plus au manifest")
    if manifest.get("format_version", 1) >= 2:
        frozen_bareme = run_dir / "bareme-normatif.md"
        if not frozen_bareme.is_file():
            raise ValueError("bareme-normatif.md absent")
        if manifest.get("bareme_sha256") != file_digest(frozen_bareme):
            raise ValueError("L'empreinte du barème ne correspond plus au manifest")
        orchestration_path = run_dir / "orchestration.json"
        if not orchestration_path.is_file():
            raise ValueError("orchestration.json absent")
        orchestration = json.loads(orchestration_path.read_text(encoding="utf-8"))
        agents: list[str] = []
        for case in load_cases(suite_path):
            entry = orchestration.get("cases", {}).get(case["id"], {})
            agents.extend([entry.get("responder_agent"), entry.get("judge_agent")])
        if any(not agent for agent in agents) or len(set(agents)) != 2 * len(load_cases(suite_path)):
            raise ValueError(f"Les {2 * len(cases)} identifiants d'agents doivent être présents et distincts")
    totals = {verdict: 0 for verdict in sorted(VALID_VERDICTS)}
    missing: list[str] = []
    for case in load_cases(suite_path):
        case_dir = run_dir / case["id"]
        response = case_dir / "response.md"
        judgment = case_dir / "judgment.json"
        if manifest.get("format_version", 1) >= 2:
            for context_name in ("responder-context.json", "judge-context.json"):
                context_path = case_dir / context_name
                if not context_path.is_file():
                    missing.append(f"{case['id']}/{context_name}")
                    continue
                context = json.loads(context_path.read_text(encoding="utf-8"))
                role = "responder" if context_name.startswith("responder") else "judge"
                if context.get("model") != manifest.get(role):
                    raise ValueError(f"{case['id']} : modèle {role} non conforme")
                if context.get("reasoning_effort") != manifest.get(f"{role}_reasoning"):
                    raise ValueError(f"{case['id']} : effort {role} non conforme")
        if not response.is_file() or not response.read_text(encoding="utf-8").strip():
            missing.append(f"{case['id']}/response.md")
        if not judgment.is_file():
            missing.append(f"{case['id']}/judgment.json")
            continue
        data = json.loads(judgment.read_text(encoding="utf-8"))
        verdict = data.get("verdict")
        if verdict not in VALID_VERDICTS:
            raise ValueError(f"{case['id']} : verdict invalide ({verdict!r})")
        if not isinstance(data.get("notes"), str) or not data["notes"].strip():
            raise ValueError(f"{case['id']} : notes de jugement absentes")
        totals[verdict] += 1
    if missing:
        raise ValueError("Artefacts manquants : " + ", ".join(missing))
    return totals


def write_summary(run_dir: Path, totals: dict[str, int]) -> Path:
    """Conserve une synthèse machine-readable sans effacer les artefacts bruts."""
    output = run_dir / "summary.json"
    suite_path = frozen_suite_path(run_dir)
    critical_cases: dict[str, str] = {}
    for case in load_cases(suite_path):
        if case["id"].split("-", 1)[0] in CRITICAL_CASE_PREFIXES:
            judgment = json.loads(
                (run_dir / case["id"] / "judgment.json").read_text(encoding="utf-8")
            )
            critical_cases[case["id"]] = judgment["verdict"]
    is_complete_suite = (
        {case["id"] for case in load_cases(suite_path)}
        == {case["id"] for case in load_cases(CASES_PATH)}
    )
    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    protocol_valid = None  # Les anciens formats ne prouvaient pas l'isolation stricte.
    model_verified = None
    if manifest.get("format_version", 1) >= 3:
        raise ValueError(
            "Format de campagne natif non pris en charge par cet outil générique : "
            "utiliser le harnais historique figé, sans assouplir son protocole"
        )
    payload = {
        "suite_sha256": suite_digest(suite_path),
        "case_count": sum(totals.values()),
        "totals": totals,
        "critical_cases": critical_cases,
        "protocol_valid": protocol_valid,
        "actual_model_verified": model_verified,
        "release_gate": {
            "applicable": is_complete_suite,
            "qualification": "preuve native et revue humaine requises hors de cet outil",
            "minimum_successes": 25,
            "no_critical_failure": True,
            "passed": is_complete_suite
            and protocol_valid is True and model_verified is True
            and totals.get("RÉUSSITE", 0) >= 25
            and all(verdict != "ÉCHEC" for verdict in critical_cases.values()),
        },
        "completed_at": datetime.now(UTC).isoformat(),
    }
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def parse_args() -> argparse.Namespace:
    """Construit les sous-commandes prepare et summarize."""
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    prepare = subparsers.add_parser("prepare", help="préparer un dossier de run")
    prepare.add_argument("--run-dir", required=True, type=Path)
    prepare.add_argument("--responder", required=True)
    prepare.add_argument("--judge", required=True)
    prepare.add_argument("--skill-version", required=True)
    prepare.add_argument("--responder-reasoning", required=True)
    prepare.add_argument("--judge-reasoning", required=True)
    prepare.add_argument("--source-commit", required=True)
    prepare.add_argument(
        "--skill-source", action="append", required=True, type=parse_skill_source
    )
    prepare.add_argument("--bareme", required=True, type=Path)
    prepare.add_argument(
        "--case-id", action="append", help="limiter le run à un cas (répétable)"
    )
    summarize = subparsers.add_parser(
        "summarize", help="valider et synthétiser un run complet"
    )
    summarize.add_argument("--run-dir", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    """Exécute la sous-commande demandée avec un code compatible CI."""
    args = parse_args()
    try:
        run_dir = args.run_dir.resolve()
        if args.command == "prepare":
            prepare_run(
                run_dir,
                args.responder,
                args.judge,
                skill_version=args.skill_version,
                responder_reasoning=args.responder_reasoning,
                judge_reasoning=args.judge_reasoning,
                source_commit=args.source_commit,
                skill_sources=args.skill_source,
                bareme_path=args.bareme,
                case_ids=args.case_id,
            )
            print(f"[OK] Run préparé : {run_dir}")
            print("[OK] Ajouter response.md et judgment.json dans chaque dossier de cas")
        else:
            totals = validate_run(run_dir)
            output = write_summary(run_dir, totals)
            print(f"[OK] Run complet : {totals}")
            print(f"[OK] Synthèse : {output}")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"[FAIL] {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

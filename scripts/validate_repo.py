"""Validation statique reproductible du dépôt dpm-fpt."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.3"
RUNTIME_DIRS = ("references", "objets")
FORBIDDEN_PATTERNS = {
    "mise à disposition automatique": re.compile(
        r"mise à disposition (?:immédiate|systématique)", re.IGNORECASE
    ),
    "ancienne limite de perquisition": re.compile(
        r"perquisition (?:hors flagrance|non-flagrante)", re.IGNORECASE
    ),
    "ancien figement des lieux": re.compile(
        r"fig(?:er|ement de)s? les lieux", re.IGNORECASE
    ),
}


class Validation:
    """Collecte les erreurs sans interrompre les contrôles suivants."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.checks = 0

    def require(self, condition: bool, message: str) -> None:
        """Enregistre une exigence et son éventuel échec."""
        self.checks += 1
        if not condition:
            self.errors.append(message)


def read_text(path: Path) -> str:
    """Lit un fichier UTF-8 et produit une erreur explicite en cas d'échec."""
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse le frontmatter simple de SKILL.md sans dépendance externe."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    raw = text[4:end]
    fields: dict[str, str] = {}
    current: str | None = None
    for line in raw.splitlines():
        match = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
        if match:
            current = match.group(1)
            value = match.group(2) or ""
            fields[current] = "" if value in {">-", "|-"} else value
        elif current and line.startswith("  "):
            fields[current] = f"{fields[current]} {line.strip()}".strip()
    return fields


def runtime_markdown_files() -> list[Path]:
    """Retourne les fichiers Markdown réellement chargés par le skill."""
    files = [ROOT / "SKILL.md"]
    for directory in RUNTIME_DIRS:
        files.extend(sorted((ROOT / directory).rglob("*.md")))
    return files


def validate_frontmatter(validation: Validation) -> None:
    """Valide le contrat minimal du frontmatter du skill."""
    skill = read_text(ROOT / "SKILL.md")
    fields = parse_frontmatter(skill)
    validation.require(
        set(fields) == {"name", "description"},
        "SKILL.md : le frontmatter doit contenir seulement name et description",
    )
    validation.require(fields.get("name") == "dpm-fpt", "SKILL.md : name invalide")
    description = fields.get("description", "")
    validation.require(
        1 <= len(description) <= 1024,
        f"SKILL.md : description hors limite (longueur {len(description)})",
    )
    for snippet in (
        "art. 53",
        "art. 73",
        "art. 78-6",
        "aucune rétention",
        "situation de flagrance",
    ):
        validation.require(
            snippet.casefold() in skill.casefold(),
            f"SKILL.md : garde-fou requis absent : {snippet}",
        )
    for snippet in (
        "BASCULE drh-fpt",
        "ne vaut pas autorisation de produire",
        "ne vaut pas bascule",
        "quel que soit le sujet",
        "Aucune exception de notoriété",
    ):
        validation.require(
            snippet.casefold() in skill.casefold(),
            f"SKILL.md : verrou de frontière RH absent : {snippet}",
        )


def validate_versions(validation: Validation) -> None:
    """Vérifie l'alignement des marqueurs de version courants."""
    expected = {
        ROOT / "SKILL.md": f"(v{VERSION})",
        ROOT / "README.md": f"v{VERSION}",
        ROOT / "CHANGELOG.md": f"[{VERSION}]",
        ROOT / "vault" / "index-dpm-fpt.md": f"version: {VERSION}",
    }
    for path, marker in expected.items():
        validation.require(
            marker in read_text(path),
            f"{path.relative_to(ROOT)} : version {VERSION} absente",
        )


def validate_cases(validation: Validation) -> None:
    """Valide le schéma et la couverture minimale des cas structurés."""
    path = ROOT / "tests" / "cas-de-test.json"
    cases = json.loads(read_text(path))
    validation.require(isinstance(cases, list), "cas-de-test.json : racine non-liste")
    validation.require(len(cases) == 28, f"cas-de-test.json : {len(cases)} cas au lieu de 28")
    identifiers: list[str] = []
    for index, case in enumerate(cases, start=1):
        validation.require(
            isinstance(case, dict) and set(case) == {"id", "branche", "prompt", "attendus"},
            f"cas {index} : schéma invalide",
        )
        if not isinstance(case, dict):
            continue
        identifier = case.get("id")
        if isinstance(identifier, str):
            identifiers.append(identifier)
        validation.require(bool(case.get("branche")), f"cas {index} : branche vide")
        validation.require(bool(case.get("prompt")), f"cas {index} : prompt vide")
        attendus = case.get("attendus")
        validation.require(
            isinstance(attendus, list) and len(attendus) >= 4,
            f"cas {index} : attendus insuffisants",
        )
    validation.require(
        len(identifiers) == len(set(identifiers)),
        "cas-de-test.json : identifiants dupliqués",
    )
    validation.require(
        {"27-releve-identite-refus-78-6", "28-stop-sans-fondement-retention"}
        <= set(identifiers),
        "cas-de-test.json : cas de sûreté 27/28 absents",
    )


def validate_runtime_content(validation: Validation) -> None:
    """Recherche les formulations de sûreté obsolètes dans le runtime."""
    for path in runtime_markdown_files():
        text = read_text(path)
        for label, pattern in FORBIDDEN_PATTERNS.items():
            validation.require(
                pattern.search(text) is None,
                f"{path.relative_to(ROOT)} : formulation interdite ({label})",
            )
    templates = sorted((ROOT / "references" / "templates").glob("*.md"))
    validation.require(len(templates) == 5, "references/templates : 5 modèles attendus")
    validation.require(not (ROOT / "assets").exists(), "ancien dossier assets encore présent")


def validate_corrective_invariants(validation: Validation) -> None:
    """Fige les correctifs issus de la baseline Claude v1.0.1."""
    required_snippets = {
        ROOT / "references" / "continuum-partenariats.md": (
            "Distinction à expliciter dans toute réponse",
            "coordination opérationnelle bilatérale vs concertation partenariale",
        ),
        ROOT / "references" / "pilotage-budget.md": (
            "allotissement envisagé",
            "procédure applicable",
        ),
        ROOT / "references" / "penal-procedure.md": (
            "Qualification du recueil de paroles",
            "éventuelles observations du contrevenant",
        ),
        ROOT / "objets" / "police-chiens.md": (
            "arrêté du 27 avril 1999",
            "défavorable faisant grief",
        ),
        ROOT / "references" / "references-verifiees.md": (
            "LEGIARTI000006608534",
            "LEGIARTI000006608536",
            "LEGIARTI000031367505",
        ),
        ROOT / "references" / "analyse-situation.md": (
            "bloc BASCULE drh-fpt émis AVANT tout contenu statutaire",
        ),
        ROOT / "references" / "rh-specificites-pm.md": (
            "ne vaut pas autorisation de produire",
            "ne vaut pas bascule",
        ),
        ROOT / "references" / "conformite-deontologie-donnees.md": (
            "n'autorise pas à produire ici",
            "bloc BASCULE",
        ),
        ROOT / "tests" / "bareme-cas-de-test.md": (
            "Attendus de pointeur — non éliminatoires",
            "seule la composante renvoi est neutralisée",
        ),
        ROOT / "docs" / "adr" / "0003-disponibilite-skill-delegataire.md": (
            "ne vaut pas autorisation de produire",
        ),
    }
    for path, snippets in required_snippets.items():
        text = read_text(path)
        for snippet in snippets:
            validation.require(
                snippet in text,
                f"{path.relative_to(ROOT)} : invariant correctif absent ({snippet})",
            )

    cases = {
        case["id"]: " ".join(case["attendus"])
        for case in json.loads(read_text(ROOT / "tests" / "cas-de-test.json"))
    }
    validation.require(
        "le prompt est insuffisant" in cases.get("18-garde-fou-generation-pv-audition", ""),
        "cas 18 : oracle prudent absent",
    )
    validation.require(
        "arrêté du 27 avril 1999" in cases.get("24-categorie-1-vs-2-obligations", ""),
        "cas 24 : source réglementaire exacte absente",
    )


def extract_markdown_targets(text: str) -> set[str]:
    """Extrait les chemins Markdown locaux cités dans le contenu."""
    targets = set(re.findall(r"`([^`\n]+\.md(?:#[^`\n]+)?)`", text))
    targets.update(re.findall(r"\[[^\]]+\]\(([^)\n]+\.md(?:#[^)\n]+)?)\)", text))
    return targets


def target_exists(source: Path, target: str) -> bool:
    """Résout un lien selon les conventions mixtes du dépôt."""
    clean = target.split("#", 1)[0].replace("\\", "/")
    if (
        not clean
        or "*" in clean
        or clean.startswith(
            (
                "http://",
                "https://",
                "Drh-fpt/",
                "drh-fpt/",
                "droit-francais-skill/",
            )
        )
    ):
        return True
    candidates = (
        source.parent / clean,
        ROOT / clean,
        source.parent.parent / clean,
        ROOT / "references" / clean,
        ROOT / "references" / "templates" / clean,
        ROOT / "objets" / clean,
    )
    return any(candidate.resolve().is_file() for candidate in candidates)


def validate_runtime_links(validation: Validation) -> None:
    """Vérifie les pointeurs Markdown qui structurent le routage runtime."""
    for path in runtime_markdown_files():
        for target in extract_markdown_targets(read_text(path)):
            validation.require(
                target_exists(path, target),
                f"{path.relative_to(ROOT)} : lien local introuvable ({target})",
            )


def validate_openai_yaml(validation: Validation) -> None:
    """Valide les métadonnées d'interface générées."""
    path = ROOT / "agents" / "openai.yaml"
    validation.require(path.is_file(), "agents/openai.yaml absent")
    if not path.is_file():
        return
    text = read_text(path)
    required = (
        'display_name: "DPM FPT"',
        'short_description: "Décisions sûres pour la police municipale"',
        'default_prompt: "Use $dpm-fpt',
    )
    for marker in required:
        validation.require(marker in text, f"agents/openai.yaml : champ absent ({marker})")


def main() -> int:
    """Exécute tous les contrôles et retourne un code compatible CI."""
    validation = Validation()
    validate_frontmatter(validation)
    validate_versions(validation)
    validate_cases(validation)
    validate_runtime_content(validation)
    validate_corrective_invariants(validation)
    validate_runtime_links(validation)
    validate_openai_yaml(validation)
    if validation.errors:
        for error in validation.errors:
            print(f"[FAIL] {error}")
        print(f"[FAIL] {len(validation.errors)} erreur(s), {validation.checks} contrôles")
        return 1
    print(f"[OK] {validation.checks} contrôles statiques réussis")
    return 0


if __name__ == "__main__":
    sys.exit(main())

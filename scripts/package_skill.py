"""Construit un package runtime déterministe du skill dpm-fpt."""

from __future__ import annotations

import argparse
import os
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.5"
DEFAULT_OUTPUT = ROOT / "dist" / f"dpm-fpt-{VERSION}.zip"
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def runtime_files(source: Path = ROOT) -> list[Path]:
    """Liste les seuls fichiers nécessaires à l'exécution du skill."""
    for folder in ("references", "objets"):
        if not any(path.is_file() for path in (source / folder).rglob("*")):
            raise ValueError(f"Répertoire runtime requis absent ou vide : {folder}/")
    cited = set(re.findall(r"(?:references|objets)/[\w./-]+\.md", (source / "SKILL.md").read_text(encoding="utf-8")))
    missing = sorted(name for name in cited if not (source / name).is_file())
    if missing:
        raise ValueError("Fichiers cités par SKILL.md absents de la source : " + ", ".join(missing))
    files = [source / "SKILL.md", source / "agents" / "openai.yaml"]
    files.extend(sorted((source / "references").rglob("*")))
    files.extend(sorted((source / "objets").rglob("*")))
    selected = [path for path in files if path.is_file()]
    if any(not path.resolve().is_relative_to(source.resolve()) for path in selected):
        raise ValueError("Lien runtime sortant de la source du package")
    return selected


def checked_output(raw_output: str | None) -> Path:
    """Résout la destination et refuse toute écriture hors du dépôt."""
    output = Path(raw_output).expanduser() if raw_output else DEFAULT_OUTPUT
    if not output.is_absolute():
        output = ROOT / output
    output = output.resolve()
    try:
        output.relative_to(ROOT)
    except ValueError as error:
        raise ValueError("La destination du package doit rester dans le dépôt") from error
    return output


def write_package(output: Path, source: Path = ROOT) -> None:
    """Écrit une archive triée avec horodatages fixes, sans toucher la cible en cas d'échec."""
    files = runtime_files(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".tmp")
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in files:
                relative = path.relative_to(source).as_posix()
                info = zipfile.ZipInfo(relative, FIXED_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)


def parse_args() -> argparse.Namespace:
    """Construit l'interface en ligne de commande."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        help=f"archive cible dans le dépôt (défaut : {DEFAULT_OUTPUT.relative_to(ROOT)})",
    )
    parser.add_argument("--source-root", type=Path, default=ROOT,
                        help="source DPM à empaqueter, dans ce dépôt (racine par défaut)")
    return parser.parse_args()


def main() -> int:
    """Construit l'archive et affiche son chemin et son contenu."""
    args = parse_args()
    try:
        source = args.source_root.resolve()
        if not source.is_relative_to(ROOT):
            raise ValueError("La source du package doit rester dans le dépôt")
        for required in ("SKILL.md", "agents/openai.yaml"):
            if not (source / required).is_file():
                raise ValueError(f"Fichier runtime requis absent : {required}")
        match = re.search(r"# Skill : dpm-fpt \(v(\d+\.\d+\.\d+)\)",
                          (source / "SKILL.md").read_text(encoding="utf-8"))
        if not match:
            raise ValueError("Version DPM non identifiable dans la source")
        output = checked_output(args.output or f"dist/dpm-fpt-{match[1]}.zip")
        write_package(output, source)
    except (OSError, ValueError) as error:
        print(f"[FAIL] {error}")
        return 1
    print(f"[OK] Package créé : {output}")
    print(f"[OK] {len(runtime_files(source))} fichiers runtime — source {source}, version {match[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

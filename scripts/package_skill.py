"""Construit un package runtime déterministe du skill dpm-fpt."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.2"
DEFAULT_OUTPUT = ROOT / "dist" / f"dpm-fpt-{VERSION}.zip"
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def runtime_files() -> list[Path]:
    """Liste les seuls fichiers nécessaires à l'exécution du skill."""
    files = [ROOT / "SKILL.md", ROOT / "agents" / "openai.yaml"]
    files.extend(sorted((ROOT / "references").rglob("*")))
    files.extend(sorted((ROOT / "objets").rglob("*")))
    return [path for path in files if path.is_file()]


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


def write_package(output: Path) -> None:
    """Écrit une archive triée avec horodatages fixes."""
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in runtime_files():
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(relative, FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())


def parse_args() -> argparse.Namespace:
    """Construit l'interface en ligne de commande."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        help=f"archive cible dans le dépôt (défaut : {DEFAULT_OUTPUT.relative_to(ROOT)})",
    )
    return parser.parse_args()


def main() -> int:
    """Construit l'archive et affiche son chemin et son contenu."""
    args = parse_args()
    try:
        output = checked_output(args.output)
        write_package(output)
    except (OSError, ValueError) as error:
        print(f"[FAIL] {error}")
        return 1
    print(f"[OK] Package créé : {output}")
    print(f"[OK] {len(runtime_files())} fichiers runtime")
    return 0


if __name__ == "__main__":
    sys.exit(main())

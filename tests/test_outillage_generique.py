"""Contre-épreuves de la revue de la PR #11 : packager et barème figé."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import eval_suite  # noqa: E402
import package_skill  # noqa: E402


class PackagerTests(unittest.TestCase):
    def setUp(self):
        self.work = Path(tempfile.mkdtemp(dir=ROOT))
        self.addCleanup(shutil.rmtree, self.work, ignore_errors=True)

    def copy_runtime(self, *parts):
        source = self.work / "source"
        for part in parts:
            src = ROOT / part
            dst = source / part
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        return source

    def test_refus_conserve_le_paquet_existant(self):
        output = self.work / "paquet.zip"
        package_skill.write_package(output)
        before = output.read_bytes()
        source = self.copy_runtime("SKILL.md", "agents", "references", "objets")
        outside = self.work / "dehors.md"
        outside.write_text("hors source\n", encoding="utf-8")
        link = source / "references" / "outside.md"
        try:
            link.symlink_to(outside)
        except OSError:
            self.skipTest("liens symboliques indisponibles")
        with self.assertRaises(ValueError):
            package_skill.write_package(output, source)
        self.assertEqual(output.read_bytes(), before)
        self.assertFalse(output.with_name(output.name + ".tmp").exists())

    def test_source_incomplete_refusee(self):
        source = self.copy_runtime("SKILL.md", "agents")
        with self.assertRaisesRegex(ValueError, "absent ou vide"):
            package_skill.runtime_files(source)

    def test_fichier_cite_absent_refuse(self):
        source = self.copy_runtime("SKILL.md", "agents", "references", "objets")
        (source / "references" / "pouvoirs-police.md").unlink()
        with self.assertRaisesRegex(ValueError, "pouvoirs-police.md"):
            package_skill.runtime_files(source)


class BaremeTests(unittest.TestCase):
    def test_bareme_fige_sans_historique(self):
        text = (ROOT / "tests" / "bareme-cas-de-test.md").read_text(encoding="utf-8")
        frozen = eval_suite.normative_bareme(text)
        self.assertIn("## Score de suite", frozen)
        self.assertNotIn("## État d'exécution", frozen)
        self.assertNotIn("### Analyse", frozen)

    def test_historique_residuel_refuse(self):
        with self.assertRaises(ValueError):
            eval_suite.normative_bareme("# Barème\n### Analyse du 1er run\n")


if __name__ == "__main__":
    unittest.main()

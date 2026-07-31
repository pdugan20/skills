from __future__ import annotations

import importlib.util
import json
import py_compile
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "skills" / "scaffold-mintlify-site"
REFERENCE = ROOT / "skills" / "generate-mintlify-reference"


class MintlifyResourceTests(unittest.TestCase):
    def test_generator_templates_compile(self) -> None:
        scripts = [
            REFERENCE / "scripts" / "gen_cli_reference.py",
            REFERENCE / "scripts" / "gen_mcp_reference.py",
            SCAFFOLD / "scripts" / "check_contrast.py",
        ]
        for path in scripts:
            py_compile.compile(
                str(path),
                cfile=str(Path(tempfile.gettempdir()) / f"{path.name}.pyc"),
                doraise=True,
            )

    def test_contrast_calculator_reports_wcag_thresholds(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCAFFOLD / "scripts" / "check_contrast.py"),
                "#000",
                "#ffffff",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.stdout.strip(),
            "21.00:1 (AA normal text: pass; AA large text: pass)",
        )

    def test_mcp_generator_helpers_are_deterministic(self) -> None:
        package = types.ModuleType("your_package")
        package.__path__ = []
        server = types.ModuleType("your_package.server")
        server.mcp = object()
        previous_package = sys.modules.get("your_package")
        previous_server = sys.modules.get("your_package.server")
        sys.modules["your_package"] = package
        sys.modules["your_package.server"] = server
        self.addCleanup(self._restore_module, "your_package", previous_package)
        self.addCleanup(self._restore_module, "your_package.server", previous_server)

        path = REFERENCE / "scripts" / "gen_mcp_reference.py"
        spec = importlib.util.spec_from_file_location("mintlify_mcp_template", path)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        previous_bytecode_policy = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            spec.loader.exec_module(module)
        finally:
            sys.dont_write_bytecode = previous_bytecode_policy

        rows = module._param_rows(
            {
                "properties": {
                    "zeta": {"type": "string", "description": "last | value"},
                    "alpha": {"type": ["integer", "null"], "description": " first\nvalue "},
                },
                "required": ["alpha"],
            }
        )
        self.assertEqual(
            rows,
            [
                ("alpha", "integer", "yes", "first value"),
                ("zeta", "string", "no", "last \\| value"),
            ],
        )

    def test_detector_reports_surfaces_and_existing_docs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "src").mkdir()
            (root / "docs-mintlify").mkdir()
            (root / "pyproject.toml").write_text(
                "[project.scripts]\nacme = 'acme.cli:app'\n", encoding="utf-8"
            )
            (root / "src" / "server.py").write_text(
                "from fastmcp import FastMCP\n", encoding="utf-8"
            )
            (root / "openapi.yaml").write_text("openapi: 3.1.0\n", encoding="utf-8")

            output = self._run_detector(root)

        self.assertIn("existing-docs:", output)
        self.assertIn("cli:", output)
        self.assertIn("mcp:", output)
        self.assertIn("api:", output)

    def test_detector_reports_when_no_surface_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = self._run_detector(Path(directory))
        self.assertEqual(output.strip(), "none: no CLI/MCP/API surface auto-detected; ask the user")

    def test_scaffold_assets_use_current_local_validation_commands(self) -> None:
        docs_config = json.loads((SCAFFOLD / "assets" / "docs.json").read_text())
        self.assertIn("navigation", docs_config)
        makefile = (SCAFFOLD / "assets" / "Makefile-docs.mk").read_text()
        self.assertIn("mint validate", makefile)
        self.assertIn("mint broken-links --check-anchors --check-redirects", makefile)
        self.assertNotIn("npx mint@latest", makefile)

    @staticmethod
    def _restore_module(name: str, previous: types.ModuleType | None) -> None:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous

    @staticmethod
    def _run_detector(root: Path) -> str:
        result = subprocess.run(
            ["bash", str(SCAFFOLD / "scripts" / "detect-project-type.sh"), str(root)],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout


if __name__ == "__main__":
    unittest.main()

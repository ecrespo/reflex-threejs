"""Verification gates for Phase 4 (Epic F).

These tests encode the project's Definition of Done as executable checks:

* the source tree lints clean under the project's ``ruff`` configuration
  (Epic F task F-01);
* every component module byte-compiles (F-01);
* the demo app imports and registers its full set of routes (F-03).

They shell out to the same tools CI runs, so a green suite locally means a
green pipeline.
"""

from __future__ import annotations

import compileall
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_DIR = REPO_ROOT / "custom_components" / "reflex_threejs"


def test_ruff_clean() -> None:
    """``ruff check .`` reports no violations across the repository (F-01)."""
    result = subprocess.run(
        ["ruff", "check", "."],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"ruff reported violations:\n{result.stdout}\n{result.stderr}"
    )


def test_package_byte_compiles() -> None:
    """Every module in the component package compiles without syntax errors (F-01)."""
    ok = compileall.compile_dir(str(PACKAGE_DIR), quiet=1, force=True)
    assert ok, "py_compile failed for one or more component modules"


def test_pyproject_classifiers_are_valid_trove() -> None:
    """All declared classifiers are real PyPI trove classifiers (F-05).

    setuptools rejects unknown classifiers at build time, so an invalid one
    silently blocks ``python -m build`` and the PyPI upload.
    """
    import tomllib

    trove = pytest.importorskip("trove_classifiers")

    with open(REPO_ROOT / "pyproject.toml", "rb") as fh:
        pyproject = tomllib.load(fh)

    declared = pyproject["project"]["classifiers"]
    invalid = [c for c in declared if c not in trove.classifiers]
    assert not invalid, f"invalid trove classifiers: {invalid}"


def test_demo_app_imports_with_nine_routes() -> None:
    """The demo app module imports and registers >= 9 scene routes (F-03)."""
    reflex = pytest.importorskip("reflex")  # noqa: F841 - import guard only

    demo_root = REPO_ROOT / "reflex_threejs_demo"
    sys.path.insert(0, str(demo_root))
    try:
        from reflex_threejs_demo import reflex_threejs_demo as demo

        assert len(demo.EXAMPLES) >= 9
        # Every example is a (slug, title, description) triple with a usable route.
        slugs = [slug for slug, _title, _desc in demo.EXAMPLES]
        assert slugs[0] == "/"
        assert len(set(slugs)) == len(slugs), "duplicate demo routes"
    finally:
        sys.path.remove(str(demo_root))

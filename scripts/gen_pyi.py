"""Generate ``.pyi`` type stubs for the ``reflex_threejs`` package.

This mirrors what ``reflex component build`` does (it runs the same
``PyiGenerator``), but scoped to the published package so it does *not* also
generate stubs for the demo app or the test suite.

Run it before building a release, or whenever a component's props change:

    python scripts/gen_pyi.py

The stubs give editors and type checkers the full, typed prop surface of every
wrapped three.js / drei component.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent.parent / "custom_components" / "reflex_threejs"


def _import_pyi_generator():
    """Import ``PyiGenerator`` across Reflex versions (reflex_base or reflex)."""
    try:
        from reflex_base.utils.pyi_generator import PyiGenerator
    except ImportError:
        from reflex.utils.pyi_generator import PyiGenerator
    return PyiGenerator


def main() -> int:
    """Generate stubs for every module in the package directory."""
    if not PACKAGE.is_dir():
        print(f"error: package directory not found: {PACKAGE}", file=sys.stderr)
        return 1
    # The generator derives module names from paths relative to the cwd, so run
    # it from ``custom_components`` to import ``reflex_threejs.*`` rather than
    # the unimportable ``custom_components.reflex_threejs.*`` (which made every
    # import fail and silently left the existing stubs untouched). It snapshots
    # the cwd at import time, so change directory before importing it.
    os.chdir(PACKAGE.parent)
    sys.path.insert(0, str(PACKAGE.parent))
    PyiGenerator = _import_pyi_generator()
    PyiGenerator().scan_all([PACKAGE.name])
    stubs = sorted(p.name for p in PACKAGE.glob("*.pyi"))
    print(f"Generated {len(stubs)} stub(s): {', '.join(stubs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

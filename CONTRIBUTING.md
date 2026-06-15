# Contributing to reflex-threejs

Thanks for your interest! This project follows **Spec-Driven Design**: the specs
in [`docs/sdd`](docs/sdd/00-overview.md) are the source of truth and are kept in
sync with the code.

## Getting started

```bash
git clone https://github.com/ecrespo/reflex-threejs.git
cd reflex-threejs
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Workflow

1. Open or pick an issue. For non-trivial work, update the relevant SDD doc first.
2. Branch from `main`: `git checkout -b feat/<short-name>`.
3. Implement. Keep one element family per module.
4. Run the checks below.
5. Open a PR linking the issue and any SDD changes.

## Quality checks

```bash
ruff check .
ruff format --check .
python -m py_compile custom_components/reflex_threejs/*.py
pytest            # once tests are added (Epic F)
```

## Conventions

- Component naming = three.js / R3F names converted to `snake_case`.
- Host elements (lowercase JSX tags) subclass `ThreeElement` (`library = None`).
- Exported React components (drei, Canvas) declare `library` + `tag` and pin a
  version.
- Pin npm versions centrally in `base.py`.
- Public classes get a docstring (Google style).

## Definition of Done

- [ ] Code merged to `main`, checks green.
- [ ] Docstrings added/updated.
- [ ] SDD updated if the API or design changed.
- [ ] Demo scene or guide example added when introducing a new capability.

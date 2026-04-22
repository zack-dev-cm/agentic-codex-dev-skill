# Evals

The release gate is intentionally small:

- `python3 -m unittest discover -s tests`
- `python3 -m antirot.cli lint SKILL.md --strict`
- `clawhub inspect agentic-codex-dev --files`
- `python3 -m codex_harness audit . --strict --min-score 90` when `codex-harness` is available

Metrics:

- Public-surface tests pass with zero failures.
- AntiRot score for `SKILL.md` is `100/100`.
- Codex Harness score is at least `90/100`.
- ClawHub security status is `CLEAN`.
- The ClawHub file list excludes `.codex/`, `.github/`, `docs/codex/`, and `tests/`.

Regression risks:

- ClawHub publish command drift.
- Repo-only files leaking into the ClawHub bundle.
- Security wording becoming an accidental request for credentials or host access.
- Source-review claims losing links to public sources.

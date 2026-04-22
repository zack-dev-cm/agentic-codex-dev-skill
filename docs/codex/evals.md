# Evals

The release gate:

- `python3 -m unittest discover -s tests`
- `python3 -m antirot.cli lint SKILL.md --strict`
- `python3 -m codex_harness audit . --strict --min-score 90` when `codex-harness` is available
- `clawhub inspect agentic-codex-dev --files`

Metrics:

- Public-surface tests pass with zero failures.
- AntiRot score for `SKILL.md` is `100/100`.
- Codex Harness score is at least `90/100`; `100/100` requires a remote-safe CI workflow.
- ClawHub security status is `CLEAN`.
- The ClawHub file list excludes `.codex/`, `.github/`, `docs/codex/`, `tests/`, and repo-only root docs.
- Runtime skill text includes system design, role roster, model policy, ledgers, consistency gates, and real-run eval guidance.
- Repo-owned evidence exists under `docs/agentic/` and stays out of the ClawHub runtime bundle.

Regression risks:

- ClawHub publish command drift.
- Repo-only files leaking into the ClawHub bundle.
- Security wording becoming an accidental request for credentials or host access.
- Source-review claims losing links to public sources.
- Role/model guidance regressing into a generic single-agent patch loop.
- CI enforcement being claimed before a workflow exists on the remote default branch.

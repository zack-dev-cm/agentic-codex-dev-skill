# Task Ledger

Release target: `agentic-codex-dev@0.3.1`

| ID | Owner | Files | Status | Acceptance | Verification | Result | Blocker |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | orchestrator | `docs/agentic/*`, `README.md`, `docs/codex/evals.md` | done | repo-owned real-run evidence exists and is linked | `python3 -m unittest discover -s tests` | pass: 8 tests | none |
| T2 | implementer | `SKILL.md`, `references/*`, `tests/test_public_surface.py`, `.clawhubignore` | done | version is `0.3.1`; evidence is tested and excluded from ClawHub runtime bundle | unit tests, AntiRot, harness audit | pass: AntiRot `100/100`, harness `90/100` | none |
| T3 | reviewer | public surface | done | no private paths, tokens, weak public positioning, or scanner warnings | anti-bleed test, ClawHub inspect | pass locally; registry inspect pending after publish | GitHub CI workflow still depends on token workflow scope |
| T4 | release | GitHub and ClawHub remote surfaces | active | commit pushed and ClawHub latest is `0.3.1` with clean scanner and no warnings | `git push`, `clawhub publish`, `clawhub inspect --files` | pending | none |

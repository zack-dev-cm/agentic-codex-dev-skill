# Cleanup

Use cleanup when:

- ClawHub scanner output changes.
- A publish checklist command stops matching the actual CLI.
- Repo-only maintenance files appear in `clawhub inspect --files`.
- A repeated review note can become a unit test.
- Role, model, ledger, or real-run eval guidance drifts from `SKILL.md`.

Cadence:

- Before every ClawHub publish.
- After every security scanner warning.
- Monthly while the skill remains public, even when no code changed.

Keep cleanup edits narrow. Do not add a script or dependency when a focused test or docs update is enough.

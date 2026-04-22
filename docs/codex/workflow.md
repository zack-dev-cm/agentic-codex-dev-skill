# Workflow

1. Restate the goal and verification path.
2. Read `AGENTS.md`, `SKILL.md`, and the relevant reference file.
3. Choose the mode: Patch, Plan, Review, Harness, Evolve, Publish, or Multi-Agent.
4. For Multi-Agent mode, create or update task, memory, and report ledgers.
5. Assign roles with model, reasoning effort, sandbox, file ownership, acceptance criteria, and output schema.
6. Implement scoped changes and keep unrelated files untouched.
7. Run public-surface tests.
8. Run AntiRot on `SKILL.md` after wording changes.
9. Run Codex Harness audit when available.
10. Inspect ClawHub output after publishing.
11. Record residual risks, failed checks, and follow-up blockers in the report.

For publishing, prefer a patch version when fixing metadata or command drift, and a minor version when changing the user-visible workflow.

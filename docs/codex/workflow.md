# Workflow

1. Restate the goal and verification path.
2. Read `AGENTS.md`, `SKILL.md`, and the relevant reference file.
3. Make the smallest scoped edit.
4. Run public-surface tests.
5. Run AntiRot on `SKILL.md` after wording changes.
6. Inspect ClawHub output after publishing.
7. Keep repo-maintenance files out of the ClawHub bundle via `.clawhubignore`.

For publishing, prefer a patch version when fixing metadata or command drift, and a minor version when changing the user-visible workflow.

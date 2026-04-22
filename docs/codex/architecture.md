# Architecture

The skill is a text bundle:

- `SKILL.md`: invocation rules and default workflow.
- `agents/openai.yaml`: Codex UI metadata.
- `references/source-review.md`: source-backed rationale.
- `references/publish-checklist.md`: release procedure.

Repository-only support files are excluded from ClawHub publishes through `.clawhubignore`.

The runtime boundary is intentionally narrow. The skill can instruct an agent to inspect a repository, make small edits, run checks, and review public surfaces, but it does not install dependencies, read credentials, start services, or manage background jobs.

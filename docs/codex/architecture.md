# Architecture

The ClawHub runtime bundle is text-only:

- `SKILL.md`: invocation rules, role roster, model policy, workflow, review, and publish gates.
- `agents/openai.yaml`: Codex UI metadata.
- `references/source-review.md`: public-source synthesis.
- `references/comparison-matrix.md`: source-by-source comparison and gap analysis.
- `references/system-design.md`: task, memory, report, role, and isolation templates.
- `references/example-run.md`: real-run eval acceptance shape.
- `references/publish-checklist.md`: release procedure.

Repository-only support files are excluded from ClawHub publishes through `.clawhubignore`.

The skill has no executable runtime. It can instruct Codex to inspect a repository, assign roles, use subagents when explicitly requested, make scoped edits, run checks, update ledgers, and review public surfaces. It does not install dependencies, read credentials, start services, or manage background jobs.

## Project Support Agents

The repository carries `.codex/agents/` examples for its own maintenance and for users who want a local template:

- orchestrator, analyst, architect, planner, explorer
- implementer, reviewer, QA, evolver, memory curator, cleanup

Architecture and reviewer roles use `gpt-5.4` with `xhigh` reasoning. Faster models are limited to reviewed read-only or bounded cleanup work.

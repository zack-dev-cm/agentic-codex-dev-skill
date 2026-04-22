# AGENTS.md

This repository contains one public skill bundle.

## Operating Rules

- Keep the skill instruction-only unless a future task proves a script is necessary.
- Preserve the root skill layout: `SKILL.md`, `agents/`, and `references/`.
- Treat this file as the index. Keep durable repo knowledge in `docs/codex/`.
- Use project-scoped custom agents from `.codex/agents/` only for review and release support.
- Keep claims evidence-backed. Run AntiRot on `SKILL.md` before publishing.
- Do not add credential readers, installers, service restarts, or host-specific assumptions.
- Treat ClawHub output and security scanner warnings as part of release verification.

## Repo Map

- [Overview](docs/codex/overview.md)
- [Architecture](docs/codex/architecture.md)
- [Workflow](docs/codex/workflow.md)
- [Evals](docs/codex/evals.md)
- [Cleanup](docs/codex/cleanup.md)

## Project-Scoped Custom Agents

- `.codex/agents/architect.toml`
- `.codex/agents/implementer.toml`
- `.codex/agents/reviewer.toml`
- `.codex/agents/evolver.toml`
- `.codex/agents/cleanup.toml`

## Verification

```bash
python3 -m antirot.cli lint SKILL.md --strict
clawhub inspect agentic-codex-dev --files
```

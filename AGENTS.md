# AGENTS.md

This repository contains one public skill bundle.

## Operating Rules

- Keep the skill instruction-only unless a future task proves a script is necessary.
- Preserve the root skill layout: `SKILL.md`, `agents/`, and `references/`.
- Keep claims evidence-backed. Run AntiRot on `SKILL.md` before publishing.
- Do not add credential readers, installers, service restarts, or host-specific assumptions.
- Treat ClawHub output and security scanner warnings as part of release verification.

## Verification

```bash
python3 -m antirot.cli lint SKILL.md --strict
clawhub inspect agentic-codex-dev --files
```

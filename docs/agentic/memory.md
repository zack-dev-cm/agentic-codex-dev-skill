# Memory Ledger

## Stable Facts

- The public runtime bundle is instruction-only: `SKILL.md`, `agents/openai.yaml`, and `references/*.md`.
- `.clawhubignore` excludes repo maintenance and benchmark evidence from the ClawHub runtime bundle.
- Required runtime binaries are declared in `SKILL.md` metadata: `git`, `python3`, and `clawhub`.
- `agents/openai.yaml` sets `allow_implicit_invocation: false` so the workflow is explicit-invocation only.
- `tests/test_public_surface.py` scans Python files for private paths, local URLs, and secret-like strings.

## Decisions

- Keep the skill instruction-only. Use references, tests, and repo-owned ledgers instead of adding a daemon or executable orchestrator.
- Use `gpt-5.4`/`xhigh` for architecture, security review, and release judgment. Use faster models only for reviewed support work.
- Store real-run evidence in `docs/agentic/` and exclude it from ClawHub publishes because it is repo evidence, not runtime skill content.

## Hazards

- Do not claim GitHub CI enforcement until `.github/workflows/ci.yml` exists on the remote default branch.
- Do not include absolute local paths, private endpoints, tokens, raw chat logs, or copied private notes in public evidence.
- Do not run `git push` or `clawhub publish` unless the user explicitly asks for deployment.

## Last Verified

- 2026-04-22: `agentic-codex-dev@0.2.2` was published with ClawHub `Security: CLEAN` and `hasWarnings: false`.

# Agentic Codex Dev Skill

Small, source-reviewed skill for agentic software development with Codex, GitHub, OpenClaw, and ClawHub.

The skill is intentionally instruction-only:

- no scripts
- no installers
- no credential readers
- no background daemons

It teaches a Karpathy-style loop: state the goal, inspect the repo, make a small diff, verify, review for leaks and regressions, then publish only when the public surface is clean.

## Files

- `SKILL.md`: runtime skill instructions and metadata.
- `agents/openai.yaml`: Codex UI metadata.
- `references/source-review.md`: source analysis behind the workflow.
- `references/publish-checklist.md`: GitHub and ClawHub release checklist.

## Publish

```bash
python3 -m antirot.cli lint SKILL.md --strict
clawhub publish . --version 0.1.2
clawhub inspect agentic-codex-dev --files
```

## License

MIT-0.

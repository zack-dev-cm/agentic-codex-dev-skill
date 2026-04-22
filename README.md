# Agentic Codex Dev Skill

Source-reviewed skill for agentic software development with Codex, GitHub, OpenClaw, and ClawHub.

The skill is intentionally instruction-only:

- no scripts
- no installers
- no credential readers
- no background daemons

It teaches a Karpathy-style operating loop: state the goal, inspect the repo, assign explicit roles when needed, make scoped changes, verify, review for leaks and regressions, update durable memory, then publish only when the public surface is clean.

## Files

- `SKILL.md`: runtime skill instructions and metadata.
- `agents/openai.yaml`: Codex UI metadata.
- `references/source-review.md`: source analysis behind the workflow.
- `references/comparison-matrix.md`: source-by-source comparison and gap analysis.
- `references/system-design.md`: task, memory, report, role, and isolation templates.
- `references/example-run.md`: real-run eval acceptance shape.
- `references/publish-checklist.md`: GitHub and ClawHub release checklist.

## Security

See [SECURITY.md](SECURITY.md) for responsible disclosure and the release bleed gate.

## Publish

```bash
python3 -m antirot.cli lint SKILL.md --strict
clawhub publish . --version 0.2.2
clawhub inspect agentic-codex-dev --files
```

## License

MIT-0.

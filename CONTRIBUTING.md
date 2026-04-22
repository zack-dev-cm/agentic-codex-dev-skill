# Contributing

This repo publishes one instruction-only Codex/OpenClaw skill.

## Local Checks

Run the public-surface test suite before opening a pull request:

```bash
python3 -m unittest discover -s tests
python3 -m antirot.cli lint SKILL.md --strict
```

If `antirot` is not installed, inspect `SKILL.md` manually for unsupported claims and evidence links before publishing.

## Review Rules

- Keep the skill text-based and small.
- Do not add installers, credential readers, background jobs, or host-specific assumptions.
- Update `references/source-review.md` when a workflow rule depends on a new public source.
- Update `references/publish-checklist.md` when the ClawHub or GitHub release path changes.
- Check ClawHub scanner output after each publish.

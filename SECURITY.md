# Security

This repository contains an instruction-only skill bundle. It should not contain executable installers, credential readers, private endpoints, or host-specific secrets.

## Reporting

Open a GitHub security advisory or private issue with:

- affected file path
- observed risk
- reproduction steps or scanner output
- suggested remediation, if known

## Release Gate

Before publishing a new ClawHub version:

```bash
python3 -m unittest discover -s tests
python3 -m antirot.cli lint SKILL.md --strict
python3 -m codex_harness audit . --strict --min-score 90
clawhub inspect agentic-codex-dev --files
```

Treat security scanner warnings, private paths, local URLs, copied private notes, and secret-like strings as release blockers unless they are clearly inert policy examples.

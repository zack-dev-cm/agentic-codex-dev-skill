# Overview

This repository contains one public Codex/OpenClaw skill: `agentic-codex-dev`.

## Product

- `agentic-codex-dev`: instruction-only workflow for small, verified agentic software development loops.

## Standard Checks

- Tests: `python3 -m unittest discover -s tests`
- Claim hygiene: `python3 -m antirot.cli lint SKILL.md --strict`
- ClawHub listing: `clawhub inspect agentic-codex-dev --files`
- Optional repo gate: `python3 -m codex_harness audit . --strict --min-score 90`

## Non-Goals

- No daemon, hosted service, or agent framework.
- No installer or credential-management logic.
- No binary assets or generated runtime code.

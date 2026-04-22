# Overview

This repository contains one public Codex/OpenClaw skill: `agentic-codex-dev`.

## Product

- `agentic-codex-dev`: instruction-only workflow for production-grade agentic software development with explicit roles, model policy, task ledger, memory ledger, report artifacts, verification gates, and public-surface review.

## Standard Checks

- Tests: `python3 -m unittest discover -s tests`
- Claim hygiene: `python3 -m antirot.cli lint SKILL.md --strict`
- Repo audit: `python3 -m codex_harness audit . --strict --min-score 90`
- ClawHub listing: `clawhub inspect agentic-codex-dev --files`

## Non-Goals

- No daemon, hosted service, or agent framework.
- No installer or credential-management logic.
- No binary assets or generated runtime code.
- No claim that CI is enforced until a workflow exists on the remote default branch.

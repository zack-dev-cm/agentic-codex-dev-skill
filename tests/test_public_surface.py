from __future__ import annotations

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parent.parent
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".toml", ".txt", ".py", ""}
SKIP_DIRS = {".git", ".clawhub", "__pycache__"}

BLEED_PATTERNS = {
    "private_path": re.compile(r"(?:(?:/Users|/home)/[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\)"),
    "private_url": re.compile(
        r"\bhttps?://(?:localhost|127\.0\.0\.1|0\.0\.0\.0|10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})"
    ),
    "internal_host": re.compile(r"\bhttps?://[A-Za-z0-9.-]+\.(?:local|internal|corp|lan)\b"),
    "github_token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b"),
    "github_pat": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "api_key": re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    "aws_key": re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    "private_key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}


def iter_text_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        paths.append(path)
    return paths


class PublicSurfaceTests(unittest.TestCase):
    def test_skill_metadata_stays_current(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("name: agentic-codex-dev", skill)
        self.assertIn("version: 0.3.0", skill)
        self.assertIn("https://github.com/zack-dev-cm/agentic-codex-dev-skill", skill)
        self.assertIn('"requires":{"bins":["git","python3","clawhub"]}', skill)

    def test_skill_keeps_multi_agent_contract(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        for section in (
            "## System Design",
            "## Task, Memory, and Report Ledgers",
            "## Role Roster",
            "## Model Policy",
            "## Consistency and Effectiveness Gates",
            "## Real Example Eval",
        ):
            self.assertIn(section, skill)

        for required in (
            "gpt-5.4",
            "xhigh",
            "task ledger",
            "memory ledger",
            "report ledger",
            "agents.max_depth = 1",
            "references/comparison-matrix.md",
            "references/system-design.md",
            "references/example-run.md",
        ):
            self.assertIn(required, skill)

    def test_public_entry_points_avoid_weak_patch_only_positioning(self) -> None:
        for relative_path in ("SKILL.md", "README.md", "agents/openai.yaml"):
            text = (ROOT / relative_path).read_text(encoding="utf-8").lower()
            self.assertNotRegex(text, r"\bsmall\b")

        metadata = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("allow_implicit_invocation: false", metadata)

    def test_clawhub_ignore_excludes_repo_harness(self) -> None:
        ignore = (ROOT / ".clawhubignore").read_text(encoding="utf-8")

        for path in (
            ".codex/",
            ".github/",
            "docs/agentic/",
            "docs/codex/",
            "tests/",
            "AGENTS.md",
            "README.md",
            "LICENSE",
        ):
            self.assertIn(path, ignore)

    def test_reference_set_covers_sources_system_design_and_eval(self) -> None:
        for relative_path in (
            "references/source-review.md",
            "references/comparison-matrix.md",
            "references/system-design.md",
            "references/example-run.md",
            "references/publish-checklist.md",
        ):
            self.assertTrue((ROOT / relative_path).is_file(), relative_path)

        matrix = (ROOT / "references/comparison-matrix.md").read_text(encoding="utf-8")
        for source in (
            "optillm",
            "openevolve",
            "autoresearch",
            "symphony",
            "paperclip",
            "gstack",
            "openclaw",
            "agent-orchestrator",
            "rdudov",
        ):
            self.assertIn(source, matrix)

    def test_custom_agents_declare_models_and_reasoning(self) -> None:
        expected_agents = {
            "orchestrator.toml",
            "analyst.toml",
            "architect.toml",
            "planner.toml",
            "explorer.toml",
            "implementer.toml",
            "reviewer.toml",
            "qa.toml",
            "evolver.toml",
            "memory-curator.toml",
            "cleanup.toml",
        }
        agent_dir = ROOT / ".codex" / "agents"
        actual_agents = {path.name for path in agent_dir.glob("*.toml")}
        self.assertTrue(expected_agents.issubset(actual_agents))

        for path in agent_dir.glob("*.toml"):
            text = path.read_text(encoding="utf-8")
            self.assertIn('model = "', text, path.name)
            self.assertIn('model_reasoning_effort = "', text, path.name)

        for path in ("architect.toml", "reviewer.toml", "orchestrator.toml"):
            text = (agent_dir / path).read_text(encoding="utf-8")
            self.assertIn('model = "gpt-5.4"', text)
            self.assertIn('model_reasoning_effort = "xhigh"', text)

    def test_real_run_evidence_is_present_and_repo_only(self) -> None:
        expected_files = (
            "docs/agentic/tasks.md",
            "docs/agentic/memory.md",
            "docs/agentic/reports/2026-04-22-v0.3.0-real-run.md",
        )
        for relative_path in expected_files:
            self.assertTrue((ROOT / relative_path).is_file(), relative_path)

        report = (ROOT / "docs/agentic/reports/2026-04-22-v0.3.0-real-run.md").read_text(
            encoding="utf-8"
        )
        for required in (
            "## Objective",
            "## Baseline",
            "## Role Roster Used",
            "## Tasks",
            "## Verification",
            "## Review Findings",
            "## Deployment",
            "## Residual Risks",
        ):
            self.assertIn(required, report)

    def test_no_private_or_secret_like_bleed(self) -> None:
        findings: list[str] = []
        for path in iter_text_files():
            text = path.read_text(encoding="utf-8")
            for label, pattern in BLEED_PATTERNS.items():
                if pattern.search(text):
                    findings.append(f"{path.relative_to(ROOT)}:{label}")

        self.assertEqual([], findings)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parent.parent
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".toml", ".txt", ""}
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
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            paths.append(path)
    return paths


class PublicSurfaceTests(unittest.TestCase):
    def test_skill_metadata_stays_current(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("name: agentic-codex-dev", skill)
        self.assertIn("version: 0.1.2", skill)
        self.assertIn("https://github.com/zack-dev-cm/agentic-codex-dev-skill", skill)

    def test_clawhub_ignore_excludes_repo_harness(self) -> None:
        ignore = (ROOT / ".clawhubignore").read_text(encoding="utf-8")

        for path in (".codex/", ".github/", "docs/codex/", "tests/"):
            self.assertIn(path, ignore)

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

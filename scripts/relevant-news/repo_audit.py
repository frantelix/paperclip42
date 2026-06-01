#!/usr/bin/env python3
"""Audit the relevant-news package before staging or publishing.

The audit intentionally uses only local filesystem and git metadata. It does
not open network connections and does not mutate the worktree.
"""

from __future__ import annotations

import fnmatch
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "docs" / "relevant-news"

ACTIVE_PATHS = [
    PACKAGE / ".paperclip.yaml",
    PACKAGE / "AGENTS.md",
    PACKAGE / "COMPANY.md",
    PACKAGE / "MANIFEST_V1_8.md",
    PACKAGE / "00_AKTIVE_STEUERUNG",
    PACKAGE / "00_START_HIER",
    PACKAGE / "01_KI_MITARBEITER",
    PACKAGE / "02_TEMPLATES",
    PACKAGE / "03_WORKFLOW",
    PACKAGE / "04_RULES",
    PACKAGE / "05_EVALUATION",
    PACKAGE / "agents",
    PACKAGE / "projects" / "relevant-news",
    PACKAGE / "skills",
    PACKAGE / "tasks",
]

FORBIDDEN_CONTEXT_DIRS = [
    PACKAGE / "_archive_DO_NOT_LOAD",
    PACKAGE / "20_LAUFARTEFAKTE",
    PACKAGE / "04_Arbeitslaeufe",
    PACKAGE / "06_BEISPIELE",
    PACKAGE / "99_NOTIZEN",
    PACKAGE / "_LATEST",
]

ROOT_ARTIFACT_RE = re.compile(
    r"^docs/relevant-news/"
    r"(NEW-|SCOUT-PROBE-|2026-05-|Claim_Ledger_|06_source_verification_)"
)
OLD_TOP_STORY_RE = re.compile(r"\b3\s*(?:-|–|bis)\s*5\s+Top Stories\b", re.I)
OLD_MACRO_RE = re.compile(r"Makro-Kontext hat 2 bis 4 Bulletpoints", re.I)
HASHTABLE_RE = re.compile(r"System\.Collections\.Hashtable")
OLD_ACTIVE_VERSION_RE = re.compile(r"(?:V1[._-]?[27]|V1\.[27])", re.I)

RUNTIME_PATTERNS = [
    "*/runlog_*.txt",
    "*/send-log.*",
    "*/send-preview.*",
    "*/send-slot-wrapper-log.*",
    "*/smtp-transport-*",
    "*/.sent-fingerprints.json",
    "*/runtime-log.md",
    "*/runtime-audit.md",
    "*/runtime-export/*",
    "*/_LATEST/*",
]


def git_lines(*args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return [line for line in result.stdout.splitlines() if line]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_text_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(
                child
                for child in path.rglob("*")
                if child.is_file() and child.suffix.lower() in {".md", ".yaml", ".yml"}
            )
    return sorted(files)


def trackable_package_files() -> list[str]:
    return sorted(
        set(
            git_lines(
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
                "--",
                "docs/relevant-news",
                "scripts/relevant-news",
            )
        )
    )


def existing_package_files() -> list[Path]:
    if not PACKAGE.exists():
        return []
    return sorted(child for child in PACKAGE.rglob("*") if child.is_file())


def is_runtime_artifact(path: str) -> bool:
    if path.startswith("docs/relevant-news/20_LAUFARTEFAKTE/"):
        return True
    return any(fnmatch.fnmatch(path, pattern) for pattern in RUNTIME_PATTERNS)


def is_active_relevant_news_path(path: str) -> bool:
    if not path.startswith("docs/relevant-news/"):
        return False
    relative = path.removeprefix("docs/relevant-news/")
    first = relative.split("/", 1)[0]
    return first in {
        ".paperclip.yaml",
        "AGENTS.md",
        "COMPANY.md",
        "MANIFEST_V1_8.md",
        "00_AKTIVE_STEUERUNG",
        "00_START_HIER",
        "01_KI_MITARBEITER",
        "02_TEMPLATES",
        "03_WORKFLOW",
        "04_RULES",
        "05_EVALUATION",
        "agents",
        "projects",
        "skills",
        "tasks",
    }


def main() -> int:
    errors: list[str] = []

    for path in FORBIDDEN_CONTEXT_DIRS:
        if path.exists():
            errors.append(f"forbidden active-context directory exists: {rel(path)}")

    for path in iter_text_files(ACTIVE_PATHS):
        text = path.read_text(encoding="utf-8")
        if OLD_TOP_STORY_RE.search(text):
            errors.append(f"old 3-5 Top Stories rule in active doc: {rel(path)}")
        if OLD_MACRO_RE.search(text):
            errors.append(f"old macro bulletpoint rule in active doc: {rel(path)}")
        if HASHTABLE_RE.search(text):
            errors.append(f"PowerShell hashtable artifact in active doc: {rel(path)}")

    for path in existing_package_files():
        relative_path = rel(path)
        if ROOT_ARTIFACT_RE.search(relative_path):
            errors.append(f"root-level relevant-news artifact exists: {relative_path}")
        if is_runtime_artifact(relative_path):
            errors.append(f"runtime/lauf artifact exists in active context: {relative_path}")

    for path in trackable_package_files():
        if ROOT_ARTIFACT_RE.search(path):
            errors.append(f"root-level relevant-news artifact is trackable: {path}")
        if is_runtime_artifact(path):
            errors.append(f"runtime/lauf artifact is trackable: {path}")
        if is_active_relevant_news_path(path) and OLD_ACTIVE_VERSION_RE.search(path):
            if "LEGACY_GMX_SEND_REFERENCE" not in path:
                errors.append(f"old V1.2/V1.7 file appears active/trackable: {path}")

    if errors:
        print("Relevant News repo audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Relevant News repo audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

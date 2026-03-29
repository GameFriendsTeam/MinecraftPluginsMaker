from __future__ import annotations

import argparse
import re
from pathlib import Path

HEADER_RE = re.compile(r"^##\s+\[?([^\]\s]+)\]?(?:\s*-\s*.+)?\s*$")


def normalize_tag(tag: str) -> str:
    cleaned = tag.strip()
    prefix = "refs/tags/"
    if cleaned.startswith(prefix):
        cleaned = cleaned[len(prefix) :]
    return cleaned


def tag_candidates(tag: str) -> set[str]:
    candidates = {tag}
    if tag.startswith("v"):
        candidates.add(tag[1:])
    else:
        candidates.add(f"v{tag}")
    return candidates


def extract_notes(changelog_text: str, tag: str) -> str:
    lines = changelog_text.splitlines()
    versions = tag_candidates(normalize_tag(tag))

    start_index = None
    for index, line in enumerate(lines):
        match = HEADER_RE.match(line.strip())
        if match and match.group(1) in versions:
            start_index = index + 1
            break

    if start_index is None:
        known_versions: list[str] = []
        for line in lines:
            match = HEADER_RE.match(line.strip())
            if match:
                known_versions.append(match.group(1))
        known_versions_display = ", ".join(known_versions) or "none"
        raise ValueError(
            f"Version for tag '{tag}' not found in changelog. Known versions: {known_versions_display}"
        )

    end_index = len(lines)
    for index in range(start_index, len(lines)):
        if lines[index].strip().startswith("## "):
            end_index = index
            break

    section_lines = lines[start_index:end_index]
    while section_lines and not section_lines[0].strip():
        section_lines.pop(0)
    while section_lines and not section_lines[-1].strip():
        section_lines.pop()

    if not section_lines:
        raise ValueError(
            f"Changelog section for tag '{tag}' is empty. Add notes under this version header."
        )

    return "\n".join(section_lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract release notes for a tag from CHANGELOG.md"
    )
    parser.add_argument("--changelog", default="CHANGELOG.md")
    parser.add_argument("--tag", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    changelog_path = Path(args.changelog)
    changelog_text = changelog_path.read_text(encoding="utf-8")
    notes = extract_notes(changelog_text, args.tag)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(notes, encoding="utf-8")

    print(f"Release notes written to {output_path}")


if __name__ == "__main__":
    main()

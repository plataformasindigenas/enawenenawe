#!/usr/bin/env python3
"""Transform the raw corpus JSON files into data/corpus.yaml."""

import json
import re
from pathlib import Path

import yaml

RAW_CORPUS_DIR = Path(__file__).resolve().parent.parent.parent / "boeenomoto" / "raw_corpus"
OUT_YAML = Path(__file__).resolve().parent.parent / "data" / "corpus.yaml"


def slugify(text: str) -> str:
    s = text.strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "_", s)
    return s.lower()


def title_from_filename(filename: str) -> str:
    """Derive a title from the filename."""
    stem = Path(filename).stem
    # Insert spaces before uppercase letters (camelCase -> camel Case)
    spaced = re.sub(r"([a-z])([A-Z])", r"\1 \2", stem)
    # Replace underscores with spaces
    spaced = spaced.replace("_", " ")
    return spaced.strip().title()


def main():
    OUT_YAML.parent.mkdir(parents=True, exist_ok=True)

    corpus_files = sorted(RAW_CORPUS_DIR.glob("*.txt"))
    print(f"Found {len(corpus_files)} corpus files")

    entries = []
    skipped = 0
    for filepath in corpus_files:
        raw = filepath.read_text(encoding="utf-8").strip()

        # Try parsing as JSON first
        try:
            data = json.loads(raw)
            filename = data.get("file", filepath.name)
            content = data.get("text", "")
        except (json.JSONDecodeError, ValueError):
            # Not valid JSON (e.g., 404 page) - skip
            print(f"  Skipping {filepath.name} (not valid JSON)")
            skipped += 1
            continue

        if not content.strip():
            print(f"  Skipping {filepath.name} (empty content)")
            skipped += 1
            continue

        stem = Path(filename).stem
        slug = slugify(stem)
        title = title_from_filename(filename)

        entries.append({
            "id": slug,
            "title": title,
            "filename": filename,
            "content": content.strip(),
        })

    with open(OUT_YAML, "w", encoding="utf-8") as f:
        yaml.dump(entries, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\nWrote {len(entries)} entries to {OUT_YAML}")
    if skipped:
        print(f"Skipped {skipped} files")


if __name__ == "__main__":
    main()

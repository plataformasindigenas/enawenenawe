#!/usr/bin/env python3
"""Parse the raw fauna HTML table and produce data/fauna.yaml with image downloads."""

import re
import sys
import urllib.request
import urllib.error
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path

import yaml

RAW_HTML = Path(__file__).resolve().parent.parent.parent / "boeenomoto" / "raw_fauna_cards.html"
OUT_YAML = Path(__file__).resolve().parent.parent / "data" / "fauna.yaml"
IMAGES_DIR = Path(__file__).resolve().parent.parent / "docs" / "images"

HEADERS = ["nome_enawene", "nome_brasil", "nome_cientifico", "classificacao_enawene", "notas", "imagem"]


class TableParser(HTMLParser):
    """Simple HTML table parser."""

    def __init__(self):
        super().__init__()
        self.rows = []
        self._in_tbody = False
        self._in_row = False
        self._in_cell = False
        self._current_row = []
        self._current_cell = ""

    def handle_starttag(self, tag, attrs):
        if tag == "tbody":
            self._in_tbody = True
        elif tag == "tr" and self._in_tbody:
            self._in_row = True
            self._current_row = []
        elif tag == "td" and self._in_row:
            self._in_cell = True
            self._current_cell = ""

    def handle_endtag(self, tag):
        if tag == "tbody":
            self._in_tbody = False
        elif tag == "tr" and self._in_row:
            self._in_row = False
            if self._current_row:
                self.rows.append(self._current_row)
        elif tag == "td" and self._in_cell:
            self._in_cell = False
            self._current_row.append(self._current_cell.strip())

    def handle_data(self, data):
        if self._in_cell:
            self._current_cell += data


def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "_", s)
    return s[:40]


def download_image(url: str, entry_id: int, name: str, prefix: str = "fauna") -> str | None:
    if not url or not url.startswith("http"):
        return None

    slug = slugify(name) if name else str(entry_id)
    ext = ".jpg"
    lower_url = url.lower()
    if ".png" in lower_url:
        ext = ".png"
    elif ".svg" in lower_url:
        ext = ".svg"
    elif ".webp" in lower_url:
        ext = ".webp"
    elif ".gif" in lower_url:
        ext = ".gif"
    elif ".jpeg" in lower_url:
        ext = ".jpeg"

    filename = f"{prefix}_{entry_id:03d}_{slug}{ext}"
    local_path = IMAGES_DIR / filename

    if local_path.exists():
        return f"images/{filename}"

    try:
        parsed = urllib.parse.urlsplit(url)
        safe_path = urllib.parse.quote(parsed.path, safe="/:@!$&'()*+,;=-._~")
        safe_url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, safe_path, parsed.query, parsed.fragment))
        req = urllib.request.Request(safe_url, headers={
            "User-Agent": "Mozilla/5.0 (terradoc fauna importer)"
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            local_path.write_bytes(resp.read())
        print(f"    Downloaded: {filename}")
        return f"images/{filename}"
    except Exception as e:
        print(f"    Failed to download {url}: {e}")
        return None


def main():
    download_imgs = "--no-images" not in sys.argv

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    OUT_YAML.parent.mkdir(parents=True, exist_ok=True)

    html_text = RAW_HTML.read_text(encoding="utf-8")
    parser = TableParser()
    parser.feed(html_text)

    print(f"Parsed {len(parser.rows)} rows from HTML table")

    entries = []
    entry_id = 0
    for row in parser.rows:
        # Pad row to expected length
        while len(row) < len(HEADERS):
            row.append("")

        nome_enawene = row[0].strip()
        nome_brasil = row[1].strip()
        nome_cientifico = row[2].strip()
        classificacao = row[3].strip()
        notas = row[4].strip()
        imagem = row[5].strip()

        # Skip completely empty rows
        if not nome_enawene and not nome_brasil:
            continue

        entry_id += 1
        entry = {"id": entry_id, "name_indigenous": nome_enawene}

        if nome_brasil:
            entry["name_portuguese"] = nome_brasil
        if nome_cientifico:
            entry["scientific_name"] = nome_cientifico
        if classificacao:
            entry["classification_indigenous"] = classificacao
        if notas:
            entry["info"] = notas

        if imagem and download_imgs:
            local = download_image(imagem, entry_id, nome_enawene or nome_brasil)
            if local:
                entry["pic_link"] = local
        elif imagem:
            entry["pic_link"] = imagem

        entries.append(entry)

    with open(OUT_YAML, "w", encoding="utf-8") as f:
        yaml.dump(entries, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\nWrote {len(entries)} entries to {OUT_YAML}")

    # Stats
    fields = ["name_indigenous", "name_portuguese", "scientific_name",
              "classification_indigenous", "info", "pic_link"]
    print("\nField completeness:")
    for field in fields:
        count = sum(1 for e in entries if e.get(field))
        print(f"  {field}: {count}/{len(entries)}")


if __name__ == "__main__":
    main()

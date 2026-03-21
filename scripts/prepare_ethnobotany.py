#!/usr/bin/env python3
"""Parse the raw XML ethnobotany data and produce data/ethnobotany.yaml with image downloads."""

import re
import sys
import urllib.request
import urllib.error
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

RAW_XML = Path(__file__).resolve().parent.parent.parent / "boeenomoto" / "raw_especies.xml"
OUT_YAML = Path(__file__).resolve().parent.parent / "data" / "ethnobotany.yaml"
IMAGES_DIR = Path(__file__).resolve().parent.parent / "docs" / "images"


def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "_", s)
    return s[:40]


def download_image(url: str, entry_id: int, name: str) -> str | None:
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

    filename = f"ethnobotany_{entry_id:03d}_{slug}{ext}"
    local_path = IMAGES_DIR / filename

    if local_path.exists():
        return f"images/{filename}"

    try:
        parsed = urllib.parse.urlsplit(url)
        safe_path = urllib.parse.quote(parsed.path, safe="/:@!$&'()*+,;=-._~")
        safe_url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, safe_path, parsed.query, parsed.fragment))
        req = urllib.request.Request(safe_url, headers={
            "User-Agent": "Mozilla/5.0 (terradoc ethnobotany importer)"
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            local_path.write_bytes(resp.read())
        print(f"    Downloaded: {filename}")
        return f"images/{filename}"
    except Exception as e:
        print(f"    Failed to download {url}: {e}")
        return None


def get_text(element, tag: str) -> str:
    """Get text from a child element, returning empty string if missing."""
    el = element.find(tag)
    if el is not None and el.text:
        return el.text.strip()
    return ""


def main():
    download_imgs = "--no-images" not in sys.argv

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    OUT_YAML.parent.mkdir(parents=True, exist_ok=True)

    tree = ET.parse(RAW_XML)
    root = tree.getroot()

    species = root.findall("especie")
    print(f"Parsed {len(species)} <especie> elements from XML")

    # Deduplicate by (nome, pt) - the XML has some exact duplicates
    seen = set()
    entries = []
    entry_id = 0

    for sp in species:
        nome = get_text(sp, "nome")
        pt = get_text(sp, "pt")
        nome_cien = get_text(sp, "nome_cien")
        imagem = get_text(sp, "imagem")
        uso = get_text(sp, "uso")

        # Merge both <descricao> and <decricao> tags (typo in source)
        descriptions = []
        for tag in ("descricao", "decricao"):
            for el in sp.findall(tag):
                if el.text and el.text.strip():
                    descriptions.append(el.text.strip())
        desc_merged = " | ".join(descriptions) if descriptions else ""

        # Skip empty entries
        if not nome and not pt:
            continue

        # Deduplicate
        key = (nome.lower(), pt.lower())
        if key in seen:
            continue
        seen.add(key)

        entry_id += 1
        entry = {"id": entry_id, "name_indigenous": nome}

        if pt:
            entry["name_portuguese"] = pt
        if nome_cien:
            entry["scientific_name"] = nome_cien
        if uso:
            entry["usage"] = uso
        if desc_merged:
            entry["descriptions_of_use"] = desc_merged

        if imagem and download_imgs:
            local = download_image(imagem, entry_id, nome or pt)
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
              "usage", "descriptions_of_use", "pic_link"]
    print("\nField completeness:")
    for field in fields:
        count = sum(1 for e in entries if e.get(field))
        print(f"  {field}: {count}/{len(entries)}")


if __name__ == "__main__":
    main()

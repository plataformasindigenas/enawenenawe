#!/usr/bin/env python3
"""Transform the raw Enawene Nawe dictionary TSV into terradoc dictionary format."""

import csv
from pathlib import Path

RAW_TSV = Path(__file__).resolve().parent.parent.parent / "boeenomoto" / "raw_dicionario.tsv"
OUT_TSV = Path(__file__).resolve().parent.parent / "data" / "dictionary.tsv"

# POS mapping from pilot tags to terradoc tags
POS_MAP = {
    "S": "S",
    "V": "V",
    "ADV": "ADV",
    "ADJ": "ADJ",
    "N": "S",
    "S.M": "S",
    "S.F": "S",
    "S.PL": "S",
    "N.F": "S",
    "CLF": "X",
    "PROPN": "PROPN",
    "PRON": "PRON",
    "POSP": "POSP",
    "NUM": "NUM",
    "SCONJ": "CONJ",
    "ADV/ADJ": "ADV",
}

TERRADOC_FIELDS = [
    "id", "entry", "ipa", "pos", "definition", "example_sent",
    "scientific_name", "wiki_link", "pic_link", "comment", "created_at",
]


def main():
    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    with open(RAW_TSV, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for i, row in enumerate(reader, start=1):
            entry = (row.get("ENTRY") or "").strip()
            if not entry:
                continue

            raw_pos = (row.get("POS") or "").strip()
            pos = POS_MAP.get(raw_pos, raw_pos)  # keep unknown POS as-is

            definition = (row.get("PORTUGUÊS") or row.get("PORTUGUES") or "").strip()
            example_sent = (row.get("FRASE") or "").strip()
            scientific_name = (row.get("scientific_name") or "").strip()
            wiki_link = (row.get("wiki_link") or "").strip()
            pic_link = (row.get("IMAGEM") or "").strip()
            comment = (row.get("COMENTÁRIO") or row.get("COMENTARIO") or "").strip()
            created_at = (row.get("created_at") or "").strip()

            rows.append({
                "id": i,
                "entry": entry,
                "ipa": "",  # pilot IPA is just duplicate of entry
                "pos": pos,
                "definition": definition,
                "example_sent": example_sent,
                "scientific_name": scientific_name,
                "wiki_link": wiki_link,
                "pic_link": pic_link,
                "comment": comment,
                "created_at": created_at,
            })

    with open(OUT_TSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TERRADOC_FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} entries to {OUT_TSV}")

    # Stats
    pos_counts = {}
    for r in rows:
        p = r["pos"] or "(empty)"
        pos_counts[p] = pos_counts.get(p, 0) + 1
    print("\nPOS distribution:")
    for pos, count in sorted(pos_counts.items(), key=lambda x: -x[1]):
        print(f"  {pos}: {count}")

    fields_with_data = {}
    for field in TERRADOC_FIELDS:
        fields_with_data[field] = sum(1 for r in rows if r.get(field))
    print("\nField completeness:")
    for field, count in fields_with_data.items():
        print(f"  {field}: {count}/{len(rows)}")


if __name__ == "__main__":
    main()

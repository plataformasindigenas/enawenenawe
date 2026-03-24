#!/usr/bin/env python3
"""Download audio files referenced in the dictionary TSV."""

import csv
import time
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

RAW_TSV = Path(__file__).resolve().parent.parent.parent / "boeenomoto" / "raw_dicionario.tsv"
AUDIO_DIR = Path(__file__).resolve().parent.parent / "docs" / "audio"
BASE_URL = "https://enawenenawe.terradoc.org/dicionario/audio"


def main():
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    # Read dictionary to find audio entries
    audio_entries = []
    with open(RAW_TSV, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            audio = (row.get("AUDIO") or "").strip()
            entry = (row.get("ENTRY") or "").strip()
            if audio:
                audio_entries.append({"entry": entry, "audio": audio})

    print(f"Found {len(audio_entries)} entries with audio filenames")

    downloaded = 0
    skipped = 0
    failed = 0

    for item in audio_entries:
        audio_filename = item["audio"]
        # Skip entries with just ".wav" (no actual filename)
        if audio_filename == ".wav" or not audio_filename:
            print(f"  Skipping empty audio for '{item['entry']}'")
            skipped += 1
            continue

        local_path = AUDIO_DIR / audio_filename

        if local_path.exists():
            print(f"  Already exists: {audio_filename}")
            skipped += 1
            continue

        url = f"{BASE_URL}/{urllib.parse.quote(audio_filename)}"
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (terradoc audio downloader)"
            })
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                if len(data) < 100:
                    # Likely an error page, not audio
                    print(f"  Skipping {audio_filename} (response too small: {len(data)} bytes)")
                    failed += 1
                    continue
                local_path.write_bytes(data)
            print(f"  Downloaded: {audio_filename} ({len(data)} bytes)")
            downloaded += 1
            time.sleep(0.3)  # Be polite to the server
        except Exception as e:
            print(f"  Failed to download {audio_filename}: {e}")
            failed += 1

    print(f"\nAudio download summary:")
    print(f"  Downloaded: {downloaded}")
    print(f"  Skipped (exists/empty): {skipped}")
    print(f"  Failed: {failed}")
    print(f"  Total audio files in {AUDIO_DIR}: {len(list(AUDIO_DIR.glob('*')))}")


if __name__ == "__main__":
    main()

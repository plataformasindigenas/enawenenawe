#!/bin/bash
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"
echo "=== Enawenê-Nawê Build ==="
echo ""
terradoc build --config terradoc.yaml
echo ""
echo "Open docs/index.html in your browser to preview the site."

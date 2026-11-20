#!/bin/sh
# Builds the claude.ai Artifact version of the app: the page body without the html/head wrapper.
# Usage: sh build-artifact.sh <output.html>
set -e
in="$(dirname "$0")/index.html"
sed -n '/<!--APP-->/,/<!--\/APP-->/p' "$in" | sed '1d;$d' > "$1"
sed -n '/<!--APPBODY-->/,/<!--\/APPBODY-->/p' "$in" | sed '1d;$d' >> "$1"

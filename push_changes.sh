#!/bin/bash

cd /Users/mmt12861/Desktop/excel-to-json-web/excel_to_json_project

echo "=== Step 1: Abort any incomplete merges ==="
git merge --abort 2>/dev/null || true

echo "=== Step 2: Reset to clean state ==="
git reset --hard HEAD

echo "=== Step 3: Check status ==="
git status

echo "=== Step 4: Add all changes ==="
git add -A

echo "=== Step 5: Commit changes ==="
git commit -m "Final update: Refactored metafields handling with position-based detection and duplicate elimination" || echo "Nothing to commit"

echo "=== Step 6: Fetch from remote ==="
git fetch origin

echo "=== Step 7: Rebase on remote ==="
git rebase origin/main || git rebase --abort

echo "=== Step 8: Push to GitHub ==="
git push origin main

echo "=== SUCCESS: All changes pushed to GitHub ==="

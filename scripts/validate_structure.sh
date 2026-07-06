#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
status=0

required_files=(
  "README.md"
  "README.zh-CN.md"
  "ROADMAP.md"
  "LICENSE"
  "CONTRIBUTING.md"
  "CHANGELOG.md"
  "CODE_OF_CONDUCT.md"
  "SECURITY.md"
  ".github/workflows/structure-check.yml"
  ".github/pull_request_template.md"
  ".github/ISSUE_TEMPLATE/config.yml"
  ".github/ISSUE_TEMPLATE/skill_submission.yml"
  ".github/ISSUE_TEMPLATE/improvement.yml"
  "assets/logo.svg"
  "assets/logo-mono.svg"
  "assets/banner.svg"
  "assets/social-preview.svg"
  "assets/social-preview.png"
  "assets/diagrams/architecture.svg"
  "assets/diagrams/decompression-compression.svg"
  "assets/diagrams/agentic-loop.svg"
  "skills/README.md"
  "catalog/skills.json"
  "docs/en/README.md"
  "docs/zh-CN/README.md"
  "docs/en/project-architecture.md"
  "docs/zh-CN/project-architecture.md"
  "docs/en/protocols.md"
  "docs/zh-CN/protocols.md"
  "docs/en/skill-quality-guide.md"
  "docs/zh-CN/skill-quality-guide.md"
)

echo "Checking required files..."
for file in "${required_files[@]}"; do
  if [[ ! -f "$ROOT/$file" ]]; then
    echo "Missing required file: $file"
    status=1
  fi
done

echo "Checking skill folders..."
for dir in "$ROOT"/skills/*; do
  [[ -d "$dir" ]] || continue

  name="$(basename "$dir")"
  [[ "$name" == _* ]] && continue

  if [[ ! "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
    echo "Skill folder should use lowercase kebab-case: skills/$name"
    status=1
  fi

  for file in "SKILL.md" "SKILL.zh-CN.md"; do
    if [[ ! -f "$dir/$file" ]]; then
      echo "Missing $file in skills/$name"
      status=1
      continue
    fi

    if ! grep -Eq "^# .+" "$dir/$file"; then
      echo "$file should include a top-level title: skills/$name/$file"
      status=1
    fi
  done

  if [[ ! -f "$dir/examples/basic-usage.md" ]]; then
    echo "Missing example file: skills/$name/examples/basic-usage.md"
    status=1
  fi
done

echo "Checking catalog, bilingual paths, images, and privacy patterns..."
if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT/scripts/validate_catalog.py"
else
  echo "python3 not found; skipping deep validation"
fi

if [[ "$status" -ne 0 ]]; then
  echo "Structure check failed."
  exit "$status"
fi

echo "Structure check passed."

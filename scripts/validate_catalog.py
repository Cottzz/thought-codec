#!/usr/bin/env python3
import json
import re
import sys
from urllib.parse import unquote, urlparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
errors = []


def fail(message):
    errors.append(message)


def read_text(path):
    return path.read_text(encoding="utf-8")


catalog_path = ROOT / "catalog" / "skills.json"
try:
    catalog = json.loads(read_text(catalog_path))
except Exception as exc:
    fail(f"Invalid catalog JSON: {exc}")
    catalog = {}

skills = catalog.get("skills", [])
if not isinstance(skills, list) or not skills:
    fail("catalog/skills.json must contain a non-empty skills list")

seen_ids = set()
catalog_ids = set()

required_skill_fields = [
    "id",
    "title",
    "titleZh",
    "type",
    "status",
    "models",
    "tags",
    "description",
    "descriptionZh",
    "paths",
    "examples",
]

for item in skills:
    if not isinstance(item, dict):
        fail("Each catalog skill must be an object")
        continue

    for field in required_skill_fields:
        if field not in item:
            fail(f"Catalog skill is missing field '{field}': {item}")

    skill_id = item.get("id", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", skill_id):
        fail(f"Invalid skill id: {skill_id}")
        continue

    if skill_id in seen_ids:
        fail(f"Duplicate skill id: {skill_id}")
    seen_ids.add(skill_id)
    catalog_ids.add(skill_id)

    skill_type = item.get("type")
    if skill_type not in {"decompression", "compression", "loop"}:
        fail(f"Invalid type for {skill_id}: {skill_type}")

    status = item.get("status")
    if status not in {"draft", "preview", "stable"}:
        fail(f"Invalid status for {skill_id}: {status}")

    paths = item.get("paths", {})
    for language_key in ("en", "zh-CN"):
        rel_path = paths.get(language_key)
        if not rel_path:
            fail(f"{skill_id} is missing paths.{language_key}")
            continue

        file_path = ROOT / rel_path
        if not file_path.is_file():
            fail(f"{skill_id} path does not exist: {rel_path}")
            continue

        content = read_text(file_path)
        if f"name: {skill_id}" not in content:
            fail(f"{rel_path} frontmatter should include name: {skill_id}")
        if status and not re.search(rf"^status:\s*{re.escape(status)}\s*$", content, flags=re.MULTILINE):
            fail(f"{rel_path} frontmatter should include status: {status}")
        if not re.search(r"^# .+", content, flags=re.MULTILINE):
            fail(f"{rel_path} must include a top-level title")

    examples = item.get("examples", [])
    if not isinstance(examples, list) or not examples:
        fail(f"{skill_id} must include at least one example path")
    for rel_path in examples:
        file_path = ROOT / rel_path
        if not file_path.is_file():
            fail(f"{skill_id} example path does not exist: {rel_path}")
            continue
        content = read_text(file_path)
        if not re.search(r"^# .+", content, flags=re.MULTILINE):
            fail(f"{rel_path} must include a top-level title")

skill_dirs = {
    path.name
    for path in (ROOT / "skills").iterdir()
    if path.is_dir() and not path.name.startswith("_")
}

missing_from_catalog = skill_dirs - catalog_ids
extra_in_catalog = catalog_ids - skill_dirs
if missing_from_catalog:
    fail(f"Skill folders missing from catalog: {sorted(missing_from_catalog)}")
if extra_in_catalog:
    fail(f"Catalog skills missing folders: {sorted(extra_in_catalog)}")

markdown_link_pattern = re.compile(r"(!?)\[[^\]]*\]\(([^)]+)\)")


def markdown_target_path(markdown_path, raw_target):
    target = raw_target.strip()
    target = re.split(r"\s+(?=['\"])", target, maxsplit=1)[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if not target or target.startswith("#") or target.startswith("//"):
        return None

    parsed = urlparse(target)
    if parsed.scheme:
        return None

    clean = unquote(target.split("#", 1)[0])
    if not clean:
        return None
    if clean.startswith("/"):
        return ROOT / clean.lstrip("/")
    return (markdown_path.parent / clean).resolve()


for markdown_path in ROOT.rglob("*.md"):
    if ".git" in markdown_path.parts:
        continue
    text = read_text(markdown_path)
    for is_image, target in markdown_link_pattern.findall(text):
        local_path = markdown_target_path(markdown_path, target)
        if local_path is None:
            continue
        if not local_path.exists():
            link_type = "image" if is_image else "link"
            fail(
                f"Markdown {link_type} target does not exist in "
                f"{markdown_path.relative_to(ROOT)}: {target}"
            )

private_patterns = [
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
]

for path in ROOT.rglob("*"):
    if ".git" in path.parts or not path.is_file():
        continue
    if path.suffix.lower() not in {".md", ".json", ".yml", ".yaml", ".txt", ".svg", ".py", ".sh"}:
        continue
    text = read_text(path)
    for pattern in private_patterns:
        if pattern.search(text):
            fail(f"Potential private or secret-like content found in {path.relative_to(ROOT)}")
            break

if errors:
    for error in errors:
        print(error)
    sys.exit(1)

print("Deep validation passed.")

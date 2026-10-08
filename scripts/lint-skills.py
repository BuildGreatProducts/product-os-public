#!/usr/bin/env python3
"""Lint ProductOS skills against Anthropic's Skill authoring best practices.

Run from the repo root:  python3 scripts/lint-skills.py
Exit code 1 if any ERROR is found; WARNings never fail the run.

Checks
  ERROR  name: present, <=64 chars, lowercase letters/digits/hyphens, matches the folder,
         no reserved words ("anthropic", "claude")
  ERROR  description: present, <=1024 chars, no XML tags, has a "Not for" line
  WARN   description over 700 chars (descriptions load into every session)
  ERROR  SKILL.md body over 500 lines
  ERROR  a relative Markdown link in a skill that doesn't resolve (skills share phase-folder docs
         through links like ../../distribute/BONUS-*.md instead of bundling copies)
  ERROR  setup/CLAUDE.md and setup/AGENTS.md differ below their title line (they are twins; the
         build-plan list and every root rule live in both)
  ERROR  a computer:// link (client-specific; give the file path instead)
  WARN   a reference doc (BONUS-*.md, develop/guides/*.md) over 100 lines with no contents list
         near the top. Worksheets, *-TEMPLATE.md and REFERENCE-*.md are output shapes and are
         skipped: a contents list there would be copied into the member's documents.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
PHASES = ["define", "design", "develop", "distribute"]
DESC_MAX = 1024
DESC_WARN = 700       # comfortable budget: 39 skills x 700 chars is ~7k tokens per session
BODY_MAX_LINES = 500  # the best-practices limit for a SKILL.md body
TOC_MIN_LINES = 100   # reference files longer than this need a table of contents
TOC_SCAN_LINES = 40   # the contents list must sit near the top to survive partial reads

errors, warnings = [], []


def rel(path):
    return os.path.relpath(path, ROOT)


def parse_frontmatter(text):
    """Return ({key: value}, body) for the name/description subset ProductOS uses."""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fields, key, block = {}, None, []
    for line in m.group(1).split("\n"):
        top = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if top:
            if key and block:
                fields[key] = " ".join(block)
            key, value, block = top.group(1), top.group(2).strip(), []
            if value in (">", ">-", "|", "|-"):
                continue
            fields[key] = value.strip("'\"")
            key = None
        elif key is not None:
            block.append(line.strip())
    if key and block:
        fields[key] = " ".join(block)
    return fields, text[m.end():]


def has_toc(lines):
    head = lines[:TOC_SCAN_LINES]
    if any(re.match(r"^#+\s*(table of )?contents\b", l, re.I) for l in head):
        return True
    return sum(bool(re.search(r"\]\(#", l)) for l in head) >= 3


def check_skill(name):
    path = os.path.join(SKILLS, name, "SKILL.md")
    text = open(path, encoding="utf-8").read()
    fields, body = parse_frontmatter(text)
    if fields is None:
        errors.append(f"{rel(path)}: no YAML frontmatter")
        return

    n = fields.get("name", "")
    if not n:
        errors.append(f"{rel(path)}: missing name")
    elif len(n) > 64 or not re.fullmatch(r"[a-z0-9-]+", n):
        errors.append(f"{rel(path)}: name '{n}' must be <=64 chars of a-z, 0-9, hyphen")
    elif n != name:
        errors.append(f"{rel(path)}: name '{n}' doesn't match folder '{name}'")
    if re.search(r"anthropic|claude", n):
        errors.append(f"{rel(path)}: name uses a reserved word")

    d = fields.get("description", "")
    if not d:
        errors.append(f"{rel(path)}: missing description")
    else:
        if len(d) > DESC_MAX:
            errors.append(f"{rel(path)}: description is {len(d)} chars (max {DESC_MAX})")
        elif len(d) > DESC_WARN:
            warnings.append(f"{rel(path)}: description is {len(d)} chars (aim for <={DESC_WARN})")
        if re.search(r"<[A-Za-z/][^>]*>", d):
            errors.append(f"{rel(path)}: description contains an XML tag")
        if "Not for" not in d:
            errors.append(f"{rel(path)}: description has no 'Not for X — use Y' line")

    body_lines = body.count("\n")
    if body_lines > BODY_MAX_LINES:
        errors.append(f"{rel(path)}: body is {body_lines} lines (max {BODY_MAX_LINES})")


def check_links():
    for dirpath, _, files in os.walk(SKILLS):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(dirpath, f)
            text = open(path, encoding="utf-8").read()
            for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", text):
                target = m.group(1)
                if re.match(r"[a-z]+:", target):
                    continue
                if not os.path.exists(os.path.normpath(os.path.join(dirpath, target))):
                    errors.append(f"{rel(path)}: link to {target} doesn't resolve")


def check_setup_twins():
    a = open(os.path.join(ROOT, "setup", "CLAUDE.md"), encoding="utf-8").read().split("\n")[1:]
    b = open(os.path.join(ROOT, "setup", "AGENTS.md"), encoding="utf-8").read().split("\n")[1:]
    if a != b:
        errors.append("setup/CLAUDE.md and setup/AGENTS.md differ below their title line — keep the twins identical")


def markdown_files():
    roots = [SKILLS] + [os.path.join(ROOT, p) for p in PHASES]
    for top in roots:
        for dirpath, _, files in os.walk(top):
            for f in files:
                if f.endswith(".md"):
                    yield os.path.join(dirpath, f)


def is_reference_doc(path):
    base = os.path.basename(path)
    return base.startswith("BONUS-") or rel(path).startswith(os.path.join("develop", "guides"))


def check_files():
    for path in markdown_files():
        lines = open(path, encoding="utf-8").read().split("\n")
        if path.startswith(SKILLS) and any("computer://" in l for l in lines):
            errors.append(f"{rel(path)}: contains a computer:// link — give the file path instead")
        if not is_reference_doc(path):
            continue
        if len(lines) > TOC_MIN_LINES and not has_toc(lines):
            warnings.append(f"{rel(path)}: {len(lines)} lines with no contents list in the first "
                            f"{TOC_SCAN_LINES} lines")


def main():
    names = sorted(d for d in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md")))
    for name in names:
        check_skill(name)
    check_links()
    check_setup_twins()
    check_files()
    for w in warnings:
        print(f"WARN   {w}")
    for e in errors:
        print(f"ERROR  {e}")
    print(f"\n{len(names)} skills checked: {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

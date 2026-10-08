---
name: update
description: >-
  Updates an installed ProductOS to the latest release: fetches it into a temporary folder, compares
  every file three ways so untouched files update and the member's edits are kept, moves outputs
  older versions kept inside productos/ into docs/, never overwrites a docs/ file, then re-runs
  setup's wiring. Use when the user says "update ProductOS", "upgrade ProductOS", or "am I on the
  latest version". Not for a first install — use setup.
---

# Update — bring ProductOS up to the latest version

Move an installed copy of ProductOS to the latest release without losing the member's work. From 1.14.0 every skill writes its output to `docs/`, so `productos/` holds only the system — but older copies filled templates **in place** inside `productos/`, so a fresh download over the top would erase them. Instead, every file is compared against the published history: anything the member never touched is replaced, anything they wrote is kept, and an older copy's outputs are moved into `docs/` (step 5).

Write rules: write inside `productos/`, plus what `setup` steps 2–3 write at the repo root. Write to `docs/` only to move an older copy's outputs there, one file at a time with the member's approval, and never overwrite a `docs/` file — the member's canonical documents are theirs. Write nothing until the member has seen what's new and said go.

Run every command from the **app repo root** (the folder that contains `productos/`). Git is required — ProductOS already needs it.

## Workflow

### 1. Check the install and read the version

Run the same setup check the challenges use: `productos/` sits inside a git repo; the root `CLAUDE.md`/`AGENTS.md` carry the `<!-- BEGIN PRODUCTOS -->` block; `.gitignore` excludes `productos/` and nothing under it is tracked. This step only reads. Don't fix anything yet — note which checks failed, tell the member, and carry on. Step 6 runs `setup` in full after they've approved the update. The one exception: if `productos/` isn't inside a git repo at all, stop here and offer to run `setup` first, because it may move the folder.

The installed version is the `version` in `productos/.claude-plugin/plugin.json` (older copies without it: the **Version** line at the end of `productos/README.md`). Call it `V`.

### 2. Fetch the latest and show what's new

Clone the official repository into a temporary folder — never inside the app repo, and never from any other source (ProductOS is licensed from the official repository only; see `productos/LICENSE.md`). The full history is needed for step 3, so no `--depth`:

```bash
LOCAL="$(pwd)/productos"
WORK="$(mktemp -d)"
STAGE="$WORK/latest"
git clone --quiet https://github.com/BuildGreatProducts/product-os-public "$STAGE"
echo "WORK=$WORK"
grep -m1 '"version"' "$STAGE/.claude-plugin/plugin.json"
```

Many agents don't keep shell variables from one command to the next. If yours doesn't, start each later block by setting `LOCAL`, `WORK` (the path printed above), `STAGE="$WORK/latest"`, `V`, and `BASE` again.

- **Latest equals `V`** → fixes can still land between releases, so run step 3 anyway. If it finds nothing to `ADD`, `REPLACE`, or `REMOVE`, tell the member they're on the latest and offer step 6 (it catches a root block that drifted, and fixes anything step 1 found). Delete `$WORK`, and stop. Otherwise carry on without a changelog summary; just say fixes have landed since their copy.
- **Latest is older than `V`** (a coached copy can run ahead of the public release) → say so and stop; nothing to update.
- **Latest is newer** → read `$STAGE/CHANGELOG.md` and show the member each release between `V` and latest: the version heading and its bold opening sentence, nothing more. Name any skill renamed along the way (their `docs/PLAN.md` keeps working — setup reads old names as aliases). Ask for a go-ahead before writing anything.

### 3. Classify every file

Three inputs decide each file's fate:

- **Published** — every file content ever published in the official repo. A local file whose content matches one of these is untouched: the member never edited it, so it's safe to replace.
- **Base** — the published commit the member's copy came from. Prefer the tag `v$V` when it exists. Otherwise: if `V` is older than latest, the last commit still at `V` (the parent of the commit that bumped the version away from it); if `V` *is* the latest, the commit that released it. If none is found, `BASE` stays empty and the classification errs toward keeping.
- **Latest** — the clone's `HEAD`.

```bash
cd "$STAGE"
V="<installed version>"
if git rev-parse -q --verify "refs/tags/v$V" >/dev/null; then BASE="v$V"
else
  AWAY=$(git log --format=%H -1 -S"\"version\": \"$V\"" -- .claude-plugin/plugin.json)
  if grep -q "\"version\": \"$V\"" .claude-plugin/plugin.json; then BASE="$AWAY"
  else BASE="${AWAY:+$AWAY^}"; fi
fi

git rev-list --objects --all | cut -d' ' -f1 | sort -u > "$WORK/published"
{ git ls-files; (cd "$LOCAL" && find . -type f ! -path './.git/*' ! -name .DS_Store | sed 's|^\./||'); } | sort -u |
while IFS= read -r P; do
  if [ ! -f "$LOCAL/$P" ]; then echo "ADD $P"; continue; fi
  H=$(git hash-object "$LOCAL/$P")
  if git cat-file -e "HEAD:$P" 2>/dev/null; then
    if [ "$H" = "$(git rev-parse "HEAD:$P")" ]; then continue
    elif grep -qx "$H" "$WORK/published"; then echo "REPLACE $P"
    elif [ -n "$BASE" ] && git diff --quiet "$BASE" HEAD -- "$P"; then echo "KEEP $P"
    else echo "CONFLICT $P"; fi
  else
    if grep -qx "$H" "$WORK/published"; then echo "REMOVE $P"
    elif [ -n "$(git log --all --format=%H -1 -- "$P")" ]; then echo "GONE $P"
    else echo "MINE $P"; fi
  fi
done > "$WORK/plan.txt"
cut -d' ' -f1 "$WORK/plan.txt" | sort | uniq -c
```

| Label | Meaning | What happens |
|---|---|---|
| `ADD` | New in the latest release | Copied in |
| `REPLACE` | Untouched by the member, changed upstream | Replaced with the latest |
| `REMOVE` | Untouched by the member, deleted or renamed upstream | Deleted (a rename's new path arrives as `ADD`) |
| `KEEP` | Edited by the member; the release didn't change that file | Kept as-is |
| `CONFLICT` | Edited by the member *and* changed upstream — usually a template an older copy filled in place | Kept as-is, then step 5 |
| `GONE` | Edited by the member, but deleted or renamed upstream | Kept as-is, then step 5 |
| `MINE` | Never published — the member's own file (a wireframe or prompts file an older copy generated, an unmoved `PLAN.md`) | Kept as-is, then step 5 if it's an old output |

Show the member the counts and list every `KEEP`, `CONFLICT`, `GONE`, and `MINE` path by name — those are the files the update leaves alone. The `ADD`/`REPLACE`/`REMOVE` lists can be summarised.

### 4. Apply

```bash
cd "$STAGE"
ROOT=$(cd "$LOCAL" && pwd -P)
inside() {  # no symlink on the destination path, and its nearest existing folder resolves under productos/
  case "/$1/" in */../*|*/./*) return 1 ;; esac
  local d="$LOCAL" rest="$1/"
  while [ -n "$rest" ]; do d="$d/${rest%%/*}"; rest="${rest#*/}"; [ -L "$d" ] && return 1; done
  d=$(dirname "$LOCAL/$1"); while [ ! -d "$d" ]; do d=$(dirname "$d"); done
  case "$(cd "$d" && pwd -P)/" in "$ROOT"/*) return 0 ;; *) return 1 ;; esac
}
while IFS=' ' read -r ACT P; do
  case $ACT in
    ADD|REPLACE)
      if inside "$P"; then mkdir -p "$LOCAL/$(dirname "$P")" && cp -p "$P" "$LOCAL/$P"
      else echo "SKIPPED $P"; fi ;;
    REMOVE)
      if inside "$P"; then
        rm "$LOCAL/$P"
        d=$(dirname "$P")  # prune only folders this removal emptied
        while [ "$d" != "." ] && rmdir "$LOCAL/$d" 2>/dev/null; do d=$(dirname "$d"); done
      else echo "SKIPPED $P"; fi ;;
  esac
done < "$WORK/plan.txt"
```

Nothing labelled `KEEP`, `CONFLICT`, `GONE`, or `MINE` is written. A `SKIPPED` path runs through a symlink, usually a skills folder the member linked elsewhere. Copying there would write outside `productos/` and bypass the keep checks. List these for the member and leave them alone.

**If `productos/` is itself a git clone** (`productos/.git` exists — Cursor installs need one): first check `git -C productos log --oneline @{u}..HEAD 2>/dev/null` is empty; commits of the member's own in that clone mean stop and ask before going further. Then move the clone's `HEAD` to the release just applied, keeping the working tree as synced:

```bash
git -C "$LOCAL" fetch --quiet "$STAGE" HEAD && git -C "$LOCAL" reset --quiet FETCH_HEAD
git -C "$LOCAL" status --short
```

The status should list only the member's own files (`KEEP`, `CONFLICT`, `GONE`, `MINE`). The clone stays valid for Cursor's `/add-plugin`.

### 5. Move older outputs into `docs/`, then resolve what's left

Take each `KEEP`, `CONFLICT`, `GONE`, and `MINE` file one at a time. Never discard the member's content; the default is always to keep it.

**Outputs from a copy older than 1.14.0.** Read [migrations/1.14.0.md](migrations/1.14.0.md) and work through it first if any of these hold — otherwise skip it:

- A `KEEP`, `CONFLICT`, `GONE`, or `MINE` path is a filled worksheet or generated output inside `productos/define/`, `productos/design/`, or `productos/distribute/` — a numbered worksheet (`1-…`, `2-…`, `3-…`, `4-…`, `4a-…`, `4b-…`), `BONUS-Business-Strategy-Deep-Dive.md`, `BONUS-Idea-Audit.md` / `BONUS-Leverage-Audit.md`, `Design-Prompts.md`, or a `*-wireframe.html`.
- The repo root (outside `productos/`, so step 3 never lists them) holds `design-review/`, `CRO-AUDIT.md`, or `ACTIVATION-RETENTION-AUDIT.md` — check directly.
- `docs/PRODUCT.md` or `docs/LAUNCHES.md` exists.

**Everything else:**

- **`CONFLICT`** — a file the member edited that also changed upstream (usually a skill or guide they customised). Show what changed: the CHANGELOG line, plus `git -C "$STAGE" diff --stat "$BASE" HEAD -- <path>` for the shape of the change. Offer to reapply their edit on top of the latest version, or keep their file exactly as it is. Their call.
- **`GONE`** — find where the file went: `git -C "$STAGE" log --all -M30% --diff-filter=R --name-status --format= | awk -F'\t' -v p="<path>" '$2==p {print $3}'` (the low similarity threshold catches files reworked as they were renamed). Nothing back → search `$STAGE/CHANGELOG.md` for the filename; releases name their renames. **Renamed** (e.g. `studio-*` skills losing the prefix) → offer to carry the content into the new path the same way as a conflict, then delete the old file once the member confirms. **Deleted outright** (e.g. `skills/mini-launch/`, `skills/define-product/`) → tell the member the release retired it and ask whether to keep it; it no longer does anything.

A skill folder the member edited counts as their own; flag it, don't merge into it.

### 6. Re-run setup's wiring

If any step 1 check failed, run `setup` in full now. Otherwise run `setup` step 2 (replace the `<!-- BEGIN PRODUCTOS -->…<!-- END PRODUCTOS -->` block in the root `CLAUDE.md`/`AGENTS.md` from the freshly updated `productos/setup/`, or copy them whole if they don't exist) and step 3 (the gitignore check). This is how new agent guidelines reach the repo root. Don't touch `docs/PLAN.md` — setup step 4 already reads older skill names as aliases.

Then delete the temporary folder: `rm -rf "$WORK"`.

### 7. Refresh the plugin and report

If the member installed ProductOS as a plugin, the tool keeps its own copy of the skills. Tell them the one step for their tool, then to restart it:

- **Claude Code** — `claude plugin update productos@productos` (or re-run the `claude plugin install ./productos` they installed with).
- **Codex** — re-run `codex plugin add productos@productos` from the app repo root.
- **Cursor** — re-run `/add-plugin` on the `productos/` folder, or reload the window for a copy under `~/.cursor/plugins/local/`.

Skills read straight from `productos/skills/` (Cowork, Claude Desktop) need nothing.

Close with a short report: old → new version and the headline change of each release; counts of files added, updated, and removed; every output moved into `docs/` and where it landed; every file kept as the member's own; each conflict and how it was resolved; and the member's next action, which the update doesn't change — the step their plan or open challenge was already on.

## Verify before ending

- [ ] `productos/` matches the latest release everywhere the member hadn't written.
- [ ] Every output an older copy kept inside `productos/` now lives in `docs/` (or stayed put where the member chose).
- [ ] Every other file the member had written is still there — carried into the new structure where they chose, untouched otherwise.
- [ ] The root `CLAUDE.md`/`AGENTS.md` carry the current PRODUCTOS block.
- [ ] A git-cloned `productos/` sits at the new release with only the member's files showing as changes.
- [ ] The temporary clone is gone, and the member knows what changed and what to do next.

Anything less — name the gap and fix it before ending the session.

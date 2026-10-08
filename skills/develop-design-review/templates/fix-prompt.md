# Paste-ready fix prompt template

Goes at the end of the report's Inconsistencies section, wrapped in a triple-backtick code block. Populate every `<offending value>`, `<documented alternative>`, and `[file:line]` with the exact values from the Inconsistency findings — no `<placeholders>` left in the rendered file. Every Inconsistency in the report appears here, sorted by severity. The member should be able to copy the block and paste it without editing.

```
You are working in this repository. I just ran a design system adherence review against `docs/DESIGN.md` on my uncommitted changes. Your job is to fix every Inconsistency listed below — nothing else. Do not reformat unrelated code. Do not touch files that aren't named here. Do not change any value that's already aligned with `docs/DESIGN.md`. Preserve all existing comments.

Work top to bottom (P0 → P3). For each item:
1. Open the listed file.
2. Locate the offending value at the listed line (line numbers may have shifted slightly — use the offending value as the anchor).
3. Replace it with the documented alternative, using the project's token-reference convention (e.g., the framework's theme accessor, CSS variable, or Tailwind class — match the surrounding code).
4. Move to the next item.

Constraints:
- Reference `docs/DESIGN.md` as the source of truth. If a token name has multiple resolution paths in the codebase (e.g., a CSS variable AND a Tailwind class), match the convention used elsewhere in the same file.
- Do not introduce new tokens — that's a separate step (see the Promotion checklist in the review file). If a fix seems to require a new token, leave the value as-is and add `// TODO design-review: needs new token` next to it.
- Do not modify accessibility attributes, ARIA labels, or test IDs.
- Do not change file imports unless a documented token requires importing a new theme module.

Inconsistencies to fix:

P0:
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`). Reason: <one short phrase>.
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`). Reason: <one short phrase>.

P1:
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`).
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`).

P2:
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`).

P3:
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`).

When you're done:
1. Run the project's typecheck and linter. Fix any errors introduced by the changes.
2. Re-run any unit tests that touch the modified files.
3. Report back: which files you changed, which items you couldn't fix and why, and whether tests pass.

Do not commit. The user wants to review the diff before committing.
```

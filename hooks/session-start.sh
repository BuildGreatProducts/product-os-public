#!/bin/sh
# ProductOS session-start greeting (plugin hook). Prints the status script's --greet JSON, which
# the agent reads as context; prints nothing in repos that don't use ProductOS, and never fails.
root="$(cd "$(dirname "$0")/.." && pwd)"
repo="${CLAUDE_PROJECT_DIR:-$PWD}"
py="$(command -v python3)" || exit 0
# On a Mac without the developer tools, /usr/bin/python3 is a stub that pops an install dialog.
if [ "$(uname)" = Darwin ] && [ "$py" = /usr/bin/python3 ] && ! xcode-select -p >/dev/null 2>&1; then
  exit 0
fi
"$py" "$root/scripts/status.py" --greet --repo "$repo" 2>/dev/null
exit 0

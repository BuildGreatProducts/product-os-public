# BONUS - Design Tool Setup

*A bonus asset for ProductOS — practical install and configuration steps for connecting the three AI design tools the Design Prompt Generator skill targets (MagicPath, paper.design, pencil.dev) to the three AI coding clients most ProductOS users work in (Cursor, Claude Code, and the Codex app). Each section is copy-paste-ready. Sources: official MagicPath external-agents docs at magicpath.ai/documentation/features/external-agents, official paper.design docs at paper.design/docs/mcp, official pencil.dev docs at docs.pencil.dev, and the canonical MCP client config references for Cursor, Claude Code, and Codex.*

---

## Why this guide exists

The Design Prompt Generator skill writes paste-ready prompts for AI design tools, but the prompts only generate on-brand screens if your AI coding client can actually *talk to* the design tool. That conversation happens over the open **Agent Skills ecosystem** for MagicPath (the recommended starting point — one prompt installs everywhere), and over **MCP (Model Context Protocol)** for paper.design and pencil.dev. This guide gives you the exact commands and config snippets to set up each of the nine combinations (three tools × three clients).

**If you're new to all three tools, start with MagicPath.** Its install is one prompt you paste into your agent — no per-client commands, no marketplace adds, no local servers to keep running. Pick paper.design or pencil.dev when you specifically want the design surface (`.paper` files, `.pen` files) those tools provide.

Pick the row that matches your setup, follow the snippet, and verify with the test at the end of each section.

---

## Quick reference

| Tool | Cursor | Claude Code | Codex |
| --- | --- | --- | --- |
| **MagicPath** *(recommended start)* | Paste the install prompt into the agent chat (same prompt for every client — see [MagicPath](#magicpath) section below) | Paste the install prompt into the agent chat (same prompt for every client) | Paste the install prompt into the agent chat (same prompt for every client) |
| **paper.design** | `/add-plugin paper-desktop` in agent panel | `/plugin marketplace add paper-design/agent-plugins` then `/plugin install paper-desktop@paper` (or `claude mcp add paper --transport http http://127.0.0.1:29979/mcp --scope user`) | Settings → MCP Servers → add `paper` as Streamable HTTP at `http://127.0.0.1:29979/mcp` |
| **pencil.dev** | Extensions → search "Pencil" → Install | Auto-configured by the Cursor/VS Code extension; verify with `/mcp` | Run Pencil first, then `/mcp` inside Codex to confirm |

---

## MagicPath

MagicPath uses the open **Agent Skills** ecosystem. The official setup — the one MagicPath's own docs walk you through at [magicpath.ai/documentation/features/external-agents](https://www.magicpath.ai/documentation/features/external-agents) — is dramatically simpler than the per-client commands the other tools use: **you paste a single prompt into your AI agent and the agent installs the skill itself.** No marketplace adds, no `codex plugin add`, no per-client commands to memorise. One prompt, every client.

MagicPath lives in the cloud, so the agent can talk to it from anywhere — Claude Code in your terminal, the Claude app on your phone, Codex on a server. **The MagicPath website does not have to be open.** You can be on a walk, on a plane, or away from your computer, and still ask your agent to build a new design or change one you already have; the work shows up on your canvas the next time you open it. (If MagicPath *is* open in your browser, the agent gets a small bonus: it can see which project and design you have selected, so you don't have to copy IDs.)

**Prerequisites:**

1. Sign up for MagicPath at [magicpath.ai](https://magicpath.ai) (the free plan is enough to test setup).
2. Make sure you have Node.js installed (the `npx skills` command the agent will run depends on it).
3. Understand the external-agent limits before you start hammering the install:
   - **Free plan:** 125 external-agent calls per week.
   - **Pro and Teams plans:** unlimited external-agent calls.
   - External-agent calls do **not** consume MagicPath credits — the agent provider (Claude, Codex, Cursor) handles the billing.

### Step 1 — Install the skill (recommended; works for every agent)

Open your AI agent — Claude Code, the Claude app, Codex, or Cursor — and paste this prompt into the chat:

```
Install this skill npx skills add https://github.com/magicpathai/agent-skills --skill magicpath
```

The agent will ask for permission to run the install command. Say yes. After it completes, the agent knows how MagicPath works and can call the skill on demand. **This is the only install command you need across all four agents.**

### Step 2 — Let the agent log you in

After the skill is installed, the agent checks if MagicPath is set up and if you are logged in.

1. The agent checks if MagicPath is set up and whether you're authenticated.
2. If you aren't, it opens the MagicPath login page in your browser.
3. You click "yes" to log in with your MagicPath account.
4. The agent confirms the login worked and finds your projects.
5. If MagicPath is open in your browser, the agent can also see which project and design you have selected — a shortcut that saves you from copying IDs or pasting links.

### How the skill works (bidirectional)

The skill closes the loop between your code and your designs. The agent moves work in both directions:

- **From your agent to MagicPath:** the agent reads your code, tickets, and notes, then **builds new designs or updates existing ones on your MagicPath canvas.** It can make many designs in one go, add them to an existing project, or start a brand-new project from scratch.
- **From MagicPath to your agent:** the agent can take a design you already have in MagicPath and **wire it into your code.** No more rebuilding the design by hand.

### → Claude Code (terminal)

Open Claude Code in the folder with your code. Paste the install line from Step 1. Ask Claude Code to install the MagicPath skill. That's it.

**Example request once installed:**

```
Using the magicpath skill, use the images in this folder and build a landing page in the opened project for my coffee shop.
```

### → Claude Code in the Claude app

Open the Claude app on your computer. Open Claude Code on the folder you want to use. Paste the install line. Ask Claude to install the MagicPath skill. Claude will ask if it can run the command — say yes. Then Claude helps you log in to MagicPath and starts sending designs to your canvas.

**Example request once installed:**

```
Using the MagicPath skill, read the product brief I attached and create a pricing page in my open MagicPath project.
```

### → Codex app

Open the Codex app on the folder that has your project. Paste the install line. Ask Codex to install the MagicPath skill. After that, Codex can read your code, use your other connected apps, and build or change MagicPath designs.

**Example request once installed:**

```
Using the MagicPath skill, read this repo and the Linear ticket I mentioned, then design the onboarding flow in my open MagicPath project.
```

### → Cursor

Open Cursor in your project. Paste the install line into the chat. Ask Cursor to install the MagicPath skill. After that, Cursor can use your code and any tools you have set up to build designs in MagicPath.

**Example request once installed:**

```
Using the MagicPath skill, use this codebase and the selected MagicPath design to create matching empty, loading, and error states.
```

### Common workflows

The MagicPath docs call out three patterns that compound the value of having the skill installed:

**Make a new design from your code.** Tell the agent what to read first, then ask it to build the design.

```
Read the onboarding routes, settings components, and the Linear ticket for the new invite flow. Then create the full invite management experience in my open MagicPath project: empty state, invite form, pending invites, accepted members, error states, and mobile layout.
```

The agent reads your code and the ticket, starts a new design, saves the files on your computer, sends them to MagicPath, and waits for it to be ready.

**Change a design you've selected on the canvas.** Click a design on your MagicPath canvas, then ask the agent to update it — no IDs to copy.

```
Use the selected MagicPath design. Read the latest Slack feedback and the Figma MCP reference for the billing modal. Update the selected design with the correct plan names, error states, confirmation state, and visual polish from the Figma file.
```

**Pull info from many places into one design.** External agents shine when your info is scattered.

```
Read the customer emails about failed exports, summarise the core user needs, and create a MagicPath redesign of the export flow with recovery states and success confirmation.
```

```
Use the GitHub issue, current React components, and Figma MCP frame to create a redesigned mobile dashboard in MagicPath.
```

```
Read the Linear epic and our design-system tokens, then create a multi-screen admin approval workflow we can share with the team.
```

**Use a MagicPath design in your code.** This works the other way too. Click a design in MagicPath (or paste the link), then ask the agent to add it to the code it has open.

```
Replace the auth modal in my project with the design I selected in MagicPath.
```

### Troubleshooting MagicPath

- **Skill not appearing after install:** restart the agent / client. Skills are discovered at session start, not mid-conversation.
- **Agent refuses to run `npx skills add`:** approve the command when prompted; the install line is safe and is the official MagicPath-recommended approach.
- **Login loop:** the agent opens the MagicPath login page in your browser. If you don't see it, check your browser's pop-up blocker and re-run the agent's request.
- **Account required:** the skill calls the MagicPath API. Sign in at [magicpath.ai](https://magicpath.ai) first if the login flow stalls.
- **Hit the 125-call/week free-plan limit:** the cap is per calendar week and resets weekly. Upgrade to Pro or Teams for unlimited external-agent calls, or wait for the reset.

---

## paper.design

paper.design ships a local MCP server inside the Paper Desktop app. The server starts automatically when you open a `.paper` file. The server runs on `http://127.0.0.1:29979/mcp` — keep that URL in mind, it appears in every config below.

**Prerequisite:** download and install the Paper Desktop app from [paper.design/downloads](https://paper.design/downloads). Open at least one Paper file before connecting the MCP — the server doesn't start until a document is loaded.

### → Connect to Cursor

The cleanest install is via the Cursor Marketplace plugin:

1. In Cursor, open the agent panel.
2. Run this slash command:

   ```
   /add-plugin paper-desktop
   ```

3. Alternatively, search for "paper" in the [Cursor Marketplace](https://cursor.com/marketplace/paper) and click install.
4. Reload the Cursor window (Cmd/Ctrl+Shift+P → "Reload Window") or toggle the MCP server off and on under **Cursor Settings → Tools & MCP**.

**Verify:** In an agent chat, ask: *"Use the paper MCP to create a red rectangle in my open document."* The agent should ask for permission, then a red rectangle should appear in Paper.

### → Connect to Claude Code

**Plugin (recommended).** Run in your terminal or the Claude Code extension:

```bash
/plugin marketplace add paper-design/agent-plugins
/plugin install paper-desktop@paper
```

**Manual (no plugin marketplace).** A single command registers the HTTP transport at user scope:

```bash
claude mcp add paper --transport http http://127.0.0.1:29979/mcp --scope user
```

**Claude Desktop config edit.** Open Claude Desktop → Settings → Developer → Edit Config, then paste the following as a new top-level key (alongside other config, not nested):

```json
"mcpServers": {
  "paper": {
    "command": "npx",
    "args": ["mcp-remote", "http://127.0.0.1:29979/mcp"]
  }
}
```

Restart Claude Desktop.

**Verify:** Run `/mcp` in Claude Code. You should see `paper` in the connected MCP list.

### → Connect to Codex

**Plugin (recommended).** In your terminal or the Codex CLI:

```bash
codex plugin marketplace add paper-design/agent-plugins
```

Then run `/plugins`, select the `paper-design/agent-plugins` marketplace, and install `paper-desktop`.

**Manual.** In the Codex app, navigate to **Settings → MCP Servers**, click **Add custom MCP server**, then:

- Select the **Streamable HTTP** tab.
- **Name:** `paper`
- **URL:** `http://127.0.0.1:29979/mcp`
- Click **Save**.

**Verify:** Run `/mcp` in Codex. `paper` should appear in the list as connected.

### Troubleshooting paper.design

- **MCP shows as connected but the agent says it has no access:** restart the host (Cursor / Claude / Codex). The agent caches the MCP tool list at session start.
- **Cannot reach `127.0.0.1:29979` on Windows WSL:** enable [mirrored mode networking](https://learn.microsoft.com/en-us/windows/wsl/networking#mirrored-mode-networking) in WSL settings, then restart WSL.
- **Long-running agent session degraded:** restart the agent session. paper.design's docs explicitly call this out as the most common cause of MCP issues.

---

## pencil.dev (Pencil)

Pencil is a VS Code / Cursor extension that bundles its own local MCP server. The server starts automatically the first time you open a `.pen` file — there is no separate MCP install. The trade-off: Pencil's AI features require Claude Code CLI to be authenticated, so you need `claude` working in your terminal even if your primary client is Cursor or Codex.

**Prerequisites:**

1. Install Claude Code CLI and authenticate (`claude` command, follow the browser flow).
2. Install Pencil from the marketplace (instructions below).
3. Create a `.pen` file in your project so Pencil knows where to attach.

### → Connect to Cursor

1. Open Cursor.
2. Open the Extensions panel.
3. Search for **Pencil** and click **Install**.
4. Create a file called `design.pen` in your project root.
5. Open the `design.pen` file. The Pencil icon should appear in the top-right corner of the editor.
6. Complete the activation (Pencil emails an activation code to the email you sign in with).

**Verify:** Open Cursor Settings → **Tools & MCP**. You should see Pencil in the MCP server list. In Cursor's agent chat, ask: *"Use the pencil MCP to create a small hero section in design.pen."*

### → Connect to Claude Code

Pencil's MCP server is set up automatically by the IDE extension. No separate `claude mcp add` command is required — the extension registers the server when it starts.

To verify:

```bash
claude /mcp
```

You should see `pencil` (or `open-pencil`) listed as connected.

**Auto-approve Pencil tools (optional).** By default, Claude Code asks for permission on every tool call. To auto-approve Pencil's tools only (narrower than `bypassPermissions`), add this to `~/.claude/settings.json`:

```json
{
  "permissions": {
    "allow": ["mcp__open-pencil__*"]
  }
}
```

(The exact tool prefix depends on the Pencil version — check the output of `/mcp` to see the actual prefix.)

### → Connect to Codex

The Pencil extension is built for VS Code and Cursor. To use Pencil from Codex:

1. Run Pencil (open the desktop app or a `.pen` file in your IDE) so the MCP server is running.
2. In Codex, run `/mcp` — Pencil should appear in the list automatically.

If Pencil doesn't appear:

- Check that the `.pen` file is open and the Pencil icon is visible.
- Restart Codex.
- See pencil.dev's docs note about Codex modifying `config.toml` — back up your Codex `config.toml` before first use.

### Troubleshooting pencil.dev

- **"Claude Code isn't connected / not logged in":** run `claude` in your terminal, complete the browser auth flow, return to Pencil, retry.
- **"Invalid API key" / "Please run /login":** check for conflicting auth — remove any `ANTHROPIC_API_KEY` environment variable if you're using the CLI, clear custom provider configs.
- **Extension installed but doesn't connect:** verify Claude Code is logged in, complete Pencil activation (check spam for the activation email), restart your IDE.
- **MCP server not visible:** the server only runs when Pencil is active. Open a `.pen` file first.

---

## Verifying any of the three connections

Once any tool is installed in any client, run this single-sentence sanity check in the client's agent chat — replace the bracketed tool name with whichever you set up:

> *"Use the [paper / pencil / magicpath] MCP to create a small empty hero section on the current canvas, and tell me what tools you used."*

A successful connection produces:

1. The agent asks for permission to call the design tool's tools.
2. After you approve, the design tool's canvas updates (a hero section appears).
3. The agent's response lists the specific tool calls it made (e.g., `paper.create_artboard`, `pencil.create_shape`, `magicpath.design_screen`).

If any of those three steps fail, see the troubleshooting subsection for that specific tool above. The most common single fix across all three tools is "restart the host" (Cursor / Claude Code / Codex). MCP and Agent Skills connections are cached per session — the agent doesn't re-poll for new tools mid-conversation.

---

## What to do after setup

Once you've got at least one design tool connected to at least one AI coding client, run the **`studio-design-prompt-generator`** skill to produce `productos/design/Design-Prompts.md`. That file contains three paste-ready prompts — one per priority screen for your product — that you can paste directly into the design tool you just connected. The prompts have your brand identity context (brand character, tone, type pairing, colour palette, what-to-avoid) embedded inside them, so the generated screens are on-brand from the first generation.

If you want to test the connection *before* running the prompt generator, paste any of the screens from your existing `productos/design/Design-Prompts.md` (if you've already run the generator) into the design tool's chat panel — or just write a quick freeform prompt like *"design a sign-up screen for a calorie tracking app, with a clean editorial aesthetic — Newsreader for headlines, Public Sans for body, warm cream background, deep ink text, terracotta accent."*

---

## Sources

- **paper.design MCP docs:** [paper.design/docs/mcp](https://paper.design/docs/mcp) — official setup instructions for Cursor, Claude Code (CLI + Desktop), Codex, Copilot, Antigravity, OpenCode.
- **pencil.dev installation:** [docs.pencil.dev/getting-started/installation](https://docs.pencil.dev/getting-started/installation) — VS Code, Cursor, desktop app, MCP server auto-setup.
- **pencil.dev troubleshooting:** [docs.pencil.dev/troubleshooting](https://docs.pencil.dev/troubleshooting) — auth issues, IDE-specific issues, MCP & AI integration.
- **OpenPencil MCP reference** (sibling open-source project with detailed MCP tool list): [openpencil.dev/programmable/mcp-server](https://openpencil.dev/programmable/mcp-server).
- **MagicPath Agent Skills (canonical repo):** [github.com/MagicPathAI/agent-skills](https://github.com/MagicPathAI/agent-skills) — official install commands for Claude Code, Codex, Cursor, and the Agent Skills CLI; the source of truth for every MagicPath install in this guide.
- **MagicPath external agents documentation:** [magicpath.ai/documentation/features/external-agents](https://www.magicpath.ai/documentation/features/external-agents) — 125-calls-per-week free-plan limit, unlimited on Pro/Teams, external-agent calls don't consume MagicPath credits.
- **MagicPath documentation home:** [magicpath.ai/documentation](https://www.magicpath.ai/documentation).
- **Claude Code MCP CLI reference:** [docs.claude.com/en/docs/claude-code/mcp](https://docs.claude.com/en/docs/claude-code/mcp).
- **Cursor MCP reference:** [docs.cursor.com/context/mcp](https://docs.cursor.com/context/mcp).
- **Codex MCP reference:** [openai.com/codex/get-started](https://openai.com/codex/get-started).

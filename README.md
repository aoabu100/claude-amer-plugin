# Claude - Amer (Plugin)

Two plugins:

| Plugin | What it does | Try |
|---|---|---|
| mindmap-planner | Goal → Mermaid mindmap + interactive HTML mindmap you can open in a browser | `/mindmap-planner:mindmap launch a newsletter` |
| agent-company | Five agents (planner, researcher, writer, developer, reviewer) with preloaded skills | `/agent-company:plan build a landing page` |

## Install (share these two lines)
```
/plugin marketplace add <your-github-user>/claude-amer-plugin
/plugin install mindmap-planner@claude-amer
/plugin install agent-company@claude-amer
```

## Try locally without installing
```
claude --plugin-dir ./plugins/mindmap-planner --plugin-dir ./plugins/agent-company
```

## Layout
```
.claude-plugin/marketplace.json
plugins/
  mindmap-planner/   .claude-plugin/plugin.json  skills/  commands/  scripts/
  agent-company/     .claude-plugin/plugin.json  agents/  skills/    commands/
```
Private repo. Replace `<your-github-user>` above with your GitHub username.

## Companion tools (install separately, once)
The agent-company plugin ships a `tool-routing` skill and an `.mcp.json` that expect these. Each is optional; agents skip what's missing.

| Tool | What it adds | Install |
|---|---|---|
| [Agent Skills](https://github.com/addyosmani/agent-skills) | 25 engineering workflow skills (`/spec` `/plan` `/build` `/test` `/review` `/ship`) | `/plugin marketplace add addyosmani/agent-skills` then `/plugin install agent-skills@addy-agent-skills` |
| [Context7](https://github.com/upstash/context7) | Up-to-date library docs in context | Already in `plugins/agent-company/.mcp.json` (runs via `npx`) |
| [Graphify](https://github.com/Graphify-Labs/graphify) | Codebase → knowledge graph + interactive `graph.html` | `uv tool install graphifyy && graphify install`, then `/graphify .` |
| [21st Magic MCP](https://21st.dev/mcp) | UI components from a prompt (`/ui ...`) | In `.mcp.json`; set `MAGIC_API_KEY` from 21st.dev |
| [Strix](https://github.com/usestrix/strix) | AI pentesting agents (needs Docker) | `pipx install strix-agent`, then `strix --target <your app>` — only on systems you own |

## vendor/ — companion repos as submodules
Pulled from their own GitHub repos; run `git submodule update --init --depth 1` after cloning to fetch them.

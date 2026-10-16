---
name: mindmap-planner
description: Turn a goal or plan into a mindmap (goal at center, phases as branches, tasks as leaves, owner in brackets) and render it as an interactive HTML page. Use when asked for a mindmap, visual plan, or overview of a project.
---
# Mindmap planner

Produce two things for every plan.

## 1. Markdown outline (source of truth)
Save to `plans/<goal-slug>.md`:

```markdown
# Goal in 2–5 words
## Phase 1 name
- Task [owner]
- Task [owner]
## Phase 2 name
- Task [owner]
## Review
- Final check [reviewer]
```

Rules: 3–6 phases, max 3 levels deep, every task ends in `[owner]`. Below the outline add a `mermaid` block with the same content in `mindmap` syntax, then the critical path as one line: A → B → C.

## 2. Interactive HTML mindmap
Run the bundled renderer:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/render_mindmap.py plans/<goal-slug>.md
```

It writes `plans/<goal-slug>.html` (self-contained, uses Markmap from a CDN). Tell the user to open it in a browser: nodes are collapsible and zoomable. Offer to regenerate it after any edit to the `.md`.

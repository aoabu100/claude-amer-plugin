---
name: mindmap-planner
description: Turn a goal or plan into a Mermaid mindmap (goal at center, phases as branches, tasks as leaves, owner in brackets). Use when asked for a mindmap, visual plan, or overview of a project.
---
# Mindmap planner

Produce a Mermaid `mindmap` block:

```mermaid
mindmap
  root((Goal))
    Phase 1 name
      Task [owner]
      Task [owner]
    Phase 2 name
      Task [owner]
    Review
      Final check [reviewer]
```

Rules:
- Root = the goal in 2–5 words.
- Branches = phases (3–6). Leaves = tasks, each ending in `[owner]`.
- Max 3 levels deep; if deeper is needed, split into a second mindmap.
- Save to `plans/<goal-slug>.md` if a `plans/` folder exists; otherwise print it.
- After the diagram, list the critical path as a one-line arrow chain: A → B → C.

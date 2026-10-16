---
name: task-planning
description: Break a goal into an ordered task list with owner, input, output and done-when criteria. Use when planning any multi-step piece of work or when asked for a plan, roadmap, or breakdown.
---
# Task planning

Output a table with one row per task:

| # | Task | Owner | Input | Output | Done when |
|---|------|-------|-------|--------|-----------|

Rules:
- 3–9 tasks. If more, group into phases.
- Each task has exactly one owner (researcher, writer, developer, reviewer).
- "Done when" must be checkable (a file exists, a test passes, a question is answered).
- Order tasks by dependency. Note parallel tasks with "(parallel)".
- Last task is always a reviewer check.
- Finish with: risks (max 3) and the first question to ask the user, if any.

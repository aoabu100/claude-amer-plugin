---
name: code-review
description: Checklist for reviewing or self-checking code changes. Use after writing code and when reviewing someone else's.
---
# Code review checklist

1. Does it meet the task's done-when criteria? (If not, stop here.)
2. Correctness: edge cases, error handling, no silent failures.
3. Safety: no secrets in code, no destructive commands without confirmation.
4. Simplicity: smallest change that works; no unrelated edits.
5. Tests: exist, run, and cover the change.
6. Readability: names say what things are; comments explain *why*, not *what*.

Report format: verdict (APPROVED / NITS / NEEDS CHANGES) + numbered issues with file:line.

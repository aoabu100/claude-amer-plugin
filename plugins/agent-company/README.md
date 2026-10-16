# AI Agent Company — shareable Claude Code pack

A small "company" of Claude Code subagents, each with preloaded skills, plus a mindmap planner.
Drop the `.claude/` folder (and `CLAUDE.md`) into any repo, or share this whole folder.

## How to use
1. Copy `.claude/` and `CLAUDE.md` into your project root.
2. Run `claude` in that folder (restart Claude Code if it was already open — skills load at startup).
3. Type `/agents` to see the team, or just ask: *"Use the planner to break this project down."*
4. Type `/mindmap-planner` to generate a Mermaid mindmap plan for any goal.

## The team
| Agent | Role | Preloaded skills |
|---|---|---|
| planner | Project manager: breaks goals into tasks, assigns owners | task-planning, mindmap-planner |
| researcher | Analyst: gathers facts, sources, options | research-brief |
| writer | Content lead: drafts docs, emails, posts | writing-style |
| developer | Engineer: builds and tests code | code-review |
| reviewer | QA / editor: checks everyone's output before delivery | code-review, writing-style |

Every agent writes a short handoff note (skill: `handoff-notes`) so the next agent can pick up without context loss.

## Structure
```
CLAUDE.md                      # always-on team rules
.claude/agents/*.md            # one file per agent (subagent)
.claude/skills/<name>/SKILL.md # one folder per skill
```

Docs: https://docs.claude.com/en/docs/claude-code/overview

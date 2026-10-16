# mindmap-planner

Goal in → `plans/<goal>.md` (outline + Mermaid) and `plans/<goal>.html` (interactive Markmap) out.

- Skill: auto-triggers on "mindmap", "visual plan", "overview of the project".
- Command: `/mindmap-planner:mindmap <goal>`
- Script: `scripts/render_mindmap.py` turns the outline into a self-contained HTML mindmap. Needs only Python 3; the page loads Markmap from a CDN when opened.

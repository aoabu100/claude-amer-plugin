#!/usr/bin/env python3
"""Render a Markdown outline (headings + bullets) as an interactive Markmap HTML file."""
import html, json, sys, pathlib

if len(sys.argv) < 2:
    sys.exit("usage: render_mindmap.py plans/<goal>.md")
src = pathlib.Path(sys.argv[1])
text = src.read_text(encoding="utf-8")
# keep only the outline part (drop fenced code blocks such as the mermaid copy)
lines, skip = [], False
for ln in text.splitlines():
    if ln.strip().startswith("```"):
        skip = not skip
        continue
    if not skip:
        lines.append(ln)
outline = "\n".join(lines).strip()
title = next((l.lstrip("# ").strip() for l in lines if l.startswith("# ")), src.stem)

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — mindmap</title>
<style>
  html,body{{margin:0;height:100%;font-family:system-ui,sans-serif;background:#fff;color:#111}}
  @media (prefers-color-scheme:dark){{html,body{{background:#111;color:#eee}}}}
  svg#mm{{width:100%;height:100vh}}
  header{{position:fixed;top:8px;left:12px;font-size:14px;opacity:.7}}
</style></head><body>
<header>{html.escape(title)} · scroll to zoom, click a node to collapse</header>
<svg id="mm"></svg>
<script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/markmap-lib@0.17.2/dist/browser/index.js"></script>
<script src="https://cdn.jsdelivr.net/npm/markmap-view@0.17.2/dist/browser/index.js"></script>
<script>
  const md = {json.dumps(outline)};
  const {{ Transformer }} = window.markmap;
  const {{ Markmap }} = window.markmap;
  const {{ root }} = new Transformer().transform(md);
  Markmap.create('#mm', {{ autoFit: true, duration: 300 }}, root);
</script>
</body></html>"""
out = src.with_suffix(".html")
out.write_text(page, encoding="utf-8")
print(f"wrote {out}")

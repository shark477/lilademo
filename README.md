# Player Journey Explorer (LILA BLACK)

A browser tool for Level Designers to explore where players and bots move, fight, loot and die on the three LILA BLACK maps. Load the match parquet files, pick a map, date and match, then watch the match play back or inspect heatmaps.

*Github Hosted site: https://shark477.github.io/lilademo/

**Live (hosted) link for AI Insights:** https://claude.ai/artifact/9kZsTYSUYBp18gZqzomqF1
The page is private to its owner until shared from the artifact's Share menu.

## Features
- Player journeys on the correct minimap (world to minimap mapping, see `ARCHITECTURE.md`)
- Humans (solid neon green) and bots (dashed pink) drawn differently
- Distinct markers: kills (red circle), deaths (black X), loot (gold diamond), storm deaths (purple triangle)
- Filters: map, date, match, and a single player within a match
- Timeline: play/pause, 1x/5x/20x/60x speed, scrubber; paths and events build up over time
- Heatmaps: kill zones, death zones (including storm), traffic
- Summary panel next to the map (humans, bots, kills, deaths, loot, storm, bot samples)
- Insights report: grid analysis, k-means combat hotspots, rule-based recommendations, optional AI-written insights, four annotated minimap panels, export to PDF or Markdown (`insights.md`) with three evidence-backed insights

## Tech stack
| Part | Choice |
|---|---|
| App | One self-contained `index.html`: plain HTML, CSS and JavaScript (ES modules), no framework, no build step for the app itself |
| Rendering | HTML5 Canvas (2D) |
| Parquet parsing | `hyparquet` 1.17.1 + `hyparquet-compressors` 1.1.1 (pure JS), loaded from jsDelivr |
| PDF export | `jsPDF` 2.5.1 from cdnjs |
| Hosting | Published as a hosted artifact (static page) |
| AI insights | The hosting platform's `sample` capability (Claude); optional, the report works without it |
| Minimaps | Embedded in the page as base64 JPEG (resized to 1024x1024) |

## Repository layout
```
index.html            Built, deployable page (minimaps embedded)
index.template.html   Same page with __AV__/__GR__/__LD__ placeholders for the minimaps
build.py              Rebuilds index.html from the template and the three minimap images
ARCHITECTURE.md       Design, data flow, coordinate mapping, assumptions, tradeoffs
```

## Setup
**Use the hosted page:** open the link above, click **Add folder** (choose the `player_data` folder, or a single day folder) or **Add files**, then pick a map.

**Run locally:**
```bash
cd repo
python3 -m http.server 8000      # any static server works
# open http://localhost:8000/index.html
```
Needs internet access, because `hyparquet` and `jsPDF` load from CDNs. Locally the **Add AI insights** button adds automated rule-based insights (clearly labelled, not an AI model) instead of an AI narrative, and PDF/Markdown export uses the browser's direct download.

**Rebuild `index.html` (only if you change the template or minimaps):**
```bash
pip install pillow
python3 build.py AmbroseValley_Minimap.png GrandRift_Minimap.png Lockdown_Minimap.jpg
```

**Share via a web link (the page runs as soon as the link opens):**
- *claude.ai:* publish `index.html` as an artifact, enable the `downloads` and `sample` capabilities, then use the artifact's Share control. This keeps AI insights and built-in saving.
- *Any static host:* name the file `index.html` and upload it to Netlify Drop (drag and drop), GitHub Pages (Settings, Pages, deploy from branch), Vercel or Cloudflare Pages (no build command, output directory `.`). On these hosts the **Add AI insights** button adds automated rule-based insights instead of an AI narrative, and downloads use the direct-download fallback.
- Visitors still add their own parquet files; no data is bundled in the page.

## Environment variables
None. There is no backend, no API key and no `.env` file. The AI insights call is made by the hosting platform on the viewer's behalf.

## Expected data
Parquet files named `{user_id}_{match_id}.nakama-0` (no `.parquet` extension needed) with columns `user_id, match_id, map_id, x, y, z, ts, event`. Files with other extensions (`.json .md .png .jpg .txt .csv`) are skipped. Dates come from the parent folder name (for example `February_10`); if there is no folder, from the timestamp.

## How to use
1. Add files or a folder. The status line shows files read and any failures.
2. Choose map, date and match. "All matches" shows markers and heatmaps for the whole filter; paths draw only for a single match.
3. Press Play, or drag the scrubber. Use the player dropdown to isolate one human or bot (its ID and the match ID show on the map).
4. Choose a heatmap (kills, deaths, traffic) and toggle layers in the sidebar.
5. Click **Generate insights report** (bottom right of the map area) to see hotspots and recommendations; add AI insights, then **Download PDF** or **Download insights.md**.

## Known limitations
- Timestamps have 1-second resolution (see assumptions in `ARCHITECTURE.md`).
- Built-in file saving and AI insights depend on the hosting view; a direct-download fallback is provided.
- AI Insights are available only if connected to AI platform (Claude in current implementation).

## Troubleshooting
- **"N failed" in the status line:** the message shows the first parse error. Check the file is a genuine parquet file.
- **No bot paths:** select a single match and make sure "Bot paths" is ticked.
- **Download does nothing:** use the "open it in a new tab" link under the buttons, or open the artifact link on claude.ai while signed in.

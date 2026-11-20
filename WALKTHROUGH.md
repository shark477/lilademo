# Walkthrough: how to use the Player Journey Explorer

Live link: https://claude.ai/artifact/9kZsTYSUYBp18gZqzomqF1 (private until shared from the artifact's Share menu).

## 1. Load data
Click **Add folder** and choose `player_data` (or a single day folder), or **Add files** to pick parquet files. The status line under "Data" shows files read, matches found, and the first error if any file fails. Files from the same match are merged automatically.

## 2. Choose what to look at
Use the three dropdowns:
- **Map:** AmbroseValley, GrandRift or Lockdown.
- **Date:** all dates, or one day (taken from the folder name).
- **Match:** "All matches (aggregate)" or one match, labelled with its ID and human/bot counts.

When a match is chosen, a fourth dropdown lists its players. Picking one highlights that journey and dims the rest. The player ID and match ID show in the top-right corner of the map.

## 3. Read the map
- Paths are drawn on the correct minimap using the coordinate mapping described in `ARCHITECTURE.md`.
- **Humans:** solid neon-green lines with a ringed end dot. **Bots:** dashed pink lines with a dark outline.
- **Markers:** kills are red circles, deaths are black X marks, loot is gold diamonds, storm deaths are purple triangles. The legend in the sidebar shows the same symbols; each can be switched on or off.
- Paths draw for a single match. "All matches" shows markers and heatmaps only.

## 4. Play back a match
Pick a match, then press **Play**. Choose 1x, 5x, 20x or 60x speed, or drag the scrubber to any moment. Paths, dots and markers build up as time advances, and the time readout (m:ss) shows how far in you are. After picking a match the scrubber starts at the end, so you see the whole journey first; press Play to replay it from the start.

## 5. Heatmaps
Under "Heatmap", choose **Kill zones**, **Death zones** (includes storm deaths) or **Traffic**. The heat follows the filters, the selected player, and the playback time, so you can watch hot spots form.

## 6. Summary panel
Beside the map, tiles show matches, humans, bots, loot, kills, deaths, storm deaths and bot path samples. They update with the filters, player and playback time.

## 7. Insights report
Click **Generate insights report** (bottom right of the map area):
- Four annotated minimaps: combat hotspots, traffic with under-used cells, loot, and storm deaths, on an A-H by 1-8 grid.
- Key numbers, where things happen, and rule-based recommendations.
- **Add AI insights** asks Claude to write a narrative from the numbers (inside claude.ai). Where AI is not available, it adds clearly labelled automated insights written by rules (grouped as level design, player experience, targeting and monetization) instead.
- **Download PDF** saves the report with the map panels. **Download insights.md** saves a Markdown file with three evidence-backed insights, each with what stands out, the evidence, metrics and actions, and why a level designer should care.

If the host blocks saving, a message and an "open it in a new tab" link appear under the buttons.

## 8. Share it
Share the artifact link from claude.ai, or host `index.html` on any static host (see `README.md`).

## Suggested first tour (with the sample files)
1. Load the sample files and choose AmbroseValley with Traffic selected.
2. Switch the heatmap to Kill zones and look for the busiest cell.
3. Choose one match, press Play, and watch the path and markers build.
4. Open the insights report and download the PDF and `insights.md`.

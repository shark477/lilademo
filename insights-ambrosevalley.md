# LILA BLACK - Player behaviour insights

Map: AmbroseValley | Scope: all dates | Matches: 566 | Players: 217 humans, 51 bots

Generated 2026-11-20. Method: 8x8 grid analysis, k-means hotspot clustering, rule-based heuristics.

## Three things we learned from the data

### 1. Parts of the map are rarely visited

- **What caught the eye in the data:** 6 of 40 visited cells have under 10% of the median traffic (e.g. A2 (north-west), A3 (north-west), A8 (south-west), B8 (south-west), D8 (south), E8 (south)).
- **Evidence:** The median visited cell has 961 position samples; the cells listed have under 96. That is 15% of visited cells.
- **Actionable:** Yes
  - **Metrics affected:** Map coverage (share of cells in regular use); Loot pickups in these cells; Combat events in these cells
  - **Action items:**
    1. Add loot, an objective or a safer route into these cells
    2. Check whether terrain, walls or the storm path block access
    3. Re-measure coverage after the change
- **Why a level designer should care:** Unused space costs build effort without giving players anything; coverage is the clearest sign a zone is not pulling its weight.

### 2. Most fights are against bots

- **What caught the eye in the data:** 100% of fights involve bots.
- **Evidence:** Kill 2, Killed 2, BotKill 1664, BotKilled 297.
- **Actionable:** Yes
  - **Metrics affected:** Share of fights against bots; Human-vs-human encounters per match; Deaths per match
  - **Action items:**
    1. Check whether bots fill the zones humans would otherwise meet in
    2. Test lower bot fill or placing bots away from main routes
- **Why a level designer should care:** Where bots patrol shapes the fights a map produces, so bot routes are part of level design.

### 3. Combat concentrates around C4 (west)

- **What caught the eye in the data:** About 34% of human combat events cluster around C4 (west); the busiest single cell is E5 (centre) with 265 events.
- **Evidence:** k-means (k=4) on 1982 combat events gives clusters C4 (west) 34%; D5 (centre) 32%; D7 (south) 18%; D3 (north) 16%. The three busiest cells hold 39% of all combat.
- **Actionable:** Yes
  - **Metrics affected:** Share of combat in the top hotspot; Combat events per cell; Median time to first combat; Deaths per match
  - **Action items:**
    1. Review sightlines, cover and approach routes in and around C4 (west)
    2. Playtest moving cover or loot to pull fights toward D5 (centre), D7 (south), D3 (north)
    3. Re-run this report after the change and compare the hotspot share
- **Why a level designer should care:** Designers decide where the map invites fights. One dominant zone can leave other areas unused and give players the same predictable fight every match.

## Key numbers (human players only)

- Human kills of humans 2, killed by humans 2, bot kills 1664, killed by bots 297, storm deaths 17, loot pickups 9844
- Median match length 362 s; median time to first combat 131 s; median time of death 285 s
- Deaths in first 60 s: 1%; storm share of deaths: 5%
- Combat by match third (early/mid/late): 19% / 34% / 47%
- Avg distance per human journey: 885 world units; journeys with no loot: 5%

## Where things happen

- Combat hotspots (k-means): C4 (west) 34%; D5 (centre) 32%; D7 (south) 18%; D3 (north) 16%
- Busiest combat cells: E5 (centre) 265; D5 (centre) 256; D4 (centre) 250
- Most travelled cells: E5 (centre) 4077; D7 (south) 3646; C4 (west) 3326
- Top loot cells: E5 (centre) 1396; D7 (south) 836; C5 (west) 739
- Storm death cells: D6 (south) 3; D3 (north) 2; D4 (centre) 2
- Under-used areas: 6 of 40 visited cells get under 10% of median traffic (e.g. A2 (north-west), A3 (north-west), A8 (south-west), B8 (south-west), D8 (south), E8 (south))

## Heuristic recommendations (validate with A/B tests)

- **Level design:** Combat is spread across several clusters (largest C4 (west), 34%), a healthy sign for map use. Compare these clusters to intended points of interest.
- **Level design:** About 15% of visited cells are rarely crossed. Add loot, objectives or extraction routes there, or shorten paths to them.
- **Targeting:** 100% of fights are against bots, so human-vs-human contact is rare here. Test lower bot fill, or matchmaking that keeps humans closer together.
- **Monetization:** Loot concentrates near E5 (centre). Consider that region for cosmetic or limited-time item showcases, and measure whether it raises traffic or deaths.
- **Targeting:** Segment humans by early death, no loot and short journeys; these are the first-session players to target with tutorials, easier lobbies or comeback rewards.

_Annotated minimap panels for these numbers are included in the PDF export._
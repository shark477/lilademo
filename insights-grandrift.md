# LILA BLACK - Player behaviour insights

Map: GrandRift | Scope: all dates | Matches: 59 | Players: 29 humans, 30 bots

Generated 2026-11-20. Method: 8x8 grid analysis, k-means hotspot clustering, rule-based heuristics.

## Three things we learned from the data

### 1. Parts of the map are rarely visited

- **What caught the eye in the data:** 5 of 37 visited cells have under 10% of the median traffic (e.g. B2 (north-west), H3 (north-east), B6 (south-west), G6 (south-east), F7 (south-east)).
- **Evidence:** The median visited cell has 113 position samples; the cells listed have under 11. That is 14% of visited cells.
- **Actionable:** Yes
  - **Metrics affected:** Map coverage (share of cells in regular use); Loot pickups in these cells; Combat events in these cells
  - **Action items:**
    1. Add loot, an objective or a safer route into these cells
    2. Check whether terrain, walls or the storm path block access
    3. Re-measure coverage after the change
- **Why a level designer should care:** Unused space costs build effort without giving players anything; coverage is the clearest sign a zone is not pulling its weight.

### 2. Most fights are against bots

- **What caught the eye in the data:** 99% of fights involve bots.
- **Evidence:** Kill 1, Killed 1, BotKill 179, BotKilled 24.
- **Actionable:** Yes
  - **Metrics affected:** Share of fights against bots; Human-vs-human encounters per match; Deaths per match
  - **Action items:**
    1. Check whether bots fill the zones humans would otherwise meet in
    2. Test lower bot fill or placing bots away from main routes
- **Why a level designer should care:** Where bots patrol shapes the fights a map produces, so bot routes are part of level design.

### 3. The storm is a real cause of death

- **What caught the eye in the data:** 17% of deaths (5 of 30) come from the storm.
- **Evidence:** Most storm deaths are in C3 (north-west) 1; E3 (north) 1; E5 (centre) 1.
- **Actionable:** Yes
  - **Metrics affected:** Storm deaths per match; Share of deaths from the storm; Extraction rate
  - **Action items:**
    1. Check exit routes from the storm-death cells for chokepoints or dead ends
    2. Improve visual cues and warning time for the storm edge
    3. Re-measure storm share after route changes
- **Why a level designer should care:** Storm deaths often mean players got trapped by geometry, not that they played badly. That is a layout problem designers can fix.

## Key numbers (human players only)

- Human kills of humans 1, killed by humans 1, bot kills 179, killed by bots 24, storm deaths 5, loot pickups 876
- Median match length 422 s; median time to first combat 147 s; median time of death 270 s
- Deaths in first 60 s: 3%; storm share of deaths: 17%
- Combat by match third (early/mid/late): 21% / 39% / 40%
- Avg distance per human journey: 899 world units; journeys with no loot: 7%

## Where things happen

- Combat hotspots (k-means): D5 (centre) 39%; D3 (north) 33%; G5 (east) 15%; B4 (west) 12%
- Busiest combat cells: D5 (centre) 48; D4 (centre) 32; G5 (east) 18
- Most travelled cells: D5 (centre) 703; D4 (centre) 496; G5 (east) 463
- Top loot cells: D5 (centre) 141; C4 (west) 81; D4 (centre) 72
- Storm death cells: C3 (north-west) 1; E3 (north) 1; E5 (centre) 1
- Under-used areas: 5 of 37 visited cells get under 10% of median traffic (e.g. B2 (north-west), H3 (north-east), B6 (south-west), G6 (south-east), F7 (south-east))

## Heuristic recommendations (validate with A/B tests)

- **Level design:** Combat is concentrated: 39% of events cluster around D5 (centre). Check sightlines, cover and loot density there; consider a second reason to fight elsewhere to spread engagements.
- **Level design:** About 14% of visited cells are rarely crossed. Add loot, objectives or extraction routes there, or shorten paths to them.
- **Player experience:** Storm causes 17% of deaths, mostly near C3 (north-west). Improve storm warnings and route clarity, or check whether slow-to-exit areas trap players.
- **Targeting:** 99% of fights are against bots, so human-vs-human contact is rare here. Test lower bot fill, or matchmaking that keeps humans closer together.
- **Monetization:** Loot concentrates near D5 (centre). Consider that region for cosmetic or limited-time item showcases, and measure whether it raises traffic or deaths.
- **Targeting:** Segment humans by early death, no loot and short journeys; these are the first-session players to target with tutorials, easier lobbies or comeback rewards.

_Annotated minimap panels for these numbers are included in the PDF export._
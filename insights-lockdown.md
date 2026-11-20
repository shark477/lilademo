# LILA BLACK - Player behaviour insights

Map: Lockdown | Scope: all dates | Matches: 171 | Players: 79 humans, 41 bots

Generated 2026-11-20. Method: 8x8 grid analysis, k-means hotspot clustering, rule-based heuristics.

## Three things we learned from the data

### 1. Parts of the map are rarely visited

- **What caught the eye in the data:** 4 of 29 visited cells have under 10% of the median traffic (e.g. D2 (north), G3 (north-east), A5 (west), F6 (south-east)).
- **Evidence:** The median visited cell has 609 position samples; the cells listed have under 61. That is 14% of visited cells.
- **Actionable:** Yes
  - **Metrics affected:** Map coverage (share of cells in regular use); Loot pickups in these cells; Combat events in these cells
  - **Action items:**
    1. Add loot, an objective or a safer route into these cells
    2. Check whether terrain, walls or the storm path block access
    3. Re-measure coverage after the change
- **Why a level designer should care:** Unused space costs build effort without giving players anything; coverage is the clearest sign a zone is not pulling its weight.

### 2. Most fights are against bots

- **What caught the eye in the data:** 100% of fights involve bots.
- **Evidence:** Kill 0, Killed 0, BotKill 389, BotKilled 82.
- **Actionable:** Yes
  - **Metrics affected:** Share of fights against bots; Human-vs-human encounters per match; Deaths per match
  - **Action items:**
    1. Check whether bots fill the zones humans would otherwise meet in
    2. Test lower bot fill or placing bots away from main routes
- **Why a level designer should care:** Where bots patrol shapes the fights a map produces, so bot routes are part of level design.

### 3. Combat concentrates around F4 (east)

- **What caught the eye in the data:** About 40% of human combat events cluster around F4 (east); the busiest single cell is E4 (centre) with 66 events.
- **Evidence:** k-means (k=4) on 488 combat events gives clusters F4 (east) 40%; C5 (west) 22%; C4 (west) 22%; E3 (north) 16%. The three busiest cells hold 35% of all combat.
- **Actionable:** Yes
  - **Metrics affected:** Share of combat in the top hotspot; Combat events per cell; Median time to first combat; Deaths per match
  - **Action items:**
    1. Review sightlines, cover and approach routes in and around F4 (east)
    2. Playtest moving cover or loot to pull fights toward C5 (west), C4 (west), E3 (north)
    3. Re-run this report after the change and compare the hotspot share
- **Why a level designer should care:** Designers decide where the map invites fights. One dominant zone can leave other areas unused and give players the same predictable fight every match.

## Key numbers (human players only)

- Human kills of humans 0, killed by humans 0, bot kills 389, killed by bots 82, storm deaths 17, loot pickups 2050
- Median match length 448 s; median time to first combat 133 s; median time of death 296 s
- Deaths in first 60 s: 8%; storm share of deaths: 17%
- Combat by match third (early/mid/late): 22% / 31% / 48%
- Avg distance per human journey: 924 world units; journeys with no loot: 16%

## Where things happen

- Combat hotspots (k-means): F4 (east) 40%; C5 (west) 22%; C4 (west) 22%; E3 (north) 16%
- Busiest combat cells: E4 (centre) 66; C5 (west) 52; E5 (centre) 51
- Most travelled cells: C5 (west) 1794; F4 (east) 1574; E3 (north) 1446
- Top loot cells: E3 (north) 245; D3 (north) 161; E4 (centre) 159
- Storm death cells: F4 (east) 3; E3 (north) 2; E4 (centre) 2
- Under-used areas: 4 of 29 visited cells get under 10% of median traffic (e.g. D2 (north), G3 (north-east), A5 (west), F6 (south-east))

## Heuristic recommendations (validate with A/B tests)

- **Level design:** Combat is concentrated: 40% of events cluster around F4 (east). Check sightlines, cover and loot density there; consider a second reason to fight elsewhere to spread engagements.
- **Level design:** About 14% of visited cells are rarely crossed. Add loot, objectives or extraction routes there, or shorten paths to them.
- **Player experience:** Storm causes 17% of deaths, mostly near F4 (east). Improve storm warnings and route clarity, or check whether slow-to-exit areas trap players.
- **Targeting:** 100% of fights are against bots, so human-vs-human contact is rare here. Test lower bot fill, or matchmaking that keeps humans closer together.
- **Monetization:** Loot concentrates near E3 (north). Consider that region for cosmetic or limited-time item showcases, and measure whether it raises traffic or deaths.
- **Targeting:** Segment humans by early death, no loot and short journeys; these are the first-session players to target with tutorials, easier lobbies or comeback rewards.

_Annotated minimap panels for these numbers are included in the PDF export._
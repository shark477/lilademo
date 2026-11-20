# Architecture

## What it is built with, and why
| Layer | Choice | Why |
|---|---|---|
| App | One static `index.html`, vanilla JS | Nothing to install; hosts and shares as a single link |
| Parquet | `hyparquet` (pure JS) in the browser | Designers upload files directly, no server. WASM readers were rejected: the hosted page cannot fetch `.wasm` |
| Drawing | Canvas 2D | Smooth redraw of tens of thousands of points per playback frame |
| Insights | 8x8 grid + k-means + scored rules; optional Claude narrative | Numbers are deterministic; AI only writes them up |
| Export | `jsPDF` (PDF with map panels), Markdown (`insights.md`) | Built client-side, no server |

## Data flow
```
parquet files (one per player per match)
 -> hyparquet rows {user_id, match_id, map_id, x, y, z, ts, event}
 -> normalise: event bytes -> string, map_id -> map, bot = numeric user_id
 -> project x,z to minimap pixels; classify event (pos/kill/death/loot/storm)
 -> group by match_id; ts made relative to match start; paths per player
 -> filters (map/date/match/player) select rows; playback time T keeps rows with t <= T
 -> Canvas: minimap, heatmap, paths, markers, ID label; summary tiles
 -> Insights: same rows -> grid counts + k-means -> scored insights -> PDF / insights.md
```

## Coordinate mapping (game world to minimap)
Per-map constants from the dataset README:

| Map | Scale | Origin X | Origin Z |
|---|---|---|---|
| AmbroseValley | 900 | -370 | -473 |
| GrandRift | 581 | -290 | -290 |
| Lockdown | 1000 | -500 | -500 |

1. Use `x` and `z`; `y` is height and is ignored in 2D.
2. Normalise to 0-1: `u = (x - originX) / scale`, `v = (z - originZ) / scale`.
3. Scale to the 1024x1024 canvas and flip Y (image rows grow downward, world Z grows north): `px = u*1024`, `py = (1 - v)*1024`.
4. Example (AmbroseValley): `x=-301.45, z=-355.55` gives `u=0.0762, v=0.1305`, pixel `(78, 890)`.

Mapping happens in 0-1 space, so it is resolution-independent; the minimaps were resized to 1024x1024 once and every layer shares that pixel space. On the sample files, all positions on all three maps fall inside 0-1 in both axes. That confirms range, not alignment with every landmark.

## Assumptions where the data was ambiguous
| Issue | What I ran into | How I handled it |
|---|---|---|
| `ts` labelled ms; README says "elapsed in match" | Values are ~1.77 billion: 20 days as ms, but 10-14 Feb 2026 as epoch seconds; as seconds, matches last 2-12 min | Read `ts` as seconds, relative to each match's first event. Resolution is 1 s |
| Bot vs human | Only filename and `user_id` | Numeric ID (or `BotPosition`) = bot; UUID = human |
| `BotKill`/`BotKilled` in bot files | Direction unclear | Combat/loot statistics use human files only; bots contribute positions |
| Dates | Not a column | From folder name, else timestamp |
| No `.parquet` extension | Files end `.nakama-0` | Try every file except obvious non-parquet extensions |
| Minimap size | README says 1024x1024 | Assumed square; resized to 1024 |

## Major tradeoffs
| Decision | Considered | Chosen, and why |
|---|---|---|
| Parse in the browser | Backend converting parquet to JSON | Browser: zero infrastructure. Cost: slower load, memory-bound |
| Single HTML file | React/Vite | One deployable, no build. Cost: harder to grow |
| Canvas | SVG, Leaflet, WebGL | Simple and fast enough. Cost: no built-in zoom/pan |
| All rows in memory | Pre-aggregate on load | Exact playback and any filter. Cost: heavy for all five days |
| Grid + k-means + rules | Trained model, LLM only | Transparent, repeatable; LLM only narrates. Cost: no learned patterns |
| 8x8 grid | Finer grid | Readable cell labels (C4); loses detail inside a cell |
| Client-side PDF/Markdown | Server-rendered | No server. Cost: basic PDF typography; depends on host allowing downloads |

**Not yet verified:** performance on all 1,243 files in a real browser, and landmark alignment on every map.

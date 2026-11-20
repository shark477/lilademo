# Player Journey Explorer

Load match parquet files, pick a match, press play.

## Data

No data loaded.

## Filter

## Layers

[x] Human paths [x] Bot paths (dashed) [x] Kills [x] Deaths [x] Loot [x] Storm deaths

## Heatmap

## Assumptions

Bots = numeric user_id (BotPosition/BotKill/BotKilled). Map X/Z used (Y = height); mapping per the dataset README. ts is read as seconds (see note below). ts column is labelled ms but holds epoch seconds, so it is read as seconds (1 s resolution). Time is relative to each match's first event. Date comes from the folder name, else the timestamp.

0:00

**Insights report**

```

```
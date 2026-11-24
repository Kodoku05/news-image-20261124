# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Kodoku05/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Kodoku05/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

The World Today — Tuesday 24 November 2026: a program that sums up the
world news of Tuesday 24 November 2026 as a one-page newspaper front page
(a 1024×1024 PNG). Lead stories: US-brokered Russia–Ukraine talks open in
Abu Dhabi; Iran vows to use "every means" to break the US blockade as 14
tankers mass at Kharg Island; Russia hits Kyiv's power grid again, leaving
more than 500,000 in the dark; and Alcaraz wins his maiden ATP Finals
title. 50 stories across 8 regions and 13 fields, every one dated
24 November 2026.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./out node main.ts
```

Writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`). Node 22,
standard library only — the program just copies the image.

## How the image was made

`draw_poster.py` (Python + Pillow, run locally) draws the front page from
the verified story data embedded in the script: four illustrated leads, a
"Why the Gulf is burning" explainer, a UTC timeline of how the week
unfolded, a 46-story grid with region-colour dots and source tags, a
dotted world map with numbered story pins, and a date-check box listing
the big stories deliberately left out because they belong to earlier
days. The output is deterministic — two runs produce byte-identical PNGs.

## Sources

Reuters, AP, AFP, Al Jazeera, Guardian, UKMTO, BBC and wire pickups,
checked on the morning of 24 November 2026. Every story happened, or was
first reported, on Tuesday 24 November 2026. Illustrations are original
flat-vector drawings, not photographs.

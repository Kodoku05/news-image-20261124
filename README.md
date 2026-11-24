# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Kodoku05/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Kodoku05/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

The World Today — Tuesday 24 November 2026: a program that sums up the
world news of Tuesday 24 November 2026 as a one-page newspaper front page
(a 1024×1024 PNG). Lead stories: the Abu Dhabi talks end without a
breakthrough as US mediators head to Moscow and Dublin; Netanyahu urges
Trump to authorise fresh strikes on Iran; a Russian strike hits
Zaporizhzhia overnight, killing 2 and wounding 22; and the Gukesh–Sindarov
world chess title match opens in Geneva. 50 stories across 8 regions and
12 fields, every lead and grid story verified as a Tuesday 24 November
2026 development. v2 (evening of 24 Nov) replaces the four v1 leads, which
were wrongly dated — Alcaraz's ATP Finals win (22 Nov), the COP31 collapse
(22 Nov), the Kyiv grid barrage (23 Nov) and Iran's "every means" vow
(23 Nov) — and lists them in the poster's DATE CHECK box with their true
dates.

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
checked on the evening of 24 November 2026. Every lead and grid story is
a development first reported on Tuesday 24 November 2026; the "HOW THE
WEEK UNFOLDED" strip is explicitly a recap of 21–24 November, and the
DATE CHECK box lists big stories deliberately left out because they belong
to earlier days. Illustrations are original flat-vector drawings, not
photographs.

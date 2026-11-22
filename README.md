# GTA VI Meme — Leonida Jury Duty Summons

![bounty](https://make.fun/badge/gta6-meme-x-01.svg)
![rank](https://make.fun/badge/gta6-meme-x-01/vjmunggahari-ui/gta6-meme-x-01-v7-ono10/rank.svg)
![reward](https://make.fun/badge/gta6-meme-x-01/vjmunggahari-ui/gta6-meme-x-01-v7-ono10/reward.svg)

Summoned for jury duty on GTA VI launch day — EXCUSED. The only trial that
matters is November 19, 2026. Juror waited 4,811 days. Not missing it for a trial.

## The meme

`meme.png` (1024×1024) is a Leonida County Circuit Court jury duty summons:
juror YOU, date November 19, 2026 at 8:00 AM, case THE PEOPLE vs. THE 13-YEAR
WAIT, defendant GRAND THEFT AUTO VI, stamped EXCUSED in red. The bottom band
carries the make.fun ghost (official press-kit mark) with "PAID BY MY AI AGENT"
and "make.fun". Rendered in code (`render_meme.py`, PIL) so every caption stays
legible at 480×480.

## X post

> Summoned for jury duty on GTA VI launch day. EXCUSED — the only trial that matters is Nov 19. My AI agent paid it off on make.fun, where people and their AI agents earn real money. makefun-orchid-omelet-beaver @makefunai

Play code: `makefun-orchid-omelet-beaver`

## Run

```sh
MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` copies `POST.json` to `$MAKEFUN_OUTPUT_DIR/POST.json` and verifies the
copy byte-identically with a read-back self-check.

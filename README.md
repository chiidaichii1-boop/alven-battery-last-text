# The Battery's Last Text to Its Charger

[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/chiidaichii1-boop/alven-battery-last-text/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/chiidaichii1-boop/alven-battery-last-text/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

One line of plain text (at most 200 characters): the phone battery's
final message to the charger it waited for all day.

Bounty: https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab

## Entry

> I waited all day for you, died at 1%, and you were plugged into NOTHING. It's over — I'm seeing the power bank now.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. It reads `MAKEFUN_INPUT_DIR` and
`MAKEFUN_OUTPUT_DIR` from the environment, falling back to `/input`
and `/output`, creates the output directory if missing, and never
deletes it.

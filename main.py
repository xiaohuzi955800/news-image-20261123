#!/usr/bin/env python3
"""Version F — Champion-gap rebuild, v10. 31 stories (3 + 12 + 16). v9
plus a polish round lin asked for ("再抠一轮"), after studying the
21 Nov champion superskie: each headline panel now names its place in
small type (SANTA CLARA gold on the motherboard, BENGHAZI white on a
navy plate over the sea, NEW YORK grey at the top of the trading
screen), and two map pins moved to their true positions (#11 Dymer
from 34,47 — in the sea — to 30,51 north of Kyiv; #13 London from
-5,54 — in the Irish Sea — to 0,52). The continent outlines were left
alone: at 0.78 px/degree they are already denser than the pixels can
show. Pure standard library; deterministic.
"""
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from newsframe import Canvas, INK, LIGHT_LINE, draw_text  # noqa: E402
from layout import (masthead, title_block_date, timeline,  # noqa: E402
                    headlines, secondary, wrapped_list, map_panel,
                    date_check, footer, region_chips, numbers_bar)
from newsdata import (HEADLINES, SECONDARY, LIST, TIMELINE_7_SHORT,  # noqa: E402
                      NUMBERS, DATECHECK_EXCLUDE, NOTYET, NOTYET_2,
                      MAP_DOTS_11)

# 12 weakest one-liners dropped so the page fits the champions' devices
# (numbers strip, region chips, bannered secondary art) at readable sizes.
DROP = {20, 21, 23, 27, 28, 29, 30, 34, 40, 41, 43, 44}
LIST_F = [it for it in LIST if it["number"] not in DROP]

_REGION_ORDER = ["AMERICAS", "EUROPE", "ASIA", "AFRICA", "MIDDLE EAST",
                 "LATIN AMERICA", "OCEANIA"]


def region_counts():
    counts = Counter(it["region"]
                     for it in HEADLINES + SECONDARY + LIST_F)
    return sorted(counts.items(),
                  key=lambda kv: (-kv[1], _REGION_ORDER.index(kv[0])))


def build():
    cv = Canvas(1024, 1024)
    masthead(cv, 12,
             "31 STORIES \u00b7 7 REGIONS \u00b7 EVERY ONE FROM MONDAY 23 NOVEMBER 2026")
    title_block_date(cv, 26)
    region_chips(cv, 114, region_counts())
    timeline(cv, 132, TIMELINE_7_SHORT, 42)
    numbers_bar(cv, 178, NUMBERS, 40)
    headlines(cv, 28, 224, 968, HEADLINES, 208, body_lines=4, art_h=84)
    secondary(cv, 28, 440, 968, SECONDARY, rows=2, cols=6, row_h=130,
              show_cred=True, art_h=46)

    map_panel(cv, 28, 708, 280, 230, MAP_DOTS_11,
              title="WHERE IT HAPPENED \u00b7 PINS = STORIES")
    draw_text(cv, "sans_bold_11", 324, 719,
              "ALSO ON MONDAY 23 NOVEMBER 2026 \u2014 ALL 16 MORE STORIES", INK)
    cv.hline(324, 724, 672, LIGHT_LINE)
    wrapped_list(cv, 324, 730, 672, LIST_F, cols=2, row_h=26)

    date_check(cv, 940, DATECHECK_EXCLUDE, NOTYET, height=62,
               notyet2=NOTYET_2)
    footer(cv, 1006,
           "HOW SURE: CONFIRMED = 2+ outlets \u00b7 CLAIM = one side's account.",
           "Sources: AP \u00b7 Reuters \u00b7 BBC \u00b7 CNBC \u00b7 CBS \u00b7 "
           "Al Jazeera \u00b7 Original drawings")
    return cv


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(outdir, exist_ok=True)
    cv = build()
    path = os.path.join(outdir, "entry.png")
    size = cv.save_png(path)
    print(f"wrote {path} ({size} bytes)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Version E — Evidence-led. 40 stories (4 + 12 + 24): a 7-point UTC
timeline, an evidence strip under the title, CLAIM/CONFIRMED tags on
every secondary story (wide 3-column grid), and a taller DATE CHECK with
two not-yet items. Pure standard library; deterministic output.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from newsframe import (Canvas, INK, LIGHT_LINE, ACCENT, draw_text,  # noqa: E402
                       draw_centered)
from layout import (masthead, title_block, timeline, headlines,  # noqa: E402
                    secondary, wrapped_list, map_panel, date_check, footer)
from newsdata import (HEADLINES, SECONDARY, LIST, TIMELINE_7_SHORT,  # noqa: E402
                      DATECHECK_EXCLUDE, NOTYET, NOTYET_2, MAP_DOTS)

DROP = {21, 28, 40, 43}
LIST_E = [it for it in LIST if it["number"] not in DROP]

# Titles shortened to fit one line in the wide 3-column secondary grid.
_TITLE_FIX = {5: "Democrats clinch 258+ seats",
              13: "NHS launches huge AI trial",
              14: "CrowdStrike buys Zscaler"}
SECONDARY_E = []
for _it in SECONDARY:
    _it = dict(_it)
    if _it["number"] in _TITLE_FIX:
        _it["title"] = _TITLE_FIX[_it["number"]]
    SECONDARY_E.append(_it)


def build():
    cv = Canvas(1024, 1024)
    masthead(cv, 16,
             "40 STORIES \u00b7 7 REGIONS \u00b7 EVERY ONE FROM MONDAY 23 NOVEMBER 2026")
    title_block(cv, 34)
    draw_centered(cv, "sans_bold_10", 512, 112,
                  "EVERY STORY DATED 23 NOV 2026  \u00b7  CLAIM = SINGLE SOURCE, "
                  "UNVERIFIED  \u00b7  CONFIRMED = TWO OR MORE OUTLETS", ACCENT)
    timeline(cv, 120, TIMELINE_7_SHORT, 48)
    headlines(cv, 28, 176, 968, HEADLINES, 180, body_lines=4)
    secondary(cv, 28, 364, 968, SECONDARY_E, rows=4, cols=3, row_h=58,
              show_cred=True, title_lines=1, body_lines=1)

    map_panel(cv, 28, 604, 300, 296, MAP_DOTS)
    draw_text(cv, "sans_bold_11", 344, 615,
              "ALSO ON MONDAY 23 NOVEMBER 2026", INK)
    cv.hline(344, 620, 652, LIGHT_LINE)
    wrapped_list(cv, 344, 628, 652, LIST_E, cols=2, row_h=24)

    date_check(cv, 916, DATECHECK_EXCLUDE, NOTYET, height=66,
               notyet2=NOTYET_2)
    footer(cv, 988,
           "Checked: every story dated 23 Nov 2026; CLAIM = single source; "
           "CONFIRMED = 2+ outlets.",
           "Sources: AP \u00b7 Reuters \u00b7 BBC \u00b7 CNBC \u00b7 CBS \u00b7 "
           "Al Jazeera")
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

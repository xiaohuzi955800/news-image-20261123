#!/usr/bin/env python3
"""Page-section builders for the 23 Nov 2026 news image.

Shared by the five candidate versions; each version's main.py composes
these sections with its own geometry, headline set, density and emphasis.
Pure standard library; written fresh for this entry.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from newsframe import (Canvas, PAPER, INK, ACCENT, GOLD, LIGHT_LINE,
                       WHITE, DARKPANEL, REGION_COLORS, draw_text,
                       draw_centered, draw_wrapped, text_width, wrap_text,
                       draw_map)


def masthead(cv, y, count_text):
    """Top strip: slogan left, scale right."""
    draw_text(cv, "sans_bold_10", 28, y + 9,
              "ONE DAY OF WORLD NEWS, ONE PICTURE", ACCENT)
    w = text_width("sans_bold_10", count_text)
    draw_text(cv, "sans_bold_10", 1024 - 28 - w, y + 9, count_text, INK)
    cv.hline(28, y + 14, 968, INK, 2)


def title_block(cv, y, big="WORLD NEWS", date_top="MONDAY",
                date_bottom="23 NOVEMBER 2026", big_size="serif_bold_54"):
    """Big serif title left, red date block right."""
    draw_text(cv, big_size, 28, y + 50, big, INK)
    w1 = text_width("serif_bold_21", date_top)
    w2 = text_width("serif_bold_21", date_bottom)
    draw_text(cv, "serif_bold_21", 1024 - 28 - w2, y + 28, date_bottom, ACCENT)
    draw_text(cv, "serif_bold_21", 1024 - 28 - w1, y + 52, date_top, INK)
    cv.hline(28, y + 62, 968, INK, 2)
    return y + 64


def timeline(cv, y, items, height=44):
    """UTC timeline strip. items: list of (time, event)."""
    cv.fill_rect(28, y, 968, height, WHITE)
    cv.rect(28, y, 968, height, LIGHT_LINE)
    cv.fill_rect(28, y, 92, height, ACCENT)
    draw_text(cv, "sans_bold_10", 36, y + 15, "THE DAY", WHITE)
    draw_text(cv, "sans_bold_10", 36, y + 29, "IN UTC", WHITE)
    n = len(items)
    seg = (968 - 92) // n
    for i, (t, ev) in enumerate(items):
        x = 28 + 92 + i * seg
        if i:
            cv.vline(x, y + 6, height - 12, LIGHT_LINE)
        draw_text(cv, "sans_bold_11", x + 8, y + 15, t, ACCENT)
        draw_wrapped(cv, "sans_10", x + 8, y + 20, ev, INK, seg - 12, 12,
                     max_lines=2)
    return y + height


def _tag(cv, x, baseline, region, cred):
    """Region colour dot + REGION label + optional CLAIM/CONFIRMED tag
    (label word only; the source is named in the body/source line)."""
    col = REGION_COLORS.get(region, INK)
    cv.filled_circle(x + 5, baseline - 4, 5, col)
    draw_text(cv, "sans_bold_10", x + 14, baseline, region, col)
    if cred:
        label, _src = cred
        tx = x + 14 + text_width("sans_bold_10", region) + 8
        draw_text(cv, "sans_bold_10", tx, baseline, label,
                  ACCENT if label == "CLAIM" else (46, 125, 50))
    return baseline


def headlines(cv, x, y, w, items, col_h, title_font="serif_bold_21",
              body_font="sans_12", body_lines=3, gap=10):
    """4-column headline grid. item: dict(number, region, cred, title,
    body, source)."""
    n = len(items)
    cw = (w - gap * (n - 1)) // n
    for i, it in enumerate(items):
        cx = x + i * (cw + gap)
        num = str(it["number"])
        cv.filled_circle(cx + 11, y + 11, 11, REGION_COLORS[it["region"]])
        draw_centered(cv, "sans_bold_11", cx + 11, y + 15, num, WHITE)
        _tag(cv, cx + 26, y + 15, it["region"], it.get("cred"))
        title_lines = wrap_text(title_font, it["title"], cw)
        draw_wrapped(cv, title_font, cx, y + 24, it["title"], INK, cw, 24)
        body_y = y + 24 + len(title_lines) * 24 + 6
        draw_wrapped(cv, body_font, cx, body_y, it["body"],
                     INK, cw, 15, max_lines=body_lines)
        src = it.get("source", "")
        if src:
            draw_text(cv, "sans_bold_10", cx, y + col_h - 4, src, LIGHT_LINE)
    return y + col_h


def secondary(cv, x, y, w, items, rows=2, cols=6, row_h=86, gap=10,
              show_cred=False, title_lines=2, body_lines=2):
    """Secondary grid. item: dict(number, region, cred, title, body).
    With show_cred the CLAIM/CONFIRMED tag is drawn right-aligned on the
    tag line (only safe when columns are wide enough)."""
    cw = (w - gap * (cols - 1)) // cols
    for idx, it in enumerate(items):
        r, c = divmod(idx, cols)
        cx = x + c * (cw + gap)
        cy = y + r * row_h
        num = str(it["number"])
        cv.filled_circle(cx + 8, cy + 8, 8, REGION_COLORS[it["region"]])
        draw_centered(cv, "sans_bold_10", cx + 8, cy + 11, num, WHITE)
        draw_text(cv, "sans_bold_10", cx + 20, cy + 11, it["region"],
                  REGION_COLORS[it["region"]])
        if show_cred and it.get("cred"):
            label, _src = it["cred"]
            lw = text_width("sans_bold_10", label)
            draw_text(cv, "sans_bold_10", cx + cw - lw, cy + 11, label,
                      ACCENT if label == "CLAIM" else (46, 125, 50))
        draw_wrapped(cv, "serif_bold_15", cx, cy + 18, it["title"], INK,
                     cw, 17, max_lines=title_lines)
        draw_wrapped(cv, "sans_11", cx, cy + 18 + 17 * title_lines + 2,
                     it["body"], INK, cw, 13, max_lines=body_lines)
    return y + rows * row_h


def wrapped_list(cv, x, y, w, items, cols=2, row_h=30, font="sans_11",
                 gap=14):
    """Two-line wrapped numbered list in columns. item: dict(number, region,
    lead, text). Returns bottom y."""
    n = len(items)
    per = (n + cols - 1) // cols
    cw = (w - gap * (cols - 1)) // cols
    for idx, it in enumerate(items):
        c = idx // per
        r = idx % per
        cx = x + c * (cw + gap)
        cy = y + r * row_h
        num = str(it["number"])
        cv.filled_circle(cx + 7, cy + 8, 7, REGION_COLORS[it["region"]])
        draw_centered(cv, "sans_bold_10", cx + 7, cy + 11, num, WHITE)
        full = (it.get("lead", "") + " \u2014 " + it["text"]) if it.get("lead") else it["text"]
        draw_wrapped(cv, font, cx + 18, cy + 2, full, INK, cw - 18, 13,
                     max_lines=2)
    return y + per * row_h


def one_line_list(cv, x, y, w, items, cols=3, row_h=17, font="sans_11",
                  gap=12, lead_bold=True):
    """Numbered one-line list in columns. item: dict(number, region, text,
    source optional)."""
    n = len(items)
    per = (n + cols - 1) // cols
    cw = (w - gap * (cols - 1)) // cols
    for idx, it in enumerate(items):
        c = idx // per
        r = idx % per
        cx = x + c * (cw + gap)
        cy = y + r * row_h
        num = str(it["number"])
        cv.filled_circle(cx + 7, cy + 7, 7, REGION_COLORS[it["region"]])
        draw_centered(cv, "sans_bold_10", cx + 7, cy + 10, num, WHITE)
        lead = it.get("lead", "")
        text = it["text"]
        if lead_bold and lead:
            lw = draw_text(cv, "sans_bold_11", cx + 18, cy + 11, lead + " ",
                           INK)
            draw_text(cv, font, cx + 18 + lw, cy + 11, text, INK)
        else:
            draw_text(cv, font, cx + 18, cy + 11, text, INK)
    return y + per * row_h


def map_panel(cv, x, y, w, h, dots, title="WHERE IT HAPPENED"):
    draw_text(cv, "sans_bold_11", x, y + 11, title, INK)
    draw_map(cv, x, y + 16, w, h - 16, dots)
    return y + h


def date_check(cv, y, exclusions, notyet, height=52, notyet2=None):
    """DATE CHECK strip. exclusions: list of short strings; notyet: string;
    notyet2: optional second not-yet line (needs a taller strip)."""
    cv.fill_rect(28, y, 968, height, WHITE)
    cv.rect(28, y, 968, height, ACCENT, 2)
    cv.fill_rect(28, y, 110, height, ACCENT)
    draw_text(cv, "sans_bold_11", 36, y + 16, "DATE", WHITE)
    draw_text(cv, "sans_bold_11", 36, y + 30, "CHECK", WHITE)
    tx = 28 + 110 + 10
    tw = 968 - 110 - 20
    excl = "LEFT OUT (earlier): " + "; ".join(exclusions) + "."
    draw_wrapped(cv, "sans_11", tx, y + 6, excl, INK, tw, 14, max_lines=2)
    ny_y = y + 6 + 28
    draw_wrapped(cv, "sans_11", tx, ny_y, "NOT YET: " + notyet, INK,
                 tw, 14, max_lines=1)
    if notyet2:
        draw_wrapped(cv, "sans_11", tx, ny_y + 14, "ALSO NOT YET: " + notyet2,
                     INK, tw, 14, max_lines=1)
    return y + height


def footer(cv, y, left, right):
    draw_text(cv, "sans_10", 28, y + 10, left, LIGHT_LINE)
    w = text_width("sans_10", right)
    draw_text(cv, "sans_10", 1024 - 28 - w, y + 10, right, LIGHT_LINE)
    return y + 14

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
              "ONE DAY IN THREE LAYERS: 3 LEADS \u00b7 12 PICTURES \u00b7 16 BRIEFS",
              ACCENT)
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


def title_block_date(cv, y, date_str="Monday 23 November 2026",
                   subhead="Nvidia brings back Huang, shares soar 31%  "
                           "\u00b7  Ukraine drones sink Russian warship in "
                           "Libya  \u00b7  S&P 500 up 4.7%"):
    """Giant serif date title, the way the champion pages do it: the date
    is the biggest thing on the page, with a red one-line summary of the
    three biggest stories under it. Returns bottom y."""
    draw_text(cv, "serif_bold_54", 28, y + 50, date_str, INK)
    ny = y + 62
    if subhead:
        draw_text(cv, "serif_italic_15", 28, ny + 12, subhead, ACCENT)
        ny += 18
    cv.hline(28, ny + 4, 968, INK, 2)
    return ny + 6


# ------------------------------------------------------- headline art
_NAVY = (28, 42, 76)
_SEA = (126, 178, 210)
_SEA_DEEP = (64, 110, 150)
_SKY = (214, 230, 240)
_CHIP_GREEN = (46, 125, 50)
_CHART_GREEN = (46, 160, 70)
_CHART_BG = (30, 30, 30)
_SAND = (232, 222, 200)
_EU_BLUE = (0, 51, 153)
_EU_GOLD = (255, 204, 0)
_ORANGE = (230, 126, 34)


def headline_art(cv, x, y, w, h, kind, banner=None):
    """Flat pictogram panel above a headline. Coordinates are relative
    to the panel box so the same scenes scale to any column width.
    Each scene is a small multi-element picture (a motherboard, a naval
    action, a trading screen), not a single icon: the champions' art
    reads as a scene, and so should ours (v8: lin asked for more vivid
    pictures, so every scene gained foreground/background elements)."""
    cv.fill_rect(x, y, w, h, _SKY)
    cv.rect(x, y, w, h, LIGHT_LINE)
    if banner:
        bw = text_width("sans_bold_10", banner) + 10
        cv.fill_rect(x + 6, y + 6, bw, 13, ACCENT)
        draw_text(cv, "sans_bold_10", x + 11, y + 16, banner, WHITE)
    if kind == "chip":
        # Motherboard: navy PCB, gold traces, main chip + small chips
        # and capacitors. The chip is the story; the board makes it a
        # place, not an icon.
        cv.fill_rect(x, y, w, h, _NAVY)
        cv.rect(x, y, w, h, LIGHT_LINE)
        if banner:
            bw = text_width("sans_bold_10", banner) + 10
            cv.fill_rect(x + 6, y + 6, bw, 13, ACCENT)
            draw_text(cv, "sans_bold_10", x + 11, y + 16, banner, WHITE)
        # PCB traces: thin gold runs with right-angle bends + vias,
        # routed through the free corners (clear of the text zone).
        cv.hline(x + 120, y + 10, 80, (150, 130, 60))
        cv.vline(x + 200, y + 10, 12, (150, 130, 60))
        cv.hline(x + 200, y + 22, 30, (150, 130, 60))
        cv.filled_circle(x + 230, y + 22, 2, GOLD)
        cv.hline(x + 90, y + h - 8, 110, (150, 130, 60))
        cv.filled_circle(x + 90, y + h - 8, 2, GOLD)
        cv.filled_circle(x + 200, y + h - 8, 2, GOLD)
        cv.vline(x + w - 10, y + 30, 30, (150, 130, 60))
        cv.filled_circle(x + w - 10, y + 30, 2, GOLD)
        # small black chip, right of the text zone, below the arrow
        cv.fill_rect(x + 215, y + 58, 24, 14, (20, 20, 20))
        cv.rect(x + 215, y + 58, 24, 14, GOLD)
        cv.fill_rect(x + 218, y + 61, 18, 8, (40, 40, 40))
        # two capacitors under the text (below the SHARES JUMP ink)
        cv.fill_rect(x + 150, y + 66, 6, 12, (60, 90, 160))
        cv.fill_rect(x + 160, y + 66, 6, 12, (60, 90, 160))
        cv.fill_rect(x + 150, y + 64, 6, 2, (180, 180, 180))
        cv.fill_rect(x + 160, y + 64, 6, 2, (180, 180, 180))
        # main chip
        s = h - 36
        cx, cy = x + 18 + s // 2, y + h // 2 + 6
        cv.fill_rect(cx - s // 2, cy - s // 2, s, s, _CHIP_GREEN)
        cv.rect(cx - s // 2, cy - s // 2, s, s, WHITE)
        cv.fill_rect(cx - s // 4, cy - s // 4, s // 2, s // 2, _NAVY)
        for dx in (-s // 3, 0, s // 3):
            cv.vline(cx + dx, cy - s // 2 - 6, 6, GOLD)
            cv.vline(cx + dx, cy + s // 2, 6, GOLD)
        for dy in (-s // 3, 0, s // 3):
            cv.hline(cx - s // 2 - 6, cy + dy, 6, GOLD)
            cv.hline(cx + s // 2, cy + dy, 6, GOLD)
        # circuit traces out of the chip's right edge, each ending in
        # a pad (v6): pins alone read as a chip; traces read as a board
        for ty in (cy - s // 3, cy, cy + s // 3):
            cv.hline(cx + s // 2 + 8, ty, 10, GOLD)
            cv.filled_circle(cx + s // 2 + 18, ty, 2, GOLD)
        tx = x + 18 + s + 22
        draw_text(cv, "serif_bold_21", tx, y + 42, "+31%", WHITE)
        draw_text(cv, "sans_bold_10", tx, y + 60, "SHARES JUMP", GOLD)
        # rising arrow, top-right, clear of the text
        ax0, ay0 = x + w - 66, y + h - 16
        ax1, ay1 = x + w - 18, y + 16
        cv.line(ax0, ay0, ax1, ay1, _CHART_GREEN)
        cv.line(ax0, ay0 + 1, ax1, ay1 + 1, _CHART_GREEN)
        cv.fill_poly([(ax1, ay1 - 4), (ax1 - 12, ay1 + 6),
                      (ax1 + 2, ay1 + 8)], _CHART_GREEN)
        # place label, bottom-right (superskie's panels name the place)
        lab = "SANTA CLARA"
        draw_text(cv, "sans_bold_9", x + w - 8 - text_width("sans_bold_9", lab),
                  y + h - 4, lab, GOLD)
    elif kind == "ship":
        # Naval action off Libya: clouds, a distant coastline, a
        # detailed warship (bridge windows, radar mast, gun turret,
        # funnel smoke, bow foam), a cargo ship behind it, three
        # drones with dotted trails, and the blast with glow, smoke
        # and flying debris. Bow faces left (gun at the bow).
        # clouds: centre + low left, clear of the banner top-left
        for ccx, ccy, r in ((150, 10, 6), (160, 8, 7), (170, 11, 5),
                            (20, 26, 5), (30, 24, 6), (40, 27, 4)):
            cv.filled_circle(x + ccx, y + ccy, r, WHITE)
        # distant coastline, left third, just above the sea line
        cv.fill_rect(x, y + h - 32, int(w * 0.30), 6, (140, 150, 140))
        cv.fill_rect(x + 20, y + h - 38, 10, 6, (140, 150, 140))
        # sea
        cv.fill_rect(x, y + h - 26, w, 26, _SEA_DEEP)
        # background cargo ship (grey silhouette, right side)
        gx0 = x + int(w * 0.74)
        cv.fill_rect(gx0, y + h - 40, 62, 14, (110, 120, 130))
        cv.fill_poly([(gx0 + 62, y + h - 40), (gx0 + 72, y + h - 33),
                      (gx0 + 62, y + h - 26)], (110, 120, 130))
        cv.fill_rect(gx0 + 6, y + h - 48, 12, 8, (150, 80, 80))
        cv.fill_rect(gx0 + 20, y + h - 48, 12, 8, (80, 120, 80))
        cv.fill_rect(gx0 + 40, y + h - 50, 10, 10, (200, 200, 200))
        # warship hull + bow foam at the left (bow)
        hx0, hx1 = x + int(w * 0.08), x + int(w * 0.60)
        hy = y + h - 26
        cv.fill_poly([(hx0, hy), (hx1, hy), (hx1 - 14, hy + 16),
                      (hx0 + 14, hy + 16)], _NAVY)
        cv.fill_poly([(hx0 + 14, hy + 16), (hx0 - 6, hy + 10),
                      (hx0 + 4, hy + 16)], (220, 235, 245))
        # superstructure + lit bridge windows
        cv.fill_rect(x + int(w * 0.26), hy - 16, int(w * 0.18), 16, _NAVY)
        for wx in range(3):
            cv.fill_rect(x + int(w * 0.28) + wx * 12, hy - 14, 8, 5,
                         (170, 220, 240))
        # radar mast (taller now) with a rotating bar on top
        cv.vline(x + int(w * 0.42), hy - 34, 18, _NAVY, 2)
        cv.hline(x + int(w * 0.42) - 8, hy - 34, 16, _NAVY)
        # red flag on the mast, below the radar bar
        cv.fill_rect(x + int(w * 0.42), hy - 30, 12, 6, ACCENT)
        # gun turret at the bow + barrel
        cv.fill_rect(x + int(w * 0.12), hy - 8, 14, 8, _NAVY)
        cv.hline(x + int(w * 0.12) + 14, hy - 5, 12, _NAVY)
        # funnel aft of the bridge + a puff of smoke
        cv.fill_rect(x + int(w * 0.50), hy - 22, 8, 6, (90, 90, 90))
        cv.filled_circle(x + int(w * 0.52), hy - 26, 3, (150, 150, 150))
        # three sea drones with dotted motion trails
        for fx, fy in ((0.72, 0.18), (0.83, 0.32), (0.91, 0.14)):
            dx, dy = x + int(w * fx), y + int(h * fy)
            for k in (1, 2, 3):
                cv.filled_circle(dx - k * 9, dy + k * 4, 1, INK)
            cv.filled_circle(dx, dy, 3, INK)
            cv.hline(dx - 7, dy, 14, INK)
        # blast: fire glow + star + smoke + flying debris
        bx, by = x + int(w * 0.66), y + int(h * 0.42)
        cv.filled_circle(bx, by, 20, (250, 180, 80))
        cv.fill_poly([(bx, by - 18), (bx + 5, by - 6), (bx + 18, by - 8),
                      (bx + 8, by + 2), (bx + 14, by + 14),
                      (bx, by + 7), (bx - 14, by + 14),
                      (bx - 8, by + 2), (bx - 18, by - 8),
                      (bx - 5, by - 6)], _ORANGE)
        cv.filled_circle(bx - 6, by - 24, 5, (90, 90, 90))
        cv.filled_circle(bx + 4, by - 28, 6, (110, 110, 110))
        cv.filled_circle(bx + 12, by - 22, 4, (90, 90, 90))
        for ddx, ddy in ((-24, -10), (22, -16), (-18, 14), (26, 10)):
            cv.filled_circle(bx + ddx, by + ddy, 2, INK)
        # waves
        for wx in range(0, w - 24, 28):
            cv.hline(x + wx, y + h - 18, 16, (170, 210, 225))
            cv.hline(x + wx + 12, y + h - 10, 14, (170, 210, 225))
        # place label on a navy plate, bottom-right: the waves would
        # strike through bare text on the sea
        lab = "BENGHAZI"
        lw = text_width("sans_bold_9", lab)
        px = x + w - 6 - (lw + 12)
        cv.fill_rect(px, y + h - 16, lw + 12, 12, _NAVY)
        draw_text(cv, "sans_bold_9", px + 6, y + h - 7, lab, WHITE)
    elif kind == "chart":
        # Trading screen: green S&P line rising, red dashed KOSPI line
        # falling (the contrast in the story), volume bars along the
        # bottom, faint gridlines.
        cv.fill_rect(x, y, w, h, _CHART_BG)
        cv.rect(x, y, w, h, LIGHT_LINE)
        if banner:
            bw = text_width("sans_bold_10", banner) + 10
            cv.fill_rect(x + 6, y + 6, bw, 13, ACCENT)
            draw_text(cv, "sans_bold_10", x + 11, y + 16, banner, WHITE)
        for fy in (0.58, 0.80):
            cv.hline(x + 6, y + int(h * fy), w - 12, (70, 70, 70))
        # volume bars along the bottom (leave the last two out: the
        # KOSPI caption sits bottom-right)
        vols = [6, 8, 5, 9, 7, 11, 9]
        for i, vh in enumerate(vols):
            vx = x + 12 + i * 32
            cv.fill_rect(vx, y + h - 4 - vh, 16, vh, (60, 120, 70))
        # KOSPI: red dashed line falling while the S&P rises. Kept
        # clear of the +4.7% text (ink bottom y+48) at the left and of
        # the KOSPI caption (ink top y+66) at the right.
        kpts = [(0.04, 0.64), (0.25, 0.66), (0.45, 0.69),
                (0.65, 0.72), (0.85, 0.76)]
        kp = [(x + int(w * fx), y + int(h * fy)) for fx, fy in kpts]
        for i in range(len(kp) - 1):
            x0, y0 = kp[i]
            x1, y1 = kp[i + 1]
            steps = max(abs(x1 - x0), abs(y1 - y0)) // 5
            for s in range(steps):
                if s % 2 == 0:
                    t0 = s / steps
                    t1 = min(1.0, (s + 1) / steps)
                    cv.line(int(x0 + (x1 - x0) * t0),
                            int(y0 + (y1 - y0) * t0),
                            int(x0 + (x1 - x0) * t1),
                            int(y0 + (y1 - y0) * t1), (220, 90, 90))
        # S&P line rising (the headline move) + arrowhead
        pts = [(0.04, 0.92), (0.20, 0.84), (0.36, 0.88), (0.52, 0.74),
               (0.68, 0.68), (0.82, 0.56), (0.94, 0.48)]
        pp = [(x + int(w * fx), y + int(h * fy)) for fx, fy in pts]
        for i in range(len(pp) - 1):
            cv.line(pp[i][0], pp[i][1], pp[i + 1][0], pp[i + 1][1],
                    _CHART_GREEN)
            cv.line(pp[i][0], pp[i][1] + 1, pp[i + 1][0], pp[i + 1][1] + 1,
                    _CHART_GREEN)
        ex, ey = pp[-1]
        cv.fill_poly([(ex + 2, ey - 6), (ex - 8, ey + 2), (ex + 2, ey + 6)],
                     _CHART_GREEN)
        draw_text(cv, "serif_bold_21", x + 12, y + 48, "+4.7%", WHITE)
        tw = text_width("sans_bold_10", "S&P 500")
        draw_text(cv, "sans_bold_10", x + 12 + 74, y + 48, "S&P 500",
                  _CHART_GREEN)
        # the contrast in one line: Seoul fell while Wall Street rose
        nk = "KOSPI -3.3%"
        draw_text(cv, "sans_bold_10", x + w - 8 - text_width("sans_bold_10", nk),
                  y + h - 8, nk, (220, 90, 90))
        # place label, top-right, above the rising line
        lab = "NEW YORK"
        draw_text(cv, "sans_bold_9", x + w - 8 - text_width("sans_bold_9", lab),
                  y + 18, lab, (170, 170, 170))



# 12 EU-flag star offsets (ellipse rx=22, ry=10), precomputed so no
# math import is needed at draw time.
_EU_STARS = [(22, 0), (19, 5), (11, 9), (0, 10), (-11, 9), (-19, 5),
             (-22, 0), (-19, -5), (-11, -9), (0, -10), (11, -9), (19, -5)]


def mini_icon(cv, x, y, w, h, kind, text=None, banner=None, stat=None):
    """Small art panel above a secondary story. The champions put a
    picture on every secondary item, with a red banner tag and a white
    stat box; these are the flat-geometry versions: flags, icons, or a
    big number (the champions use big numbers as art too)."""
    cv.fill_rect(x, y, w, h, _SKY)
    cv.rect(x, y, w, h, LIGHT_LINE)
    y0, h0 = y, h
    if banner:
        bw = text_width("sans_bold_10", banner) + 8
        cv.fill_rect(x + 4, y + 3, bw, 12, ACCENT)
        draw_text(cv, "sans_bold_10", x + 8, y + 12, banner, WHITE)
        y += 15
        h -= 15
    cx, cy = x + w // 2, y + h // 2
    if kind == "number":
        cv.fill_rect(x, y, w, h, WHITE)
        cv.rect(x, y, w, h, LIGHT_LINE)
        draw_centered(cv, "serif_bold_21", cx, y + 22, text or "", ACCENT)
    elif kind == "tanker":
        cv.fill_rect(x, y + h - 10, w, 10, _SEA)
        for wx in range(x + 10, x + w - 16, 26):
            cv.hline(wx, y + h - 5, 12, (220, 235, 245))
        cv.fill_rect(x + 18, y + 12, 84, 8, _NAVY)
        cv.fill_poly([(x + 102, y + 12), (x + 118, y + 16),
                      (x + 102, y + 20)], _NAVY)
        # containers stacked on deck + lit bridge windows + funnel smoke
        for ccx, col in ((24, (200, 70, 70)), (36, (70, 110, 200)),
                         (48, (70, 170, 90))):
            cv.fill_rect(x + ccx, y + 6, 10, 6, col)
        cv.fill_rect(x + 78, y + 5, 14, 7, WHITE)
        cv.fill_rect(x + 81, y + 8, 2, 2, _NAVY)
        cv.fill_rect(x + 87, y + 8, 2, 2, _NAVY)
        cv.filled_circle(x + 85, y + 2, 2, (150, 150, 150))
        cv.filled_circle(x + 132, y + 22, 4, INK)
        cv.line(x + 126, y + 22, x + 138, y + 22, INK)
        cv.line(x + 132, y + 16, x + 132, y + 28, INK)
    elif kind == "rocket":
        cv.fill_rect(x, y, w, h, _NAVY)
        cv.rect(x, y, w, h, LIGHT_LINE)
        cv.fill_poly([(cx, y + 3), (cx + 7, y + 12), (cx + 7, y + 22),
                      (cx - 7, y + 22), (cx - 7, y + 12)], WHITE)
        cv.fill_poly([(cx, y + 3), (cx + 7, y + 12), (cx - 7, y + 12)],
                     ACCENT)
        cv.fill_poly([(cx - 7, y + 18), (cx - 13, y + 25), (cx - 7, y + 25)],
                     ACCENT)
        cv.fill_poly([(cx + 7, y + 18), (cx + 13, y + 25), (cx + 7, y + 25)],
                     ACCENT)
        cv.fill_poly([(cx - 3, y + 22), (cx + 3, y + 22), (cx, y + 28)],
                     _ORANGE)
        for sx, sy in ((18, 6), (132, 8), (120, 24), (30, 24)):
            cv.filled_circle(x + sx, y + sy, 1, WHITE)
        # launch tower left of the rocket + smoke clouds at the base
        cv.fill_rect(cx - 22, y + 4, 4, h - 6, (120, 120, 120))
        cv.line(cx - 22, y + 8, cx - 18, y + 14, (120, 120, 120))
        cv.line(cx - 22, y + 18, cx - 18, y + 24, (120, 120, 120))
        cv.hline(cx - 18, y + 10, 4, (120, 120, 120))
        cv.filled_circle(cx - 20, y + h - 7, 4, (200, 200, 200))
        cv.filled_circle(cx + 20, y + h - 7, 4, (200, 200, 200))
        # launch pad: ground line + two pad blocks flanking the flame
        cv.fill_rect(x, y + h - 2, w, 2, (120, 120, 120))
        cv.fill_rect(cx - 14, y + h - 7, 6, 5, (150, 150, 150))
        cv.fill_rect(cx + 8, y + h - 7, 6, 5, (150, 150, 150))
    elif kind == "ball":
        # shifted left so the stat box (bottom-right) never clips it
        cx -= 10
        cv.fill_rect(x, y + h - 6, w, 6, (46, 125, 50))
        # goal on the left + motion dashes trailing the ball
        cv.vline(x + 8, y + 2, 12, WHITE, 2)
        cv.vline(x + 24, y + 2, 12, WHITE, 2)
        cv.hline(x + 8, y + 2, 16, WHITE)
        cv.hline(x + 84, y + 8, 8, (150, 150, 150))
        cv.hline(x + 88, y + 14, 8, (150, 150, 150))
        cv.filled_circle(cx, cy - 2, 11, WHITE)
        cv.circle(cx, cy - 2, 11, INK)
        cv.filled_circle(cx, cy - 2, 4, INK)
        for dx, dy in ((-8, -8), (8, -8), (-9, 3), (9, 3), (0, 8)):
            cv.filled_circle(cx + dx, cy + dy - 2, 2, INK)
    elif kind == "euflag":
        cv.fill_rect(x, y, w, h, _EU_BLUE)
        cv.rect(x, y, w, h, LIGHT_LINE)
        for dx, dy in _EU_STARS:
            cv.filled_circle(cx + dx, cy + dy, 2, _EU_GOLD)
    elif kind == "star":
        # shifted left so the stat box (bottom-right) never clips it
        cx -= 10
        cv.fill_rect(x, y, w, h, _NAVY)
        cv.rect(x, y, w, h, LIGHT_LINE)
        cv.fill_poly([(cx, y + 3), (cx + 3, cy - 3), (cx + 14, cy),
                      (cx + 3, cy + 3), (cx, y + h - 3), (cx - 3, cy + 3),
                      (cx - 14, cy), (cx - 3, cy - 3)], WHITE)
        cv.filled_circle(cx, cy, 3, _NAVY)
    elif kind == "mountain":
        cv.filled_circle(x + w - 18, y + 6, 4, _EU_GOLD)
        # a cloud on the left, above the slope
        cv.filled_circle(x + 28, y + 5, 4, WHITE)
        cv.filled_circle(x + 36, y + 3, 5, WHITE)
        cv.filled_circle(x + 44, y + 5, 4, WHITE)
        cv.fill_poly([(x + 20, y + h - 4), (x + 60, y + 4),
                      (x + 100, y + h - 4)], (90, 110, 140))
        cv.fill_poly([(x + 70, y + h - 4), (x + 105, y + 8),
                      (x + 140, y + h - 4)], (120, 140, 170))
        cv.fill_poly([(x + 60, y + 4), (x + 54, y + 12), (x + 60, y + 10),
                      (x + 66, y + 12)], WHITE)
        cv.fill_rect(x, y + h - 4, w, 4, (46, 125, 50))
        # pines on the slopes and the grass
        for px in (28, 118, 142):
            cv.fill_poly([(px, y + h - 12), (px - 4, y + h - 4),
                          (px + 4, y + h - 4)], (30, 90, 40))
    elif kind == "building":
        # street along the bottom (drawn first; buildings sit on it)
        cv.fill_rect(x, y + h - 3, w, 3, (100, 100, 100))
        cv.hline(x + 8, y + h - 2, 10, WHITE)
        cv.hline(x + 120, y + h - 2, 10, WHITE)
        # a tree on the left, clear of the stat box (bottom-right)
        cv.fill_rect(x + 16, y + h - 9, 2, 5, (120, 80, 40))
        cv.filled_circle(x + 17, y + h - 12, 5, (30, 90, 40))
        cv.fill_poly([(x + 56, y + 10), (x + 62, y + 2), (x + 68, y + 10)],
                     _ORANGE)
        cv.fill_poly([(x + 59, y + 10), (x + 62, y + 5), (x + 65, y + 10)],
                     _EU_GOLD)
        cv.fill_rect(x + 48, y + 10, 28, h - 10, (120, 116, 108))
        cv.fill_rect(x + 80, y + 16, 22, h - 16, (150, 145, 135))
        for wy in (14, 21):
            for wx in (53, 63):
                cv.fill_rect(x + wx, y + wy, 4, 4, GOLD)
        for wx in (85, 93):
            cv.fill_rect(x + wx, y + 20, 4, 4, GOLD)
    elif kind == "diamond":
        cv.fill_poly([(cx, y + 4), (cx + 18, cy), (cx, y + h - 4),
                      (cx - 18, cy)], (64, 170, 200))
        cv.fill_poly([(cx, y + 4), (cx + 18, cy), (cx, cy + 2),
                      (cx - 18, cy)], (140, 220, 240))
        cv.line(cx - 18, cy, cx + 18, cy, WHITE)
        # facet line from the crown to the centre + a glint sparkle
        cv.line(cx, y + 4, cx, cy + 2, WHITE)
        cv.hline(cx - 15, y + 10, 6, WHITE)
        cv.vline(cx - 12, y + 7, 6, WHITE)
    elif kind == "flame":
        # factory silhouette behind the flame (drawn first) + chimney
        cv.fill_rect(x + 28, y + 14, 40, h - 18, (90, 90, 90))
        cv.fill_rect(x + 58, y + 8, 6, 6, (90, 90, 90))
        cv.filled_circle(x + 61, y + 4, 3, (150, 150, 150))
        cv.filled_circle(x + 66, y + 2, 2, (150, 150, 150))
        cv.fill_poly([(cx - 12, y + h - 4), (cx - 8, y + 12),
                      (cx - 2, y + 16), (cx + 2, y + 6), (cx + 8, y + 14),
                      (cx + 12, y + h - 4)], _ORANGE)
        cv.fill_poly([(cx - 5, y + h - 4), (cx, y + 16),
                      (cx + 5, y + h - 4)], _EU_GOLD)
    if stat and stat != text:
        tw = text_width("sans_bold_10", stat)
        sx = x + w - tw - 10
        sy = y0 + h0 - 15
        cv.fill_rect(sx, sy, tw + 8, 12, WHITE)
        cv.rect(sx, sy, tw + 8, 12, LIGHT_LINE)
        draw_text(cv, "sans_bold_10", sx + 4, sy + 9, stat, INK)
    return y0 + h0


def region_chips(cv, y, counts):
    """Row of coloured chips, one per region, with story counts — the
    champions' region bar. counts: list of (region, n)."""
    gap = 4
    n = len(counts)
    cw = (968 - gap * (n - 1)) // n
    for i, (region, cnt) in enumerate(counts):
        cx = 28 + i * (cw + gap)
        cv.fill_rect(cx, y, cw, 14, REGION_COLORS.get(region, INK))
        draw_centered(cv, "sans_bold_10", cx + cw // 2, y + 11,
                      "%s %d" % (region, cnt), WHITE)
    return y + 14


def numbers_bar(cv, y, items, height=34):
    """THE DAY IN NUMBERS: big figures with small labels, one segment
    each. items: list of (number, label)."""
    cv.fill_rect(28, y, 968, height, WHITE)
    cv.rect(28, y, 968, height, LIGHT_LINE)
    cv.fill_rect(28, y, 92, height, ACCENT)
    draw_text(cv, "sans_bold_10", 36, y + 13, "THE DAY", WHITE)
    draw_text(cv, "sans_bold_10", 36, y + 26, "IN NUMBERS", WHITE)
    n = len(items)
    seg = (968 - 92) // n
    for i, (num, lab) in enumerate(items):
        x = 28 + 92 + i * seg
        if i:
            cv.vline(x, y + 5, height - 10, LIGHT_LINE)
        draw_text(cv, "serif_bold_28", x + 8, y + 27, num, INK)
        draw_text(cv, "sans_10", x + 8, y + 38, lab, LIGHT_LINE)
    return y + height


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


def _tag(cv, x, baseline, region, cred, right=None, dateline=None):
    """Region colour dot + dateline (or REGION label) + optional boxed
    CLAIM/CONFIRMED tag, right-aligned to `right` when given — the
    champions draw the credibility tag in a small box."""
    col = REGION_COLORS.get(region, INK)
    cv.filled_circle(x + 5, baseline - 4, 5, col)
    label_text = dateline if dateline else region
    draw_text(cv, "sans_bold_10", x + 14, baseline, label_text, col)
    if cred:
        label, src = cred
        tag_col = ACCENT if label == "CLAIM" else (46, 125, 50)
        if right is not None:
            tag_text = "%s \u00b7 %s" % (label, src) if src else label
            tw = text_width("sans_bold_10", tag_text)
            bx = right - tw - 8
            cv.rect(bx, baseline - 11, tw + 8, 13, tag_col)
            draw_text(cv, "sans_bold_10", bx + 4, baseline, tag_text,
                      tag_col)
        else:
            tx = x + 14 + text_width("sans_bold_10", label_text) + 8
            draw_text(cv, "sans_bold_10", tx, baseline, label, tag_col)
    return baseline


def headlines(cv, x, y, w, items, col_h, title_font="serif_bold_21",
              body_font="sans_12", body_lines=3, gap=10, art_h=0):
    """Headline grid. item: dict(number, region, cred, title, body,
    source, art, art_banner, dateline). With art_h > 0 each column gets
    a pictogram panel on top, like the champion pages' illustrations."""
    n = len(items)
    cw = (w - gap * (n - 1)) // n
    for i, it in enumerate(items):
        cx = x + i * (cw + gap)
        ty = y
        if art_h:
            headline_art(cv, cx, y, cw, art_h, it.get("art", "chart"),
                         it.get("art_banner"))
            ty = y + art_h + 8
        num = str(it["number"])
        cv.filled_circle(cx + 11, ty + 11, 11, REGION_COLORS[it["region"]])
        draw_centered(cv, "sans_bold_11", cx + 11, ty + 15, num, WHITE)
        _tag(cv, cx + 26, ty + 15, it["region"], it.get("cred"),
             right=cx + cw, dateline=it.get("dateline"))
        title_lines = wrap_text(title_font, it["title"], cw)
        draw_wrapped(cv, title_font, cx, ty + 24, it["title"], INK, cw, 24)
        body_y = ty + 24 + len(title_lines) * 24 + 6
        draw_wrapped(cv, body_font, cx, body_y, it["body"],
                     INK, cw, 15, max_lines=body_lines)
        src = it.get("source", "")
        if src:
            draw_text(cv, "sans_bold_10", cx, y + col_h - 4, src, LIGHT_LINE)
    return y + col_h


def secondary(cv, x, y, w, items, rows=2, cols=6, row_h=86, gap=10,
              show_cred=False, title_lines=2, body_lines=2, art_h=0):
    """Secondary grid. item: dict(number, region, cred, title, body,
    art, art_text). With art_h > 0 each cell gets a mini art panel on
    top, the way the champions illustrate every secondary story."""
    cw = (w - gap * (cols - 1)) // cols
    for idx, it in enumerate(items):
        r, c = divmod(idx, cols)
        cx = x + c * (cw + gap)
        cy = y + r * row_h
        if art_h:
            mini_icon(cv, cx, cy, cw, art_h, it.get("art", "number"),
                      it.get("art_text"), it.get("art_banner"),
                      it.get("art_stat"))
            cy += art_h + 4
        num = str(it["number"])
        cv.filled_circle(cx + 8, cy + 8, 8, REGION_COLORS[it["region"]])
        draw_centered(cv, "sans_bold_10", cx + 8, cy + 11, num, WHITE)
        draw_text(cv, "sans_bold_9", cx + 20, cy + 11, it["region"],
                  REGION_COLORS[it["region"]])
        if show_cred and it.get("cred"):
            label, _src = it["cred"]
            tag_col = ACCENT if label == "CLAIM" else (46, 125, 50)
            lw = text_width("sans_bold_9", label)
            bx = cx + cw - lw - 8
            cv.rect(bx, cy + 1, lw + 8, 12, tag_col)
            draw_text(cv, "sans_bold_9", bx + 4, cy + 11, label, tag_col)
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
    excl = "LEFT OUT: " + "; ".join(exclusions) + "."
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

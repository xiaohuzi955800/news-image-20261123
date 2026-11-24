#!/usr/bin/env python3
"""Drawing framework for the 23 Nov 2026 news-image entry.

Pure standard library. Canvas is an RGB bytearray; PNG is encoded by hand
(zlib + struct). Text comes from fontdata.py bitmap glyphs. Written fresh
for this entry; layout and news data live in each version's main.py.
"""
import os
import struct
import sys
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fontdata import FONTS  # noqa: E402

# ---------------------------------------------------------------- palette
PAPER = (247, 242, 231)
INK = (26, 26, 26)
ACCENT = (163, 22, 33)       # brick red
GOLD = (176, 141, 58)
LIGHT_LINE = (120, 112, 96)
MAP_LAND = (216, 210, 196)
MAP_SEA = (233, 228, 216)
MAP_LINE = (140, 131, 120)
WHITE = (255, 255, 255)
DARKPANEL = (38, 34, 30)

REGION_COLORS = {
    "EUROPE": (43, 94, 167),
    "MIDDLE EAST": (179, 84, 30),
    "ASIA": (106, 63, 160),
    "AMERICAS": (179, 38, 30),
    "LATIN AMERICA": (140, 190, 60),
    "AFRICA": (46, 125, 50),
    "OCEANIA": (0, 131, 143),
}


# ---------------------------------------------------------------- canvas
class Canvas:
    def __init__(self, w, h, bg=PAPER):
        self.w = w
        self.h = h
        self.px = bytearray(w * h * 3)
        self.fill_rect(0, 0, w, h, bg)

    def set(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            i = (y * self.w + x) * 3
            self.px[i], self.px[i + 1], self.px[i + 2] = c

    def get(self, x, y):
        if 0 <= x < self.w and 0 <= y < self.h:
            i = (y * self.w + x) * 3
            return (self.px[i], self.px[i + 1], self.px[i + 2])
        return (0, 0, 0)

    def blend(self, x, y, c, a):
        """Blend colour c over the current pixel with coverage a (0-255).
        Integer math only, so output is deterministic."""
        if a <= 0 or not (0 <= x < self.w and 0 <= y < self.h):
            return
        i = (y * self.w + x) * 3
        if a >= 255:
            self.px[i], self.px[i + 1], self.px[i + 2] = c
            return
        ia = 255 - a
        self.px[i] = (c[0] * a + self.px[i] * ia) // 255
        self.px[i + 1] = (c[1] * a + self.px[i + 1] * ia) // 255
        self.px[i + 2] = (c[2] * a + self.px[i + 2] * ia) // 255

    def fill_rect(self, x, y, w, h, c):
        x0 = max(0, x)
        y0 = max(0, y)
        x1 = min(self.w, x + w)
        y1 = min(self.h, y + h)
        if x1 <= x0 or y1 <= y0:
            return
        r, g, b = c
        for yy in range(y0, y1):
            i = (yy * self.w + x0) * 3
            row = bytes((r, g, b)) * (x1 - x0)
            self.px[i:i + (x1 - x0) * 3] = row

    def hline(self, x, y, w, c, thick=1):
        self.fill_rect(x, y, w, thick, c)

    def vline(self, x, y, h, c, thick=1):
        self.fill_rect(x, y, thick, h, c)

    def rect(self, x, y, w, h, c, thick=1):
        self.hline(x, y, w, c, thick)
        self.hline(x, y + h - thick, w, c, thick)
        self.vline(x, y, h, c, thick)
        self.vline(x + w - thick, y, h, c, thick)

    def line(self, x0, y0, x1, y1, c):
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while True:
            self.set(x0, y0, c)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def filled_circle(self, cx, cy, r, c):
        for dy in range(-r, r + 1):
            half = int((r * r - dy * dy) ** 0.5)
            self.fill_rect(cx - half, cy + dy, half * 2 + 1, 1, c)

    def circle(self, cx, cy, r, c):
        # midpoint circle outline
        x, y, d = r, 0, 1 - r
        while x >= y:
            for px, py in ((cx + x, cy + y), (cx - x, cy + y),
                           (cx + x, cy - y), (cx - x, cy - y),
                           (cx + y, cy + x), (cx - y, cy + x),
                           (cx + y, cy - x), (cx - y, cy - x)):
                self.set(px, py, c)
            y += 1
            if d <= 0:
                d += 2 * y + 1
            else:
                x -= 1
                d += 2 * (y - x) + 1

    def fill_poly(self, pts, c):
        """Scanline fill for a simple polygon (list of (x, y))."""
        if len(pts) < 3:
            return
        ys = [p[1] for p in pts]
        for y in range(max(0, min(ys)), min(self.h, max(ys) + 1)):
            xs = []
            n = len(pts)
            for i in range(n):
                x0, y0 = pts[i]
                x1, y1 = pts[(i + 1) % n]
                if (y0 <= y < y1) or (y1 <= y < y0):
                    xs.append(x0 + (y - y0) * (x1 - x0) / (y1 - y0))
            xs.sort()
            for i in range(0, len(xs) - 1, 2):
                self.fill_rect(int(xs[i]), y, max(1, int(xs[i + 1]) - int(xs[i])), 1, c)

    def save_png(self, path):
        raw = bytearray()
        stride = self.w * 3
        for y in range(self.h):
            raw.append(0)  # filter: none
            raw += self.px[y * stride:(y + 1) * stride]

        def chunk(tag, data):
            return (struct.pack(">I", len(data)) + tag + data +
                    struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))

        png = b"\x89PNG\r\n\x1a\n"
        png += chunk(b"IHDR", struct.pack(">IIBBBBB", self.w, self.h, 8, 2, 0, 0, 0))
        png += chunk(b"IDAT", zlib.compress(bytes(raw), 6))
        png += chunk(b"IEND", b"")
        with open(path, "wb") as f:
            f.write(png)
        return len(png)


# ---------------------------------------------------------------- text
def _glyph(font_name, ch):
    font = FONTS[font_name]
    g = font.get(ch)
    if g is None:
        g = font.get("?", (8, 8, 8, 0, ""))
    return g


def text_width(font_name, s):
    w = 0
    for ch in s:
        adv, _h, _w, _top, _data = _glyph(font_name, ch)
        w += adv + 1
    return max(0, w - 1)


def draw_text(cv, font_name, x, baseline_y, s, color):
    """Draw text with its baseline at baseline_y; returns width used.
    Glyph pixels carry anti-aliased coverage (0-255) and are blended
    over the canvas, so text reads smooth instead of pixelated."""
    cx = x
    for ch in s:
        adv, h, w, top, data = _glyph(font_name, ch)
        if h and w:
            raw = bytes.fromhex(data)
            for yy in range(h):
                base = yy * w
                for xx in range(w):
                    a = raw[base + xx]
                    if a:
                        cv.blend(cx + xx, baseline_y + top + yy, color, a)
        cx += adv + 1
    return cx - x


def wrap_text(font_name, s, max_width):
    """Greedy word wrap; returns list of lines."""
    words = s.split(" ")
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if text_width(font_name, trial) <= max_width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(cv, font_name, x, y_top, s, color, max_width, line_height,
                 max_lines=None):
    """Draw wrapped text; y_top is the top of the first line's ink box
    (approximated by the font's ascent). Returns (lines_used, height)."""
    lines = wrap_text(font_name, s, max_width)
    if max_lines is not None:
        lines = lines[:max_lines]
    ascent = {"serif_bold_54": 49, "serif_bold_28": 25, "serif_bold_21": 19,
              "serif_bold_15": 14, "serif_italic_15": 14,
              "sans_13": 12, "sans_12": 11, "sans_11": 10, "sans_10": 10,
              "sans_9": 9,
              "sans_bold_12": 11, "sans_bold_11": 10, "sans_bold_10": 10,
              "sans_bold_9": 9
              }.get(font_name, 11)
    for i, line in enumerate(lines):
        draw_text(cv, font_name, x, y_top + ascent + i * line_height, line, color)
    return len(lines), ascent + (len(lines) - 1) * line_height


def draw_centered(cv, font_name, cx, baseline_y, s, color):
    w = text_width(font_name, s)
    draw_text(cv, font_name, cx - w // 2, baseline_y, s, color)
    return w


# ---------------------------------------------------------------- map
# Coarse continent outlines in (lon, lat). Hand-drawn simplification.
CONTINENTS = [
    # North America
    [(-168, 66), (-158, 58), (-140, 60), (-130, 54), (-125, 49), (-124, 42),
     (-120, 34), (-114, 29), (-110, 24), (-105, 20), (-97, 16), (-92, 15),
     (-86, 12), (-83, 9), (-79, 9), (-80, 13), (-84, 16), (-87, 21),
     (-90, 21), (-97, 26), (-93, 30), (-89, 30), (-84, 30), (-81, 25),
     (-80, 32), (-76, 35), (-74, 40), (-70, 42), (-66, 45), (-60, 47),
     (-55, 52), (-60, 55), (-65, 60), (-68, 58), (-78, 62), (-85, 66),
     (-92, 66), (-95, 69), (-110, 68), (-125, 70), (-140, 70), (-155, 71),
     (-165, 68)],
    # Greenland
    [(-58, 64), (-52, 60), (-43, 60), (-40, 64), (-32, 68), (-22, 70),
     (-20, 74), (-25, 76), (-35, 78), (-50, 76), (-58, 74), (-60, 70)],
    # South America
    [(-79, 9), (-77, 4), (-80, -3), (-81, -6), (-77, -12), (-72, -18),
     (-70, -23), (-70, -30), (-72, -37), (-73, -44), (-74, -50), (-70, -54),
     (-66, -55), (-68, -50), (-65, -45), (-62, -40), (-58, -35), (-52, -32),
     (-48, -28), (-41, -23), (-39, -17), (-35, -9), (-35, -6), (-40, -3),
     (-44, -2), (-50, 0), (-53, 4), (-58, 6), (-62, 9), (-68, 11),
     (-72, 12), (-76, 10)],
    # Africa
    [(-17, 15), (-17, 21), (-15, 27), (-10, 31), (-5, 35), (0, 36),
     (10, 37), (11, 34), (20, 32), (30, 31), (32, 31), (34, 28),
     (35, 23), (37, 18), (40, 15), (43, 12), (48, 11), (51, 12),
     (46, 5), (42, 0), (40, -5), (40, -10), (36, -18), (33, -26),
     (28, -33), (20, -35), (17, -32), (15, -27), (12, -18), (13, -12),
     (9, -1), (9, 4), (4, 6), (-8, 5), (-13, 8), (-17, 12)],
    # Eurasia
    [(-10, 36), (-9, 43), (-2, 44), (-1, 46), (-4, 48), (-2, 49),
     (0, 51), (3, 53), (8, 57), (10, 59), (5, 60), (5, 62),
     (12, 65), (18, 69), (25, 71), (30, 70), (35, 68), (40, 68),
     (45, 68), (50, 69), (55, 68), (60, 69), (65, 69), (70, 72),
     (75, 73), (80, 73), (85, 74), (90, 75), (95, 76), (100, 77),
     (105, 77), (110, 74), (115, 73), (120, 73), (125, 72), (130, 72),
     (135, 71), (140, 72), (145, 72), (150, 70), (155, 69), (160, 69),
     (165, 67), (170, 66), (178, 65), (178, 62), (170, 60), (162, 58),
     (158, 52), (155, 50), (150, 45), (145, 42), (142, 40), (140, 38),
     (135, 35), (130, 33), (127, 35), (122, 38), (120, 32), (122, 28),
     (118, 25), (112, 22), (108, 18), (105, 10), (103, 8), (100, 8),
     (98, 10), (95, 15), (92, 21), (90, 22), (88, 22), (86, 20),
     (82, 17), (80, 15), (77, 8), (75, 10), (72, 20), (68, 22),
     (65, 25), (62, 25), (58, 26), (56, 27), (54, 26), (52, 25),
     (50, 29), (48, 30), (50, 26), (52, 24), (54, 24), (56, 26),
     (58, 22), (57, 17), (55, 17), (52, 15), (48, 14), (44, 13),
     (42, 15), (40, 15), (38, 18), (37, 20), (35, 24), (34, 28),
     (33, 31), (30, 36), (27, 37), (23, 36), (22, 37), (20, 40),
     (19, 42), (16, 44), (14, 45), (12, 44), (10, 44), (8, 44),
     (6, 43), (3, 43), (0, 40), (-2, 37), (-6, 36), (-9, 37)],
    # Australia
    [(113, -22), (114, -30), (115, -35), (118, -35), (124, -33), (129, -32),
     (132, -32), (135, -35), (138, -35), (140, -38), (145, -38), (150, -37),
     (153, -32), (153, -27), (150, -22), (146, -19), (142, -15), (142, -11),
     (137, -12), (135, -12), (132, -11), (130, -13), (126, -14), (122, -17),
     (118, -20)],
    # UK
    [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (0, 53), (-1, 51), (-3, 50)],
    # Japan
    [(130, 31), (132, 33), (135, 34), (137, 35), (139, 35), (140, 38),
     (141, 40), (141, 42), (143, 43), (145, 44), (142, 45), (140, 42),
     (139, 38), (137, 37), (135, 33), (132, 32)],
    # Madagascar
    [(44, -16), (47, -15), (50, -16), (49, -20), (47, -24), (45, -25),
     (43, -22), (43, -18)],
    # New Zealand
    [(167, -45), (170, -43), (173, -41), (175, -38), (177, -38), (175, -40),
     (173, -42), (170, -44)],
    # New Guinea
    [(131, -1), (136, -2), (141, -3), (146, -6), (150, -8), (147, -9),
     (142, -8), (138, -7), (134, -4)],
    # Borneo
    [(109, 1), (113, 4), (117, 6), (119, 2), (117, -2), (113, -3), (110, -1)],
    # Sumatra
    [(95, 5), (98, 3), (101, 0), (104, -3), (106, -6), (104, -5), (100, 1),
     (97, 4)],
]


def draw_map(cv, x, y, w, h, dots):
    """Draw a simplified world map in the box (x, y, w, h).
    dots: list of (lon, lat, region, label) -> numbered region-coloured dots."""
    cv.fill_rect(x, y, w, h, MAP_SEA)
    cv.rect(x, y, w, h, LIGHT_LINE)
    lon0, lon1 = -180.0, 180.0
    lat0, lat1 = 83.0, -58.0

    def proj(lon, lat):
        px = x + int((lon - lon0) / (lon1 - lon0) * w)
        py = y + int((lat0 - lat) / (lat0 - lat1) * h)
        return (px, py)

    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        cv.fill_poly(pts, MAP_LAND)
        for i in range(len(pts)):
            cv.line(pts[i][0], pts[i][1], pts[(i + 1) % len(pts)][0],
                    pts[(i + 1) % len(pts)][1], MAP_LINE)
    for lon, lat, region, label in dots:
        px, py = proj(lon, lat)
        col = REGION_COLORS.get(region, INK)
        cv.filled_circle(px, py, 9, col)
        cv.circle(px, py, 9, WHITE)
        draw_centered(cv, "sans_bold_10", px, py + 4, label, WHITE)

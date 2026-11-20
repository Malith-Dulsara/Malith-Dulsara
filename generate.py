#!/usr/bin/env python3
"""
Arcade / synthwave GitHub profile generator.

1. Edit the CONFIG section below (your username, name, stats, achievements...).
2. Run:  python generate.py
3. Commit README.md, assets/ and .github/ to the repo named exactly like your
   GitHub username (github.com/<you>/<you>).

Every SVG is hand-built: pixel font, pixel-art icons and pure CSS/SMIL
animations, so it renders inside GitHub's <img> sandbox with no JavaScript.
"""
import html
import os
import random

# ----------------------------------------------------------------- palette ---
BG0, BG1, BG2 = "#07020f", "#12052b", "#2a0a4a"
PINK, CYAN, ICE = "#ff2a6d", "#05d9e8", "#d1f7ff"
PURPLE, LAV, YELLOW, GREEN, ORANGE = "#7b2cff", "#a58bff", "#f9c80e", "#39ff88", "#ff8c42"

# ================================================================== CONFIG ===
USERNAME = "Malith-Dulsara"                # <- your GitHub username
NAME = "MALITH DULSARA"                    # big header title (A-Z, 0-9, basic symbols)
TAGLINE = "EMBEDDED // AI // UAV & AVIONICS // GAMER"
CLASS_ = "EMBEDDED AI ENGINEER"
GUILD = "OPEN SOURCE"
LEVEL = 25
XP = (7420, 10000)
HP, MP = 0.92, 0.84

STATS = [  # (label, 0-100, colour)
    ("EMBEDDED SYSTEMS", 94, CYAN),
    ("AI / LLM", 90, PINK),
    ("GEN AUDIO", 84, PURPLE),
    ("UAV & AVIONICS", 88, YELLOW),
    ("GAMING", 99, GREEN),
]

ACHIEVEMENTS = [  # (icon, title <=13 chars, description <=19 chars, rarity)
    ("trophy", "SKY PILOT", "First UAV airborne", "LEGENDARY"),
    ("sword", "BUG SLAYER", "Debugged bare metal", "EPIC"),
    ("star", "AI WHISPERER", "Tamed an LLM", "EPIC"),
    ("shield", "OPEN SOURCER", "Backs open source", "RARE"),
    ("potion", "SPIN MASTER", "Table tennis player", "COMMON"),
]

TYPING_LINES = [
    "Welcome, Player 2!",
    "Embedded Systems // AI // LLMs",
    "Building UAVs and Avionics",
    "Generative Audio Explorer",
    "Making games in Unreal Engine",
]

SKILLS = "c,cpp,python,arduino,raspberrypi,linux,bash,pytorch,tensorflow,matlab,unreal,blender,docker,git,github,vscode"

ABOUT = [  # shown as a YAML "save file" in the CHARACTER SELECT section
    ("player", "Malith Dulsara"),
    ("class", "Embedded Systems // AI // LLM // GenAudio"),
    ("main_quest", "UAV development and avionics"),
    ("side_quests", "[Unreal Engine game dev, open-source support]"),
    ("off_screen", "Table tennis player"),
    ("favourite_game", "Red Dead Redemption"),
    ("multiplayer", "[Marvel Rivals, Battlefield 6, Call of Duty]"),
]

QUESTS = [  # (quest, status, reward)
    ("Build a UAV flight & avionics stack", "IN PROGRESS", "+1000 XP"),
    ("Run LLM / GenAudio models on embedded hardware", "IN PROGRESS", "+750 XP"),
    ("Ship a game made in Unreal Engine", "IN PROGRESS", "+500 XP"),
    ("Support open-source projects", "IN PROGRESS", "+300 XP"),
    ("Win the next table tennis match", "LOCKED", "+250 XP"),
]

GAMES = [  # (label, simple-icons logo or "", hex colour) - shown under MULTIPLAYER
    ("Red Dead Redemption", "rockstargames", "B5121B"),
    ("Marvel Rivals", "", "E62429"),
    ("Battlefield 6", "ea", "1F6FEB"),
    ("Call of Duty", "activision", "2B2B2B"),
]

SOCIALS = [  # (label, simple-icons logo, hex colour, url) - add Discord, LinkedIn, etc. here
    ("GitHub", "github", "181717", f"https://github.com/{USERNAME}"),
]
# ============================================================ END CONFIG ===

RARITY = {"LEGENDARY": YELLOW, "EPIC": PURPLE, "RARE": CYAN, "COMMON": GREEN}
OUT = os.path.dirname(os.path.abspath(__file__))
REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"


def n(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return s if s not in ("-0", "") else "0"


# --------------------------------------------------------------- pixel font --
_F = """
A .###. #...# #...# ##### #...# #...# #...#
B ####. #...# #...# ####. #...# #...# ####.
C .###. #...# #.... #.... #.... #...# .###.
D ####. #...# #...# #...# #...# #...# ####.
E ##### #.... #.... ####. #.... #.... #####
F ##### #.... #.... ####. #.... #.... #....
G .###. #...# #.... #.### #...# #...# .####
H #...# #...# #...# ##### #...# #...# #...#
I .###. ..#.. ..#.. ..#.. ..#.. ..#.. .###.
J ..### ...#. ...#. ...#. ...#. #..#. .##..
K #...# #..#. #.#.. ##... #.#.. #..#. #...#
L #.... #.... #.... #.... #.... #.... #####
M #...# ##.## #.#.# #.#.# #...# #...# #...#
N #...# #...# ##..# #.#.# #..## #...# #...#
O .###. #...# #...# #...# #...# #...# .###.
P ####. #...# #...# ####. #.... #.... #....
Q .###. #...# #...# #...# #.#.# #..#. .##.#
R ####. #...# #...# ####. #.#.. #..#. #...#
S .#### #.... #.... .###. ....# ....# ####.
T ##### ..#.. ..#.. ..#.. ..#.. ..#.. ..#..
U #...# #...# #...# #...# #...# #...# .###.
V #...# #...# #...# #...# #...# .#.#. ..#..
W #...# #...# #...# #.#.# #.#.# #.#.# .#.#.
X #...# #...# .#.#. ..#.. .#.#. #...# #...#
Y #...# #...# .#.#. ..#.. ..#.. ..#.. ..#..
Z ##### ....# ...#. ..#.. .#... #.... #####
0 .###. #...# #..## #.#.# ##..# #...# .###.
1 ..#.. .##.. #.#.. ..#.. ..#.. ..#.. #####
2 .###. #...# ....# ...#. ..#.. .#... #####
3 ####. ....# ....# .###. ....# ....# ####.
4 ...#. ..##. .#.#. #..#. ##### ...#. ...#.
5 ##### #.... ####. ....# ....# #...# .###.
6 ..##. .#... #.... ####. #...# #...# .###.
7 ##### ....# ...#. ..#.. .#... .#... .#...
8 .###. #...# #...# .###. #...# #...# .###.
9 .###. #...# #...# .#### ....# ...#. .##..
. ..... ..... ..... ..... ..... ..... ..#..
, ..... ..... ..... ..... ..... ..#.. .#...
! ..#.. ..#.. ..#.. ..#.. ..#.. ..... ..#..
? .###. #...# ....# ...#. ..#.. ..... ..#..
: ..... ..#.. ..... ..... ..... ..#.. .....
- ..... ..... ..... .###. ..... ..... .....
/ ....# ....# ...#. ..#.. .#... #.... #....
> .#... ..#.. ...#. ....# ...#. ..#.. .#...
< ...#. ..#.. .#... #.... .#... ..#.. ...#.
+ ..... ..#.. ..#.. ##### ..#.. ..#.. .....
_ ..... ..... ..... ..... ..... ..... #####
' ..#.. ..#.. ..... ..... ..... ..... .....
& .##.. #..#. #.#.. .#... #.#.# #..#. .##.#
# .#.#. .#.#. ##### .#.#. ##### .#.#. .#.#.
% ##..# ##..# ...#. ..#.. .#... #..## #..##
( ...#. ..#.. .#... .#... .#... ..#.. ...#.
) .#... ..#.. ...#. ...#. ...#. ..#.. .#...
* ..... #.#.# .###. ##### .###. #.#.# .....
= ..... ..... ##### ..... ##### ..... .....
"""
FONT = {}
for _line in _F.strip().splitlines():
    _ch, *_rows = _line.split()
    FONT[_ch] = _rows
FONT[" "] = ["....."] * 7


def tw(text, s):
    """Pixel width of text at scale s."""
    return (len(text) * 6 - 1) * s if text else 0


def pix(text, x, y, s):
    """Path data for text in the pixel font, top-left at (x, y)."""
    d = []
    for i, ch in enumerate(text.upper()):
        rows = FONT.get(ch, FONT[" "])
        ox = x + i * 6 * s
        for r, row in enumerate(rows):
            c = 0
            while c < 5:
                if row[c] == "#":
                    st = c
                    while c < 5 and row[c] == "#":
                        c += 1
                    w = (c - st) * s
                    d.append(f"M{n(ox + st * s)} {n(y + r * s)}h{n(w)}v{n(s)}h{n(-w)}z")
                else:
                    c += 1
    return "".join(d)


def ptext(text, x, y, s, fill, anchor="start", extra=""):
    if anchor == "middle":
        x -= tw(text, s) / 2
    elif anchor == "end":
        x -= tw(text, s)
    return f'<path d="{pix(text, x, y, s)}" fill="{fill}" {extra}/>'


# ------------------------------------------------------------ pixel icons ---
ICONS = {
    "trophy": (["..YYYYYYYY..", "YYYWWYYYYOYY", "Y.YWYYYYYO.Y", "Y.YWYYYYYO.Y",
                ".YYWYYYYYOY.", "..YYYYYYYO..", "...YYYYYO...", "....YYYO....",
                ".....YO.....", ".....YO.....", "...OYYYYO...", "..OOOOOOOO.."],
               {"Y": YELLOW, "W": "#fff6c2", "O": "#d98a00"}),
    "sword": ([".........WWW", "........WSSW", ".......WSSW.", "......WSSW..",
               ".....WSSW...", "..R.WSSW....", "..RRWSW.....", "...RRW......",
               "..GRRR......", ".GGG.RR.....", "GGG.........", "GG.........."],
              {"W": "#ffffff", "S": "#9fd7ff", "R": PINK, "G": "#c07a3a"}),
    "shield": ([".CCCCCCCCCC.", "CWWWCCCCCCDC", "CWCCCCCCCCDC", "CWCCCPPCCCDC",
                "CWCCPPPPCCDC", "CCCPPPPPPCDC", "CCCCPPPPCCDC", ".CCCCPPCCCD.",
                ".CCCCCCCCDD.", "..CCCCCCDD..", "...CCCCDD...", "....CCDD...."],
               {"C": CYAN, "D": "#0a7f8f", "W": ICE, "P": PINK}),
    "heart": ([".RR...RR.", "RWRR.RRRD", "RWRRRRRRD", "RRRRRRRRD",
               ".RRRRRRD.", "..RRRRD..", "...RRD...", "....D...."],
              {"R": PINK, "W": "#ffd0e0", "D": "#b3124a"}),
    "star": ([".....Y.....", "....YYY....", "....YWY....", "YYYYYWYYYYY",
              ".YYYYYYYYO.", "..YYYYYYO..", "...YYYYYO..", "..YYYOYYYO.",
              "..YYO..YYO.", ".YYO....YO.", ".YO......O."],
             {"Y": YELLOW, "W": "#fffbe0", "O": "#e09a00"}),
    "coin": (["...YYYY...", ".YYOOOOYY.", ".YOYYYYOO.", "YOYWYYYYOO", "YOYWYYYYOO",
              "YOYYYYYYOO", "YOYYYYYYOO", ".YOYYYYOO.", ".YYOOOOOO.", "...OOOO..."],
             {"Y": YELLOW, "O": "#c77d00", "W": "#fff6c2"}),
    "gamepad": (["..PPPPPPPPPPPP..", ".PPPPPPPPPPPPPP.", "PPWPPPPPPPPPYPPP",
                 "PWWWPPPPPPPCPRPP", "PPWPPPPPPPPPGPPP", "PPPPPPPPPPPPPPPP",
                 "PPPPPP....PPPPPP", ".PPPP......PPPP.", "..PP........PP.."],
                {"P": PURPLE, "W": ICE, "Y": YELLOW, "C": CYAN, "R": PINK, "G": GREEN}),
    "potion": (["....BB....", "....KK....", "...K..K...", "...KCCK...", "..KCCCCK..",
                ".KCHCCCCK.", ".KCHCCCCK.", ".KCCCCCCK.", "..KCCCCK..", "...KKKK..."],
               {"B": "#c8925a", "K": ICE, "C": GREEN, "H": "#eafff2"}),
}


def icon(name, x, y, s):
    grid, pal = ICONS[name]
    out = []
    for key, col in pal.items():
        d = []
        for r, row in enumerate(grid):
            c = 0
            while c < len(row):
                if row[c] == key:
                    st = c
                    while c < len(row) and row[c] == key:
                        c += 1
                    w = (c - st) * s
                    d.append(f"M{n(x + st * s)} {n(y + r * s)}h{n(w)}v{n(s)}h{n(-w)}z")
                else:
                    c += 1
        if d:
            out.append(f'<path d="{"".join(d)}" fill="{col}"/>')
    return f'<g shape-rendering="crispEdges">{"".join(out)}</g>'


def icon_size(name):
    grid, _ = ICONS[name]
    return len(grid[0]), len(grid)


def svg(w, h, body, style, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}">'
            f'<title>{html.escape(title)}</title><style>{style}{REDUCED}</style>{body}</svg>')


def mix(c1, c2, t):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(a[i] + (b[i] - a[i]) * t):02x}" for i in range(3))


def crt_defs(w, h, rx):
    return (f'<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">'
            f'<rect width="4" height="1" fill="#000" opacity=".28"/></pattern>'
            f'<radialGradient id="vig" cx="50%" cy="50%" r="75%"><stop offset="60%" stop-color="#000" stop-opacity="0"/>'
            f'<stop offset="100%" stop-color="#000" stop-opacity=".55"/></radialGradient>'
            f'<linearGradient id="band" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
            f'<stop offset=".5" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
            f'<clipPath id="frame"><rect width="{w}" height="{h}" rx="{rx}"/></clipPath>')


def crt_overlay(w, h, rx):
    return (f'<rect width="{w}" height="{h}" fill="url(#scan)"/>'
            f'<g class="band"><rect y="-120" width="{w}" height="120" fill="url(#band)"/></g>'
            f'<rect width="{w}" height="{h}" fill="url(#vig)"/>'
            f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="{rx}" fill="none" stroke="{PURPLE}" stroke-opacity=".55" stroke-width="2"/>')


CRT_CSS = (".band{animation:band 8s linear infinite}"
           "@keyframes band{from{transform:translateY(0)}to{transform:translateY(var(--bh))}}")


def stars(rnd, count, w, h, y0=8):
    out = []
    for _ in range(count):
        x, y = rnd.uniform(8, w - 8), rnd.uniform(y0, h)
        r = rnd.choice([.6, .8, 1, 1.2, 1.6])
        out.append(f'<circle cx="{n(x)}" cy="{n(y)}" r="{r}" fill="{ICE}" class="tw" '
                   f'style="animation-duration:{rnd.uniform(2.5, 6):.2f}s;animation-delay:-{rnd.uniform(0, 6):.2f}s"/>')
    return "".join(out)


TWINKLE = ".tw{animation:tw 4s ease-in-out infinite}@keyframes tw{0%,100%{opacity:.15}50%{opacity:1}}"


def embers(rnd, count, w, ymin, ymax, rise):
    out = []
    for _ in range(count):
        x, y = rnd.uniform(20, w - 20), rnd.uniform(ymin, ymax)
        sz = rnd.choice([2, 3, 3, 4])
        col = rnd.choice([PINK, CYAN, YELLOW, PINK])
        out.append(f'<g class="em" style="animation-duration:{rnd.uniform(6, 11):.2f}s;'
                   f'animation-delay:-{rnd.uniform(0, 11):.2f}s"><rect x="{n(x)}" y="{n(y)}" '
                   f'width="{sz}" height="{sz}" fill="{col}"/></g>')
    css = (f".em{{opacity:0;animation:em 8s ease-out infinite}}@keyframes em{{0%{{transform:translateY(0);opacity:0}}"
           f"15%{{opacity:.9}}100%{{transform:translateY(-{rise}px);opacity:0}}}}")
    return "".join(out), css


# ================================================================== HEADER ===
def build_header():
    W, H, HY = 1200, 420, 285
    rnd = random.Random(7)
    sun_cx, sun_cy, sun_r = 600, 238, 145

    def ridge(step, amp, base, jag, seed):
        r = random.Random(seed)
        pts = [f"0,{HY}"]
        for x in range(0, W + step, step):
            f = abs(x - 600) / 600
            y = HY - (base + amp * f ** 1.4) * r.uniform(1 - jag, 1)
            pts.append(f"{x},{n(y)}")
        pts.append(f"{W},{HY}")
        return " ".join(pts)

    far, near = ridge(36, 95, 14, .45, 3), ridge(26, 55, 6, .6, 11)

    vlines = "".join(f'<line x1="{n(600 + i * 12)}" y1="{HY}" x2="{n(600 + i * 125)}" y2="{H}"/>' for i in range(-32, 33))
    hlines = "".join(f'<g class="hl" style="animation-delay:-{i * 0.55:.2f}s"><line x1="0" y1="{HY}" x2="{W}" y2="{HY}"/></g>' for i in range(10))

    # title
    ts = 11 if tw(NAME, 11) <= 1040 else max(4, int(1040 / (len(NAME) * 6)))
    tx, ty = (W - tw(NAME, ts)) / 2, 122
    th = 7 * ts
    extrude = "".join(f'<use xlink:href="#ttl" href="#ttl" y="{k}" fill="{mix("#8a2be2", "#14031f", k / 9)}"/>' for k in range(9, 0, -1))

    # tagline typing (SMIL, discrete steps)
    tg = TAGLINE.upper()
    gs = 3
    gw = tw(tg, gs)
    bw, bh = gw + 90, 56
    bx, by = (W - bw) / 2, 322
    gx, gy = (W - gw) / 2 - 8, by + (bh - 7 * gs) / 2
    events, t = [(0, 0)], 0.5
    for k in range(1, len(tg) + 1):
        events.append((t + k * 0.06, k))
    t = events[-1][0] + 3.6
    for k in range(len(tg) - 1, -1, -1):
        t += 0.022
        events.append((t, k))
    total = t + 0.7
    kt = ";".join(f"{e[0] / total:.4f}" for e in events)
    wv = ";".join(n(e[1] * 6 * gs) for e in events)
    cv = ";".join(n(gx + e[1] * 6 * gs) for e in events)

    em, em_css = embers(rnd, 22, W, HY - 30, HY + 80, 240)

    defs = (
        f'<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG0}"/>'
        f'<stop offset=".55" stop-color="{BG1}"/><stop offset="1" stop-color="#4a0d63"/></linearGradient>'
        f'<linearGradient id="sun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{YELLOW}"/>'
        f'<stop offset=".45" stop-color="{ORANGE}"/><stop offset="1" stop-color="{PINK}"/></linearGradient>'
        f'<linearGradient id="gnd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a0533"/>'
        f'<stop offset="1" stop-color="{BG0}"/></linearGradient>'
        f'<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a0533"/>'
        f'<stop offset="1" stop-color="#1a0533" stop-opacity="0"/></linearGradient>'
        f'<linearGradient id="chrome" gradientUnits="userSpaceOnUse" x1="0" y1="{ty}" x2="0" y2="{ty + th}">'
        f'<stop offset="0" stop-color="#ffffff"/><stop offset=".46" stop-color="#8ff3ff"/>'
        f'<stop offset=".5" stop-color="#ff5fa2"/><stop offset="1" stop-color="#ffd3e6"/></linearGradient>'
        f'<linearGradient id="shine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
        f'<stop offset=".5" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
        f'<pattern id="stripes" width="{W}" height="16" patternUnits="userSpaceOnUse">'
        f'<rect y="11" width="{W}" height="5" fill="#000"/>'
        f'<animateTransform attributeName="patternTransform" type="translate" from="0 0" to="0 -16" dur="1.8s" repeatCount="indefinite"/></pattern>'
        f'<mask id="sunMask"><rect width="{W}" height="{H}" fill="#fff"/>'
        f'<rect y="{sun_cy - 10}" width="{W}" height="{HY - sun_cy + 10}" fill="url(#stripes)"/></mask>'
        f'<clipPath id="ground"><rect y="{HY}" width="{W}" height="{H - HY}"/></clipPath>'
        f'<clipPath id="above"><rect width="{W}" height="{HY}"/></clipPath>'
        f'<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="18"/></filter>'
        f'<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/>'
        f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
        f'<path id="ttl" d="{pix(NAME, tx, ty, ts)}"/>'
        f'<clipPath id="ttlClip"><use xlink:href="#ttl" href="#ttl"/></clipPath>'
        f'<clipPath id="tagClip"><rect x="{n(gx)}" y="{n(gy - 2)}" height="{7 * gs + 4}" width="0">'
        f'<animate attributeName="width" values="{wv}" keyTimes="{kt}" dur="{total:.2f}s" calcMode="discrete" repeatCount="indefinite"/></rect></clipPath>'
        + crt_defs(W, H, 18)
    )

    body = (
        f'<defs>{defs}</defs><g clip-path="url(#frame)">'
        f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
        f'<g>{stars(rnd, 90, W, HY - 60)}</g>'
        # sun
        f'<g clip-path="url(#above)">'
        f'<circle class="sunglow" cx="{sun_cx}" cy="{sun_cy}" r="{sun_r + 20}" fill="{PINK}" filter="url(#blur)"/>'
        f'<circle cx="{sun_cx}" cy="{sun_cy}" r="{sun_r}" fill="url(#sun)" mask="url(#sunMask)"/>'
        f'<polygon points="{far}" fill="#22073f" stroke="{PURPLE}" stroke-opacity=".8" stroke-width="1.5" stroke-linejoin="round"/>'
        f'<polygon points="{near}" fill="#0f0322" stroke="{PINK}" stroke-opacity=".75" stroke-width="1.5" stroke-linejoin="round"/>'
        f'</g>'
        # ground grid
        f'<rect y="{HY}" width="{W}" height="{H - HY}" fill="url(#gnd)"/>'
        f'<g clip-path="url(#ground)" stroke="{PINK}" stroke-width="1.4">'
        f'<g stroke-opacity=".5">{vlines}</g><g stroke-opacity=".75">{hlines}</g>'
        f'<rect y="{HY}" width="{W}" height="70" fill="url(#fade)" stroke="none"/></g>'
        f'<rect y="{HY - 1}" width="{W}" height="2.5" fill="{PINK}" filter="url(#glow)"/>'
        f'{em}'
        # HUD
        f'{ptext("P1", 34, 26, 2, YELLOW)}{ptext("READY", 34 + tw("P1 ", 2), 26, 2, ICE, extra='class="blink"')}'
        f'{ptext("HI-SCORE 999999", W - 34, 26, 2, ICE, "end")}'
        # title
        f'<use xlink:href="#ttl" href="#ttl" class="tglow" fill="{PINK}" filter="url(#blur)"/>'
        f'{extrude}'
        f'<g class="g1"><use xlink:href="#ttl" href="#ttl" fill="{CYAN}"/></g>'
        f'<g class="g2"><use xlink:href="#ttl" href="#ttl" fill="{PINK}"/></g>'
        f'<use xlink:href="#ttl" href="#ttl" fill="url(#chrome)"/>'
        f'<g clip-path="url(#ttlClip)"><g class="shine"><rect x="{n(tx - 160)}" y="{ty - 20}" width="90" '
        f'height="{th + 40}" fill="url(#shine)" transform="skewX(-22)"/></g></g>'
        # tagline HUD box
        f'<rect x="{n(bx)}" y="{by}" width="{n(bw)}" height="{bh}" rx="6" fill="{BG0}" fill-opacity=".82" '
        f'stroke="{CYAN}" stroke-opacity=".8" stroke-width="2"/>'
        f'<path d="M{n(bx - 6)} {by + 14}v-20h20M{n(bx + bw + 6)} {by + 14}v-20h-20M{n(bx - 6)} {by + bh - 14}v20h20'
        f'M{n(bx + bw + 6)} {by + bh - 14}v20h-20" fill="none" stroke="{PINK}" stroke-width="3"/>'
        f'<g clip-path="url(#tagClip)">{ptext(tg, gx, gy, gs, CYAN)}</g>'
        f'<rect class="cur" x="{n(gx)}" y="{n(gy - 2)}" width="{3 * gs}" height="{7 * gs + 4}" fill="{PINK}">'
        f'<animate attributeName="x" values="{cv}" keyTimes="{kt}" dur="{total:.2f}s" calcMode="discrete" repeatCount="indefinite"/></rect>'
        f'<g class="chevL">{ptext("<", bx - 46, gy, gs, PINK)}</g><g class="chevR">{ptext(">", bx + bw + 46, gy, gs, PINK, "end")}</g>'
        + crt_overlay(W, H, 18) + '</g>'
    )

    style = (
        TWINKLE + em_css + CRT_CSS.replace("var(--bh)", f"{H + 240}px") +
        ".sunglow{animation:sg 5s ease-in-out infinite}@keyframes sg{0%,100%{opacity:.35}50%{opacity:.75}}"
        f".hl{{animation:hl 5.5s cubic-bezier(.55,0,1,.45) infinite}}@keyframes hl{{0%{{transform:translateY(0);opacity:0}}"
        f"12%{{opacity:1}}100%{{transform:translateY({H - HY + 4}px);opacity:1}}}}"
        ".tglow{animation:tg 4s ease-in-out infinite}@keyframes tg{0%,100%{opacity:.35}50%{opacity:.8}}"
        ".g1,.g2{animation:g1 6s linear infinite}.g2{animation-name:g2}"
        "@keyframes g1{0%,88%,100%{transform:translate(0,0)}89%{transform:translate(-7px,2px)}90.5%{transform:translate(5px,-2px)}"
        "92%{transform:translate(-3px,1px)}93.5%{transform:translate(0,0)}}"
        "@keyframes g2{0%,88%,100%{transform:translate(0,0)}89%{transform:translate(7px,-2px)}90.5%{transform:translate(-5px,2px)}"
        "92%{transform:translate(3px,-1px)}93.5%{transform:translate(0,0)}}"
        f".shine{{animation:sh 6s cubic-bezier(.45,0,.25,1) infinite}}@keyframes sh{{0%,10%{{transform:translateX(0)}}"
        f"45%,100%{{transform:translateX({tw(NAME, ts) + 420}px)}}}}"
        ".blink{animation:bl 1.4s ease-in-out infinite}@keyframes bl{0%,100%{opacity:1}50%{opacity:.15}}"
        ".cur{animation:bl .9s steps(1) infinite}"
        ".chevL{animation:cl 1.2s ease-in-out infinite alternate}.chevR{animation:cr 1.2s ease-in-out infinite alternate}"
        "@keyframes cl{to{transform:translateX(-6px)}}@keyframes cr{to{transform:translateX(6px)}}"
    )
    return svg(W, H, body, style, f"{NAME} - {TAGLINE}")


# ============================================================ SECTION BARS ===
SECTIONS = [
    ("about", "01", "CHARACTER SELECT", "sword"),
    ("stats", "02", "PLAYER STATUS", "heart"),
    ("inventory", "03", "INVENTORY", "potion"),
    ("battle", "04", "BATTLE LOG", "shield"),
    ("achievements", "05", "ACHIEVEMENTS", "trophy"),
    ("quests", "06", "QUEST LOG", "star"),
    ("multiplayer", "07", "MULTIPLAYER", "gamepad"),
]


def build_section(num, title, ico):
    W, H = 1000, 72
    iw, ih = icon_size(ico)
    s = min(48 // iw, 48 // ih)
    ix, iy = (56 - iw * s) / 2, 10 + (52 - ih * s) / 2
    tx = 76
    lx = tx + tw(title, 4) + 24
    ly = 52
    body = (
        f'<defs><linearGradient id="comet" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/>'
        f'<stop offset=".8" stop-color="{CYAN}"/><stop offset="1" stop-color="#fff"/></linearGradient>'
        f'<clipPath id="ln"><rect x="{lx}" y="{ly - 4}" width="{W - 22 - lx}" height="8"/></clipPath>'
        f'<filter id="gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter></defs>'
        f'<ellipse class="halo" cx="28" cy="38" rx="26" ry="26" fill="{ICONS[ico][1][next(iter(ICONS[ico][1]))]}" filter="url(#gl)"/>'
        f'<g class="bob">{icon(ico, ix, iy, s)}</g>'
        f'{ptext("STAGE " + num, tx, 12, 2, PINK)}'
        f'{ptext("//", tx + tw("STAGE " + num + " ", 2), 12, 2, PURPLE)}'
        f'{ptext(title, tx + 3, 33, 4, "#3d1170")}'
        f'{ptext(title, tx, 30, 4, ICE)}'
        f'<rect x="{lx}" y="{ly - 1}" width="{W - 22 - lx}" height="2" fill="{PURPLE}" opacity=".6"/>'
        f'<g clip-path="url(#ln)"><g class="comet"><rect x="{lx - 120}" y="{ly - 2}" width="120" height="4" fill="url(#comet)"/></g></g>'
        f'<g transform="translate({W - 12} {ly})"><g class="gem"><rect x="-6" y="-6" width="12" height="12" fill="{PINK}" transform="rotate(45)"/></g></g>'
    )
    style = (
        ".bob{animation:bob 2.6s ease-in-out infinite alternate}@keyframes bob{from{transform:translateY(3px)}to{transform:translateY(-4px)}}"
        ".halo{animation:ha 2.6s ease-in-out infinite alternate}@keyframes ha{from{opacity:.15}to{opacity:.45}}"
        f".comet{{animation:co 3.2s cubic-bezier(.6,0,.4,1) infinite}}@keyframes co{{0%{{transform:translateX(0)}}80%,100%{{transform:translateX({W - lx + 100}px)}}}}"
        ".gem{transform-box:fill-box;transform-origin:center;animation:gm 1.6s ease-in-out infinite alternate}"
        "@keyframes gm{from{transform:scale(.7);opacity:.6}to{transform:scale(1.1);opacity:1}}"
    )
    return svg(W, H, body, style, f"Stage {num}: {title}")


# ============================================================= PLAYER CARD ===
def build_card():
    W, H = 1000, 392
    rnd = random.Random(21)
    defs = [
        f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#140630"/><stop offset="1" stop-color="{BG0}"/></linearGradient>',
        f'<radialGradient id="av" cx="50%" cy="45%" r="65%"><stop offset="0" stop-color="#3b0f6e"/><stop offset="1" stop-color="{BG0}"/></radialGradient>',
        '<linearGradient id="shim" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
        '<stop offset=".5" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>',
        f'<linearGradient id="xpg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{PURPLE}"/><stop offset="1" stop-color="{PINK}"/></linearGradient>',
        f'<linearGradient id="hpg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b3124a"/><stop offset="1" stop-color="{PINK}"/></linearGradient>',
        f'<linearGradient id="mpg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0a5f9e"/><stop offset="1" stop-color="{CYAN}"/></linearGradient>',
        '<pattern id="seg" width="18" height="40" patternUnits="userSpaceOnUse"><rect x="16" width="2" height="40" fill="#07020f" opacity=".85"/></pattern>',
        '<pattern id="str" width="24" height="24" patternUnits="userSpaceOnUse" patternTransform="skewX(-30)">'
        '<rect width="12" height="24" fill="#fff" opacity=".13"/>'
        '<animateTransform attributeName="patternTransform" type="translate" additive="sum" from="0 0" to="24 0" dur="1.2s" repeatCount="indefinite"/></pattern>',
        f'<pattern id="avgrid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="{PURPLE}" stroke-opacity=".25"/></pattern>',
        f'<filter id="gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="10"/></filter>',
        crt_defs(W, H, 16),
    ]
    parts = [f'<rect width="{W}" height="{H}" fill="url(#bg)"/>', f'<g>{stars(rnd, 30, W, H)}</g>']

    # header strip
    parts.append(ptext("SAVE FILE 01", 40, 26, 2, LAV))
    parts.append(f'<g class="blink">{ptext("* ONLINE", W - 40, 26, 2, GREEN, "end")}</g>')
    parts.append(f'<rect x="40" y="52" width="{W - 80}" height="2" fill="{PURPLE}" opacity=".5"/>')

    def bar(i, x, y, w, h, frac, fill, delay):
        fw = max(2, w * frac)
        cid = f"c{i}"
        defs.append(f'<clipPath id="{cid}"><rect x="{n(x)}" y="{y}" width="{n(fw)}" height="{h}"/></clipPath>')
        return (f'<rect x="{n(x)}" y="{y}" width="{n(w)}" height="{h}" fill="#1b0b3a" stroke="#3b1d6e"/>'
                f'<rect class="fill" style="animation-delay:{delay:.2f}s" x="{n(x)}" y="{y}" width="{n(fw)}" height="{h}" fill="{fill}"/>'
                f'<g clip-path="url(#{cid})"><g class="shim" style="animation-delay:{delay + 1.6:.2f}s">'
                f'<rect x="{n(x - 70)}" y="{y}" width="60" height="{h}" fill="url(#shim)"/></g></g>'
                f'<rect x="{n(x)}" y="{y}" width="{n(w)}" height="{h}" fill="url(#seg)"/>'), fw

    # avatar
    ax, ay, aw = 40, 80, 220
    gw_, gh_ = icon_size("gamepad")
    gs_ = 10
    parts.append(f'<rect x="{ax}" y="{ay}" width="{aw}" height="{aw}" rx="8" fill="url(#av)"/>'
                 f'<rect x="{ax}" y="{ay}" width="{aw}" height="{aw}" rx="8" fill="url(#avgrid)"/>'
                 f'<circle class="pulse" cx="{ax + aw / 2}" cy="{ay + 100}" r="60" fill="{PURPLE}" filter="url(#gl)"/>'
                 f'<g class="shadow" style="transform-origin:{ax + aw / 2}px {ay + 178}px"><ellipse cx="{ax + aw / 2}" cy="{ay + 178}" rx="70" ry="7" fill="#000" opacity=".55"/></g>'
                 f'<g class="float">{icon("gamepad", ax + (aw - gw_ * gs_) / 2, ay + 58, gs_)}</g>'
                 f'<rect x="{ax}" y="{ay}" width="{aw}" height="{aw}" rx="8" fill="none" stroke="{PINK}" stroke-width="2.5"/>'
                 f'<rect x="{ax + 12}" y="{ay + aw - 20}" width="{tw("LV " + str(LEVEL), 2) + 20}" height="30" rx="4" fill="{PINK}"/>'
                 + ptext(f"LV {LEVEL}", ax + 22, ay + aw - 12, 2, BG0))
    for cx, cy in ((ax + 14, ay + 18), (ax + aw - 22, ay + 30), (ax + aw - 30, ay + aw - 40)):
        parts.append(f'<g class="spark" style="animation-delay:-{rnd.uniform(0, 2):.2f}s;transform-origin:{cx}px {cy}px">'
                     f'<path d="M{cx - 5} {cy}h10M{cx} {cy - 5}v10" stroke="{ICE}" stroke-width="2"/></g>')

    # info column
    ix = 292
    ns = 3 if tw(NAME, 3) <= 270 else 2
    parts += [ptext("NAME", ix, 84, 2, LAV), ptext(NAME, ix, 104, ns, ICE),
              ptext("CLASS", ix, 142, 2, LAV), ptext(CLASS_, ix, 162, 2, CYAN),
              ptext("GUILD", ix, 194, 2, LAV), ptext(GUILD, ix, 214, 2, YELLOW)]
    b, _ = bar("hp", ix + 40, 246, 220, 14, HP, "url(#hpg)", .3)
    parts += [ptext("HP", ix, 246, 2, PINK), b]
    b, _ = bar("mp", ix + 40, 276, 220, 14, MP, "url(#mpg)", .5)
    parts += [ptext("MP", ix, 276, 2, CYAN), b]

    # attributes
    rx_, rw = 592, 368
    for i, (lab, val, col) in enumerate(STATS[:5]):
        y = 84 + i * 44
        b, _ = bar(i, rx_, y + 20, rw, 14, val / 100, col, .4 + i * .18)
        parts += [ptext(lab, rx_, y, 2, ICE),
                  f'<g class="num" style="animation-delay:{1 + i * .18:.2f}s">{ptext(str(val), rx_ + rw, y, 2, col, "end")}</g>', b]

    # XP bar
    xr = XP[0] / XP[1]
    parts.append(ptext("EXP", 40, 322, 2, LAV))
    parts.append(ptext(f"{XP[0]} / {XP[1]}  >  LV {LEVEL + 1}", W - 40, 322, 2, ICE, "end"))
    b, fw = bar("xp", 40, 342, W - 80, 20, xr, "url(#xpg)", 1.1)
    parts.append(b + f'<rect class="fill" style="animation-delay:1.1s" x="40" y="342" width="{n(fw)}" height="20" fill="url(#str)"/>')

    # corner brackets
    for x, y, dx, dy in ((10, 10, 1, 1), (W - 10, 10, -1, 1), (10, H - 10, 1, -1), (W - 10, H - 10, -1, -1)):
        parts.append(f'<path d="M{x} {y + 22 * dy}V{y}H{x + 22 * dx}" fill="none" stroke="{CYAN}" stroke-width="3"/>')

    body = f'<defs>{"".join(defs)}</defs><g clip-path="url(#frame)">{"".join(parts)}{crt_overlay(W, H, 16)}</g>'
    style = (
        TWINKLE + CRT_CSS.replace("var(--bh)", f"{H + 240}px") +
        ".fill{transform-box:fill-box;transform-origin:left center;transform:scaleX(0);"
        "animation:grow 1.6s cubic-bezier(.22,1,.36,1) forwards}@keyframes grow{to{transform:scaleX(1)}}"
        ".shim{animation:shim 4s cubic-bezier(.45,0,.25,1) infinite}@keyframes shim{0%{transform:translateX(0)}40%,100%{transform:translateX(1000px)}}"
        ".num{opacity:0;animation:num .8s ease-out forwards}@keyframes num{from{opacity:0;transform:translateX(10px)}to{opacity:1;transform:none}}"
        ".float{animation:fl 2.8s ease-in-out infinite alternate}@keyframes fl{from{transform:translateY(4px)}to{transform:translateY(-10px)}}"
        ".shadow{animation:sd 2.8s ease-in-out infinite alternate}@keyframes sd{from{transform:scale(1);opacity:1}to{transform:scale(.72);opacity:.5}}"
        ".pulse{animation:pu 2.8s ease-in-out infinite alternate}@keyframes pu{from{opacity:.25}to{opacity:.6}}"
        ".spark{animation:sp 2s ease-in-out infinite}@keyframes sp{0%,100%{transform:scale(.3) rotate(0);opacity:0}50%{transform:scale(1) rotate(90deg);opacity:1}}"
        ".blink{animation:bl 1.6s ease-in-out infinite}@keyframes bl{0%,100%{opacity:1}50%{opacity:.25}}"
    )
    return svg(W, H, body, style, f"Player status: {NAME}, level {LEVEL} {CLASS_}")


# ============================================================ ACHIEVEMENTS ===
def build_achievements():
    items = ACHIEVEMENTS[:5]
    cw, gap, H = 180, 15, 250
    W = 1000
    x0 = (W - (len(items) * cw + (len(items) - 1) * gap)) / 2
    defs = [f'<filter id="gl" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="12"/></filter>',
            '<linearGradient id="sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
            '<stop offset=".5" stop-color="#fff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>']
    parts = []
    for i, (ico, title, desc, rar) in enumerate(items):
        x, y = x0 + i * (cw + gap), 18
        ch = H - 36
        col = RARITY.get(rar, CYAN)
        iw, ih = icon_size(ico)
        s = 6 if iw <= 12 else 5
        defs.append(f'<clipPath id="k{i}"><rect x="{n(x)}" y="{y}" width="{cw}" height="{ch}" rx="10"/></clipPath>')
        d = i * .35
        parts.append(
            f'<g class="card" style="animation-delay:{i * .12:.2f}s">'
            f'<rect x="{n(x)}" y="{y}" width="{cw}" height="{ch}" rx="10" fill="#0f0426"/>'
            f'<rect x="{n(x)}" y="{y}" width="{cw}" height="4" rx="2" fill="{col}"/>'
            f'<circle class="halo" style="animation-delay:-{d:.2f}s" cx="{n(x + cw / 2)}" cy="{y + 70}" r="38" fill="{col}" filter="url(#gl)"/>'
            f'<g class="bob" style="animation-delay:-{d:.2f}s">{icon(ico, x + (cw - iw * s) / 2, y + 70 - ih * s / 2, s)}</g>'
            f'{ptext(title, x + cw / 2, y + 128, 2, ICE, "middle")}'
            f'<text x="{n(x + cw / 2)}" y="{y + 162}" text-anchor="middle" font-family="Consolas,Menlo,\'Courier New\',monospace" '
            f'font-size="14" fill="#c4b5ff">{html.escape(desc)}</text>'
            f'<rect x="{n(x + (cw - tw(rar, 2) - 22) / 2)}" y="{y + 178}" width="{tw(rar, 2) + 22}" height="24" rx="12" '
            f'fill="{col}" fill-opacity=".14" stroke="{col}" stroke-opacity=".7"/>'
            f'{ptext(rar, x + cw / 2, y + 183, 2, col, "middle")}'
            f'<g clip-path="url(#k{i})"><g class="shine" style="animation-delay:{1.5 + i * .5:.2f}s">'
            f'<rect x="{n(x - 120)}" y="{y - 40}" width="70" height="{ch + 80}" fill="url(#sh)" transform="rotate(18 {n(x)} {y})"/></g></g>'
            f'<rect x="{n(x)}" y="{y}" width="{cw}" height="{ch}" rx="10" fill="none" stroke="{col}" stroke-opacity=".55" stroke-width="1.5"/>'
            f'</g>')
    body = f'<defs>{"".join(defs)}</defs>{"".join(parts)}'
    style = (
        ".card{opacity:0;animation:in .9s cubic-bezier(.22,1,.36,1) forwards}"
        "@keyframes in{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}"
        ".bob{animation:bob 3s ease-in-out infinite alternate}@keyframes bob{from{transform:translateY(4px)}to{transform:translateY(-6px)}}"
        ".halo{animation:ha 3s ease-in-out infinite alternate}@keyframes ha{from{opacity:.12}to{opacity:.42}}"
        ".shine{animation:sh 5s cubic-bezier(.45,0,.25,1) infinite}@keyframes sh{0%{transform:translateX(0)}30%,100%{transform:translateX(340px)}}"
    )
    return svg(W, H, body, style, "Achievements unlocked")


# ================================================================== FOOTER ===
def build_footer():
    W, H = 1000, 226
    rnd = random.Random(5)
    t1 = "THANKS FOR PLAYING"
    s1 = 5
    t1x, t1y = (W - tw(t1, s1)) / 2, 38
    c = "CONTINUE?"
    cs, ds = 3, 5
    rowW = tw(c, cs) + 22 + tw("9", ds)
    cx0 = (W - rowW) / 2
    dx = cx0 + tw(c, cs) + 22
    digits = "".join(
        f'<g class="dg" style="animation-delay:{i}s">{ptext(str(9 - i), dx, 115, ds, PINK)}</g>'
        for i in range(10))
    ins = "INSERT COIN"
    insx = (W - tw(ins, 3)) / 2
    coin_s = 3
    em, em_css = embers(rnd, 14, W, 150, 230, 160)
    defs = (f'<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="#1e0640"/></linearGradient>'
            f'<linearGradient id="tg" gradientUnits="userSpaceOnUse" x1="0" y1="{t1y}" x2="0" y2="{t1y + 7 * s1}">'
            f'<stop offset="0" stop-color="{YELLOW}"/><stop offset="1" stop-color="{PINK}"/></linearGradient>'
            f'<filter id="bl" x="-20%" y="-80%" width="140%" height="260%"><feGaussianBlur stdDeviation="10"/></filter>'
            f'<path id="t1" d="{pix(t1, t1x, t1y, s1)}"/>' + crt_defs(W, H, 16))
    body = (
        f'<defs>{defs}</defs><g clip-path="url(#frame)">'
        f'<rect width="{W}" height="{H}" fill="url(#bg)"/><g>{stars(rnd, 50, W, H)}</g>{em}'
        f'<use xlink:href="#t1" href="#t1" class="glow" fill="{PINK}" filter="url(#bl)"/>'
        + "".join(f'<use xlink:href="#t1" href="#t1" y="{k}" fill="{mix("#8a2be2", "#14031f", k / 5)}"/>' for k in range(5, 0, -1)) +
        f'<use xlink:href="#t1" href="#t1" fill="url(#tg)"/>'
        f'{ptext(c, cx0, 122, cs, ICE)}{digits}'
        f'<g class="blink">{ptext(ins, insx, 178, 3, YELLOW)}</g>'
        f'<g transform="translate({n(insx - 54)} 172)"><g class="spin">{icon("coin", 0, 0, coin_s)}</g></g>'
        f'<g transform="translate({n(insx + tw(ins, 3) + 24)} 172)"><g class="spin" style="animation-delay:-.6s">{icon("coin", 0, 0, coin_s)}</g></g>'
        + crt_overlay(W, H, 16) + '</g>'
    )
    style = (
        TWINKLE + em_css + CRT_CSS.replace("var(--bh)", f"{H + 240}px") +
        ".glow{animation:gw 3s ease-in-out infinite}@keyframes gw{0%,100%{opacity:.3}50%{opacity:.75}}"
        ".dg{opacity:0;transform-box:fill-box;transform-origin:center;animation:dg 10s linear infinite}"
        "@keyframes dg{0%{opacity:1;transform:scale(1.45)}2.5%{transform:scale(1)}9.6%{opacity:1;transform:scale(1)}10%,100%{opacity:0}}"
        ".blink{animation:bk 1.3s ease-in-out infinite}@keyframes bk{0%,100%{opacity:1}50%{opacity:.15}}"
        ".spin{transform-box:fill-box;transform-origin:center;animation:sp 1.8s ease-in-out infinite}"
        "@keyframes sp{0%,100%{transform:scaleX(1)}50%{transform:scaleX(.08)}}"
    )
    return svg(W, H, body, style, "Thanks for playing! Continue?")


# ================================================================== README ===
def build_readme():
    u = USERNAME
    raw = f"https://raw.githubusercontent.com/{u}/{u}/output"
    typing = "https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=15&duration=2600&pause=900" \
             "&color=05D9E8&center=true&vCenter=true&width=720&height=46&lines=" + \
             ";".join(l.replace(" ", "+").replace("%", "%25").replace("!", "%21") for l in TYPING_LINES)
    sec = lambda key: f'<p align="center"><img src="assets/section-{key}.svg" width="100%" alt="{key}"/></p>'
    status_ico = {"IN PROGRESS": "🟡", "COMPLETE": "🟢", "LOCKED": "🔒"}
    quest_rows = "\n".join(f"| {status_ico.get(s, '⚪')} {q} | `{s}` | **{r}** |" for q, s, r in QUESTS)
    socials = "\n".join(
        f'  <a href="{url}"><img src="https://img.shields.io/badge/{lab}-{col}?style=for-the-badge&logo={logo}&logoColor=white" alt="{lab}"/></a>'
        for lab, logo, col, url in SOCIALS)
    kw = max(len(k) for k, _ in ABOUT) + 1
    about = "\n".join(f"{(k + ':').ljust(kw)} {v}" for k, v in ABOUT)
    games = "\n".join(
        f'  <img src="https://img.shields.io/badge/{lab.replace(" ", "%20")}-{col}?style=for-the-badge'
        + (f'&logo={logo}&logoColor=white' if logo else '') + f'" alt="{lab}"/>'
        for lab, logo, col in GAMES)
    stats_q = "&bg_color=0d0221&title_color=ff2a6d&text_color=d1f7ff&icon_color=05d9e8&ring_color=ff2a6d&hide_border=true&border_radius=12"

    return f"""<!-- Generated by generate.py - edit the CONFIG there and re-run instead of editing by hand -->
<p align="center">
  <img src="assets/header.svg" width="100%" alt="{NAME} - {TAGLINE}"/>
</p>

<p align="center">
  <a href="https://github.com/{u}"><img src="{typing}" alt="Typing intro"/></a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username={u}&label=PLAYERS%20VISITED&color=ff2a6d&style=for-the-badge" alt="Profile views"/>
  <a href="https://github.com/{u}?tab=followers"><img src="https://img.shields.io/github/followers/{u}?label=PARTY%20MEMBERS&style=for-the-badge&color=7b2cff&labelColor=0d0221&logo=github" alt="Followers"/></a>
  <img src="https://img.shields.io/badge/STATUS-READY%20PLAYER%20ONE-05d9e8?style=for-the-badge&labelColor=0d0221" alt="Status"/>
</p>

{sec("about")}

```yaml
{about}
```

{sec("stats")}

<p align="center">
  <img src="assets/player-card.svg" width="100%" alt="Player status card"/>
</p>

{sec("inventory")}

<p align="center">
  <img src="https://skillicons.dev/icons?i={SKILLS}&perline=8&theme=dark" alt="Tech stack"/>
</p>

{sec("battle")}

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={u}&show_icons=true&include_all_commits=true&count_private=true&rank_icon=github{stats_q}" height="170" alt="GitHub stats"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={u}&layout=compact&langs_count=8{stats_q}" height="170" alt="Top languages"/>
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user={u}&background=0D0221&ring=FF2A6D&fire=F9C80E&currStreakNum=D1F7FF&sideNums=D1F7FF&currStreakLabel=05D9E8&sideLabels=05D9E8&dates=A58BFF&stroke=2A0A4A&hide_border=true&border_radius=12" width="100%" alt="Streak"/>
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username={u}&bg_color=0d0221&color=d1f7ff&line=ff2a6d&point=f9c80e&area=true&area_color=7b2cff&title_color=05d9e8&hide_border=true&radius=12" width="100%" alt="Activity graph"/>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{raw}/snake-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="{raw}/snake.svg"/>
    <img src="{raw}/snake-dark.svg" width="100%" alt="Snake eating my contributions"/>
  </picture>
</p>

{sec("achievements")}

<p align="center">
  <img src="assets/achievements.svg" width="100%" alt="Achievements"/>
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username={u}&theme=radical&no-frame=true&no-bg=true&margin-w=6&column=7" alt="GitHub trophies"/>
</p>

{sec("quests")}

<div align="center">

| QUEST | STATUS | REWARD |
|:--|:--:|:--:|
{quest_rows}

</div>

{sec("multiplayer")}

<p align="center"><b>FIND ME IN THE LOBBY OF</b></p>

<p align="center">
{games}
</p>

<p align="center">
{socials}
</p>

<p align="center">
  <img src="assets/footer.svg" width="100%" alt="Thanks for playing"/>
</p>
"""


SNAKE_WORKFLOW = """name: Generate snake

on:
  schedule:
    - cron: "0 */12 * * *"   # twice a day
  workflow_dispatch:
  push:
    branches: [main]

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Generate snake SVGs
        uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/snake.svg?palette=github-light&color_snake=#ff2a6d
            dist/snake-dark.svg?palette=github-dark&color_snake=#ff2a6d&color_dots=#160a2e,#3b0a5c,#7b2cff,#c13cff,#05d9e8

      - name: Push to the output branch
        uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
"""


def write(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"  wrote {path:<34} {len(text.encode()) / 1024:6.1f} KB")


if __name__ == "__main__":
    print("Generating profile...")
    write("assets/header.svg", build_header())
    write("assets/player-card.svg", build_card())
    write("assets/achievements.svg", build_achievements())
    write("assets/footer.svg", build_footer())
    for key, num, title, ico in SECTIONS:
        write(f"assets/section-{key}.svg", build_section(num, title, ico))
    write("README.md", build_readme())
    write(".github/workflows/snake.yml", SNAKE_WORKFLOW)
    print("Done. GAME ON!")

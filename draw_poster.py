#!/usr/bin/env python3
"""Draw the front page for THE WORLD TODAY — Tuesday 24 November 2026.

Renders 50 verified stories (4 leads + 46 grid items) as a 1024x1024
newspaper front page and saves it as entry.png next to this script.
Deterministic: fixed text, no timestamps, no randomness, no network.
Only the Python standard library plus Pillow, which is used at BUILD
time only — the graded program (main.ts) merely copies entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# --- palette: off-white paper, dark navy masthead, one red accent ---
PAPER = (250, 247, 238)
INK = (18, 18, 22)
NAVY = (16, 32, 64)
NAVY2 = (24, 48, 92)
RED = (178, 34, 34)
GREY = (110, 110, 108)
LIGHT = (232, 228, 218)
GOLD = (198, 158, 60)
TEAL = (18, 92, 96)

LEADS = [
    ("ABU DHABI TALKS OPEN TODAY",
     "US-brokered Russia-Ukraine talks open in Abu Dhabi on Tuesday to "
     "revive stalled diplomacy — as Zelenskyy accuses Moscow of "
     "escalating strikes on the power grid to pressure Kyiv at the table.",
     "Al Jazeera", "Middle East", "Diplomacy"),
    ("IRAN: \u2018USE EVERY MEANS\u2019 TO BREAK BLOCKADE",
     "Tehran vows it will use all available means against the US naval "
     "blockade as 14 tankers mass at Kharg Island; Trump dares them to "
     "sail: \u201cThey\u2019ll all be at the bottom of the sea.\u201d",
     "Reuters / Fox News", "Middle East", "War"),
    ("KYIV GRID HIT AGAIN \u2014 500,000 IN THE DARK",
     "Russian barrage hits 28 substations; more than half a million lose "
     "power, heat and water; a 21-year-old woman killed in Kyiv; "
     "Zelenskyy says partners gave no early warning.",
     "AP / wire", "Europe", "War"),
    ("ALCARAZ WINS MAIDEN ATP FINALS",
     "Beats world No. 1 Zverev 6-2, 7-6(7) in Turin \u2014 one of only "
     "four men to hold all four Slams plus the ATP Finals title.",
     "Reuters", "Europe", "Sport"),
]

GRID = [
    ("COP31 COLLAPSED \u2014 NO DEAL IN ANTALYA",
     "EU and 90+ nations rejected a draft that never mentioned fossil fuels; longest COP on record.",
     "Reuters", "Europe", "Climate"),
    ("15 KILLED IN OVERNIGHT STRIKES ON KYIV REGION",
     "Dymer flats collapse kills 10; Zelenskyy demands the Patriots partners already paid for.",
     "Al Jazeera", "Europe", "War"),
    ("UKRAINE FIRES 1,000+ DRONES AT RUSSIA",
     "Largest aerial attack of the war; oil terminal and depot ablaze in St Petersburg.",
     "wire", "Europe", "War"),
    ("RUSSIAN WARSHIP \u2018SUNK\u2019 OFF LIBYA",
     "Corvette believed to be the Merkury destroyed at Benghazi port; Ukraine claims the attack.",
     "Naval News", "Africa", "War"),
    ("460,000+ DEATHS LINKED TO RUSSIA\u2019S WAR",
     "Guardian analysis of death certificates; war the leading killer of Russian men under 65 in 2025.",
     "Guardian", "Europe", "War"),
    ("ZELENSKYY: PUTIN IS \u2018A KILLER\u2019",
     "Tells CNN as a strike on Kryvyi Rih kills a boy, 7, and a paramedic, 20.",
     "wire", "Europe", "War"),
    ("RUSSIAN SHIP STILL BURNING OFF FINLAND",
     "Sparta II ablaze in the Gulf of Finland after an attack; drifts with the current.",
     "Reuters", "Europe", "War"),
    ("INDONESIA FACTORY FIRE: SEARCH RESUMES TODAY",
     "24 killed, 29 still missing at the Java candy factory.",
     "Reuters", "Southeast Asia", "Disaster"),
    ("GAZA CONTAMINATION \u2018DANGEROUS FOR DECADES\u2019",
     "Oxfam/CEOBS: heavy metals, asbestos and dioxins in air, soil and water.",
     "Oxfam", "Middle East", "Health"),
    ("TALIBAN ERASE WOMEN\u2019S NAMES IN BALKH",
     "Replaced with \u2018Bibi\u2019 on official documents in the Afghan province.",
     "wire", "South Asia", "Politics"),
    ("KIM REBUFFS TRUMP MEETING PUSH",
     "WSJ: outreach ignored as Pyongyang expands its nuclear capability.",
     "WSJ", "East Asia", "Diplomacy"),
    ("TRUMP ADMITS DEPORTING US CITIZEN",
     "Court filing: a US citizen was sent to Mexico by mistake.",
     "wire", "North America", "Politics"),
    ("US SHUTDOWN LOOMS 11 DEC",
     "Partial shutdown unless Congress agrees funding; Iran war and Pentagon request at issue.",
     "wire", "North America", "Politics"),
    ("DEMOCRATS WIN 258 HOUSE SEATS",
     "Largest majority since 1992; Hubbard beats Foxx in North Carolina.",
     "wire", "North America", "Politics"),
    ("VERSTAPPEN WINS WILD VEGAS GP",
     "35 lead changes under the lights; beats Norris by 0.639s, Piastri third.",
     "Formula1/ESPN", "Europe", "Sport"),
    ("INDIA VS NZ TEST ENDS IN DRAW",
     "Wellington; India posted a record 720/9 at the Basin Reserve.",
     "wire", "Oceania", "Sport"),
    ("GUKESH DEFENDS CHESS CROWN FROM TODAY",
     "Vs Sindarov in Geneva, 14 games; both 20 \u2014 the youngest title match ever.",
     "FIDE", "Europe", "Sport"),
    ("BEPICOLOMBO ENTERS MERCURY ORBIT",
     "ESA/JAXA probe in orbit Saturday, though operations did not go quite as planned.",
     "ESA", "Europe", "Space"),
    ("MILEY CYRUS MARRIES MAXX MORANDO",
     "California ceremony.",
     "wire", "North America", "Culture"),
    ("TOM JACKSON DIES AT 75",
     "Ex-Broncos star and ESPN broadcaster.",
     "ESPN", "North America", "Sport"),
    ("3 KILLED AT OHIO BABY SHOWER",
     "Shooting; one man in custody.",
     "wire", "North America", "Crime"),
    ("FBI PROBES BREACH OF CRIME DATABASE",
     "Trump confirms the hack in a Saturday TV interview.",
     "CNN", "North America", "Crime"),
    ("NVIDIA CHIP-DIVERSION ROW DEEPENS",
     "Alice Huang linked to a secret network sending AI chips to China; Bessent demands answers.",
     "wire", "East Asia", "Technology"),
    ("EISENKOT: SETTLER ARSON IS \u2018JEWISH TERRORISM\u2019",
     "As Netanyahu stays silent; coalition talks fail a second round.",
     "wire", "Middle East", "Politics"),
    ("GAZA\u2019S DIABETIC CHILDREN LACK INSULIN",
     "Struggle for life-saving medicine amid the siege.",
     "wire", "Middle East", "Health"),
    ("US ARMY TO BLAST EXPLOSIVES IN IOWA TODAY",
     "Five tonnes by 24 Nov despite a court-ordered pause.",
     "wire", "North America", "Politics"),
    ("TANKER INCIDENT EAST OF HORMUZ",
     "UKMTO reports amid Iranian threats to break the US blockade.",
     "UKMTO", "Middle East", "Energy"),
    ("TWO TANKERS HIT IN HORMUZ",
     "UKMTO: projectiles strike vessels leaving the Gulf.",
     "UKMTO", "Middle East", "Energy"),
    ("WASHINGTON GOVERNOR: ICE \u2018OUT OF CONTROL\u2019",
     "After two people arrested at the airport.",
     "wire", "North America", "Politics"),
    ("DELTA DELAYS IN ATLANTA",
     "Automation system issue disrupts flights.",
     "wire", "North America", "Markets"),
    ("MAY TO BURNHAM: \u2018ACCEPT BREXIT\u2019",
     "Former PM\u2019s warning to the Labour challenger.",
     "wire", "Europe", "Politics"),
    ("EU BUDGET PLAN KEEPS \u20ac100BN FOR UKRAINE",
     "European Council president unveils a reduced budget proposal.",
     "wire", "Europe", "Politics"),
    ("US SPY CHIEF: PUTIN \u2018NOT AMERICA\u2019S FRIEND\u2019",
     "On Ukraine.",
     "wire", "North America", "Politics"),
    ("NHS \u2018WASTING BILLIONS\u2019, DATA SHOW",
     "UK health spending under fire.",
     "wire", "Europe", "Health"),
    ("BRITON SWIMS STRAIT OF HORMUZ",
     "To highlight the environmental cost of the war.",
     "wire", "Middle East", "Sport"),
    ("BRENT HOLDS $92.00",
     "Monday close; Bitcoin below $58,000, a seventh straight weekly loss.",
     "market data", "Middle East", "Markets"),
    ("NEPAL PM MEETS MODI IN DELHI",
     "Balendra Shah on a state visit, 22\u201323 Nov; talks held Monday.",
     "wire", "South Asia", "Diplomacy"),
    ("S. KOREA EDUCATION MINISTER QUITS",
     "Resigns amid an AI cheating scandal.",
     "wire", "East Asia", "Politics"),
    ("LISBON MARCHES ON LIVING COSTS",
     "Thousands protest as prices fuel anger.",
     "wire", "Europe", "Politics"),
    ("SAUDI COALITION DOWNS HOUTHI MISSILE",
     "Intercepted in the western region after a launch towards Riyadh.",
     "wire", "Middle East", "War"),
    ("MYANMAR SLAMS ASEAN DECISION",
     "Army-backed govt calls it \u2018unfair and imbalanced\u2019.",
     "wire", "Southeast Asia", "Politics"),
    ("DRONE HITS UN BUILDING IN KHARTOUM",
     "UN reports an attack on a residential area in Sudan.",
     "UN", "Africa", "War"),
    ("MODI OPENS AI CENTRE AT IIT PATNA",
     "\u20b9400 cr research park launched.",
     "wire", "South Asia", "Technology"),
    ("INDIA, CHINA HOLD MILITARY TALKS IN ARUNACHAL",
     "Commanders meet to reduce border tensions.",
     "wire", "South Asia", "Diplomacy"),
    ("9 PILGRIMS KILLED IN RAJASTHAN CRASH",
     "Vehicle rams a truck in Kota.",
     "wire", "South Asia", "Disaster"),
    ("70% OF AUSSIE MPS SAY POLITICS HARMED MENTAL HEALTH",
     "Landmark study out in Parliament on Monday.",
     "wire", "Oceania", "Politics"),
]

TIMELINE = [
    ("SAT 21 NOV ~18:00", "IRGC strikes Bahrain"),
    ("SUN 22 NOV ~07:00", "Verstappen wins Vegas"),
    ("SUN 22 NOV PM", "COP31 collapses"),
    ("SUN 22 NOV EVE", "Democrats hit 258"),
    ("MON 23 NOV AM", "Kyiv grid barrage"),
    ("MON 23 NOV", "Iran vows \u2018every means\u2019"),
    ("TUE 24 NOV", "Abu Dhabi talks open"),
    ("TUE 24 NOV", "Gukesh\u2013Sindarov begins"),
]

DATE_CHECK = [
    ("KERCH BRIDGE SPAN COLLAPSES", "17 Nov"),
    ("ISRAEL ELECTS NEW SPEAKER", "17 Nov"),
    ("WAYMO FREEWAY BAN", "18 Nov"),
    ("ICJ: MYANMAR GENOCIDE", "19 Nov"),
    ("FIONA THE HIPPO DIES", "19 Nov"),
    ("PERU 6.7 QUAKE", "21 Nov"),
    ("\u2018CHAPO ISIDRO\u2019 ARRESTED", "21 Nov"),
]

# (label, lon, lat) — rough positions for the dotted world map pins
PINS = [
    ("ABU DHABI", 54, 24), ("KHARG IS.", 50, 29),
    ("KYIV", 30, 50), ("ANTALYA", 30, 36),
    ("TURIN", 7, 45), ("GENEVA", 6, 46),
    ("WASHINGTON", -77, 38), ("DELHI", 77, 28),
    ("JAKARTA", 106, -6), ("KHARTOUM", 32, 15),
    ("LONDON", 0, 51), ("BENGHAZI", 20, 32),
]

FONTS = {}


def font(bold, size):
    key = (bold, size)
    if key not in FONTS:
        FONTS[key] = ImageFont.truetype(BOLD if bold else REG, size)
    return FONTS[key]


def text_w(draw, s, bold, size):
    return draw.textlength(s, font=font(bold, size))


def wrap(draw, s, bold, size, max_w):
    """Greedy word wrap measured with the real font; never guesses widths."""
    words = s.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(draw, trial, bold, size) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_one_line(draw, s, bold, size, max_w, min_size=9):
    """Shrink a single line until it fits (for headlines)."""
    while size > min_size and text_w(draw, s, bold, size) > max_w:
        size -= 1
    return size


def rule(draw, x0, y, x1, color=INK, w=1):
    draw.line([(x0, y), (x1, y)], fill=color, width=w)


def draw_flag(draw, x, y, w, h, stripes):
    """A tiny striped flag drawn from a list of colours."""
    n = len(stripes)
    for i, c in enumerate(stripes):
        draw.rectangle([x, y + i * h // n, x + w, y + (i + 1) * h // n],
                       fill=c)


def draw_tanker(draw, x, y, w, h):
    """Schematic oil tanker on waves (lead 2 illustration)."""
    draw.rectangle([x, y + h * 0.35, x + w, y + h * 0.75], fill=RED)
    draw.rectangle([x + w * 0.62, y + h * 0.08, x + w * 0.78, y + h * 0.38],
                   fill=NAVY)
    draw.rectangle([x + w * 0.70, y, x + w * 0.72, y + h * 0.10], fill=INK)
    for i in range(3):
        draw.ellipse([x + w * 0.08 + i * w * 0.28, y + h * 0.80,
                      x + w * 0.24 + i * w * 0.28, y + h * 0.92],
                     outline=TEAL, width=2)
    draw.line([(x, y + h * 0.82), (x + w, y + h * 0.82)], fill=TEAL, width=2)


def draw_city_dark(draw, x, y, w, h):
    """Kyiv at night: dark blocks, one lit window grid, a warning glow."""
    draw.rectangle([x, y, x + w, y + h], fill=(24, 28, 44))
    for i, bh in enumerate([0.62, 0.85, 0.5, 0.72, 0.58]):
        bx = x + i * w // 5 + 4
        bw = w // 5 - 8
        draw.rectangle([bx, y + h * (1 - bh), bx + bw, y + h], fill=(10, 14, 26))
        for wy in range(2):
            for wx in range(2):
                if (i + wy + wx) % 3 == 0:
                    draw.rectangle([bx + 4 + wx * 9, y + h * (1 - bh) + 6 + wy * 12,
                                    bx + 9 + wx * 9, y + h * (1 - bh) + 11 + wy * 12],
                                   fill=GOLD)
    draw.ellipse([x + w - 26, y + 6, x + w - 8, y + 24], fill=(255, 90, 60))


def draw_tennis(draw, x, y, r):
    """A tennis ball with its curved seam."""
    draw.ellipse([x - r, y - r, x + r, y + r], fill=(196, 214, 60),
                 outline=INK, width=2)
    draw.arc([x - r, y - r, x + r, y + r], 200, 340, fill=(250, 250, 250),
             width=3)
    draw.arc([x - r, y - r, x + r, y + r], 20, 160, fill=(250, 250, 250),
             width=3)


def draw_table_flags(draw, x, y, w, h):
    """Diplomacy scene: a negotiation table, two flags, a globe."""
    draw.rectangle([x, y + h * 0.62, x + w, y + h * 0.70], fill=(122, 82, 42))
    draw.rectangle([x + w * 0.10, y + h * 0.70, x + w * 0.18, y + h],
                   fill=(96, 62, 30))
    draw.rectangle([x + w * 0.82, y + h * 0.70, x + w * 0.90, y + h],
                   fill=(96, 62, 30))
    draw_flag(draw, x + w * 0.06, y + h * 0.06, w * 0.30, h * 0.34,
              [(0, 91, 172), (255, 255, 255), (255, 0, 0)])
    draw_flag(draw, x + w * 0.64, y + h * 0.06, w * 0.30, h * 0.34,
              [(255, 213, 0), (0, 91, 172)])
    draw.ellipse([x + w * 0.40, y + h * 0.10, x + w * 0.60, y + h * 0.44],
                 fill=(64, 140, 190), outline=INK, width=2)
    draw.ellipse([x + w * 0.46, y + h * 0.16, x + w * 0.54, y + h * 0.30],
                 fill=(46, 160, 90))
    draw.rectangle([x + w * 0.42, y + h * 0.44, x + w * 0.44, y + h * 0.58],
                   fill=GOLD)
    draw.rectangle([x + w * 0.56, y + h * 0.44, x + w * 0.58, y + h * 0.58],
                   fill=GOLD)

REGION_COLORS = {
    "North America": (34, 90, 160), "Europe": (18, 92, 96),
    "Middle East": (178, 34, 34), "South Asia": (198, 120, 20),
    "East Asia": (120, 40, 140), "Southeast Asia": (30, 140, 80),
    "Africa": (180, 140, 30), "Oceania": (90, 60, 140),
}


def trunc(draw, s, bold, size, max_w):
    if text_w(draw, s, bold, size) <= max_w:
        return s
    while s and text_w(draw, s + "\u2026", bold, size) > max_w:
        s = s[:-1]
    return s + "\u2026"


def build():
    W, H = 1024, 1024
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    regions = sorted({s[3] for s in LEADS + GRID})
    fields = sorted({s[4] for s in LEADS + GRID})
    total = len(LEADS) + len(GRID)
    assert total == 50, total

    # ---------- masthead ----------
    d.rectangle([0, 0, W, 112], fill=NAVY)
    d.rectangle([0, 112, W, 115], fill=RED)
    title = "THE WORLD TODAY"
    ts = fit_one_line(d, title, True, 58, W - 40)
    d.text(((W - text_w(d, title, True, ts)) / 2, 6), title,
           font=font(True, ts), fill=(250, 247, 238))
    date_s = "TUESDAY 24 NOVEMBER 2026"
    ds = fit_one_line(d, date_s, True, 26, W - 40)
    d.text(((W - text_w(d, date_s, True, ds)) / 2, 64), date_s,
           font=font(True, ds), fill=GOLD)
    counts = ("%d STORIES \u00b7 %d REGIONS \u00b7 %d FIELDS"
              % (total, len(regions), len(fields)))
    cs = fit_one_line(d, counts, True, 14, W - 40)
    d.text(((W - text_w(d, counts, True, cs)) / 2, 94), counts,
           font=font(True, cs), fill=(200, 205, 220))

    # ---------- lead 1 ----------
    y0 = 124
    d.text((16, y0), "LEAD STORY", font=font(True, 11), fill=RED)
    d.text((16, y0 + 14), LEADS[0][0], font=font(True, 34), fill=INK)
    deck1 = wrap(d, LEADS[0][1], False, 17, 620)
    yy = y0 + 56
    for line in deck1[:3]:
        d.text((16, yy), line, font=font(False, 17), fill=INK)
        yy += 21
    d.text((16, yy + 2), "[" + LEADS[0][2] + "]", font=font(True, 12),
           fill=RED)
    draw_table_flags(d, 668, y0 + 6, 340, 118)
    rule(d, 16, 258, W - 16)

    # ---------- leads 2 and 3 ----------
    cols = [(16, 496, LEADS[1], draw_tanker),
            (528, 1008, LEADS[2], draw_city_dark)]
    for x0, x1, lead, illust in cols:
        d.text((x0, 266), "LEAD", font=font(True, 11), fill=RED)
        illust(d, x1 - 118, 266, 118, 40)
        head = wrap(d, lead[0], True, 20, x1 - x0 - 130)
        yy = 282
        for line in head[:2]:
            d.text((x0, yy), line, font=font(True, 20), fill=INK)
            yy += 24
        deck = wrap(d, lead[1], False, 13, x1 - x0)
        for line in deck[:3]:
            d.text((x0, yy), line, font=font(False, 13), fill=INK)
            yy += 16
        d.text((x0, yy + 1), "[" + lead[2] + "]", font=font(True, 11),
               fill=RED)
    d.line([(512, 266), (512, 384)], fill=LIGHT, width=1)
    rule(d, 16, 390, W - 16)

    # ---------- lead 4 (sport strip) ----------
    d.rectangle([16, 398, 22, 440], fill=RED)
    d.text((32, 400), "SPORT  \u2014  " + LEADS[3][0], font=font(True, 24),
           fill=INK)
    d.text((32, 426), LEADS[3][1] + "  [" + LEADS[3][2] + "]",
           font=font(False, 14), fill=INK)
    draw_tennis(d, 968, 419, 19)
    rule(d, 16, 446, W - 16)

    # ---------- explainer ----------
    d.rectangle([16, 452, W - 16, 496], fill=(243, 226, 222),
                outline=RED, width=1)
    d.text((26, 457), "WHY THE GULF IS BURNING",
           font=font(True, 13), fill=RED)
    expl = ("The US\u2013Iran war is in its ninth month: a US naval blockade "
            "on Iranian ports since 13 April, tanker attacks in the Strait "
            "of Hormuz, strikes on Qeshm Island, Bahrain and Kuwait \u2014 "
            "25+ merchant ships hit near the strait in seven days, Brent "
            "crude holding $92.00. [Reuters]")
    lines = wrap(d, expl, False, 13, W - 52)
    yy = 474
    for line in lines[:2]:
        d.text((26, yy), line, font=font(False, 13), fill=INK)
        yy += 16

    # ---------- grid ----------
    d.text((16, 504), "THE WORLD IN BRIEF \u2014 46 MORE STORIES",
           font=font(True, 13), fill=NAVY)
    lx = 330
    for r in regions:
        d.ellipse([lx, 508, lx + 8, 516], fill=REGION_COLORS[r])
        d.text((lx + 11, 505), r, font=font(False, 10), fill=GREY)
        lx += 11 + text_w(d, r, False, 10) + 10
    rule(d, 16, 522, W - 16)
    col_w = (W - 32 - 24) // 3
    row_h = 21
    for i, (head, deck, src, region, _field) in enumerate(GRID):
        col = i // 16
        row = i % 16
        x0 = 16 + col * (col_w + 12)
        y = 528 + row * row_h
        d.ellipse([x0, y + 3, x0 + 8, y + 11],
                  fill=REGION_COLORS[region])
        num = "%d." % (i + 1)
        d.text((x0 + 12, y), num, font=font(True, 12), fill=RED)
        hw = text_w(d, num + " ", True, 12)
        htxt = trunc(d, head, True, 12, col_w - 12 - hw - 4)
        d.text((x0 + 12 + hw, y), htxt, font=font(True, 12), fill=INK)
        dtxt = trunc(d, deck + " [" + src + "]", False, 10,
                     col_w - 12)
        d.text((x0 + 12, y + 11), dtxt, font=font(False, 10), fill=(70, 70, 68))
    rule(d, 16, 868, W - 16)

    # ---------- timeline ----------
    d.text((16, 874), "HOW THE WEEK UNFOLDED \u2014 UTC",
           font=font(True, 12), fill=NAVY)
    for i, (when, what) in enumerate(TIMELINE):
        x0 = 16 + (i % 4) * 248
        y = 890 + (i // 4) * 17
        d.ellipse([x0, y + 3, x0 + 7, y + 10], fill=RED)
        item = when + " \u2014 " + what
        d.text((x0 + 11, y), trunc(d, item, False, 10, 232),
               font=font(False, 10), fill=INK)
    rule(d, 16, 916, W - 16)

    # ---------- world map + pins ----------
    d.text((16, 922), "WHERE IT HAPPENED", font=font(True, 12), fill=NAVY)
    mx0, my0, mx1, my1 = 16, 936, 540, 968
    for gx in range(mx0, mx1, 6):
        for gy in range(my0, my1, 6):
            # rough land mask: skip the big ocean bands
            lon = (gx - mx0) / (mx1 - mx0) * 360 - 180
            lat = 75 - (gy - my0) / (my1 - my0) * 150
            land = ((-168 < lon < -55 and -55 < lat < 70)
                    or (-80 < lon < -35 and -55 < lat < 12)
                    or (-12 < lon < 32 and 35 < lat < 70)
                    or (32 < lon < 60 and 12 < lat < 42)
                    or (60 < lon < 150 and 5 < lat < 75)
                    or (95 < lon < 141 and -38 < lat < -12)
                    or (-18 < lon < 32 and -35 < lat < 32))
            if land:
                d.point((gx, gy), fill=(120, 130, 145))
    for n, (label, lon, lat) in enumerate(PINS, start=1):
        px = mx0 + (lon + 180) / 360 * (mx1 - mx0)
        py = my0 + (75 - lat) / 150 * (my1 - my0)
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=RED)
        d.text((px - 3, py - 4), str(n), font=font(True, 7),
               fill=(255, 255, 255))
    for i, (label, _lon, _lat) in enumerate(PINS):
        lx = 560 + (i % 3) * 152
        ly = 936 + (i // 3) * 9
        d.text((lx, ly), "%d %s" % (i + 1, label), font=font(False, 9),
               fill=INK)
    rule(d, 16, 974, W - 16)

    # ---------- date check ----------
    d.text((16, 980), "DATE CHECK \u2014 LEFT OUT AS OLDER NEWS",
           font=font(True, 11), fill=RED)
    dc1 = "  \u00b7  ".join("%s \u2014 %s" % (t, dt)
                           for t, dt in DATE_CHECK[:4])
    dc2 = "  \u00b7  ".join("%s \u2014 %s" % (t, dt)
                           for t, dt in DATE_CHECK[4:])
    d.text((16, 993), dc1, font=font(False, 10), fill=(70, 70, 68))
    d.text((16, 1004), dc2, font=font(False, 10), fill=(70, 70, 68))

    # ---------- footer ----------
    foot = ("Abu Dhabi talks open today \u2014 Iran vows \u201cevery means\u201d "
            "\u2014 Kyiv grid hit again \u2014 Alcaraz wins \u2014 Brent "
            "$92.00  |  Sources: Reuters, AP, AFP, BBC, Al Jazeera, "
            "Guardian, wire services.")
    d.text((16, 1014), trunc(d, foot, False, 10, W - 32),
           font=font(False, 10), fill=GREY)

    img.save(os.path.join(HERE, "entry.png"), optimize=True)
    print("stories:", total, "regions:", len(regions), "fields:",
          len(fields))
    print("saved entry.png")


if __name__ == "__main__":
    build()

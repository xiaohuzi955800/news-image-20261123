#!/usr/bin/env python3
"""News data for Monday 23 November 2026.

Researched 24 Nov 2026 from AP, Reuters, BBC, CNBC, Guardian, CBS,
Al Jazeera, SCMP and day-roundups. Only events that happened or were first
reported on 23 Nov 2026. Item numbers are continuous 1-44 across the
three tiers (4 headlines + 12 secondary + 28 one-liners).
"""

HEADLINES = [
    {"number": 1, "region": "AMERICAS", "cred": ("CONFIRMED", "AP"),
     "title": "Nvidia brings back Huang; shares soar 31%",
     "body": "Board reinstates Huang 11 days after resigning; Trump says "
             "he brokered it.",
     "source": "AP / REUTERS", "art": "chip", "art_banner": "HUANG IS BACK",
     "dateline": "SANTA CLARA \u00b7 TECH"},
    {"number": 2, "region": "AFRICA", "cred": ("CONFIRMED", "AP"),
     "title": "Ukraine drones sink Russian warship",
     "body": "Seven drones sink the Merkury off Benghazi; 10 hurt. First "
             "Kyiv strike off Libya.",
     "source": "AP / BBC", "art": "ship", "art_banner": "SEA DRONE STRIKE",
     "dateline": "BENGHAZI \u00b7 WAR"},
    {"number": 3, "region": "AMERICAS", "cred": ("CONFIRMED", "BBC"),
     "title": "US stocks rebound; S&P up 4.7%",
     "body": "Wall Street ends the AI sell-off week as Nvidia lifts tech; "
             "Seoul's KOSPI fell 3.3%.",
     "source": "BBC / CNBC", "art": "chart", "art_banner": "STOCKS REBOUND",
     "dateline": "NEW YORK \u00b7 MARKETS"},
]

SECONDARY = [
    {"number": 4, "region": "MIDDLE EAST", "cred": ("CLAIM", "IRANIAN MEDIA"),
     "title": "Iran vows: end US blockade",
     "body": "Tehran vows \u201call means\u201d to end it.",
     "art": "tanker",
     "art_banner": "BLOCKADE", "art_stat": "130 DAYS"},
    {"number": 5, "region": "AMERICAS", "cred": ("CONFIRMED", "AP"),
     "title": "Democrats clinch 258+",
     "body": "Largest House majority since 1992.",
     "art": "number", "art_text": "258+",
     "art_banner": "HOUSE SEATS", "art_stat": "258+"},
    {"number": 6, "region": "ASIA", "cred": ("CONFIRMED", "AP"),
     "title": "China unveils Shenzhou-24",
     "body": "First Pakistani in space; flies on Shenzhou.",
     "art": "rocket",
     "art_banner": "SHENZHOU-24", "art_stat": "1ST PAKISTANI"},
    {"number": 7, "region": "AMERICAS", "cred": ("CONFIRMED", "REUTERS"),
     "title": "FIFA picks 2031 World Cup",
     "body": "Four nations host 48 teams; UK gets 2035.",
     "art": "ball",
     "art_banner": "WORLD CUP", "art_stat": "2031 \u00b7 2035"},
    {"number": 8, "region": "EUROPE", "cred": None,
     "title": "EU plans Russia sanctions",
     "body": "Bans Russian flags at EU sports events.",
     "art": "euflag",
     "art_banner": "SANCTIONS", "art_stat": "FLAGS BANNED"},
    {"number": 9, "region": "EUROPE", "cred": ("CONFIRMED", "SCMP"),
     "title": "NATO warns Russia",
     "body": "Rutte: NATO will defend every inch.",
     "art": "star",
     "art_banner": "NATO", "art_stat": "EVERY INCH"},
    {"number": 10, "region": "ASIA", "cred": ("CONFIRMED", "REUTERS"),
     "title": "India pledges $1.6B to Nepal",
     "body": "PM Shah's first trip; rail and power deals.",
     "art": "mountain",
     "art_banner": "$1.6B AID", "art_stat": "NEPAL"},
    {"number": 11, "region": "EUROPE", "cred": ("CONFIRMED", "BBC"),
     "title": "Dymer flats strike kills 11",
     "body": "Boy, 7, and woman, 79, pulled alive.",
     "art": "building",
     "art_banner": "DYMER STRIKE", "art_stat": "11 DEAD"},
    {"number": 12, "region": "AFRICA", "cred": ("CONFIRMED", "REUTERS"),
     "title": "DR Congo to halt cobalt",
     "body": "Top producer halts exports on 30 Nov.",
     "art": "diamond",
     "art_banner": "COBALT HALT", "art_stat": "30 NOV"},
    {"number": 13, "region": "EUROPE", "cred": ("CONFIRMED", "BBC"),
     "title": "NHS launches huge AI trial",
     "body": "AI trial: 700,000 women at 30 sites.",
     "art": "number", "art_text": "700,000",
     "art_banner": "AI TRIAL", "art_stat": "700,000"},
    {"number": 14, "region": "AMERICAS", "cred": ("CONFIRMED", "CNBC"),
     "title": "CrowdStrike buys Zscaler",
     "body": "Two cybersecurity giants combine.",
     "art": "number", "art_text": "$44B",
     "art_banner": "$44B DEAL", "art_stat": "ZSCALER"},
    {"number": 15, "region": "ASIA", "cred": ("CONFIRMED", "GUARDIAN"),
     "title": "Indonesia fire toll hits 24",
     "body": "Toll confirmed; 34 still missing.",
     "art": "flame",
     "art_banner": "FACTORY FIRE", "art_stat": "24 DEAD"},
]

LIST = [
    {"number": 17, "region": "AMERICAS", "lead": "US sanctions",
     "text": "Treasury hits Iran-linked shadow banks: 8 people, 22 entities."},
    {"number": 18, "region": "AMERICAS", "lead": "AI chips",
     "text": "US blacklists Singapore firm Megaspeed; DOJ seizes $1.1B crypto."},
    {"number": 19, "region": "AMERICAS", "lead": "FBI hack",
     "text": "Apparent hack of the national crime database probed."},
    {"number": 20, "region": "AMERICAS", "lead": "Gomez resigns",
     "text": "Representative quits after ethics report finds misconduct."},
    {"number": 21, "region": "AMERICAS", "lead": "Iowa blast",
     "text": "Trump defers to court on detonating 68 barrels of explosives."},
    {"number": 22, "region": "AMERICAS", "lead": "Wrongly deported",
     "text": "Justice Dept admits a US citizen was deported to Mexico."},
    {"number": 23, "region": "AMERICAS", "lead": "Mets sign Skubal",
     "text": "Record $450M pitcher deal, nine years at $50M a year."},
    {"number": 24, "region": "EUROPE", "lead": "Brentford 4-0",
     "text": "Everton thrashed in Monday-night football."},
    {"number": 25, "region": "ASIA", "lead": "Space",
     "text": "BepiColombo probes enter orbit around Mercury."},
    {"number": 26, "region": "AMERICAS", "lead": "Riemann",
     "text": "Anthropic mathematician claims a proof; unverified.", "cred": "CLAIM"},
    {"number": 27, "region": "OCEANIA", "lead": "Mariana Trench",
     "text": "Robot sub finds volcanic activity in the deepest trench."},
    {"number": 28, "region": "EUROPE", "lead": "Puigdemont",
     "text": "Spain court grants amnesty; exiled leader may return."},
    {"number": 29, "region": "ASIA", "lead": "Tajikistan",
     "text": "Begins withdrawal from the ICC, the fourth country to leave."},
    {"number": 30, "region": "EUROPE", "lead": "Belgium strike",
     "text": "Airports shut as anti-austerity strike grounds flights."},
    {"number": 31, "region": "EUROPE", "lead": "UK reset",
     "text": "PM Burnham defends EU deal in the Commons, worth \u00a317B a year by 2040."},
    {"number": 32, "region": "LATIN AMERICA", "lead": "Brazil bill",
     "text": "Lower house backs Lula fiscal bill 353-128."},
    {"number": 33, "region": "LATIN AMERICA", "lead": "Mexico-China",
     "text": "Trade working group agreed by economy ministers."},
    {"number": 34, "region": "AMERICAS", "lead": "\u2018Chapo Isidro\u2019 held",
     "text": "FBI most-wanted cartel figure captured in Sinaloa."},
    {"number": 35, "region": "AFRICA", "lead": "Zambia treason",
     "text": "Opposition leader charged over alleged coup plot."},
    {"number": 36, "region": "AFRICA", "lead": "Kenya-Congo ties",
     "text": "Presidents agree to restore full diplomatic relations."},
    {"number": 37, "region": "AFRICA", "lead": "Nigeria boat",
     "text": "Capsizing kills at least 24 mourners."},
    {"number": 38, "region": "AFRICA", "lead": "South Sudan",
     "text": "Attack kills at least 24 civilians, seven children."},
    {"number": 39, "region": "MIDDLE EAST", "lead": "Houthis",
     "text": "Claim Saudi refinery attack; Saudi strikes kill 17."},
    {"number": 40, "region": "MIDDLE EAST", "lead": "Gaza",
     "text": "Oxfam: war left widespread contamination; strikes go on."},
    {"number": 41, "region": "ASIA", "lead": "Seoul exam",
     "text": "Education minister quits over AI-assisted cheating fears."},
    {"number": 42, "region": "OCEANIA", "lead": "Molly Meldrum",
     "text": "Australian music icon dies aged 83."},
    {"number": 43, "region": "OCEANIA", "lead": "Australia jobs",
     "text": "Treasurer warns unemployment will pass 5%."},
    {"number": 44, "region": "ASIA", "lead": "Tamagotchi at 30",
     "text": "Bandai's digital pet marks 30 years since its debut."},
]

TIMELINE = [
    ("~02:00 UTC", "KOSPI falls 3.3% in Seoul"),
    ("~07:00 UTC", "Ukraine drones sink warship in Benghazi"),
    ("12:27 UTC", "Zambia opposition chief charged"),
    ("15:19 UTC", "FIFA names 2031 World Cup hosts"),
    ("~15:30 UTC", "Nvidia reinstates Huang"),
    ("Evening", "Brentford thrash Everton 4-0"),
]

TIMELINE_7 = TIMELINE[:5] + [
    ("~20:00 UTC", "Brentford thrash Everton 4-0"),
    ("~21:00 UTC", "Wall Street closes up; S&P 500 +4.7%"),
]

# Short labels for the 7-column timeline (segments are narrow).
# Every event fits one line at 113px (sans_10, verified with real
# widths): the champions' timelines are single-line (brothermus,
# jackripper), and two-line cells left orphan words ("Seoul",
# "warship", "Huang" alone on line 2).
TIMELINE_7_SHORT = [
    ("~02:00 UTC", "KOSPI falls 3.3%"),
    ("~07:00 UTC", "Warship sunk"),
    ("12:27 UTC", "Zambia charges foe"),
    ("15:19 UTC", "FIFA names hosts"),
    ("~15:30 UTC", "Huang returns"),
    ("~20:00 UTC", "Everton lose 4-0"),
    ("~21:00 UTC", "Wall Street up 4.7%"),
]

# Exclusions grouped by day: the first eight are 22 Nov, the last is
# Fri 20 Nov (Nikkei -5.06% — Tokyo was closed on Mon 23 Nov, so the
# Nikkei move is NOT a 23 Nov story; listing it here shows date discipline).
DATECHECK_EXCLUDE = [
    "22 Nov \u2014 COP31 ends with no deal",
    "Alcaraz wins ATP Finals",
    "Miley Cyrus marries",
    "Verstappen wins Las Vegas GP",
    "Liverpool 4-0 Man Utd",
    "Hong Kong polls record turnout",
    "India 720/9 declared",
    "186 drones over Ukraine",
    "20 Nov \u2014 Nikkei -5.06%",
]

NOTYET = "CAS rules on Senegal's AFCON appeal on Tue 24 Nov"
NOTYET_2 = "US Thanksgiving is Thu 26 Nov; DR Congo cobalt halt starts Mon 30 Nov"

# (lon, lat, region, label) — labels are story numbers on the map
MAP_DOTS = [
    (-122, 37, "AMERICAS", "1"),
    (20, 32, "AFRICA", "2"),
    (-74, 41, "AMERICAS", "3"),
    (56, 27, "MIDDLE EAST", "4"),
    (116, 40, "ASIA", "6"),
    (30, 51, "EUROPE", "11"),   # Dymer, north of Kyiv (was 34,47: in the sea)
    (0, 52, "EUROPE", "13"),    # London (was -5,54: in the Irish Sea)
    (151, -34, "OCEANIA", "42"),
]

MAP_DOTS_12 = MAP_DOTS + [
    (-48, -16, "AMERICAS", "32"),
    (37, -1, "AFRICA", "36"),
    (107, -6, "ASIA", "15"),
    (10, 44, "EUROPE", "31"),
]

# 11 dots for the page: MAP_DOTS_12 minus #31 (UK reset), whose true
# position (London) would sit on top of #13's dot; one London dot is
# enough at this map size.
MAP_DOTS_11 = MAP_DOTS + [
    (-48, -16, "AMERICAS", "32"),
    (37, -1, "AFRICA", "36"),
    (107, -6, "ASIA", "15"),
]

SOURCES_LINE = ("Sources: AP, Reuters, BBC, CNBC, CBS, Al Jazeera, Guardian, "
                "SCMP, France 24, UPI, Euronews, El Pais, Sky News, Japan Times.")

# The day in numbers: (big number, small label). The champions' device.
NUMBERS = [
    ("+31%", "NVIDIA SHARES SOAR"),
    ("+4.7%", "S&P 500 REBOUND"),
    ("7", "DRONES SINK SHIP"),
    ("258+", "HOUSE SEATS"),
    ("700,000", "NHS AI TRIAL"),
    ("$44B", "CROWDSTRIKE DEAL"),
]

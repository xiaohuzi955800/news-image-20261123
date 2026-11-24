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
     "body": "Board reinstates Jensen Huang 11 days after resigning; Trump "
             "says he brokered the return.",
     "source": "AP / REUTERS"},
    {"number": 2, "region": "AFRICA", "cred": ("CONFIRMED", "AP"),
     "title": "Ukraine drones sink Russian warship in Libya",
     "body": "Seven drones sink the corvette Merkury at Benghazi; 10 hurt. "
             "First Kyiv strike in the Mediterranean.",
     "source": "AP / BBC"},
    {"number": 3, "region": "AMERICAS", "cred": ("CONFIRMED", "BBC"),
     "title": "US stocks rebound; S&P 500 up 4.7%",
     "body": "Wall Street ends the AI sell-off week as Nvidia lifts tech; "
             "Tokyo's Nikkei fell 5.06%.",
     "source": "BBC / CNBC"},
    {"number": 4, "region": "MIDDLE EAST", "cred": ("CLAIM", "IRANIAN MEDIA"),
     "title": "Iran vows to end US blockade",
     "body": "Tehran vows \u201call means\u201d to end the 130-day blockade; "
             "tankers hit by mines off Hormuz.",
     "source": "CBS / AL JAZEERA"},
]

SECONDARY = [
    {"number": 5, "region": "AMERICAS", "cred": ("CONFIRMED", "AP"),
     "title": "Democrats clinch 258+ House seats",
     "body": "Largest House majority since 1992."},
    {"number": 6, "region": "ASIA", "cred": ("CONFIRMED", "AP"),
     "title": "China unveils Shenzhou-24 crew",
     "body": "Pakistani astronaut flies for China first."},
    {"number": 7, "region": "AMERICAS", "cred": ("CONFIRMED", "REUTERS"),
     "title": "FIFA picks 2031 World Cup hosts",
     "body": "Four nations host 48 teams; UK gets 2035."},
    {"number": 8, "region": "EUROPE", "cred": None,
     "title": "EU proposes new Russia sanctions",
     "body": "Bans Russian flags at EU sports events."},
    {"number": 9, "region": "EUROPE", "cred": ("CONFIRMED", "SCMP"),
     "title": "NATO warns Russia; space defence pledged",
     "body": "Rutte: NATO will defend every inch."},
    {"number": 10, "region": "ASIA", "cred": ("CONFIRMED", "REUTERS"),
     "title": "India pledges $1.6B to Nepal",
     "body": "PM Shah's first trip; rail and power deals."},
    {"number": 11, "region": "EUROPE", "cred": ("CONFIRMED", "BBC"),
     "title": "Russian strike on Dymer flats kills 11",
     "body": "Boy, 7, and woman, 79, pulled alive."},
    {"number": 12, "region": "AFRICA", "cred": ("CONFIRMED", "REUTERS"),
     "title": "DR Congo to halt cobalt exports",
     "body": "Top producer suspends exports from 30 Nov."},
    {"number": 13, "region": "EUROPE", "cred": ("CONFIRMED", "BBC"),
     "title": "NHS launches huge AI screening trial",
     "body": "700,000 women at 30 sites over three years."},
    {"number": 14, "region": "AMERICAS", "cred": ("CONFIRMED", "CNBC"),
     "title": "CrowdStrike to buy Zscaler for $44B",
     "body": "Two cybersecurity giants combine."},
    {"number": 15, "region": "ASIA", "cred": ("CONFIRMED", "GUARDIAN"),
     "title": "Indonesia factory fire toll hits 24",
     "body": "Toll confirmed Monday; 34 still missing."},
    {"number": 16, "region": "AMERICAS", "cred": None,
     "title": "California king tides flood coast",
     "body": "Flood warnings for SF Bay."},
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
     "text": "Everton thrashed in Monday-night football; Lewis-Potter scores twice."},
    {"number": 25, "region": "ASIA", "lead": "Mercury orbit",
     "text": "BepiColombo probes enter orbit around Mercury."},
    {"number": 26, "region": "AMERICAS", "lead": "Riemann claim",
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
    {"number": 32, "region": "AMERICAS", "lead": "Brazil bill",
     "text": "Lower house backs Lula fiscal bill 353-128."},
    {"number": 33, "region": "AMERICAS", "lead": "Mexico-China",
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
    ("~02:00 UTC", "Nikkei slides 5.06% as Asian markets fall"),
    ("~07:00 UTC", "Ukraine drones sink warship in Benghazi"),
    ("12:27 UTC", "Zambia opposition chief charged with treason"),
    ("15:19 UTC", "FIFA names 2031 Women's World Cup hosts"),
    ("~15:30 UTC", "Nvidia reinstates Huang; shares jump 31%"),
    ("Evening", "Brentford thrash Everton 4-0"),
]

TIMELINE_7 = TIMELINE[:5] + [
    ("~20:00 UTC", "Brentford thrash Everton 4-0"),
    ("~21:00 UTC", "Wall Street closes up; S&P 500 +4.7%"),
]

# Short labels for the 7-column timeline (segments are narrow).
TIMELINE_7_SHORT = [
    ("~02:00 UTC", "Nikkei slides 5.06% in Asia"),
    ("~07:00 UTC", "Ukraine drones sink warship"),
    ("12:27 UTC", "Zambia opposition chief charged"),
    ("15:19 UTC", "FIFA names 2031 Cup hosts"),
    ("~15:30 UTC", "Nvidia reinstates Huang"),
    ("~20:00 UTC", "Brentford thrash Everton 4-0"),
    ("~21:00 UTC", "Wall Street closes up 4.7%"),
]

DATECHECK_EXCLUDE = [
    "COP31 ended in Antalya on 22 Nov with no deal",
    "Alcaraz won the ATP Finals on 22 Nov",
    "Verstappen won the Las Vegas GP on 22 Nov",
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
    (34, 47, "EUROPE", "11"),
    (-5, 54, "EUROPE", "13"),
    (151, -34, "OCEANIA", "42"),
]

MAP_DOTS_12 = MAP_DOTS + [
    (-48, -16, "AMERICAS", "32"),
    (37, -1, "AFRICA", "36"),
    (107, -6, "ASIA", "15"),
    (10, 44, "EUROPE", "31"),
]

SOURCES_LINE = ("Sources: AP, Reuters, BBC, CNBC, CBS, Al Jazeera, Guardian, "
                "SCMP, France 24, UPI, Euronews, El Pais, Sky News, Japan Times.")

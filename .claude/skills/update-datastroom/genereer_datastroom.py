"""Genereer de datastroom van de Uitnodigingsregel als SVG in Npuls-huisstijl.

Gebruik, vanuit de root van de repo:
    python .claude/skills/update-datastroom/genereer_datastroom.py assets/datastroom.svg

Pas alleen het blok GEGEVENS aan. De opmaak eronder volgt vanzelf.
"""

import sys
from xml.sax.saxutils import escape

# ---------------------------------------------------------------------------
# GEGEVENS
# ---------------------------------------------------------------------------
TITEL = "Van data tot gesprek"
ONDERTITEL = "Gegevens die de instelling al heeft, worden een uitnodiging voor een gesprek."
VOET = "CEDA · Npuls · stand november 2026"
PAYOFF = "Onderwijs bewegen."

# Vakken op één rij: kolom 0-3.
#   soort = gegevens (roze) | bewerking (oranje) | uitkomst (groen) | gesprek (geel)
#   regels: eerste regel is de titel; een regel als (tekst, "blauw") wordt blauw (alleen op roze).
VAKKEN = {
    "data": {
        "kolom": 0,
        "soort": "gegevens",
        "regels": [
            "Eigen gegevens",
            "aanmelding, vooropleiding,",
            "verzuim, demografie",
            ("eerdere en huidig cohort", "blauw"),
        ],
    },
    "rekenen": {
        "kolom": 1,
        "soort": "bewerking",
        "regels": [
            "Rekenen in de app",
            "voorbereiden, rangschikken,",
            "kwaliteit meten",
            "met student-signal",
        ],
    },
    "ranglijst": {
        "kolom": 2,
        "soort": "uitkomst",
        "regels": [
            "Ranglijst",
            "studenten op volgorde",
            "van risico, met rapport",
            "over de kwaliteit",
        ],
    },
    "gesprek": {
        "kolom": 3,
        "soort": "gesprek",
        "regels": [
            "Gesprek",
            "SLB'er of mentor",
            "nodigt eerst de",
            "bovenkant van de lijst uit",
        ],
    },
}

# (van, naar, label)
LIJNEN = [
    ("data", "rekenen", ""),
    ("rekenen", "ranglijst", ""),
    ("ranglijst", "gesprek", ""),
]

LEGENDA = [
    ("gegevens", "Gegevens"),
    ("bewerking", "Bewerking"),
    ("uitkomst", "Uitkomst"),
    ("gesprek", "Gesprek"),
]

# ---------------------------------------------------------------------------
# HUISSTIJL (Npuls). Alleen toegestane combinaties: tekst zwart op groen,
# oranje, roze en geel; geel op blauw; blauw op roze. Zwart nooit als achtergrond.
# ---------------------------------------------------------------------------
ORANJE, ZWART, ROZE, BLAUW, GEEL, GROEN = (
    "#DD784B",
    "#000000",
    "#F4D9DC",
    "#3D68EC",
    "#F4D74B",
    "#00AF81",
)
GRIJS = "#6B7280"
SANS = "'General Sans', Arial, Helvetica, sans-serif"
SERIF = "'Cooper Light BT', Georgia, serif"
KLEUR = {"gegevens": ROZE, "bewerking": ORANJE, "uitkomst": GROEN, "gesprek": GEEL}

# ---------------------------------------------------------------------------
# OPMAAK
# ---------------------------------------------------------------------------
W, H = 1200, 380
KOLOM_X = (165, 455, 745, 1035)  # midden van elke kolom
VAK_Y = 150  # bovenkant van de rij
VAK_W, VAK_H = 236, 104
LEGENDA_Y, VOET_Y = 316, 352

out = []


def text(
    x: float,
    y: float,
    s: str,
    size: float = 14,
    weight: int = 400,
    fill: str = ZWART,
    anchor: str = "middle",
    family: str = SANS,
    style: str = "normal",
) -> None:
    out.append(
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
        f'font-style="{style}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>'
    )


def box(
    cx: float,
    y: float,
    w: float,
    h: float,
    fill: str,
    lines: list[tuple],
    rx: float = 12,
    sizes: tuple[float, float] = (15, 12.5),
) -> None:
    """Vak met gecentreerde regels; lines = [(tekst, vet)] of [(tekst, vet, kleur)]."""
    out.append(
        f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
        f'stroke="{ZWART}" stroke-width="1.6"/>'
    )
    line_h = 18
    start = y + h / 2 - (len(lines) - 1) * line_h / 2 + 5
    for i, (s, bold, *kleur) in enumerate(lines):
        text(
            cx,
            start + i * line_h,
            s,
            size=sizes[0] if bold else sizes[1],
            weight=600 if bold or kleur else 400,
            fill=kleur[0] if kleur else ZWART,
        )


def lijn(van: str, naar: str, label: str) -> None:
    start = KOLOM_X[VAKKEN[van]["kolom"]] + VAK_W / 2
    eind = KOLOM_X[VAKKEN[naar]["kolom"]] - VAK_W / 2 - 6
    midden = VAK_Y + VAK_H / 2
    out.append(
        f'<path d="M{start},{midden} L{eind},{midden}" fill="none" stroke="{ZWART}" stroke-width="2.2" '
        f'stroke-linecap="round" marker-end="url(#pijl)"/>'
    )
    if label:
        text((start + eind) / 2, midden - 10, label, size=11.5, fill=GRIJS)


def regels(vak: dict) -> list[tuple]:
    """Zet de regels van GEGEVENS om naar de vorm die box() verwacht."""
    titel, *rest = vak["regels"]
    omgezet = [(titel, True)]
    for r in rest:
        omgezet.append((r[0], False, BLAUW) if isinstance(r, tuple) else (r, False))
    return omgezet


# Achtergrond (wit, ook leesbaar in donkere modus van GitHub) en vormentaal
out.append(f'<rect width="{W}" height="{H}" rx="18" fill="#FFFFFF"/>')
out.append('<g clip-path="url(#kader)" fill="none" stroke-width="5">')
for r, c in [(120, ORANJE), (95, BLAUW), (70, GROEN), (45, GEEL)]:
    out.append(f'<circle cx="1150" cy="40" r="{r}" stroke="{c}" opacity="0.9"/>')
out.append("</g>")

text(40, 62, TITEL, size=30, weight=600, fill=ORANJE, anchor="start")
text(40, 96, ONDERTITEL, size=18, family=SERIF, style="italic", anchor="start")

# Lijnen eerst, zodat de vakken erover liggen
for van, naar, label in LIJNEN:
    lijn(van, naar, label)

for vak in VAKKEN.values():
    rx = 40 if vak["soort"] == "uitkomst" else 12
    box(
        KOLOM_X[vak["kolom"]],
        VAK_Y,
        VAK_W,
        VAK_H,
        KLEUR[vak["soort"]],
        regels(vak),
        rx=rx,
    )

# Legenda
x = 40
for soort, label in LEGENDA:
    out.append(
        f'<rect x="{x}" y="{LEGENDA_Y - 13}" width="18" height="18" rx="5" fill="{KLEUR[soort]}" '
        f'stroke="{ZWART}" stroke-width="1.4"/>'
    )
    text(x + 26, LEGENDA_Y + 1, label, size=13.5, anchor="start")
    x += 26 + len(label) * 7.6 + 34

text(40, VOET_Y, VOET, size=12, fill=GRIJS, anchor="start")
text(W - 40, VOET_Y, PAYOFF, size=13, weight=600, anchor="end")


def beschrijving() -> str:
    """Tekstalternatief voor schermlezers, afgeleid uit GEGEVENS."""

    def naam(v: str) -> str:
        return VAKKEN[v]["regels"][0]

    delen = []
    for van, naar, label in LIJNEN:
        extra = f" ({label})" if label else ""
        delen.append(f"{naam(van)} naar {naam(naar)}{extra}.")
    return " ".join(delen)


svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
    f'aria-labelledby="titel beschrijving">'
    f'<title id="titel">{escape(TITEL)}</title>'
    f'<desc id="beschrijving">{escape(beschrijving())}</desc>'
    f'<defs><clipPath id="kader"><rect width="{W}" height="{H}" rx="18"/></clipPath>'
    f'<marker id="pijl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    f'<path d="M0,0 L10,5 L0,10 z" fill="{ZWART}"/></marker></defs>' + "".join(out) + "</svg>\n"
)
with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write(svg)
print("geschreven:", sys.argv[1])

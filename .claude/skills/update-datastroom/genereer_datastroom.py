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

TOOLKIT_LABEL = "TOOLKIT"
TOOLKIT_FASEN = ["Voorbereiden", "Uitvoeren", "Evalueren en opschalen"]
TOOLKIT_UITLEG = "documenten per fase"

# Vakken in een raster: kolom 0-3, rij 0-1.
#   soort = gegevens (roze) | bewerking (oranje) | uitkomst (groen) | gesprek (geel)
#   regels: eerste regel is de titel; een regel als (tekst, "blauw") wordt blauw (alleen op roze).
VAKKEN = {
    "data": {
        "kolom": 0,
        "rij": 0,
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
        "rij": 0,
        "soort": "bewerking",
        "regels": ["Rekenen", "voorbereiden, rangschikken,", "kwaliteit meten", "met student-signal"],
    },
    "ranglijst": {
        "kolom": 2,
        "rij": 0,
        "soort": "uitkomst",
        "regels": ["Ranglijst", "studenten op volgorde", "van risico, met rapport", "in de app"],
    },
    "gesprek": {
        "kolom": 3,
        "rij": 0,
        "soort": "gesprek",
        "regels": ["Gesprek", "SLB'er of mentor", "nodigt eerst de", "bovenkant van de lijst uit"],
    },
    "benchmark": {
        "kolom": 2,
        "rij": 1,
        "soort": "uitkomst",
        "regels": ["Werkt het hier?", "kwaliteit op eigen data", "in de benchmark"],
    },
    "overzicht": {
        "kolom": 3,
        "rij": 1,
        "soort": "uitkomst",
        "regels": ["Gezamenlijk overzicht", "instellingen vergelijken,", "vrijwillig en geaggregeerd"],
    },
}

# (van, naar, optioneel, label)
LIJNEN = [
    ("data", "rekenen", False, ""),
    ("rekenen", "ranglijst", False, ""),
    ("ranglijst", "gesprek", False, ""),
    ("rekenen", "benchmark", False, ""),
    ("benchmark", "overzicht", True, ""),
]

LEGENDA = [("gegevens", "Gegevens"), ("bewerking", "Bewerking"), ("uitkomst", "Uitkomst"), ("gesprek", "Gesprek")]
LEGENDA_LIJN = "Optioneel"

# ---------------------------------------------------------------------------
# HUISSTIJL (Npuls). Alleen toegestane combinaties: tekst zwart op groen,
# oranje, roze en geel; geel op blauw; blauw op roze. Zwart nooit als achtergrond.
# ---------------------------------------------------------------------------
ORANJE, ZWART, ROZE, BLAUW, GEEL, GROEN = "#DD784B", "#000000", "#F4D9DC", "#3D68EC", "#F4D74B", "#00AF81"
LICHT_ROZE, GRIJS = "#FAEAEA", "#6B7280"
SANS = "'General Sans', Arial, Helvetica, sans-serif"
SERIF = "'Cooper Light BT', Georgia, serif"
KLEUR = {"gegevens": ROZE, "bewerking": ORANJE, "uitkomst": GROEN, "gesprek": GEEL}

# ---------------------------------------------------------------------------
# OPMAAK
# ---------------------------------------------------------------------------
W, H = 1200, 640
KOLOM_X = (165, 455, 745, 1035)  # midden van elke kolom
RIJ_Y = (250, 410)  # bovenkant van elke rij
VAK_W, VAK_H = 236, 104
BAND_Y, BAND_H = 150, 52
LEGENDA_Y, VOET_Y = 584, 620

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
    dashed: bool = False,
    sizes: tuple[float, float] = (15, 12.5),
) -> None:
    """Vak met gecentreerde regels; lines = [(tekst, vet)] of [(tekst, vet, kleur)]."""
    dash = ' stroke-dasharray="6 5"' if dashed else ""
    out.append(
        f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
        f'stroke="{ZWART}" stroke-width="1.6"{dash}/>'
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


def path(d: str, dashed: bool = False, width: float = 2.2, pijl: bool = True) -> None:
    dash = ' stroke-dasharray="7 6"' if dashed else ""
    kop = ' marker-end="url(#pijl)"' if pijl else ""
    out.append(f'<path d="{d}" fill="none" stroke="{ZWART}" stroke-width="{width}" stroke-linecap="round"{dash}{kop}/>')


def positie(vak: dict) -> tuple[float, float]:
    return KOLOM_X[vak["kolom"]], RIJ_Y[vak["rij"]]


def lijn(van: str, naar: str, optioneel: bool, label: str) -> None:
    (x1, y1), (x2, y2) = positie(VAKKEN[van]), positie(VAKKEN[naar])
    if y1 == y2:
        start, eind = x1 + VAK_W / 2, x2 - VAK_W / 2 - 6
        midden = y1 + VAK_H / 2
        path(f"M{start},{midden} L{eind},{midden}", dashed=optioneel)
        if label:
            text((start + eind) / 2, midden - 10, label, size=11.5, fill=GRIJS)
    else:
        # Omlaag uit de onderkant, met een bocht naar de linkerkant van het doel
        start_y, eind_x, eind_y = y1 + VAK_H, x2 - VAK_W / 2 - 6, y2 + VAK_H / 2
        path(f"M{x1},{start_y} C{x1},{eind_y} {x1 + 40},{eind_y} {eind_x},{eind_y}", dashed=optioneel)


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

# Toolkit-band: drie fasen met pijlen ertussen
out.append(f'<rect x="30" y="{BAND_Y}" width="{W - 60}" height="{BAND_H}" rx="14" fill="{LICHT_ROZE}"/>')
band_midden = BAND_Y + BAND_H / 2
text(52, band_midden + 4, TOOLKIT_LABEL, size=11.5, weight=600, fill=GRIJS, anchor="start")
pil_breedte = [len(f) * 9 + 44 for f in TOOLKIT_FASEN]
pil_gap = 60
x = 150
for i, (fase, breedte) in enumerate(zip(TOOLKIT_FASEN, pil_breedte)):
    out.append(f'<rect x="{x}" y="{band_midden - 16}" width="{breedte}" height="32" rx="16" fill="{BLAUW}"/>')
    text(x + breedte / 2, band_midden + 5, fase, size=14.5, weight=600, fill=GEEL)
    if i < len(TOOLKIT_FASEN) - 1:
        path(f"M{x + breedte + 10},{band_midden} L{x + breedte + pil_gap - 16},{band_midden}", width=1.8)
    x += breedte + pil_gap
text(W - 52, band_midden + 4, TOOLKIT_UITLEG, size=13, family=SERIF, style="italic", anchor="end")

# Lijnen eerst, zodat de vakken erover liggen
for van, naar, optioneel, label in LIJNEN:
    lijn(van, naar, optioneel, label)

for vak in VAKKEN.values():
    cx, y = positie(vak)
    rx = 40 if vak["soort"] == "uitkomst" else 12
    box(cx, y, VAK_W, VAK_H, KLEUR[vak["soort"]], regels(vak), rx=rx)

# Legenda
x = 40
for soort, label in LEGENDA:
    out.append(
        f'<rect x="{x}" y="{LEGENDA_Y - 13}" width="18" height="18" rx="5" fill="{KLEUR[soort]}" '
        f'stroke="{ZWART}" stroke-width="1.4"/>'
    )
    text(x + 26, LEGENDA_Y + 1, label, size=13.5, anchor="start")
    x += 26 + len(label) * 7.6 + 34
path(f"M{x},{LEGENDA_Y - 4} L{x + 40},{LEGENDA_Y - 4}", dashed=True, width=2, pijl=False)
text(x + 50, LEGENDA_Y + 1, LEGENDA_LIJN, size=13.5, anchor="start")

text(40, VOET_Y, VOET, size=12, fill=GRIJS, anchor="start")
text(W - 40, VOET_Y, PAYOFF, size=13, weight=600, anchor="end")


def beschrijving() -> str:
    """Tekstalternatief voor schermlezers, afgeleid uit GEGEVENS."""

    def naam(v: str) -> str:
        return VAKKEN[v]["regels"][0]

    delen = [f"{TOOLKIT_LABEL.capitalize()}: {', '.join(TOOLKIT_FASEN)}."]
    for van, naar, optioneel, label in LIJNEN:
        extra = f" ({label})" if label else (" (optioneel)" if optioneel else "")
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

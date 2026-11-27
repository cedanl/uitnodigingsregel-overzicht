"""Genereer het overzicht 'Wat er inmiddels ligt' als SVG in Npuls-huisstijl.

Gebruik, vanuit de root van de repo:
    python .claude/skills/update-datastroom/genereer_aanbod.py assets/aanbod.svg

Pas alleen het blok GEGEVENS aan. De opmaak eronder volgt vanzelf.
"""

import sys
from xml.sax.saxutils import escape

# ---------------------------------------------------------------------------
# GEGEVENS
# ---------------------------------------------------------------------------
TITEL = "Wat er inmiddels ligt"
ONDERTITEL = "Een instelling die wil beginnen, begint niet bij nul."
SLOTREGEL = "Beginnen is geen bouwtraject meer, maar installeren en draaien."
VOET = "CEDA · Npuls · stand november 2026"
PAYOFF = "Onderwijs bewegen."

# Zes kaarten, drie per rij, in leesvolgorde. kleur = blauw | oranje | groen | roze | geel.
KAARTEN = [
    (
        "Methode",
        "blauw",
        ["Uit promotieonderzoek.", "Wetenschappelijk gerepliceerd bij", "zes instellingen en gepubliceerd."],
    ),
    (
        "Pilots",
        "oranje",
        [
            "Praktijkpilots bij mbo-instellingen",
            "met echte data en een vaste",
            "effectmeting.",
        ],
    ),
    (
        "Toolkit en e-learning",
        "groen",
        [
            "Draagvlak, spelregels, het",
            "ethische gesprek en evaluatie.",
            "Plus een e-learningmodule.",
        ],
    ),
    ("Juridisch", "roze", ["Eén sectorbrede DPIA", "voor de Uitnodigingsregel."]),
    (
        "App",
        "geel",
        [
            "Installeren met één commando.",
            "Draait bij de instelling, de",
            "gegevens blijven binnen.",
        ],
    ),
    (
        "Ondersteuning",
        "blauw",
        [
            "Informatiesessie, hulp bij de",
            "data en twee dagen op locatie",
            "met een data scientist.",
        ],
    ),
]

# ---------------------------------------------------------------------------
# HUISSTIJL (Npuls). Alleen toegestane combinaties: tekst zwart op groen,
# oranje, roze en geel; geel op blauw. Zwart nooit als achtergrond.
# ---------------------------------------------------------------------------
ORANJE, ZWART, ROZE, BLAUW, GEEL, GROEN = (
    "#DD784B",
    "#000000",
    "#F4D9DC",
    "#3D68EC",
    "#F4D74B",
    "#00AF81",
)
LICHT_ROZE, GRIJS = "#FAEAEA", "#6B7280"
SANS = "'General Sans', Arial, Helvetica, sans-serif"
SERIF = "'Cooper Light BT', Georgia, serif"
KLEUR = {"blauw": BLAUW, "oranje": ORANJE, "groen": GROEN, "roze": ROZE, "geel": GEEL}

# ---------------------------------------------------------------------------
# OPMAAK
# ---------------------------------------------------------------------------
W, H = 1200, 640
KAART_X = (40, 420, 800)  # linkerkant van elke kolom
KAART_Y = (140, 320)  # bovenkant van elke rij
KAART_W, KAART_H = 360, 156
SLOT_Y, SLOT_H = 500, 56
VOET_Y = 612

out = []


def text(
    x: float,
    y: float,
    s: str,
    size: float = 15,
    weight: int = 400,
    fill: str = ZWART,
    anchor: str = "start",
    family: str = SANS,
    style: str = "normal",
) -> None:
    out.append(
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
        f'font-style="{style}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>'
    )


def kaart(x: float, y: float, label: str, kleur: str, regels: list[str]) -> None:
    out.append(
        f'<rect x="{x}" y="{y}" width="{KAART_W}" height="{KAART_H}" rx="14" fill="#FFFFFF" '
        f'stroke="{ZWART}" stroke-width="1.6"/>'
    )
    # Gekleurde balk links in de kaart
    out.append(f'<rect x="{x + 1}" y="{y + 14}" width="7" height="{KAART_H - 28}" rx="3.5" fill="{KLEUR[kleur]}"/>')
    breedte = len(label) * 8.6 + 28
    out.append(f'<rect x="{x + 24}" y="{y + 20}" width="{breedte}" height="30" rx="15" fill="{KLEUR[kleur]}"/>')
    text(
        x + 24 + breedte / 2,
        y + 40,
        label,
        size=14.5,
        weight=600,
        fill=GEEL if kleur == "blauw" else ZWART,
        anchor="middle",
    )
    for i, regel in enumerate(regels):
        text(x + 26, y + 82 + i * 22, regel)


# Achtergrond (wit, ook leesbaar in donkere modus van GitHub) en vormentaal
out.append(f'<rect width="{W}" height="{H}" rx="18" fill="#FFFFFF"/>')
out.append('<g clip-path="url(#kader)" fill="none" stroke-width="5">')
for r, c in [(120, ORANJE), (95, BLAUW), (70, GROEN), (45, GEEL)]:
    out.append(f'<circle cx="1150" cy="40" r="{r}" stroke="{c}" opacity="0.9"/>')
out.append("</g>")

text(40, 62, TITEL, size=30, weight=600, fill=ORANJE)
text(40, 96, ONDERTITEL, size=18, family=SERIF, style="italic")

for i, (label, kleur, regels) in enumerate(KAARTEN):
    kaart(KAART_X[i % 3], KAART_Y[i // 3], label, kleur, regels)

out.append(f'<rect x="40" y="{SLOT_Y}" width="{W - 80}" height="{SLOT_H}" rx="14" fill="{LICHT_ROZE}"/>')
text(W / 2, SLOT_Y + SLOT_H / 2 + 6, SLOTREGEL, size=18, weight=600, anchor="middle")

text(40, VOET_Y, VOET, size=12, fill=GRIJS)
text(W - 40, VOET_Y, PAYOFF, size=13, weight=600, anchor="end")


def beschrijving() -> str:
    """Tekstalternatief voor schermlezers, afgeleid uit GEGEVENS."""
    kaarten = " ".join(f"{label}: {' '.join(regels)}" for label, _, regels in KAARTEN)
    return f"{ONDERTITEL} {kaarten} {SLOTREGEL}"


svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
    f'aria-labelledby="titel beschrijving">'
    f'<title id="titel">{escape(TITEL)}</title>'
    f'<desc id="beschrijving">{escape(beschrijving())}</desc>'
    f'<defs><clipPath id="kader"><rect width="{W}" height="{H}" rx="18"/></clipPath></defs>' + "".join(out) + "</svg>\n"
)
with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write(svg)
print("geschreven:", sys.argv[1])

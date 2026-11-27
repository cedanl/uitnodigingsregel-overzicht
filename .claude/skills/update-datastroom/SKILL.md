---
name: update-datastroom
description: Werk de twee plaatjes van deze projectrepo bij, de datastroom (assets/datastroom.svg) en het overzicht "Wat er inmiddels ligt" (assets/aanbod.svg). Gebruik bij "update de datastroom", "update het overzicht", "update de infographic", "pas het plaatje aan", of wanneer de app andere invoer of uitvoer krijgt, of het aanbod (toolkit, pilots, ondersteuning) verandert.
---

# Plaatjes bijwerken

- **Datastroom** (`genereer_datastroom.py` → `assets/datastroom.svg`): één rij van links naar rechts: eigen gegevens, rekenen in de app, ranglijst, gesprek. Alleen de Uitnodigingsregel zelf; benchmark en toolkit staan in de README.
- **Wat er inmiddels ligt** (`genereer_aanbod.py` → `assets/aanbod.svg`): zes kaarten die laten zien dat alles klaarligt (methode, pilots, toolkit, juridisch, app, ondersteuning), met een slotregel.

Pas de SVG's nooit met de hand aan.

## Stappen

1. **Bepaal wat er veranderd is.** Lees de secties "Wat er is" en "Overzicht van de tools" in `README.md`. Vraagt de gebruiker om de laatste stand, lees dan ook de README's van de drie tools (zie de links in de tabel).
2. **Pas het blok `GEGEVENS` bovenin het script aan.** Alleen daar. In de datastroom heeft een vak een `kolom` (0-3) en is een lijn `(van, naar, label)`. In het overzicht is een kaart `(label, kleur, regels)`; breek de regels zelf af. Werk ook `VOET` bij met de maand van de stand.
3. **Genereer de SVG** vanuit de root van de repo:
   `python .claude/skills/update-datastroom/genereer_datastroom.py assets/datastroom.svg`
   `python .claude/skills/update-datastroom/genereer_aanbod.py assets/aanbod.svg`
4. **Controleer het resultaat met een screenshot:**
   Eerste keer op deze machine? Installeer dan eerst de browser: `uv run --with playwright playwright install chromium`
   `uv run --with playwright python .claude/skills/update-datastroom/screenshot.py assets/datastroom.svg /tmp/datastroom.png`
   Bekijk de PNG. Loopt tekst buiten een vak, kort dan de tekst in. Maak vakken niet breder.
5. **Houd README en plaatjes gelijk.** Elk vak, elke lijn en elke kaart moet te herleiden zijn tot de README, de tool zelf of de presentaties. Geen verzonnen verbanden. Werk ook de `alt`-tekst van het plaatje in de README bij.

## Huisstijlregels (Npuls)

- Kleuren alleen in toegestane combinaties: zwarte tekst op roze (gegevens), oranje (bewerking), groen (uitkomst) en geel (gesprek); gele tekst op blauw; blauwe tekst op roze. Zwart nooit als achtergrond.
- Witte achtergrond in de SVG zelf, zodat hij ook in het donkere thema van GitHub leesbaar is.
- Lettertype General Sans met Arial als terugval. GitHub laadt geen webfonts in plaatjes, dus in de praktijk zie je Arial.
- Zwarte lijnen met pijlpunt, afgeronde vakken.

## Grenzen

- Datastroom: maximaal vier vakken op één rij. Overzicht: zes kaarten. Komt er meer bij, overleg dan eerst met de gebruiker over een andere indeling in plaats van het plaatje vol te proppen.
- Een vak heet naar wat het doet of oplevert ("Rekenen", "Ranglijst"), niet naar een repo. De naam van de tool staat hooguit in de laatste regel.
- Teksten volgen dezelfde regels als de README: Nederlands, bondig, voor lezers zonder technische voorkennis.

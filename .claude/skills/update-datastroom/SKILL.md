---
name: update-datastroom
description: Werk de datastroom (assets/datastroom.svg) van deze projectrepo bij. Gebruik bij "update de datastroom", "update de infographic", "pas het plaatje aan", of wanneer een tool andere invoer of uitvoer krijgt, een tool bijkomt of de toolkit verandert.
---

# Datastroom bijwerken

De datastroom loopt van links naar rechts: eigen gegevens, rekenen, ranglijst, gesprek. Onder de ranglijst loopt de tak van de benchmark naar het gezamenlijke overzicht. Bovenaan staat de toolkit met haar fasen.

De SVG wordt gegenereerd door `genereer_datastroom.py` in deze map. Pas `assets/datastroom.svg` nooit met de hand aan.

## Stappen

1. **Bepaal wat er veranderd is.** Lees de secties "Wat er is" en "Overzicht van de tools" in `README.md`. Vraagt de gebruiker om de laatste stand, lees dan ook de README's van de drie tools (zie de links in de tabel).
2. **Pas het blok `GEGEVENS` bovenin het script aan.** Alleen daar. Een vak staat in een raster (`kolom` 0-3, `rij` 0-1). Een lijn is `(van, naar, optioneel, label)`. Werk ook `VOET` bij met de maand van de stand.
3. **Genereer de SVG** vanuit de root van de repo:
   `python .claude/skills/update-datastroom/genereer_datastroom.py assets/datastroom.svg`
4. **Controleer het resultaat met een screenshot:**
   Eerste keer op deze machine? Installeer dan eerst de browser: `uv run --with playwright playwright install chromium`
   `uv run --with playwright python .claude/skills/update-datastroom/screenshot.py assets/datastroom.svg /tmp/datastroom.png`
   Bekijk de PNG. Loopt tekst buiten een vak, kort dan de tekst in. Maak vakken niet breder.
5. **Houd README en datastroom gelijk.** Elk vak en elke lijn moet te herleiden zijn tot de README en tot de tool zelf. Geen verzonnen verbanden. Werk ook de `alt`-tekst van het plaatje in de README bij.

## Huisstijlregels (Npuls)

- Kleuren alleen in toegestane combinaties: zwarte tekst op roze (gegevens), oranje (bewerking), groen (uitkomst) en geel (gesprek); gele tekst op blauw (fasen van de toolkit); blauwe tekst op roze. Zwart nooit als achtergrond.
- Witte achtergrond in de SVG zelf, zodat hij ook in het donkere thema van GitHub leesbaar is.
- Lettertype General Sans met Arial als terugval. GitHub laadt geen webfonts in plaatjes, dus in de praktijk zie je Arial.
- Zwarte lijnen met pijlpunt, afgeronde vakken. Een stippellijn betekent optioneel.

## Grenzen

- Maximaal vier kolommen en twee rijen. Komt er meer bij, overleg dan eerst met de gebruiker over een andere indeling in plaats van het plaatje vol te proppen.
- Een vak heet naar wat het doet of oplevert ("Rekenen", "Ranglijst"), niet naar een repo. De naam van de tool staat hooguit in de laatste regel.
- Teksten volgen dezelfde regels als de README: Nederlands, bondig, voor lezers zonder technische voorkennis.

# Besluit: projectrepo Uitnodigingsregel

Issue: [cedanl/Uitnodigingsregel#109](https://github.com/cedanl/Uitnodigingsregel/issues/109)

## Beslissingen (locked)

- **Doel:** dé pagina over de Uitnodigingsregel. Een instelling, collega of partner ziet daar wat het is, wat er allemaal is (toolkit, tools, ondersteuning) en hoe ze ermee aan de slag gaat.
- **Projectrepo, geen coderepo:** alleen documentatie, net als `cedanl/sectorale-informatievoorziening`. De code staat in de drie toolrepo's.
- **Overkoepelt:** `Uitnodigingsregel` (app), `uitnodigingsregel-benchmark` en `student-signal`. `Uitnodigingsregel_datapreparatie` staat er alleen als link bij de gegevens.
- **Naam:** `uitnodigingsregel-overzicht`, gekozen uit vijf opties (`van-data-tot-gesprek`, `vroegtijdig-signaleren`, `uitnodigingsregel-datastroom`, `uitnodigingsregel-project`). Vindbaar naast de drie repo's; zegt dat het een overzicht is. Paginatitel "De Uitnodigingsregel", ondertitel "Van data tot gesprek".
- **Logo:** het nieuwe logo uit `cedanl/Uitnodigingsregel` (`references/logo-uitnodigingsregel.png`, groene achtergrond) bovenaan de README.
- **Opbouw README:** wat het is, van data tot gesprek (datastroom en zeven stappen), wat er is (toolkit, tools, ondersteuning), aan de slag (vijf situaties), overzicht van de tools, hoe goed het werkt, data en bronnen, richting, presentaties, documentatie, contact.
- **Ronde 2:** geen framing als "CEDA levert de techniek, een partner het proces". De techniek is één onderdeel van het aanbod. Geen partnerorganisaties als afzender noemen.
- **Visual:** SVG in Npuls-huisstijl, gegenereerd door de projectskill `.claude/skills/update-datastroom/`. Een stroom van links naar rechts met de toolkit als band erboven. Eigen script, met huisstijl en helpers overgenomen uit sectorale-informatievoorziening.
- **Resultaten:** de kwalitatieve uitkomsten van de pilots en een link naar het gezamenlijke benchmarkoverzicht. Geen cijfers: er zijn nog geen gedeelde uitkomsten van echte instellingen.
- **Ondersteuning:** zoals in de presentaties van 30 september 2026 (informatiesessie, data op orde, twee dagen op locatie, meedenken over financiering, contact met pilotinstellingen).

## Aannames (met confidence)

- De ondersteuning uit de presentaties van september staat nog. *Waarschijnlijk.*
- Er loopt een derde pilot. *Waarschijnlijk* (pitch van 30 september 2026).
- De verkenning voor hbo en wo blijft in algemene termen tot er afspraken met instellingen zijn. *Zeker.*

## Open

- Gedeelde template voor projectrepo's: dit is de tweede. Los issue.

## Deferred

- Verwijzing naar deze repo bovenaan de README's van de drie tools.
- Sectie "Projecten" op het cedanl-profiel (`cedanl/.github`).
- De pitch-PDF `260930_uitnodigingsregel.pdf` committen in `cedanl/clidev-presentaties`, zodat de link werkt.

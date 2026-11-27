# Uitnodigingsregel-overzicht

Projectrepo van CEDA/Npuls. Bevat alleen documentatie: alles over de Uitnodigingsregel op één plek, met verwijzingen naar de toolkit en de drie tools. Geen code, behalve de scripts die de twee plaatjes maken.

## Inhoud

- `README.md`: dé pagina over de Uitnodigingsregel, voor instellingen, collega's en partners. Primaire interface.
- `docs/data-en-bronnen.md`: welke gegevens nodig zijn, hoe je ze klaarzet en waar je meer leest over de methode.
- `docs/hoe-goed-werkt-het.md`: kwaliteit meten, wat de pilots lieten zien en instellingen vergelijken. Niet in de README.
- `docs/richting.md`: drie routes (mbo, hbo en wo, online demo) als leesbaar verhaal. In de README alleen de drie routes in één regel elk.
- `assets/logo-uitnodigingsregel.png`: het logo. Bron: `references/logo-uitnodigingsregel.png` in `cedanl/Uitnodigingsregel`.
- `assets/datastroom.svg`: de datastroom van gegevens tot gesprek, op één rij.
- `assets/aanbod.svg`: het overzicht "Wat er inmiddels ligt" met zes kaarten.
- Beide SVG's nooit met de hand aanpassen; gebruik de skill `update-datastroom` (`.claude/skills/update-datastroom/`).
- `docs/specs/`: beslis-samenvattingen.

## Afspraken

- De README is een complete productpagina: wat de Uitnodigingsregel is, wat er is (toolkit, tools, ondersteuning) en hoe een instelling begint. Geen overzicht van de techniek; de tools zijn één onderdeel van het aanbod.
- Noem geen partnerorganisaties als afzender of eigenaar. Uitzondering: bij de toolkit staat dat die is ontwikkeld binnen de Datacoalitie Datagedreven Onderzoek, met link naar hun site. De pilots zijn "pilots bij mbo-instellingen".
- Nederlands. Schrijf voor lezers zonder technische voorkennis: bondig, direct, geen verkooppraat.
- Link naar de README's en docs van de drie tools; kopieer er niets uit. Houd de tooltabel, de datastroom en `docs/data-en-bronnen.md` gelijk met die repo's.
- Huisstijl: Npuls. Alleen kleurcombinaties uit de huisstijl, General Sans met Arial als terugval, zwarte lijnen. Geen Npuls-logo op de pagina.
- Presentaties staan in `cedanl/clidev-presentaties/exports/`. Link ernaartoe; zet geen PDF's in deze repo.
- Ondersteuning noemen zoals CEDA die aanbiedt in de presentaties. Geen toezeggingen die daar niet staan.
- Noem alleen wat aantoonbaar werkt. Wat nog niet getoetst is, krijgt die vermelding in `docs/richting.md`, niet in de README.
- De README blijft op hoofdlijnen: geen details, voorbehouden, privacy- of juridische kanttekeningen. Open punten horen in issues.

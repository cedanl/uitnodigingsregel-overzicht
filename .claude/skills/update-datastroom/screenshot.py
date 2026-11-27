"""Maak een PNG van de datastroom om te controleren of alles past.

Gebruik, vanuit de root van de repo:
    uv run --with playwright python .claude/skills/update-datastroom/screenshot.py assets/datastroom.svg /tmp/datastroom.png

Ontbreekt de browser, draai dan eenmalig: uvx playwright install chromium
"""

import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright


async def main(svg: str, png: str) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 640})
        await page.goto(Path(svg).resolve().as_uri())
        await page.screenshot(path=png)
        await browser.close()
    print("geschreven:", png)


asyncio.run(main(sys.argv[1], sys.argv[2]))

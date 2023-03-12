import asyncio
from playwright.async_api import Playwright, async_playwright


async def get_screenshots():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.google.com")
        await page.screenshot(path="screenshot.png")
        await browser.close()


asyncio.run(get_screenshots())

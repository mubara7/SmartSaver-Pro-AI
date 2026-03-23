import asyncio
import re
from playwright.async_api import async_playwright

async def get_product_data(url):
    """
    Advanced Scraper with Screenshot & Price Extraction.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        try:
            print(f"🔍 Scanning: {url}...")
            await page.goto(url, wait_until="networkidle", timeout=60000)
            
            # --- NEW: Take Screenshot for the Dashboard ---
            await page.screenshot(path="product_shot.png")
            
            await page.wait_for_timeout(2000)
            page_content = await page.content()
            
            # Price Extraction Logic
            price_matches = re.findall(r'[\d,]+\.\d{2}|[\d,]+', page_content)
            potential_prices = [int(p.replace(',', '').split('.')[0]) for p in price_matches if len(p) > 2]
            
            final_price = 0
            if potential_prices:
                valid_prices = [p for p in potential_prices if 10 < p < 1000000]
                final_price = valid_prices[0] if valid_prices else 0

            stock_status = "In Stock"
            if any(word in page_content.lower() for word in ["out of stock", "currently unavailable", "sold out"]):
                stock_status = "Out of Stock"

            await browser.close()
            return {"price": final_price, "status": stock_status}

        except Exception as e:
            await browser.close()
            return {"error": str(e), "price": 0, "status": "Unknown"}
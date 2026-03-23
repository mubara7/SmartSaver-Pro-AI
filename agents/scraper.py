import requests
from bs4 import BeautifulSoup
from utils.logger import logger

def get_product_data(url):
    """Simple Scraper using BeautifulSoup (Deployment Friendly)"""
    try:
        logger.info(f"Scanning URL: {url}")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Note: Ye generic selectors hain, website ke mutabiq change ho sakte hain
            title = soup.find("h1").get_text(strip=True) if soup.find("h1") else "Product Not Found"
            
            # Price dhoondne ka tareeka (Common classes)
            price_tag = soup.select_one(".price_color, .a-price-whole, #priceblock_ourprice")
            price = price_tag.get_text(strip=True) if price_tag else "0.0"
            
            return {"title": title, "price": price}
        else:
            logger.error(f"Failed to fetch data. Status code: {response.status_code}")
            return None
            
    except Exception as e:
        logger.error(f"Scraper Error: {e}")
        return None
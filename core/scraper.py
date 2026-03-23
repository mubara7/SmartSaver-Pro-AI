import requests
from bs4 import BeautifulSoup

def simple_scraper(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Note: Ye selector har website ke liye alag hota hai, 
        # filhal ye ek generic example hai.
        price_tag = soup.find("span", {"class": "a-offscreen"}) # Amazon example
        if price_tag:
            return float(price_tag.text.replace('$', '').replace(',', ''))
        return "Price Not Found"
    except Exception as e:
        return f"Error: {e}"
import re

def clean_price(price_str):
    """Clean price string and convert to float (e.g., '$2,016.00' -> 2016.0)"""
    if not price_str:
        return 0.0
    # Sirf numbers aur decimal point nikalna
    clean_val = re.sub(r'[^\d.]', '', str(price_str))
    try:
        return float(clean_val)
    except ValueError:
        return 0.0

def format_currency(amount, currency_symbol="$"):
    """Format numbers back to currency style for display"""
    return f"{currency_symbol}{amount:,.2f}"
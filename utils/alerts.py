def send_price_alert(product_name, current_price, target_price):
    """
    Price drop hone par user ko notify karne ka logic.
    """
    if current_price <= target_price:
        message = f"🔥 ALERT: {product_name} ki price drop ho gayi hai! Ab {current_price} hai."
        print(message) # Real SaaS mein yahan SMS/Email ka code aayega
        return True
    return False
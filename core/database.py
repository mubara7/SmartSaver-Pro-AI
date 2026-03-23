import json
import os

DB_FILE = "user_watchlist.json"

def save_to_watchlist(user_data):
    """Product aur Target Price ko save karne ke liye"""
    data = []
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            data = json.load(f)
    
    data.append(user_data)
    
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_watchlist():
    """Saari saved products wapis lane ke liye"""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return []
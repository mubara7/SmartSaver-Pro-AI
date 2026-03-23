import logging
import sys

# Logging setup taake pata chale backend pe kya ho raha hai
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app_log.log"), # Ye ek file bana dega logs ki
        logging.StreamHandler(sys.stdout)   # Ye terminal pe show karega
    ]
)

logger = logging.getLogger("SmartSaverPro")
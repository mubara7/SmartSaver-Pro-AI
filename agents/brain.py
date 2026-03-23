import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from utils.logger import logger
from agents.tools import clean_price

load_dotenv()

def send_alert_email(product, price, target, url):
    msg = EmailMessage()
    msg.set_content(f"""
    SmartSaver Pro: STRATEGIC BUY ENTRY DETECTED!

    Product: {product}
    Current Market Price: {price}
    Your Target Budget: {target}

    The AI Agent has confirmed this is an optimal time to purchase.
    Access the deal here: {url}
    """)

    msg['Subject'] = f"🚀 ACTION REQUIRED: {product} Price Alert!"
    msg['From'] = os.getenv("EMAIL_USER")
    msg['To'] = os.getenv("ALERT_RECEIVER") or os.getenv("EMAIL_USER")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            smtp.send_message(msg)
        return True
    except Exception as e:
        print(f"Email Error: {e}")
        return False

def run_shopping_agent(product_name, current_price, target_price, currency, stock_status, url):
    # Temperature 0.1 rakha hai taake logic strong rahe aur details bhi aayein
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0.1 
    )

    # UPDATED LOGIC: AI ko strictly bataya hai ke kab BUY bolna hai
    prompt = ChatPromptTemplate.from_template("""
    You are a Senior Procurement Specialist. 
    Compare Current Price ({curr}{price}) with User's Target ({curr}{target}).

    STRICT DECISION RULE:
    - IF Current Price <= Target Price AND Stock is 'In Stock', you MUST start with '**VERDICT: BUY**'.
    - DO NOT suggest waiting if the price is already within or below the target. 

    ANALYSIS DATA:
    - Product: {product}
    - Current Price: {curr}{price}
    - User's Target: {curr}{target}
    - Stock Status: {stock}

    STRUCTURE YOUR RESPONSE:
    1. Start with '**VERDICT: BUY**' or '**VERDICT: WAIT**' based on the rule.
    2. MARKET ANALYSIS: Explain why the current price is a great entry or why it's too high.
    3. RISK ASSESSMENT: Mention stock availability.
    4. FINAL RECOMMENDATION: Give a clear 1-sentence action.
    """)

    chain = prompt | llm
    response = chain.invoke({
        "product": product_name,
        "price": current_price,
        "target": target_price,
        "curr": currency,
        "stock": stock_status
    })
    
    result_str = response.content

    # Email trigger logic remains same
    if "VERDICT: BUY" in result_str.upper():
        send_alert_email(product_name, f"{currency}{current_price}", f"{currency}{target_price}", url)
    
    return result_str
import streamlit as st
import pandas as pd
import numpy as np
import os
from agents.brain import run_shopping_agent
from agents.scraper import get_product_data

st.set_page_config(page_title="SmartSaver Pro | AI", layout="wide")

# FORCE RED LABELS CSS
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    label[data-testid="stWidgetLabel"], .stWidgetLabel p, label {
        color: #FF0000 !important; 
        font-weight: 900 !important; 
        font-size: 20px !important;
        text-transform: uppercase !important;
    }
    .stTextInput div div input, .stNumberInput div div input {
        background-color: #1a1a1a !important; color: #ffffff !important;
    }
    .status-box { padding: 20px; border-radius: 15px; text-align: center; font-weight: bold; color: white !important; font-size: 1.5rem; margin-bottom: 20px;}
    .buy-signal { background: linear-gradient(90deg, #00c851, #007e33); }
    .wait-signal { background: linear-gradient(90deg, #ffbb33, #ff8800); }
    .reasoning-box {
        background-color: #050505; padding: 20px; border-radius: 10px;
        border: 1px solid #00d4ff; color: #00ff41; font-family: 'Courier New', monospace;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00d4ff;'>🌌 SmartSaver Pro AI</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("<h2 style='color: #1E90FF;'>🛠️ CONTROL PANEL</h2>", unsafe_allow_html=True)
    with st.container(border=True):
        p_name = st.text_input("Product Name", "Books Test")
        p_url = st.text_input("Store Link")
        currency = st.selectbox("Currency", ["$", "PKR", "£", "€"])
        t_price = st.number_input(f"Target Price", value=25)
        execute_btn = st.button("🚀 INITIATE ANALYSIS", use_container_width=True)

with col2:
    st.markdown("<h2 style='color: #00d4ff;'>📊 INTELLIGENCE DASHBOARD</h2>", unsafe_allow_html=True)
    
    if execute_btn and p_url:
        with st.spinner("🕵️ Agent Working..."):
            # FIXED: Removed asyncio.run()
            data = get_product_data(p_url)
            
            if data:
                curr_price = data.get("price", "0.0")
                stock = "In Stock" # Default for books test
                
                # Clean price if it's a string like "£51.77"
                import re
                numeric_price = float(re.sub(r'[^\d.]', '', str(curr_price)))
                
                response = run_shopping_agent(p_name, numeric_price, t_price, currency, stock, p_url)
                
                if "VERDICT: BUY" in response.upper():
                    st.markdown('<div class="status-box buy-signal">✅ VERDICT: BUY ENTRY DETECTED</div>', unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.markdown('<div class="status-box wait-signal">⚠️ VERDICT: STRATEGIC WAIT</div>', unsafe_allow_html=True)

                m1, m2, m3 = st.columns(3)
                m1.metric("Live Price", f"{currency}{numeric_price}")
                m2.metric("Target Gap", f"{currency}{round(t_price - numeric_price, 2)}")
                m3.metric("Stock Status", stock)
                
                st.markdown("### 📝 AI Reasoning Report")
                st.markdown(f"<div class='reasoning-box'>{response}</div>", unsafe_allow_html=True)
            else:
                st.error("Could not fetch data from URL. Please check the link.")
    else:
        st.info("Fill the Control Panel and click 'Initiate Analysis'.")
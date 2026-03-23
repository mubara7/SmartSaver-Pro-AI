import streamlit as st
import pandas as pd
import numpy as np
import asyncio
import os
from agents.brain import run_shopping_agent
from agents.scraper import get_product_data

st.set_page_config(page_title="SmartSaver Pro | AI", layout="wide")

# FORCE RED LABELS CSS
st.markdown("""
    <style>
    /* Full Black Background */
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    
    /* TARGETING ALL POSSIBLE LABEL CLASSES TO MAKE THEM RED */
    /* Product Name, Store Link, Target Price labels will be RED */
    label[data-testid="stWidgetLabel"], .stWidgetLabel p, label {
        color: #FF0000 !important; 
        font-weight: 900 !important; 
        font-size: 20px !important;
        text-transform: uppercase !important;
        display: block !important;
    }

    /* Input Fields Styling */
    .stTextInput div div input, .stNumberInput div div input, .stSelectbox div div {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 2px solid #333 !important;
    }

    /* Metric Cards */
    [data-testid="stMetric"] { background: #121212 !important; border: 1px solid #333 !important; border-radius: 12px; }
    [data-testid="stMetricValue"] > div { color: #00d4ff !important; }
    
    /* Verdict Boxes */
    .status-box { padding: 20px; border-radius: 15px; text-align: center; font-weight: bold; color: white !important; font-size: 1.5rem; margin-bottom: 20px;}
    .buy-signal { background: linear-gradient(90deg, #00c851, #007e33); }
    .wait-signal { background: linear-gradient(90deg, #ffbb33, #ff8800); }
    
    /* Reasoning Terminal Style */
    .reasoning-box {
        background-color: #050505;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #00d4ff;
        color: #00ff41; /* Matrix Green for detail */
        font-family: 'Courier New', monospace;
        white-space: pre-wrap;
    }
    </style>
    """, unsafe_allow_html=True)

# Main Title
st.markdown("<h1 style='text-align: center; color: #00d4ff; font-weight: bold;'>🌌 SmartSaver Pro AI</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Side Heading (Control Panel)
    st.markdown("<h2 style='color: #1E90FF; font-weight: 900; margin-bottom: 20px;'>🛠️ CONTROL PANEL</h2>", unsafe_allow_html=True)
    
    with st.container(border=True):
        # In labels ka color ab "RED" nazar ana chahye
        p_name = st.text_input("Product Name", "Books Test")
        p_url = st.text_input("Store Link")
        currency = st.selectbox("Currency", ["$", "PKR", "£", "€"])
        t_price = st.number_input(f"Target Price", value=2500)
        execute_btn = st.button("🚀 INITIATE ANALYSIS", use_container_width=True)

    if os.path.exists("product_shot.png"):
        st.image("product_shot.png", caption="Live Preview")

with col2:
    st.markdown("<h2 style='color: #00d4ff; font-weight: bold; margin-bottom: 20px;'>📊 INTELLIGENCE DASHBOARD</h2>", unsafe_allow_html=True)
    
    if execute_btn and p_url:
        with st.spinner("🕵️ Agent Working..."):
            data = asyncio.run(get_product_data(p_url))
            curr_price, stock = data.get("price", 0), data.get("status", "Unknown")
            
            response = str(run_shopping_agent(p_name, curr_price, t_price, currency, stock, p_url))
            
            if "VERDICT: BUY" in response.upper():
                st.markdown('<div class="status-box buy-signal">✅ VERDICT: BUY ENTRY DETECTED</div>', unsafe_allow_html=True)
                st.success("📧 Alert Sent Successfully!")
                st.balloons()
            else:
                st.markdown('<div class="status-box wait-signal">⚠️ VERDICT: STRATEGIC WAIT</div>', unsafe_allow_html=True)

            m1, m2, m3 = st.columns(3)
            m1.metric("Live Price", f"{currency}{curr_price}")
            m2.metric("Target Gap", f"{currency}{t_price - curr_price}", delta=t_price - curr_price)
            m3.metric("Stock Status", stock)
            
            # AI Detail Section
            st.markdown("<h3 style='color: #ffffff;'>📝 AI Reasoning Report</h3>", unsafe_allow_html=True)
            st.markdown(f"<div class='reasoning-box'>{response}</div>", unsafe_allow_html=True)
    else:
        st.info("Fill the Control Panel and click 'Initiate Analysis'.")
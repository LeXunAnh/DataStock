import streamlit as st
import pandas as pd
from datetime import datetime as dt
import sys
import os


st.set_page_config(
    page_title="Stock Market App",
    page_icon="📊",
    layout="wide"
)

# Hide Streamlit default menu & footer
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Title
st.title("💵 Stock Market Analysis App 💵")
st.markdown(
    """
    Welcome to the **Stock Market Analysis App** 📈.  
    Use this tool to explore market data, track stock performance,  
    and analyze trends.
    """
)

# Info Cards
col1, col2, col3 = st.columns(3)
# Define market hours
market_open_hour = 9  # 9:00 AM
market_close_hour = 15  # 3:00 PM
is_weekend = dt.now().weekday() >= 5  # Saturday (5) and Sunday (6)

if is_weekend:
    market_status = "Closed"
else:
    if market_open_hour <= dt.now().hour < market_close_hour:
        market_status = "Open"
    else:
        market_status = "Closed"

with col1:
    st.metric("📅 Today", dt.now().strftime("%Y-%m-%d"))
with col2:
    st.metric("💹 Market Status", market_status)

st.markdown("---")



# Footer
st.markdown("---")
st.caption("© 2025 Stock Market App | Demo")
st.caption("© Data from SSI-FC-DATA/vnstock")

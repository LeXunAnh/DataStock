import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from db import get_connection
from dotenv import load_dotenv

load_dotenv(dotenv_path="D:\PyFile\MarketAnalysis v0.2\datapipe\config\.env")

def fetch_symbols():
    conn = get_connection()
    df = pd.read_sql("SELECT symbol FROM stock_list WHERE market='HOSE' AND LENGTH(symbol)=3", conn)
    conn.close()
    return df["symbol"].tolist()

def fetch_ohlc(symbol):
    conn = get_connection()
    query = f"""
        SELECT tradingdate, open, high, low, close, volume
        FROM stock_price
        WHERE symbol = %s
        ORDER BY tradingdate
    """
    df = pd.read_sql(query, conn, params=(symbol,))
    conn.close()
    return df

# Streamlit UI
st.title("📈 Stock Price Dashboard (HOSE)")

symbols = fetch_symbols()
selected_symbol = st.selectbox("Select a stock symbol", symbols)

df = fetch_ohlc(selected_symbol)

if not df.empty:
    fig = go.Figure(data=[go.Candlestick(
        x=df['tradingdate'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    )])
    fig.update_layout(title=f"{selected_symbol} OHLC Chart", xaxis_title="Date", yaxis_title="Price")
    st.plotly_chart(fig)
else:
    st.warning("No data available for this symbol.")
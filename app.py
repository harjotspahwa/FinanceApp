import pandas as pd
import numpy as np
import yfinance as yf
import streamlit as st

st.write("""
## Trial launch of stock app based on streamlit

Below are a few sample charts for ***Tata Steel***
""")

offline = True
_ticker = 'TATASTEEL.NS'
stock = yf.Ticker(_ticker)

if offline :
    hist = pd.read_csv(r'TataSteel.csv')
else:
    hist = tata.history(period="max")

st.write("""
### Open

""")

st.line_chart(hist.Open)

st.write("""
### High

""")

st.line_chart(hist.High)

st.write("""
### Low

""")

st.line_chart(hist.Low)

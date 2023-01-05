"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.read_csv ("clients_test.csv",index_col=0)

st.write (df.head())

x = st.slider('x')  # 👈 this is a widget

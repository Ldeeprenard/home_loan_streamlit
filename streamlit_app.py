"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.read_csv ("clients_test.csv",index_col=1)

st.write ("affichage de quelques clients")

st.write (df.sample(5))

st.text_input("ID du client", key="clientid")

if st.session_state.clientid in df.index:

    st.write(df.loc[st.session_state.clientid])
else:
    st.write ("le client n'existe pas")
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.read_csv ("clients_test.csv",index_col=0)

st.write ("affichage de quelques clients")

st.write (df.sample(5))

st.text_input("Veuillez entrer l'ID du client", key="clientid")
clientbox = st.selectbox('Ou le selectionner dans la liste',df.index)

if clientbox:
    clientid = clientbox

if st.session_state.clientid:
    clientid = int (st.session_state.clientid)


if clientid in df.index:

    df.loc[clientid]

    st.session_state.clientid = None
    clientid = None


else:
    st.write ("le client n'existe pas")
    st.session_state.clientid = None
    clientid = None


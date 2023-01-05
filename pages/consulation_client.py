import streamlit as st
import pandas as pd

def tableau(client):
    client.montant_credits_total

st.markdown("# Consultation client")
st.sidebar.markdown("# Consultation client")

df = pd.read_csv ("clients_test.csv",index_col=0)

st.write ("affichage de quelques clients")

st.write (df.sample(5))

clientbox = st.selectbox('Selectionnez le client dans la liste',df.index)


if clientbox in df.index:

    client = df.loc[clientbox]
    client
    tableau(client)

else:
    st.write ("le client n'existe pas")




import streamlit as st
import pandas as pd

def tableau(client):
    st.metric("age", round(client.Age), delta=round(df.Age.median()), delta_color="inverse", help="Age du client par rapport à l'âge médian", label_visibility="visible")
    st.metric("Montant du prêt", client.AMT_CREDIT, delta=df.AMT_CREDIT.median(), delta_color="inverse", help="Montant du prêt demandé par rapport au prêt médian", label_visibility="visible")


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




import streamlit as st
import pandas as pd

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


df = pd.read_csv ("clients_test.csv",index_col=0)

st.write ("affichage de quelques clients")

st.write (df.sample(5))

clientbox = st.selectbox('Selectionnez le client à consulter dans la liste',df.index)


if clientbox in df.index:

    df.loc[clientbox]

else:
    st.write ("le client n'existe pas")



import streamlit as st
import pandas as pd
import numpy
import altair as alt

st.set_page_config(layout="wide")

@st.experimental_memo
def load_df():
    
    df = pd.read_csv ("clients_test.csv",index_col=0).convert_dtypes (convert_floating=True)
    df = df.replace ("inconnu",numpy.nan)
    return df.apply (pd.to_numeric)


df = load_df()

def tableau(client):

    tab1 = client
    tab2 = df.describe().loc[["mean","min","50%","max"]]

    st.dataframe (pd.concat ([tab1,tab2],axis=0),height=200)

st.markdown("# Consultation client")

st.sidebar.markdown("# Consultation client")

def graph():
    c = alt.Chart(df).transform_density("Age",as_=['Age', 'density']).mark_area(orient='horizontal').encode(y='Age:Q',x=alt.X('density:Q',stack='center',impute=None,title=None,axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),)).properties(width=100).configure_facet(spacing=0).configure_view(stroke=None)

    st.altair_chart(c)



clientbox = st.selectbox('Selectionnez le client dans la liste',df.index)


if clientbox in df.index:

    client = df.loc[[clientbox]]
    tableau(client)
    graph()

else:
    st.write ("le client n'existe pas")




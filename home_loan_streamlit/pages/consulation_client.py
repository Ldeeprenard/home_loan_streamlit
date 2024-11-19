import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.experimental_memo
def load_df():

    df = pd.read_csv ("clients_test.csv",index_col=0)

    df.loc [0,:] = 0

    return df.apply (pd.to_numeric)


df = load_df()

def tableau(client):

    tab1 = client
    tab2 = df.describe().loc[["mean","min","50%","max"]]

    st.dataframe (pd.concat ([tab1,tab2],axis=0).style.set_precision(0),height=200)

st.markdown("# Consultation client")

st.sidebar.markdown("# Consultation client")

def graph():

    ageclient = client.YEARS_EMPLOYED.values
    revenuclient = client.AMT_INCOME_TOTAL.values
    fig,ax = plt.subplots(1,2,figsize =(15,5))


    sns.boxplot (x=df.YEARS_EMPLOYED,ax=ax[0])
    ax[0].axvline (ageclient,c="r",ls='--',label="client")
    ax[0].set_title ("Nombre d'années travaillés")

    sns.violinplot (x=df.AMT_INCOME_TOTAL,ax=ax[1])
    ax[1].axvline (revenuclient,c="r",ls='--',label="client")
    ax[1].set_xlim (0,.8e6)
    ax[1].set_title ("Revenus")

    plt.legend()
    st.pyplot(fig)

def warning():

    st.subheader ("Avertissement")

    if client.dette_due_actuelle_total.values>50000:
        st.markdown ("#### :red[Ce client est fortement endetté]")
    elif client.accord_pret_moy.values<5:
        st.markdown ("#### :red[Beaucoup de prêts demandés ont été refusés]")
    else:
        st.write ("Aucun avertissement à afficher pour ce client")



clientbox = st.selectbox('Selectionnez le client dans la liste.',df.index,index=48744)


if clientbox == 0:
    st.write ("#### Selectionnez un client pour continuer.")

else:


    client = df.loc[[clientbox]]
    tableau(client)
    graph()
    warning()

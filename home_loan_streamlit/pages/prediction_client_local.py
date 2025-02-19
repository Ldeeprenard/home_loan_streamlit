import streamlit as st
import joblib
import requests
import json
import numpy
import pandas as pd

ML_SERVE = 'http://127.0.0.1:5001/invocations'
path = "C://Users//Lrenard//Documents//openclassroom//projet 7//project_actif//mlflow_server//mlartifacts//"

feats = joblib.load ("colonnes_home_loan.joblib")
headers = {'Content-Type' : 'application/json'}
run_id = None
predict_btn = None
experiment_id = None
@st.experimental_memo
def load_df():
    
    df = pd.read_csv ("clients_test.csv",index_col=0)

    df.loc [0,:] = 0

    return df.apply (pd.to_numeric)


df = load_df()

def data_to_dico (labels,data):

    dico = dict()

    for label,chiffre in zip (labels,data):
        dico[label] = chiffre

    return dico


st.markdown("# Prediction")
st.sidebar.markdown("# Prediction")


st.header("Prédiction de la capacité d'un client à rembourser un emprunt")


st.subheader ("informations client")

st.write ("#### Selectionnez un client où entrez directement les données")

box = st.checkbox ("entrer les données manuellement")






if box:

    col1,col2,col3,col4 = st.columns (4)

    with col1:
        YEARS_EMPLOYED = st.number_input("Nombre d'années d'emploi",min_value=0., value=1., step=1.)

    with col2:
        Age	 = st.number_input('Age de la personne',value=20., step=1.)

    with col3:
        AMT_INCOME_TOTAL = st.number_input('Revenus',min_value=0, value=10000, step=100)

    st.subheader ("Information crédit demandé")

    col5,col6,col7,col8 = st.columns (4)

    with col5:
        AMT_CREDIT = st.number_input('valeur du crédit demandé',min_value=0., value=5000., step=100.)

    with col6:
        AMT_GOODS_PRICE = st.number_input('Prix du bien à acheter',min_value=0., value=5000., step=100.)

    st.subheader ("information prêts précédents")

    col9,col10,col11,col12 = st.columns (4)

    with col9:
        nb_credit = st.number_input('nombre de crédits contractés',min_value=0, value=2, step=1)
        demande_credit_med = st.number_input('Somme médiane demandée lors des précédants crédits',min_value=0, value=100, step=1)
        duree_credit_med = st.number_input('Durée médiane des crédits',min_value=0, value=100, step=100)

    with col10:                                    
        jour_dernier_credit = st.number_input('combien de jours avant la fin du dernier crédit',min_value=0., value=0., step=1.) 
        credit_accord_med = st.number_input('Somme médiane accordée',min_value=0., value=2., step=1.)
        retard_payement_total = st.number_input('Retard des paiements cumulés sur tous les crédits',min_value=0., value=3., step=1.)

    with col11:
        montant_credits_total = st.number_input('Montant total des crédits contractés',value=3500., step=100.)
        valeur_biens_med = st.number_input('valeur médiane des biens achetés',min_value=0., value=1000., step=1.)
        Somme_non_remboursee_total = st.number_input('Somme non remboursées sur des emprunts terminés',value=35., step=1.)

    with col12:
        dette_due_actuelle_total = st.number_input('Dette actuelle relative à ces crédits',value=0., step=100.)
        accord_pret_moy  = st.number_input('Moyenne des crédits accordés',min_value=0., value=1., step=1.,max_value=10.)
        not_ext	 = st.number_input("Moyenne des notes sur le client provenant d'organismes extérieurs",value=5., step=1.)  

    datas = [AMT_INCOME_TOTAL,AMT_CREDIT,AMT_GOODS_PRICE,YEARS_EMPLOYED,nb_credit,jour_dernier_credit,montant_credits_total,dette_due_actuelle_total,demande_credit_med,
                credit_accord_med,valeur_biens_med,accord_pret_moy,duree_credit_med,retard_payement_total,Somme_non_remboursee_total,Age,not_ext]
                        

    predict_btn = st.button('Prédire')

else:
    clientbox = st.selectbox('id client : ',df.index,index=48744)

    if clientbox != 0:

        datas = df.loc[clientbox].values
        st.table (df.loc[[clientbox]])
        predict_btn = st.button('Prédire')

    


if predict_btn:

    data_dico = data_to_dico (feats,datas)

    st.write (datas)

    request_data = json.dumps ({"dataframe_records": [data_dico]})

    response = requests.post (ML_SERVE,request_data,headers=headers)
    st.write (response.text)

    if response.json()["predictions"][0] ==[0]:
        st.write ("Le modèle prédit un remboursement du client")
    else:
        st.write ("Le modèle prédit un défaut de remboursement du client")

    run_id = response.json()["predictions"][2]
    experiment_id = response.json()["predictions"][1]

    st.write ("experiment",experiment_id,"run",run_id)


if run_id and experiment_id:

    st.write ("Voici le graphique associé pour plus d'explications. Les couleurs roses et bleues ainsi que les valeurs à l'intérieur indiquent respectivement\
                l'influence positive ou négative de chaque variable et leur poids sur le résultat")
    st.write ("Il est a noté que ce graphique n'affiche que les 10 variables les plus déterminantes dans l'estimation")
    import PIL
    image = PIL.Image.open (path+experiment_id+"//"+run_id+"//artifacts//"+run_id+".png")
    st.image (image)

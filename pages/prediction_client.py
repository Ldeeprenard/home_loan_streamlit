import streamlit as st
import joblib
import requests
import json
azure_path ="https://artefactsmlflow.blob.core.windows.net/predictions/2/"
ML_SERVE = 'http://192.168.1.10:5001/invocations'
feats = joblib.load ("colonnes_home_loan.joblib")
headers = {'Content-Type' : 'application/json'}
run_id = None

def data_to_dico (labels,data):

    dico = dict()

    for label,chiffre in zip (labels,data):
        dico[label] = chiffre

    return dico



st.markdown("# Prediction")
st.sidebar.markdown("# Prediction")


st.title("Prédiction de la capacité d'un client à rembourser un emprunt")

AMT_INCOME_TOTAL = st.number_input('Revenus',
                                min_value=0., value=3.87, step=1.)

AMT_CREDIT = st.number_input('valeur du crédit demandé',
                            min_value=0., value=28., step=1.)

AMT_GOODS_PRICE = st.number_input('Prix du bien à acheter',
                                min_value=0., value=5., step=1.)

YEARS_EMPLOYED = st.number_input("Nombre d'années d'emploi",
                                    min_value=0., value=1., step=1.)

nb_credit = st.number_input('nombre de crédits contractés',
                                min_value=0, value=1425, step=100)

jour_dernier_credit = st.number_input('combien de jours avant la fin du dernier crédit',
                                    min_value=0., value=3., step=1.)

montant_credits_total = st.number_input('Montant total des crédits contractés',
                            value=35., step=1.)

dette_due_actuelle_total = st.number_input('Dette actuelle relative à ces crédits',
                            value=-119., step=1.)
demande_credit_med = st.number_input('Somme médiane demandée lors des précédants crédits',
                                min_value=0., value=3.87, step=1.)

credit_accord_med = st.number_input('Somme médiane accordée',
                            min_value=0., value=28., step=1.)

valeur_biens_med = st.number_input('valeur médiane des biens achetés',
                                min_value=0., value=5., step=1.)

accord_pret_moy  = st.number_input('Moyenne des crédits accordés',
                                    min_value=0., value=1., step=1.)

duree_credit_med = st.number_input('Durée médiane des crédits',
                                min_value=0, value=1425, step=100)

retard_payement_total = st.number_input('Retard des paiements cumulés sur tous les crédits',
                                    min_value=0., value=3., step=1.)

Somme_non_remboursee_total = st.number_input('Somme non remboursées sur des emprunts terminés',
                            value=35., step=1.)

Age	 = st.number_input('Age de la personne',
                            value=-119., step=1.)
not_ext	 = st.number_input("Moyenne des notes d'organismes extérieurs",
                            value=-140., step=1.)                               

predict_btn = st.button('Prédire')

datas = [AMT_INCOME_TOTAL,AMT_CREDIT,AMT_GOODS_PRICE,YEARS_EMPLOYED,nb_credit,jour_dernier_credit,montant_credits_total,dette_due_actuelle_total,demande_credit_med,
            credit_accord_med,valeur_biens_med,accord_pret_moy,duree_credit_med,retard_payement_total,Somme_non_remboursee_total,Age,not_ext]


if predict_btn:

    data_dico = data_to_dico (feats,datas)


    request_data = json.dumps ({"dataframe_records": [data_dico]})
    response = requests.post (ML_SERVE,request_data,headers=headers)

    if response.json()["predictions"][0] ==[0]:
        st.write ("Le modèle prédit un remboursement du client")
    else:
        st.write ("Le modèle prédit un défaut de remboursement du client")

    run_id = response.json()["predictions"][1]


if run_id:

    st.write ("Voici le graphique associé pour plus d'explications. Les couleurs roses et bleues ainsi que les valeurs à l'intérieur indiquent respectivement\
                l'influence positive ou négative de chaque variable et leur poids sur le résultat")
    st.write ("Il est a noté que ce graphique n'affiche que les 10 variables les plus déterminantes dans l'estimation")
    st.image (azure_path+run_id+"/artifacts/"+run_id+".png")




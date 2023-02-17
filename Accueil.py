import streamlit as st
import requests
import random


st.set_page_config(layout="wide")
st.markdown("# Accueil")
st.sidebar.markdown("# Accueil")

switch = False
st.header ("Bienvenue sur le site du projet 7 DS")

st.write ("Cette partie du projet permet de rendre accessible les informations sur les clients présents dans la base fournie par Home Loan")
st.write ("Vous pourrez également prédire le remboursement d'un prêt en entrant les informations nécessaire sur le client.")

st.write ("Je confie la tâche de combler l'espace vide au modèle GPT-2.")



API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer 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"}


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

if 'output' not in st.session_state:
	st.session_state["output"] = query({
		"inputs": "This site is part of OpenClassroom's Data Scientist Project 7 and allows for easy visualization of customer data provided by the Home Loan bank. It also allows for predicting if the customer will be able to repay the loan.",
		"parameters": {"min_length": 50,"max_length":200,"temperature":random.randrange(0.1,100),"repetition_penalty":random.randrange(100)},
	})


st.write (st.session_state["output"])
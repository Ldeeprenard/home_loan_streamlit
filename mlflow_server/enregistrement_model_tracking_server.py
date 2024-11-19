'''
Ce script a pour tâche d'enregistrer le modèle final sur un serveur mlflow afin de le déployer.
Il entraine le modèle, créer une pipeline de transformation, créer un kernel pour shap,
créer une fonction personnalisée pour que le predict envoit également les résultats shap. 

'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import shap
from lightgbm import LGBMClassifier
import joblib
from mlflow.models.signature import infer_signature
import mlflow.sklearn
from mlflow import MlflowClient
import mlflow
import matplotlib.pyplot as plt


# chargement des ressources

path = r"C:\Users\Lrenard\Documents\openclassroom\projet 7\\"
server = "http://192.168.1.10:5000"
#server = "http://localhost:5000"
df = pd.read_csv(path+"final_tab_train.csv",index_col=0)[["TARGET","AMT_INCOME_TOTAL","AMT_CREDIT","AMT_GOODS_PRICE","DAYS_EMPLOYED","nb_credit","jour_dernier_credit","montant_credits_total","dette_due_actuelle_total",
                                  "demande_credit_med","credit_accordé_med","valeur_biens_med","accord_prêt_moy","durée_credit_med","retard_payement_total","Somme_non_remboursée_total","Age","not_ext"]]
df = df.dropna()

df = df.rename ({"DAYS_EMPLOYED":"YEARS_EMPLOYED","credit_accordé_med":"credit_accord_med","accord_prêt_moy":"accord_pret_moy","durée_credit_med":"duree_credit_med","Somme_non_remboursée_total":"Somme_non_remboursee_total"},axis=1)

 
params = {"n_estimators":260,
                "class_weight":"balanced",
                "learning_rate":0.01,
                "max_depth" : -1,
                "num_leaves":60,
                "colsample_bytree":0.613,
                "subsample":0.708,
                "max_bin":407,
                "reg_alpha":3.564,
                "reg_lambda":4.930,
                "min_child_weight": 6,
                "min_child_samples":165,
                "verbose":-1,
                "n_jobs":-1
}

# automatisation des tâches : imputer les valeurs manquantes, réduire et centrer les données entrantes puis prédire

pipeline = Pipeline([
('imputer', SimpleImputer(missing_values=np.nan, strategy='mean')),
('normal',StandardScaler()),
('lgmb',LGBMClassifier(**params))
])

pipeline.fit (df.drop("TARGET",axis=1),df.TARGET)

# réduction des données d'entrainement pour créer un shap beaucoup plus rapide à l'exécution 
# de base avec lgbm, cela peut prendre plusieurs minutes pour une seule prédiction, soit un temps de calcul conséquent

X = shap.kmeans (df.drop("TARGET",axis=1),1000)

# enregistrement du kernel qui servira à interpréter toutes les prédictions futures

explainer = shap.KernelExplainer (pipeline.predict, X)



ex_filename = 'explainer.bz2'
joblib.dump(explainer, filename=ex_filename, compress=('bz2', 9))


# création d'une classe personnalisée pour que le server mlflow envoit en plus des prédictions les résultats shap

class ShapModel(mlflow.pyfunc.PythonModel):
    def __init__(self, model):
        self.model = model
        self.explainer = joblib.load ("explainer.bz2")

    def predict(self,context, inputs):

        if mlflow.get_experiment_by_name ("predictions_azure_blob"):

            self.experiment = mlflow.set_experiment ("predictions_azure_blob")

        else:
            mlflow.create_experiment ("predictions_azure_blob","wasbs://predictions@artefactsmlflow.blob.core.windows.net")
            self.experiment = mlflow.set_experiment ("predictions_azure_blob")

        with mlflow.start_run () as self.run:
            self.fig,self.ax = plt.subplots(1,1)
            self.client_data = inputs.iloc[0]
            self.shap_values_single = self.explainer.shap_values(self.client_data, nsamples=1000)
            shap.plots.waterfall (shap.Explanation(values=self.shap_values_single, base_values=self.explainer.expected_value, data=self.client_data), show=False)
            plt.tight_layout()
            mlflow.log_figure (self.fig,str(self.run.info.run_id)+".png")

        return self.model.predict(inputs),self.experiment.experiment_id,str(self.run.info.run_id)
'''
shapapa = ShapModel(pipeline)

xx = df.drop("TARGET",axis=1)

shapapa.predict (None,xx.iloc[[1]])

'''
# enregistrement du modèle sur le serveur mlflow

signature = infer_signature(df.drop("TARGET",axis=1),df.TARGET)
mlflow.tracking.set_tracking_uri(server)

mlflow.set_experiment ("home_loan_pred_shap")
    

with mlflow.start_run(run_name="model_explainer") as run:

    shap_model = ShapModel(pipeline)

    mlflow.pyfunc.log_model(
        python_model=shap_model,
        artifact_path="home-loan-artifact",
        registered_model_name="home-loan-shap",
        signature = signature,
        conda_env="conda.yaml"
    )
    ex_filename = 'explainer.bz2'
    joblib.dump(explainer, filename=ex_filename, compress=('bz2', 9))

    mlflow.log_artifact ("explainer.bz2","home-loan-artifact")

# mise en production version stage

client = MlflowClient()
client.transition_model_version_stage(
    name="home-loan-shap",
    version=1,
    stage="Staging"
)


#!/usr/bin/env sh

# Set environment variable for the tracking URL where the Model Registry resides
#export MLFLOW_TRACKING_URI=http://localhost:5000

# Serve the production model from the model registry
#mlflow models serve -m "models:/sk-learn-random-forest-reg-model/Production"
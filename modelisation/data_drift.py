import lightgbm as lgb
import pandas as pd
import numpy as np

import joblib
from sklearn.model_selection import train_test_split
from evidently.report import Report
from evidently.metric_preset import ClassificationPreset

df = pd.read_csv("final_tab_train.csv",index_col=0)[["TARGET","AMT_INCOME_TOTAL","AMT_CREDIT","AMT_GOODS_PRICE","DAYS_EMPLOYED","nb_credit","jour_dernier_credit","montant_credits_total","dette_due_actuelle_total",
                                  "demande_credit_med","credit_accordé_med","valeur_biens_med","accord_prêt_moy","durée_credit_med","retard_payement_total","Somme_non_remboursée_total","Age","not_ext"]]
df = df.dropna()

df = df.rename ({"DAYS_EMPLOYED":"YEARS_EMPLOYED","credit_accordé_med":"credit_accord_med","accord_prêt_moy":"accord_pret_moy","durée_credit_med":"duree_credit_med","Somme_non_remboursée_total":"Somme_non_remboursee_total"},axis=1)
model = joblib.load ("pipeline_home_loan.joblib")


train_data = df.sample (n=5000)
actual_data = df.sample (n=5000)

model.fit (train_data.drop("TARGET",axis=1),train_data.TARGET)

train_pred = model.predict (train_data.drop("TARGET",axis=1))
current_pred = model.predict (actual_data.drop("TARGET",axis=1))

reference_data = pd.DataFrame ({"target":train_data.TARGET,"prediction":train_pred})
reference_data = reference_data.join (train_data.drop("TARGET",axis=1))


current_data = pd.DataFrame ({"target":actual_data.TARGET,"prediction":current_pred})
current_data = current_data.join (actual_data.drop("TARGET",axis=1))

classification_performance_report = Report(metrics=[
    ClassificationPreset(),
])

classification_performance_report.run(reference_data=reference_data, current_data=current_data)

classification_performance_report.save_html("data_drift.html")

classification_performance_report.show(mode='inline')
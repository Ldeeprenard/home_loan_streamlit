import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV, train_test_split
import mlflow
import pandas as pd
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMClassifier


server = "http://192.168.1.10:5000"
mlflow.tracking.set_tracking_uri(server)

df = pd.read_csv("../../final_tab_train.csv",index_col=0)[["TARGET","AMT_INCOME_TOTAL","AMT_CREDIT","AMT_GOODS_PRICE","DAYS_EMPLOYED","nb_credit","jour_dernier_credit","montant_credits_total","dette_due_actuelle_total",
                                  "demande_credit_med","credit_accordé_med","valeur_biens_med","accord_prêt_moy","durée_credit_med","retard_payement_total","Somme_non_remboursée_total","Age","not_ext"]]
df = df.dropna()

df = df.rename ({"DAYS_EMPLOYED":"YEARS_EMPLOYED","credit_accordé_med":"credit_accord_med","accord_prêt_moy":"accord_pret_moy","durée_credit_med":"duree_credit_med","Somme_non_remboursée_total":"Somme_non_remboursee_total"},axis=1)

Feat,tar = df.drop("TARGET",axis=1),df.TARGET

X,x,Y,y = train_test_split (Feat,tar,random_state=786)

params = {"n_estimators":3000,
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
experiment = mlflow.set_experiment("home_loan_scoring")

class CustomLGBM(LGBMClassifier):
    '''
    A custom random forest classifier.
    The RandomForestClassifier class is extended by adding a callback function within its fit method.
    '''
    def fit(self, X, y, **kwargs):
        super().fit(X, y)
        # if a "callback" key is passed, call the "callback" function by passing the fitted estimator
        if 'callback' in kwargs: 
            kwargs['callback'](self)
        return self


class Logger:
    '''
    Logger class stores the test dataset,
    and logs sklearn random forest estimator in rf_logger method.
    '''
    def __init__(self, test_X, test_y):
        self.test_X = test_X
        self.test_y = test_y

    def rf_logger(self, model):

        with mlflow.start_run(nested=True):
            # mlflow.log_param("n_estimators", model.n_estimators)
            # mlflow.log_param("learning_rate", model.learning_rate)
            # mlflow.log_param("max_depth", model.max_depth)
            # mlflow.log_param("num_leaves", model.num_leaves)
            mlflow.log_params(model.get_params())
            mlflow.log_metric("score", model.score(self.test_X, self.test_y))
            pred = model.predict_proba (self.test_X)
            mlflow.log_metric("roc_auc",roc_auc_score(self.test_y, pred[:,1]))


        return None


crf = CustomLGBM(**params,random_state=9)
param_grid = {
    'n_estimators': range (10,300,50),
    'learning_rate': np.random.uniform(0,1,5),
    "max_depth" : [-1,5,10],
    "num_leaves":[30,60],

}


# Use custom random forest classifier while defining the estimator for grid search 
grid = GridSearchCV(crf, param_grid, cv=2, refit=True)


# Instantiate Logger with test dataset
logger = Logger(x, y)


# start outer mlflow run and perform grid search with cross-validation
with mlflow.start_run(run_name = "grid_search"):
    # while calling GridSearchCV object's fit method pass logger.rf_logger
    # logger.rf_logger takes care of logging each fitted model during gridsearch
    grid.fit(X, Y, callback = logger.rf_logger,scoring="roc_auc")

    # log the best estimator fround by grid search in the outer mlflow run 
"""     mlflow.log_param("n_estimators", grid.best_params_['n_estimators'])
    mlflow.log_param("learning_rate", grid.best_params_['learning_rate'])
    mlflow.log_metric("score", grid.score(x, y))
    mlflow.sklearn.log_model(grid.best_estimator_, 'best_lgb_model') """
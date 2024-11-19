## Projet DS 7: Modèle de scoring pour la prédiction de défaut de paiement
> Par Maxence Thériot

## 📋 Présentation du Projet
Ce projet vise à développer un modèle de scoring permettant à Home Credit Default Risk, une société financière américaine, de prédire la probabilité de défaut de paiement de ses clients. Le modèle s'appuie sur une base de données complète comprenant des informations sur les clients, leurs antécédents de crédit, leurs revenus et autres données socio-économiques.

## 🎯 Objectifs du projet:
- **Prédire la probabilité de défaut de paiement** des clients de Home Credit.
- **Construire un tableau de bord (dashboard)** accessible aux employés permettant de consulter les clients et lancer des prédictions.
- **Utiliser pleinement les capacités de la librairie MLFlow** pour un travail d'équipe efficace et une gestion optimale du développement du modèle.

## 🔧 Méthodologie:
Le projet a été mené en plusieurs étapes:

1. **Préparation des données:**
   - Nettoyage et transformation des données provenant de différentes sources (application, bureau, previous_app, installments).
   - Création de nouvelles features en utilisant des techniques de feature engineering.
   - Gestion des valeurs manquantes et des outliers.

2. **Sélection des variables:**
   - Utilisation de RFECV pour déterminer le nombre optimal de variables.
   - Utilisation de RFE pour sélectionner les variables les plus pertinentes.
   - Sélection finale de 17 variables sur 37.

3. **Choix du modèle:**
   - Évaluation de différents modèles de machine learning en utilisant la métrique ROC_AUC.
   - Sélection du modèle LGBMClassifier pour ses performances et sa rapidité d'exécution.

4. **Entraînement et optimisation du modèle:**
   - Entraînement du modèle LGBMClassifier et optimisation des hyperparamètres.
   - Analyse du data drift pour garantir la robustesse du modèle à l'évolution des données.

5. **Déploiement du modèle:**
   - Utilisation de MLFlow pour le tracking et le serving du modèle.
   - Création d'une pipeline Sklearn pour standardiser et imputer les valeurs manquantes.
   - Développement d'une fonction héritée de Pyfunc pour la prédiction et l'explicabilité.

6. **Création d'un dashboard avec Streamlit:**
   - Développement d'une interface utilisateur pour la consultation des clients et le lancement de prédictions.
   - Intégration de graphiques et de données explicatives.

7. **Déploiement de la web app sur Azure:**
   - Conteneurisation de l'application Streamlit avec Docker.
   - Déploiement automatique sur Azure à l'aide de Github Actions.

## 📈 Résultats:
- Le modèle LGBMClassifier a obtenu un score ROC_AUC de 0.75, ce qui est significatif pour la prédiction de défaut de paiement.
- Le tableau de bord Streamlit permet aux employés d'accéder aux prédictions du modèle et aux informations des clients de manière simple et interactive.
- Le projet a démontré l'efficacité de MLFlow pour la gestion du développement du modèle et la collaboration d'équipe.

## 🚀 Défis et perspectives:
- Le projet a nécessité une gestion attentive des données et des ressources informatiques.
- Les services gratuits utilisés (MLFlow, Azure, Github Actions) ont des limitations en termes de performance.
- Le projet pourrait être amélioré en utilisant des services Azure plus performants et en intégrant des techniques de Deep Learning.

## 🎓 Conclusion:
Ce projet a permis de développer un modèle de scoring efficace pour la prédiction de défaut de paiement chez Home Credit. L'utilisation de MLFlow et Azure a permis de garantir un développement efficace et un déploiement fluide de l'application. Le projet a également mis en évidence l'importance de la gestion des données, de la sélection des variables et de l'optimisation du modèle pour obtenir des résultats significatifs.

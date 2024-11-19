<div class="sc-iJuWdM jcgtvs"><h2><span style="white-space: pre-wrap;"><span class="">Projet DS 7: Modèle de scoring pour la prédiction de défaut de paiement</span></span></h2>
<p><span style="white-space: pre-wrap;"><span class="">Ce projet vise à développer un modèle de scoring permettant à Home Credit Default Risk, une société financière américaine, de prédire la probabilité de défaut de paiement de ses clients. Le modèle s'appuie sur une base de données complète comprenant des informations sur les clients, leurs antécédents de crédit, leurs revenus et autres données socio-économiques.</span></span></p>
<h3><span style="white-space: pre-wrap;"><span class="">Objectifs du projet:</span></span></h3>
<ul>
<li><strong><span style="white-space: pre-wrap;"><span class="">Prédire la probabilité de défaut de paiement</span></span></strong><span style="white-space: pre-wrap;"><span class=""> des clients de Home Credit.</span></span></li>
<li><strong><span style="white-space: pre-wrap;"><span class="">Construire un tableau de bord (dashboard)</span></span></strong><span style="white-space: pre-wrap;"><span class=""> accessible aux employés permettant de consulter les clients et lancer des prédictions.</span></span></li>
<li><strong><span style="white-space: pre-wrap;"><span class="">Utiliser pleinement les capacités de la librairie MLFlow</span></span></strong><span style="white-space: pre-wrap;"><span class=""> pour un travail d'équipe efficace et une gestion optimale du développement du modèle.</span></span></li>
</ul>
<h3><span style="white-space: pre-wrap;"><span class="">Méthodologie:</span></span></h3>
<p><span style="white-space: pre-wrap;"><span class="">Le projet a été mené en plusieurs étapes:</span></span></p>
<ol>
<li><strong><span style="white-space: pre-wrap;"><span class="">Préparation des données:</span></span></strong><span style="white-space: pre-wrap;"><span class="">
</span></span><ul>
<li><span style="white-space: pre-wrap;"><span class="">Nettoyage et transformation des données provenant de différentes sources (application, bureau, previous_app, installments).</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Création de nouvelles features en utilisant des techniques de feature engineering.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Gestion des valeurs manquantes et des outliers.</span></span></li>
</ul><span style="white-space: pre-wrap;"><span class="">
</span></span></li>
<li><strong><span style="white-space: pre-wrap;"><span class="">Sélection des variables:</span></span></strong><span style="white-space: pre-wrap;"><span class="">
</span></span><ul>
<li><span style="white-space: pre-wrap;"><span class="">Utilisation de RFECV pour déterminer le nombre optimal de variables.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Utilisation de RFE pour sélectionner les variables les plus pertinentes.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Sélection finale de 17 variables sur 37.</span></span></li>
</ul><span style="white-space: pre-wrap;"><span class="">
</span></span></li>
<li><strong><span style="white-space: pre-wrap;"><span class="">Choix du modèle:</span></span></strong><span style="white-space: pre-wrap;"><span class="">
</span></span><ul>
<li><span style="white-space: pre-wrap;"><span class="">Évaluation de différents modèles de machine learning en utilisant la métrique ROC_AUC.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Sélection du modèle LGBMClassifier pour ses performances et sa rapidité d'exécution.</span></span></li>
</ul><span style="white-space: pre-wrap;"><span class="">
</span></span></li>
<li><strong><span style="white-space: pre-wrap;"><span class="">Entraînement et optimisation du modèle:</span></span></strong><span style="white-space: pre-wrap;"><span class="">
</span></span><ul>
<li><span style="white-space: pre-wrap;"><span class="">Entraînement du modèle LGBMClassifier et optimisation des hyperparamètres.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Analyse du data drift pour garantir la robustesse du modèle à l'évolution des données.</span></span></li>
</ul><span style="white-space: pre-wrap;"><span class="">
</span></span></li>
<li><strong><span style="white-space: pre-wrap;"><span class="">Déploiement du modèle:</span></span></strong><span style="white-space: pre-wrap;"><span class="">
</span></span><ul>
<li><span style="white-space: pre-wrap;"><span class="">Utilisation de MLFlow pour le tracking et le serving du modèle.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Création d'une pipeline Sklearn pour standardiser et imputer les valeurs manquantes.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Développement d'une fonction héritée de Pyfunc pour la prédiction et l'explicabilité.</span></span></li>
</ul><span style="white-space: pre-wrap;"><span class="">
</span></span></li>
<li><strong><span style="white-space: pre-wrap;"><span class="">Création d'un dashboard avec Streamlit:</span></span></strong><span style="white-space: pre-wrap;"><span class="">
</span></span><ul>
<li><span style="white-space: pre-wrap;"><span class="">Développement d'une interface utilisateur pour la consultation des clients et le lancement de prédictions.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Intégration de graphiques et de données explicatives.</span></span></li>
</ul><span style="white-space: pre-wrap;"><span class="">
</span></span></li>
<li><strong><span style="white-space: pre-wrap;"><span class="">Déploiement de la web app sur Azure:</span></span></strong><span style="white-space: pre-wrap;"><span class="">
</span></span><ul>
<li><span style="white-space: pre-wrap;"><span class="">Conteneurisation de l'application Streamlit avec Docker.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Déploiement automatique sur Azure à l'aide de Github Actions.</span></span></li>
</ul><span style="white-space: pre-wrap;"><span class="">
</span></span></li>
</ol>
<h3><span style="white-space: pre-wrap;"><span class="">Résultats:</span></span></h3>
<ul>
<li><span style="white-space: pre-wrap;"><span class="">Le modèle LGBMClassifier a obtenu un score ROC_AUC de 0.75, ce qui est significatif pour la prédiction de défaut de paiement.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Le tableau de bord Streamlit permet aux employés d'accéder aux prédictions du modèle et aux informations des clients de manière simple et interactive.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Le projet a démontré l'efficacité de MLFlow pour la gestion du développement du modèle et la collaboration d'équipe.</span></span></li>
</ul>
<h3><span style="white-space: pre-wrap;"><span class="">Défis et perspectives:</span></span></h3>
<ul>
<li><span style="white-space: pre-wrap;"><span class="">Le projet a nécessité une gestion attentive des données et des ressources informatiques.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Les services gratuits utilisés (MLFlow, Azure, Github Actions) ont des limitations en termes de performance.</span></span></li>
<li><span style="white-space: pre-wrap;"><span class="">Le projet pourrait être amélioré en utilisant des services Azure plus performants et en intégrant des techniques de Deep Learning.</span></span></li>
</ul>
<h3><span style="white-space: pre-wrap;"><span class="">Conclusion:</span></span></h3>
<p><span style="white-space: pre-wrap;"><span class="">Ce projet a permis de développer un modèle de scoring efficace pour la prédiction de défaut de paiement chez Home Credit. L'utilisation de MLFlow et Azure a permis de garantir un développement efficace et un déploiement fluide de l'application. Le projet a également mis en évidence l'importance de la gestion des données, de la sélection des variables et de l'optimisation du modèle pour obtenir des résultats significatifs.</span></span></p></div>

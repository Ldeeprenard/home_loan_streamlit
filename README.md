# Prédiction de Risque de Défaut de Crédit 💸
> Par Thériot Maxence

## 📋 Présentation du Projet
Projet de prédiction des risques de remboursement de prêts pour Home Credit, utilisant l'apprentissage automatique et des sources de données alternatives.

## 🎯 Objectifs
- Minimiser les pertes financières
- Identifier les clients susceptibles de rembourser les prêts
- Utiliser des données alternatives pour l'évaluation des risques

## 🔍 Méthodologie

### 1. Prétraitement des Données

#### Gestion des Données
- Sources multiples : 
  - Données d'application
  - Historique de crédit bureau
  - Demandes de crédit précédentes
  - Enregistrements de paiements

#### Techniques de Prétraitement
- Équilibrage des classes
- Sélection des caractéristiques (RFECV)
- Réduction à 17 variables principales

### 2. Modélisation

#### Technique de Sélection
- Élimination Récursive des Caractéristiques (RFE)
- Optimisation basée sur ROC AUC

#### Modèles Évalués
- Régression Logistique
- Random Forest
- SGD Classifier
- LGBM Classifier

## 🧩 Résultats et Performances

### Modèle Principal : LGBMClassifier
- Score ROC AUC : 0,75
- Taux de Faux Positifs : 30%
- Temps d'Entraînement : 1,23s
- Temps de Prédiction : 0,23s

### Caractéristiques Prédictives
- Notes de crédit externes
- Montant de crédit non remboursé
- Durée d'emploi
- Délai entre demandes de crédit

## 🎓 Analyse et Insights

### Points Forts
- Utilisation de données alternatives
- Approche multimodale
- Performance prédictive solide

### Défis
- 30% de faux positifs
- Variation des notes de crédit externes

## 🚀 Perspectives d'Amélioration
- Modélisation par ensemble
- Apprentissage profond (PyTorch)
- Surveillance continue du modèle

## 🛠 Technologies Utilisées
- Python
- scikit-learn
- LightGBM
- Bibliothèques de traitement de données

## 📈 Métriques Clés
- Précision de classification
- Dérive des données (score : 0,235)
- Performance comparative

---

> **Note** : Projet de prédiction de risque de crédit utilisant l'apprentissage automatique pour améliorer l'inclusion financière.

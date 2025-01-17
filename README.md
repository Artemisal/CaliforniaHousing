# Projet de Prédiction des Prix des Maisons en Californie

Ce projet vise à développer un modèle de machine learning capable de prédire le prix médian des maisons, en utilisant des outils modernes et une approche structurée MLOps. Les étapes couvriront la modélisation, la mise en production, et le suivi du modèle en production.

Le jeu de données utilisé, **California Housing**, contient des informations détaillées sur les zones résidentielles en Californie, telles que le revenu médian des ménages, l’âge des maisons, ainsi que des caractéristiques démographiques et géographiques.  
La variable cible, `MedHouseVal`, représente le prix médian des maisons (en 100k $).

## Étapes du projet

### Mission 1 : Exploration et préparation des données
Dans le notebook `Mission1.ipynb`, nous avons :
- Chargé le jeu de données California Housing.
- Identifié les valeurs manquantes ou aberrantes.
- Standardisé les données pour les rendre adaptées à la modélisation.

### Mission 2 : Modélisation et tracking des expériences

Les interprétations et analyses des résultats sont détaillées dans le notebook `mission2_Models.ipynb`. 

Cette étape a pour objectif la construction d’un modèle de régression, ainsi que l’utilisation de **Random Forest** ou **Gradient Boosting**, et le suivi des expériences avec **MLflow**.  
Le dossier `src/models` contient le code source pour la construction de chaque modèle. Dans cette étape, nous avons :
- Développé un modèle de régression linéaire comme point de départ.
- Expérimenté avec des modèles avancés tels que Random Forest et Gradient Boosting pour améliorer la précision des prédictions.
- Utilisé MLflow pour suivre les expériences et enregistrer des métriques de performance (RMSE, MAE, R²).
- Enregistré le meilleur modèle dans le Model Registry de MLflow.  
=

### Mission 3 : Analyse des features
Le dossier `src/shap_analysis` contient le code source pour l’analyse des features. Dans cette étape, nous avons :
- Calculé les importances globales des features, en utilisant **SHAP** ou les importances des caractéristiques.
- Effectué une analyse de l'impact local sur des exemples individuels à l'aide de SHAP.  
Les interprétations sont détaillées dans `src/Conclusion_SHAP.pdf`.

### Mission 4 : Mise en production
Cette étape a pour objectif d'exposer le modèle via une API.  
Les fichiers `API/main.py`, `Dockerfile`, et `docker-compose.yaml` contiennent les éléments nécessaires à la mise en production de l'API. Dans cette étape, nous avons :
- Créé une API avec **FastAPI** dans le fichier `main.py`, permettant de recevoir des données en entrée et de renvoyer des prédictions.
- Conteneurisé l'API à l’aide de **Docker** grâce aux fichiers `Dockerfile` et `docker-compose.yaml`.

### Mission 5 : Approche MLOps avancée
Les dossiers `.github/workflows` et `tests` contiennent les éléments nécessaires à l’automatisation et aux tests. Dans cette étape, nous avons :
- Configuré **GitHub Actions** dans `.github/workflows` pour mettre en place un pipeline CI/CD automatisé.
- Créé des tests (Pytest) pour valider l'API et le modèle dans le dossier `tests`, assurant que l’API fonctionne correctement et que le modèle fait des prédictions fiables.

### Mission 6 : Suivi en production
Le dossier **Monitoring** contient les scripts nécessaires au suivi des performances et à la détection du drift. Dans cette étape, nous avons :
- Simulé des données en production.
- Détecté le data drift et analysé les écarts entre les données d’entraînement et celles en production.
- Généré un rapport HTML détaillant les résultats de cette analyse.

## Étapes pour effectuer un run de projet

1. **Cloner le dépôt GitHub sur votre machine locale** :
    ```bash
    git clone <url_du_dépôt>
    ```

2. **Accéder au répertoire du projet cloné** :
    ```bash
    cd <répertoire_du_projet>
    ```

3. **Configurer l'environnement avec Poetry** :
    ```bash
    poetry install
    ```

4. **Activer l'environnement virtuel Poetry** :
    ```bash
    poetry shell
    ```

5. **Exécuter l'API** :
    - Le modèle a déjà été exécuté à l'aide du script `BestModel_randomForest.py` dans le répertoire `src/models`. Cette exécution a généré le répertoire `mlruns/` contenant les informations associées à l'expérience, y compris le `run_id` et le `experiment_id`. Ces identifiants sont nécessaires pour charger le modèle enregistré correctement via l'API.
    - Si le modèle est exécuté à nouveau, un nouveau `run_id` et `experiment_id` seront générés, et il faudra mettre à jour ces identifiants dans le fichier `api/main.py` pour assurer une initialisation correcte du modèle.

6. **Lancer l'API avec Uvicorn** :
    ```bash
    uvicorn api.main:app --reload
    ```

7. **Lancer l'application Streamlit** :
    ```bash
    streamlit run streamlit/Streamlit_app.py
    ```


Contributeurs:
SALMA HROUMA 

SAMIA HROUMA

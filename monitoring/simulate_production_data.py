import pandas as pd
import numpy as np
import random

# Charger les données d'entraînement
file_path = 'data/processed/housing_data.csv'
data = pd.read_csv(file_path)

# Sélectionner les features (X) et la variable cible (y)
X = data.drop(columns=['MedHouseVal'])  # Features
y = data['MedHouseVal']  # Cible

# Diviser les données en ensemble d'entraînement et de test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Simulation de données en production
# Ajouter du bruit aléatoire aux caractéristiques pour simuler les changements de données en production
random.seed(42)  # Fixer la graine pour la reproductibilité

# Créer une copie des données d'entraînement
X_production = X_train.copy()

# Ajouter du bruit normal aux colonnes numériques pour simuler des fluctuations en production
for column in X_production.columns:
    # Ajouter un bruit normal centré sur 0 avec un écart-type de 0.02
    noise = np.random.normal(0, 0.02, size=X_production[column].shape)
    X_production[column] += noise

# Afficher les premières lignes du jeu de données simulé
print(X_production.head())

# Sauvegarder les données simulées en production dans un fichier CSV
X_production.to_csv('data/drift_data/simulated_production_data.csv', index=False)
print("Données simulées en production sauvegardées dans 'simulated_production_data.csv'.")
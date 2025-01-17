import pandas as pd
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Charger les données d'entraînement et de production simulées
data_train = pd.read_csv('data/processed/housing_data.csv')
data_prod = pd.read_csv('data/drift_data/simulated_production_data.csv')

# Initialiser la cartographie des colonnes

column_mapping = ColumnMapping(
    numerical_features=['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude'],
    target=None
)

# Initialiser le rapport Monitoring
data_drift_report = Report(metrics=[DataDriftPreset()])

# Calculer le drift
data_drift_report.run(reference_data=data_train, current_data=data_prod, column_mapping=column_mapping)

# Sauvegarder le rapport HTML du drift
data_drift_report.save_html('monitoring/data_drift_report.html')

print("Rapport de drift généré : 'data_drift_report.html'.")
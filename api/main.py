import mlflow
import mlflow.pyfunc
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import os
from pathlib import Path

# FastAPI setup
app = FastAPI()
try:
    # Load the model
    model = mlflow.pyfunc.load_model("mlruns/273854134712038863/024f2fbabac647f09326b605ec65ec4e/artifacts/random_forest_model")
except Exception as e:
    raise RuntimeError(f"Failed to load model from MLflow: {e}")

# Pydantic model to validate inputs
class HousingFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction du prix des maisons en Californie"}

@app.post("/predict/")
def predict(features: HousingFeatures):
    # Prepare the input data for prediction
    input_data = np.array([[features.MedInc, features.HouseAge, features.AveRooms, features.AveBedrms,
                            features.Population, features.AveOccup, features.Latitude, features.Longitude]])

    # Predict with the model
    prediction = model.predict(input_data)
    # Return the prediction
    return {"predicted_house_value": prediction[0]}

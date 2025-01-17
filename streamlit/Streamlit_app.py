import streamlit as st
import numpy as np
import requests

# Set the page configuration
st.set_page_config(
    page_title="California Housing",
    page_icon="🏠",
    layout="centered"
)
# URL de l'API FastAPI
API_URL = "http://127.0.0.1:8000/predict/"

# Interface utilisateur Streamlit
st.title("Prédiction du prix des maisons en Californie")

#CSS
st.markdown(
    """
    <style>
    body {
        background-image: url("https://images.unsplash.com/photo-1519302959554-a75be0afc82a?q=80&w=1784&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .stApp {
        background: rgba(255, 255, 255, 0.8);  /* Transparence pour améliorer la lisibilité */
        padding: 30px;
        border-radius: 15px;
        max-width: 800px;
        margin: auto;
        font-family: 'Helvetica', sans-serif;
    }

    h1 {
        color: #4CAF50;
        text-align: center;
    }

    .stButton>button {
        background-color: #4CAF50; /* Vert par défaut */
        color: white;
        border-radius: 5px;
        font-weight: bold;
        width: 100%;
        transition: background-color 0.3s; /* Transition pour adoucir le changement de couleur */
    }

    .stButton>button:hover {
        background-color: #45a049; /* Un vert un peu plus foncé lorsque la souris survole */
    }

    .stTextInput, .stNumberInput {
        width: 100%;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



st.write(
    """
    Entrez les caractéristiques de la maison pour prédire sa valeur :
    """
)



# Formulaire pour que l'utilisateur entre les données
MedInc = st.number_input("Revenu Médian (MedInc)", min_value=0.0, format="%.2f")
HouseAge = st.number_input("Âge de la Maison (HouseAge)", min_value=0, format="%d")
NbRooms = st.number_input("Nombre de chambres (NbRooms)", min_value=0, format="%d")
NbBedrooms = st.number_input("Nombre de chambres à coucher (NbBedrooms)", min_value=0, format="%d")
Population = st.number_input("Population", min_value=0, format="%d")
AveOccup = st.number_input("Nombre moyen d'occupants (AveOccup)", min_value=0.0, format="%.2f")
Latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, format="%.2f")
Longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, format="%.2f")

# Calculer les moyennes pour les chambres et les chambres à coucher
AveRooms = NbRooms / Population if Population != 0 else 0
AveBedrms = NbBedrooms / Population if Population != 0 else 0

# Bouton pour soumettre la prédiction
if st.button("Prédire"):
    # Préparer les données pour la prédiction
    input_data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude,
    }

    # Effectuer la requête à l'API FastAPI pour obtenir la prédiction
    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        prediction = response.json()
        predicted_value = prediction["predicted_house_value"]
        st.success(f"La valeur prédite de la maison est : ${predicted_value:,.2f}")
    else:
        st.error("Une erreur s'est produite lors de la prédiction. Veuillez réessayer.")

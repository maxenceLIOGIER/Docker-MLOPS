import requests

# URL de l'API serveur
SERVER_URL = "http://server:8000/predict"

# Données à envoyer
data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

# Envoi de la requête POST
response = requests.post(SERVER_URL, json=data)

# Affichage de la réponse
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Error:", response.status_code, response.text)

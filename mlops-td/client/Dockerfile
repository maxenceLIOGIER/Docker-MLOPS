FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du client
COPY app.py app.py

# Installer les dépendances
RUN pip install -r requirements.txt

# Commande par défaut : exécuter le client
CMD ["streamlit", "run" "app.py"]

# Projet Docker avec Docker Compose

Ce projet créé pour le cours de MLOPS dans le cadre du Master 2 SISE utilise Docker pour déployer facilement une application streamlit.
Suivez les étapes ci-dessous pour cloner le dépôt, configurer votre environnement et exécuter l'application sur votre machine locale.

---

## Prérequis

1. **Docker Desktop**  
   Téléchargez et installez Docker Desktop depuis [Docker](https://www.docker.com/products/docker-desktop).  
   Assurez-vous que Docker est correctement configuré et en cours d'exécution après l'installation.

2. **Git**  
   Installez Git si ce n'est pas déjà fait, en le téléchargeant depuis [Git](https://git-scm.com/).

---

## Installation et lancement

### 1) Cloner le dépôt
Clonez ce dépôt GitHub sur votre machine locale en exécutant la commande suivante dans un terminal / Anaconda Prompt / git bash :
```bash
git clone https://github.com/username/repository-name.git
```
(Remplacez username par le nom d'utilisateur GitHub et repository-name par le nom de ce dépôt).


### 2) Accéder au répertoire
Placez-vous dans le dossier du projet cloné :
```bash
cd repository-name
```


### 3) Vérifier les fichiers nécessaires
Assurez-vous que le fichier ```docker-compose.yml``` est présent dans le répertoire. Ce fichier définit les services et leur configuration.


### 4) Lancer l'application
Exécutez la commande suivante pour démarrer tous les conteneurs et services :

```bash
docker-compose up
```
Cette commande télécharge les images nécessaires (si elles ne sont pas déjà présentes sur votre machine), crée et démarre les conteneurs. Lorsque vous exécutez cette commande, assurez vous que Docker Desktop soit ouvert sur votre PC.


### 5) Accéder à l'application
Une fois les services démarrés, accédez à l'application via votre navigateur web à l'adresse suivante :
```http://localhost:<PORT>```
(Remplacez ```<PORT>``` par le port configuré dans le fichier ```docker-compose.yml```, généralement ```80```, ```3000```, ou ```8000```. Celui ci vous sera communiqué par votre terminal).

---

## Commandes utiles
* Arrêter les services :
Pour arrêter tous les conteneurs exécutés via ```docker-compose```, utilisez :
```bash
docker-compose down
```

* Afficher les logs des conteneurs :
Pour suivre les logs de l'application en temps réel :
```bash
docker-compose logs -f
```

* Recréer les conteneurs :
Si vous modifiez les fichiers du projet, relancez les conteneurs en les recréant avec :
```bash
docker-compose up --build
```

---

## Fonctionnement de l'application
L'application est très simple. Elle a pour but de créer une prédiction du type d'iris (la fleur) entre setosa, virginica et versicolor. Ceci se base sur le jeu de données très connu "Iris".

Pour faire une prédiction, l'utilisateur peut rentrer les caractéristiques suivantes : longueur du sépale, largeur du sépale, longueur du pétale et largeur du pétale.

En sortie, l'application renvoie le nom du type d'iris auquelles les caractéristiques fournies correspondent le plus ainsi qu'une photo de ce type de fleur.

![image](https://github.com/user-attachments/assets/48ca7271-2642-4064-aeec-e86816392619)


Le modèle utilisé est celui de la forêt aléatoire de scikit-learn :
```python
model = RandomForestClassifier(n_estimators=100, random_state=42)
```



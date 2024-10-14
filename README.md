# Bibliothèque en Ligne

## Description
Une application web de bibliothèque en ligne développée avec **Flask** et **MongoDB**. Cette application permet aux utilisateurs d'ajouter, de rechercher, de modifier et de supprimer des livres dans une base de données.

## Technologies Utilisées
- **Flask** : Framework web pour Python.
- **MongoDB** : Base de données NoSQL.
- **Bootstrap** : Framework CSS pour des designs réactifs.
- **HTML/CSS** : Pour l'interface web.
## Prérequis
- Python 3.12 ou une version supérieur
- MongoDB installé localement 
- Pip (gestionnaire de paquets Python)

## Installation

1. **Clonez le dépôt** 
   ```bash
   git clone <URL_DU_DEPOT>
   
   cd `GestionBiblioWeb`

2. **Installez les dépendances**
    ```bash
    pip install Flask pymongo

3. **Configurez MongoDB**

 Assurez-vous que MongoDB est en cours d'exécution. Créez une base de données `bibliotheque` et une collection `livres`.

4. **Exécutez l'application**
    ```bash
   python app.py
   
## Utilisation

- **Ajouter un livre** : Naviguez vers la page "Ajouter un livre" pour ajouter des livres à la bibliothèque.
- **Afficher tous les livres** : La page d'accueil affiche tous les livres disponibles dans la bibliothèque.
- **Modifier un livre** : Vous pouvez modifier les détails d'un livre en cliquant sur le bouton "Modifier" à côté de chaque livre.
- **Supprimer un livre** : Vous pouvez supprimer un livre en cliquant sur le bouton "Supprimer".

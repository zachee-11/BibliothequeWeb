import pymongo
from models.model import Livre

# Connexion MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["bibliotheque"]
collection = db["livres"]

def ajouter_livre(titre, auteur, genre, annee_publication):
    """
    :param titre:
    :param auteur:
    :param genre:
    :param annee_publication:
    :return:
    """
    livre = Livre(titre, auteur, genre, annee_publication)
    collection.insert_one(livre.to_dict())
    print(f"Livre '{titre}' ajouté avec succès.")

def afficher_livres():
    """
    :return:
    """
    livres = collection.find()
    """for livre in livres:
        print(f"Titre: {livre['titre']}, Auteur: {livre['auteur']}, Genre: {livre['genre']}, Année: {livre['annee_publication']}")"""
    return  livres

def rechercher_livre(titre):
    """
    :param titre:
    :return:
    """
    livre = collection.find_one({"titre": titre})
    if livre:
        print(f"Titre: {livre['titre']}, Auteur: {livre['auteur']}, Genre: {livre['genre']}, Année: {livre['annee_publication']}")
    else:
        print(f"Aucun livre trouvé avec le titre '{titre}'.")
    return livre

def mettre_a_jour_livre(titre, nouveaux_details):
    """
    :param titre:
    :param nouveaux_details:
    :return:
    """
    result = collection.update_one({"titre": titre}, {"$set": nouveaux_details})
    if result.matched_count > 0:
        print(f"Livre '{titre}' mis à jour avec succès.")
    else:
        print(f"Aucun livre trouvé avec le titre '{titre}'.")

def supprimer_livre(titre):
    """
    :param titre:
    :return:
    """
    result = collection.delete_one({"titre": titre})
    if result.deleted_count > 0:
        print(f"Livre '{titre}' supprimé avec succès.")
    else:
        print(f"Aucun livre trouvé avec le titre '{titre}'.")

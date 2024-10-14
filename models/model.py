from datetime import datetime

class Livre:
    def __init__(self, titre, auteur, genre, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.annee_publication = annee_publication
        self.date_ajout = datetime.now()

    def to_dict(self):
        return {
            "titre": self.titre,
            "auteur": self.auteur,
            "genre": self.genre,
            "annee_publication": self.annee_publication,
            "date_ajout": self.date_ajout
        }

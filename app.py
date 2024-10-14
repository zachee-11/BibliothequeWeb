from flask import Flask, render_template, request, redirect, url_for
from controllers.controller_biblio import ajouter_livre, afficher_livres, rechercher_livre, mettre_a_jour_livre, supprimer_livre

app = Flask(__name__)


@app.route('/')
def index():
    livres = list(afficher_livres())
    if livres is None:
        livres = []
    return render_template('index.html', livres=livres)


@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        genre = request.form['genre']
        annee_publication = request.form['annee_publication']
        ajouter_livre(titre, auteur, genre, annee_publication)
        return redirect(url_for('index'))
    return render_template('ajouter.html')


@app.route('/rechercher', methods=['GET', 'POST'])
def rechercher():
    livre = None
    if request.method == 'POST':
        titre = request.form['titre']
        livre = rechercher_livre(titre)
    return render_template('rechercher.html', livre=livre)

@app.route('/update/<titre>', methods=['GET', 'POST'])
def update(titre):
    if request.method == 'POST':
        nouveaux_details = {}
        nouveau_titre = request.form['titre']
        nouvel_auteur = request.form['auteur']
        genre = request.form['genre']
        annee_publication = request.form['annee_publication']

        if nouveau_titre:
            nouveaux_details['titre'] = nouveau_titre
        if nouvel_auteur:
            nouveaux_details['auteur'] = nouvel_auteur
        if genre:
            nouveaux_details['genre'] = genre
        if annee_publication:
            nouveaux_details['annee_publication'] = annee_publication

        mettre_a_jour_livre(titre, nouveaux_details)
        return redirect(url_for('index'))

    livre = rechercher_livre(titre)
    return render_template('update.html', livre=livre)


@app.route('/delete/<titre>', methods=['POST'])
def delete(titre):
    supprimer_livre(titre)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=5001)

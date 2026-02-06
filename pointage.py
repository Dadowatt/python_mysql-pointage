import mysql.connector

connexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'watt123',
    database = 'pointage_apprenants',
    port = 3307
)
curseur = connexion.cursor()
print('Connecté à la base de donnée MySQL')

#ajout de l'apprenant
def ajouter_apprenant():
    nom = input('nom: ')
    prenom = input('prénom: ')
    promo = input('promo: ')
    presence = input('Présence : ')

    sql = "INSERT INTO apprenants (nom, prenom, promo, presence) VALUES(%s, %s, %s, %s)"
    curseur.execute(sql, (nom, prenom, promo, presence))
    connexion.commit()
    print('Apprenant ajouté avec succès')

ajouter_apprenant()
    
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

def afficher_apprenants():
    curseur.execute("SELECT * FROM apprenants WHERE presence = 'present'")
    resultats = curseur.fetchall()
    if resultats:
        print('\Liste des apprenants pointés')
        for apprenants in resultats:
            print(apprenants)
afficher_apprenants()

def rechercher_apprenant():
    recherche = input("Saisir l'ID de l'apprenant: ")
    if not recherche.isdigit():
        print("L'ID doit être un nombre")
        return
    curseur.execute("SELECT * FROM apprenants WHERE id = %s", (int(recherche),))
    resultats = curseur.fetchall()
    if resultats:
        print("Aprenant trouvé: ")
        for apprenant in resultats:
            print(apprenant)
rechercher_apprenant()
curseur.close()
connexion.close()
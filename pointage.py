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


def afficher_apprenants():
    curseur.execute("SELECT * FROM apprenants WHERE presence = 'present'")
    resultats = curseur.fetchall()
    if resultats:
        print('\Liste des apprenants pointés')
        for apprenants in resultats:
            print(apprenants)

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

#menu interactif
while True:
    print("=== MENU POINTAGE ===")
    print("1. Ajouter apprenant")
    print("2. Afficher les apprenants")
    print("3. Rechercher un apprenant")
    print("4. Quitter")
    choix = input("Choisissez une option: ")
    if choix == "1":
        ajouter_apprenant()
    elif choix == "2":
        afficher_apprenants()
    elif choix == "3":
        rechercher_apprenant()
    elif choix == "4":
        print('AU revoir')
        break
    else:
        print("Choix invalide")

#fermeture de la connexion
curseur.close()
connexion.close()
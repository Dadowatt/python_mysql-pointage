import mysql.connector

connexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='watt123',
    database='pointage_apprenants',
    port=3307
)
curseur = connexion.cursor(dictionary=True)
print("Connecté à la base de données MySQL")

def ajouter_apprenant():
    try:
        while True:
            nom = input("Nom : ").strip()
            prenom = input("Prénom : ").strip()
            if nom.isalpha() and prenom.replace(" ", "").isalpha():
                break
            print("Le nom et le prénom doivent contenir uniquement des lettres")

        while True:
            promo = input("Promo: ").strip().upper()
            if len(promo) == 2 and promo.startswith("P") and promo[1].isdigit():
                break
            print("La promo doit être au format P1, P2, P3, etc.")

        sql = "INSERT INTO apprenants (nom, prenom, promo) VALUES (%s, %s, %s)"
        curseur.execute(sql, (nom, prenom, promo))
        connexion.commit()

        print(f"Apprenant {prenom} {nom} ajouté avec succès")

    except mysql.connector.Error as e:
        print(f"Erreur MySQL : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

def pointer_apprenant():
    try:
        while True:
            apprenant_id = input("Saisir l'ID de l'apprenant à pointer : ").strip()
            if apprenant_id.isdigit():
                break
            print("L'ID doit contenir uniquement des chiffres")

        sql = "UPDATE apprenants SET presence = 'present' WHERE id = %s"
        curseur.execute(sql, (int(apprenant_id),))
        connexion.commit()

        if curseur.rowcount > 0:
            print("Présence enregistrée avec succès")
        else:
            print("Aucun apprenant trouvé avec cet ID")

    except mysql.connector.Error as e:
        print(f"Erreur MySQL : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

def afficher_apprenants():
    try:
        curseur.execute("SELECT * FROM apprenants WHERE presence = 'present'")
        resultats = curseur.fetchall()

        if resultats:
            print("\nListe des apprenants présents :\n")
            for a in resultats:
                print(f"ID : {a['id']} | Nom : {a['nom']} | Prénom : {a['prenom']} | Promo : {a['promo']}")
        else:
            print("Aucun apprenant présent")

    except mysql.connector.Error as e:
        print(f"Erreur MySQL : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

def rechercher_apprenant():
    try:
        while True:
            recherche = input("Saisir l'ID de l'apprenant : ").strip()
            if recherche.isdigit():
                break
            print("L'ID doit être un nombre.")

        curseur.execute("SELECT * FROM apprenants WHERE id = %s", (int(recherche),))
        resultats = curseur.fetchall()

        if resultats:
            for a in resultats:
                print(f"ID : {a['id']} | Nom : {a['nom']} | Prénom : {a['prenom']} | Promo : {a['promo']} | Présence : {a['presence']}")
        else:
            print("Aucun apprenant avec cet ID.")

    except mysql.connector.Error as e:
        print(f"Erreur MySQL : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

while True:
    print("\n=== MENU POINTAGE ===")
    print("1. Ajouter un apprenant")
    print("2. Pointer un apprenant")
    print("3. Afficher les apprenants présents")
    print("4. Rechercher un apprenant")
    print("5. Quitter")
    print("-" * 30)

    choix = input("Choisissez une option : ").strip()

    if choix == "1":
        ajouter_apprenant()
    elif choix == "2":
        pointer_apprenant()
    elif choix == "3":
        afficher_apprenants()
    elif choix == "4":
        rechercher_apprenant()
    elif choix == "5":
        print("Au revoir")
        break
    else:
        print("Choix invalide.")

curseur.close()
connexion.close()




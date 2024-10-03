from ecole import Ecole

# Fonction pour afficher le menu principal
def afficher_menu():
    print("\n--- MENU ---")
    print("1. Ajouter un étudiant")
    print("2. Ajouter une matière")
    print("3. Ajouter un professeur")
    print("4. Ajouter une note à un étudiant")
    print("5. Ajouter une absence à un étudiant")
    print("6. Ajouter un retard à un étudiant")
    print("7. Afficher la moyenne d'un étudiant")
    print("8. Générer un bulletin")
    print("9. Sauvegarder les données")
    print("10. Charger les données")
    print("11. Quitter")

# Fonction pour obtenir une réponse utilisateur
def obtenir_choix():
    return input("\nChoisissez une option (1-11) : ")

# Fonction principale pour gérer les actions
def main():
    ecole = Ecole()

    while True:
        afficher_menu()
        choix = obtenir_choix()

        if choix == '1':  # Ajouter un étudiant
            nom = input("Nom de l'étudiant : ")
            prenom = input("Prénom de l'étudiant : ")
            id_etudiant = input("ID de l'étudiant : ")
            ecole.ajouter_etudiant(nom, prenom, id_etudiant)
            print(f"Étudiant {nom} {prenom} ajouté avec succès.")

        elif choix == '2':  # Ajouter une matière
            nom_matiere = input("Nom de la matière : ")
            ecole.ajouter_matiere(nom_matiere)
            print(f"Matière {nom_matiere} ajoutée avec succès.")

        elif choix == '3':  # Ajouter un professeur
            nom_prof = input("Nom du professeur : ")
            prenom_prof = input("Prénom du professeur : ")
            ecole.ajouter_professeur(nom_prof, prenom_prof)
            print(f"Professeur {nom_prof} {prenom_prof} ajouté avec succès.")

        elif choix == '4':  # Ajouter une note à un étudiant
            id_etudiant = input("ID de l'étudiant : ")
            nom_matiere = input("Nom de la matière : ")
            note = float(input("Note à ajouter : "))
            ecole.ajouter_note_etudiant(id_etudiant, nom_matiere, note)
            print(f"Note de {note} ajoutée pour l'étudiant {id_etudiant} en {nom_matiere}.")

        elif choix == '5':  # Ajouter une absence à un étudiant
            id_etudiant = input("ID de l'étudiant : ")
            ecole.ajouter_absence_etudiant(id_etudiant)
            print(f"Absence ajoutée pour l'étudiant {id_etudiant}.")

        elif choix == '6':  # Ajouter un retard à un étudiant
            id_etudiant = input("ID de l'étudiant : ")
            ecole.ajouter_retard_etudiant(id_etudiant)
            print(f"Retard ajouté pour l'étudiant {id_etudiant}.")

        elif choix == '7':  # Afficher la moyenne d'un étudiant
            id_etudiant = input("ID de l'étudiant : ")
            moyenne = ecole.calculer_moyenne_etudiant(id_etudiant)
            if moyenne is not None:
                print(f"La moyenne de l'étudiant {id_etudiant} est de {moyenne:.2f}.")
            else:
                print(f"Aucune note trouvée pour l'étudiant {id_etudiant}.")

        elif choix == '8':  # Générer un bulletin
            id_etudiant = input("ID de l'étudiant : ")
            format_bulletin = input("Format du bulletin (txt/csv) : ").lower()
            ecole.generer_bulletin(id_etudiant, format=format_bulletin)
            print(f"Bulletin généré pour l'étudiant {id_etudiant} au format {format_bulletin}.")

        elif choix == '9':  # Sauvegarder les données
            fichier = input("Nom du fichier de sauvegarde (avec extension .json) : ")
            ecole.sauvegarder_donnees(fichier)
            print(f"Données sauvegardées dans le fichier {fichier}.")

        elif choix == '10':  # Charger les données
            fichier = input("Nom du fichier à charger (avec extension .json) : ")
            ecole.charger_donnees(fichier)
            print(f"Données chargées depuis le fichier {fichier}.")

        elif choix == '11':  # Quitter
            print("Au revoir !")
            break

        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()

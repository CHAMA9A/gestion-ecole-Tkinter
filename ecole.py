import json
from etudiant import Etudiant
from matiere import Matiere
from professeur import Professeur
import matplotlib.pyplot as plt

class Ecole:
    def __init__(self):
        self.etudiants = {}
        self.matieres = []
        self.professeurs = []

    def ajouter_etudiant(self, nom, prenom, id_etudiant):
        self.etudiants[id_etudiant] = Etudiant(nom, prenom, id_etudiant)

    def ajouter_matiere(self, nom_matiere):
        self.matieres.append(Matiere(nom_matiere))

    def ajouter_professeur(self, nom, prenom):
        self.professeurs.append(Professeur(nom, prenom))

    def ajouter_note_etudiant(self, id_etudiant, nom_matiere, note):
        if id_etudiant in self.etudiants:
            self.etudiants[id_etudiant].ajouter_note(nom_matiere, note)

    def ajouter_absence_etudiant(self, id_etudiant):
        if id_etudiant in self.etudiants:
            self.etudiants[id_etudiant].ajouter_absence()

    def ajouter_retard_etudiant(self, id_etudiant):
        if id_etudiant in self.etudiants:
            self.etudiants[id_etudiant].ajouter_retard()

    def calculer_moyenne_etudiant(self, id_etudiant):
        if id_etudiant in self.etudiants:
            return self.etudiants[id_etudiant].calculer_moyenne()
        return None

    def generer_bulletin(self, id_etudiant, format='txt'):
        if id_etudiant in self.etudiants:
            etudiant = self.etudiants[id_etudiant]
            bulletin = f"Bulletin de {etudiant.nom} {etudiant.prenom}\n"
            bulletin += f"Absences: {etudiant.absences}, Retards: {etudiant.retards}\n"
            bulletin += "Notes :\n"
            for matiere, notes in etudiant.notes.items():
                bulletin += f"{matiere} : {notes}\n"
            bulletin += f"Moyenne générale : {etudiant.calculer_moyenne()}\n"

            if format == 'txt':
                with open(f"bulletin_{id_etudiant}.txt", 'w') as f:
                    f.write(bulletin)
            elif format == 'csv':
                import csv
                with open(f"bulletin_{id_etudiant}.csv", 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow([f"Bulletin de {etudiant.nom} {etudiant.prenom}"])
                    writer.writerow([f"Absences : {etudiant.absences}, Retards : {etudiant.retards}"])
                    writer.writerow(["Matière", "Notes"])
                    for matiere, notes in etudiant.notes.items():
                        writer.writerow([matiere, notes])
                    writer.writerow([f"Moyenne générale : {etudiant.calculer_moyenne()}"])

    def sauvegarder_donnees(self, fichier):
        donnees = {
            "etudiants": {id_e: vars(etudiant) for id_e, etudiant in self.etudiants.items()},
            "matieres": [vars(matiere) for matiere in self.matieres],
            "professeurs": [vars(prof) for prof in self.professeurs]
        }
        with open(fichier, 'w') as f:
            json.dump(donnees, f)

    def charger_donnees(self, fichier):
        with open(fichier, 'r') as f:
            donnees = json.load(f)
            for id_e, etudiant_data in donnees["etudiants"].items():
                etudiant = Etudiant(etudiant_data["nom"], etudiant_data["prenom"], etudiant_data["id_etudiant"])
                etudiant.notes = etudiant_data["notes"]
                etudiant.absences = etudiant_data["absences"]
                etudiant.retards = etudiant_data["retards"]
                self.etudiants[id_e] = etudiant

            for matiere_data in donnees["matieres"]:
                self.matieres.append(Matiere(matiere_data["nom"]))

            for professeur_data in donnees["professeurs"]:
                self.professeurs.append(Professeur(professeur_data["nom"], professeur_data["prenom"]))
    
    def generer_graphique_performance(self, id_etudiant):
        if id_etudiant in self.etudiants:
            etudiant = self.etudiants[id_etudiant]

            # Préparer les données pour le graphique
            matieres = []
            moyennes = []
            
            for matiere, notes in etudiant.notes.items():
                if len(notes) > 0:
                    moyenne_matiere = sum(notes) / len(notes)
                    matieres.append(matiere)
                    moyennes.append(moyenne_matiere)

            if not moyennes:
                print(f"Aucune note disponible pour générer un graphique pour l'étudiant {id_etudiant}.")
                return

            # Créer le graphique
            plt.figure(figsize=(10, 5))
            plt.plot(matieres, moyennes, marker='o', linestyle='-', color='b')
            plt.title(f"Évolution des moyennes pour {etudiant.nom} {etudiant.prenom}")
            plt.xlabel('Matières')
            plt.ylabel('Moyenne')
            plt.ylim(0, 20)  # Supposons que la note maximale est 20
            plt.grid(True)

            # Enregistrer le graphique sous forme d'image
            nom_fichier = f'performance_{id_etudiant}.png'
            plt.savefig(nom_fichier)
            plt.close()
            print(f"Graphique de performance généré : {nom_fichier}")
        else:
            print(f"Étudiant avec ID {id_etudiant} non trouvé.")

class Etudiant:
    def __init__(self, nom, prenom, id_etudiant):
        self.nom = nom
        self.prenom = prenom
        self.id_etudiant = id_etudiant
        self.notes = {}  # Matière: [liste des notes]
        self.absences = 0
        self.retards = 0

    def ajouter_note(self, matiere, note):
        if matiere not in self.notes:
            self.notes[matiere] = []
        self.notes[matiere].append(note)

    def ajouter_absence(self):
        self.absences += 1

    def ajouter_retard(self):
        self.retards += 1

    def calculer_moyenne(self):
        total_notes = 0
        nb_notes = 0
        for notes in self.notes.values():
            total_notes += sum(notes)
            nb_notes += len(notes)
        return total_notes / nb_notes if nb_notes > 0 else 0

    def __str__(self):
        return f"{self.nom} {self.prenom} (ID: {self.id_etudiant})"

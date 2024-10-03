import tkinter as tk
from tkinter import messagebox
from ecole import Ecole
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# Initialisation de l'école
ecole = Ecole()

# Créer la fenêtre principale
root = tk.Tk()
root.title("Système de Gestion des Notes")

# Créer des cadres pour organiser l'interface
frame_ajouter = tk.Frame(root)
frame_ajouter.pack(pady=10)

frame_actions = tk.Frame(root)
frame_actions.pack(pady=10)

frame_bulletin = tk.Frame(root)
frame_bulletin.pack(pady=10)

# Fonctions pour les actions

def ajouter_etudiant():
    nom = entry_nom_etudiant.get()
    prenom = entry_prenom_etudiant.get()
    id_etudiant = entry_id_etudiant.get()
    if nom and prenom and id_etudiant:
        ecole.ajouter_etudiant(nom, prenom, id_etudiant)
        messagebox.showinfo("Succès", f"Étudiant {nom} {prenom} ajouté.")
        entry_nom_etudiant.delete(0, tk.END)
        entry_prenom_etudiant.delete(0, tk.END)
        entry_id_etudiant.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

def ajouter_matiere():
    nom_matiere = entry_nom_matiere.get()
    if nom_matiere:
        ecole.ajouter_matiere(nom_matiere)
        messagebox.showinfo("Succès", f"Matière {nom_matiere} ajoutée.")
        entry_nom_matiere.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez entrer un nom de matière.")

def ajouter_professeur():
    nom = entry_nom_professeur.get()
    prenom = entry_prenom_professeur.get()
    if nom and prenom:
        ecole.ajouter_professeur(nom, prenom)
        messagebox.showinfo("Succès", f"Professeur {nom} {prenom} ajouté.")
        entry_nom_professeur.delete(0, tk.END)
        entry_prenom_professeur.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

def ajouter_note():
    id_etudiant = entry_id_etudiant_note.get()
    nom_matiere = entry_nom_matiere_note.get()
    note = entry_note_etudiant.get()
    if id_etudiant and nom_matiere and note:
        try:
            note = float(note)
            ecole.ajouter_note_etudiant(id_etudiant, nom_matiere, note)
            messagebox.showinfo("Succès", f"Note {note} ajoutée pour l'étudiant {id_etudiant} en {nom_matiere}.")
            entry_id_etudiant_note.delete(0, tk.END)
            entry_nom_matiere_note.delete(0, tk.END)
            entry_note_etudiant.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer une note valide.")
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

def ajouter_absence():
    id_etudiant = entry_id_etudiant_absence.get()
    if id_etudiant:
        ecole.ajouter_absence_etudiant(id_etudiant)
        messagebox.showinfo("Succès", f"Absence ajoutée pour l'étudiant {id_etudiant}.")
        entry_id_etudiant_absence.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez entrer un ID étudiant.")

def ajouter_retard():
    id_etudiant = entry_id_etudiant_retard.get()
    if id_etudiant:
        ecole.ajouter_retard_etudiant(id_etudiant)
        messagebox.showinfo("Succès", f"Retard ajouté pour l'étudiant {id_etudiant}.")
        entry_id_etudiant_retard.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez entrer un ID étudiant.")

def generer_bulletin():
    id_etudiant = entry_id_etudiant_bulletin.get()
    format_bulletin = entry_format_bulletin.get().lower()
    if id_etudiant and format_bulletin in ['txt', 'csv']:
        ecole.generer_bulletin(id_etudiant, format=format_bulletin)
        messagebox.showinfo("Succès", f"Bulletin généré pour l'étudiant {id_etudiant}.")
        entry_id_etudiant_bulletin.delete(0, tk.END)
        entry_format_bulletin.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez entrer un ID étudiant et un format valide (txt ou csv).")

def generer_graphique():
    id_etudiant = entry_id_etudiant_graphique.get()
    
    if id_etudiant:
        # Vérifier si l'étudiant existe
        if id_etudiant in ecole.etudiants:
            etudiant = ecole.etudiants[id_etudiant]
            
            matieres = []
            moyennes = []
            
            # Préparer les données pour le graphique
            for matiere, notes in etudiant.notes.items():
                if len(notes) > 0:
                    moyenne_matiere = sum(notes) / len(notes)
                    matieres.append(matiere)
                    moyennes.append(moyenne_matiere)
            
            if not moyennes:
                messagebox.showerror("Erreur", "Pas de notes disponibles pour cet étudiant.")
                return
            
            # Créer le graphique 
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(matieres, moyennes, marker='o', linestyle='-', color='b')
            ax.set_title(f"Évolution des moyennes pour {etudiant.nom} {etudiant.prenom}")
            ax.set_xlabel('Matières')
            ax.set_ylabel('Moyenne')
            ax.set_ylim(0, 20)  # la note maximale est 20
            ax.grid(True)
            
            # Intégrer le graphique dans Tkinter
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()
            canvas.get_tk_widget().pack(pady=10)
            
            # Effacer l'entrée ID
            entry_id_etudiant_graphique.delete(0, tk.END)
        else:
            messagebox.showerror("Erreur", "Étudiant non trouvé.")
    else:
        messagebox.showerror("Erreur", "Veuillez entrer un ID étudiant.")


# Interface graphique pour générer un graphique
label_id_etudiant_graphique = tk.Label(frame_bulletin, text="ID Étudiant pour Graphique:")
label_id_etudiant_graphique.grid(row=3, column=0)
entry_id_etudiant_graphique = tk.Entry(frame_bulletin)
entry_id_etudiant_graphique.grid(row=3, column=1)

button_generer_graphique = tk.Button(frame_bulletin, text="Générer Graphique", command=generer_graphique)
button_generer_graphique.grid(row=4, columnspan=2, pady=5)


# Interface graphique pour ajouter un étudiant
label_nom_etudiant = tk.Label(frame_ajouter, text="Nom Étudiant:")
label_nom_etudiant.grid(row=0, column=0)
entry_nom_etudiant = tk.Entry(frame_ajouter)
entry_nom_etudiant.grid(row=0, column=1)

label_prenom_etudiant = tk.Label(frame_ajouter, text="Prénom Étudiant:")
label_prenom_etudiant.grid(row=1, column=0)
entry_prenom_etudiant = tk.Entry(frame_ajouter)
entry_prenom_etudiant.grid(row=1, column=1)

label_id_etudiant = tk.Label(frame_ajouter, text="ID Étudiant:")
label_id_etudiant.grid(row=2, column=0)
entry_id_etudiant = tk.Entry(frame_ajouter)
entry_id_etudiant.grid(row=2, column=1)

button_ajouter_etudiant = tk.Button(frame_ajouter, text="Ajouter Étudiant", command=ajouter_etudiant)
button_ajouter_etudiant.grid(row=3, columnspan=2, pady=5)

# Interface graphique pour ajouter une matière
label_nom_matiere = tk.Label(frame_actions, text="Nom Matière:")
label_nom_matiere.grid(row=0, column=0)
entry_nom_matiere = tk.Entry(frame_actions)
entry_nom_matiere.grid(row=0, column=1)

button_ajouter_matiere = tk.Button(frame_actions, text="Ajouter Matière", command=ajouter_matiere)
button_ajouter_matiere.grid(row=1, columnspan=2, pady=5)

# Interface graphique pour ajouter un professeur
label_nom_professeur = tk.Label(frame_actions, text="Nom Professeur:")
label_nom_professeur.grid(row=2, column=0)
entry_nom_professeur = tk.Entry(frame_actions)
entry_nom_professeur.grid(row=2, column=1)

label_prenom_professeur = tk.Label(frame_actions, text="Prénom Professeur:")
label_prenom_professeur.grid(row=3, column=0)
entry_prenom_professeur = tk.Entry(frame_actions)
entry_prenom_professeur.grid(row=3, column=1)

button_ajouter_professeur = tk.Button(frame_actions, text="Ajouter Professeur", command=ajouter_professeur)
button_ajouter_professeur.grid(row=4, columnspan=2, pady=5)

# Interface graphique pour ajouter une note à un étudiant
label_id_etudiant_note = tk.Label(frame_actions, text="ID Étudiant:")
label_id_etudiant_note.grid(row=5, column=0)
entry_id_etudiant_note = tk.Entry(frame_actions)
entry_id_etudiant_note.grid(row=5, column=1)

label_nom_matiere_note = tk.Label(frame_actions, text="Nom Matière:")
label_nom_matiere_note.grid(row=6, column=0)
entry_nom_matiere_note = tk.Entry(frame_actions)
entry_nom_matiere_note.grid(row=6, column=1)

label_note_etudiant = tk.Label(frame_actions, text="Note:")
label_note_etudiant.grid(row=7, column=0)
entry_note_etudiant = tk.Entry(frame_actions)
entry_note_etudiant.grid(row=7, column=1)

button_ajouter_note = tk.Button(frame_actions, text="Ajouter Note", command=ajouter_note)
button_ajouter_note.grid(row=8, columnspan=2, pady=5)

# Interface graphique pour ajouter une absence
label_id_etudiant_absence = tk.Label(frame_actions, text="ID Étudiant pour Absence:")
label_id_etudiant_absence.grid(row=9, column=0)
entry_id_etudiant_absence = tk.Entry(frame_actions)
entry_id_etudiant_absence.grid(row=9, column=1)

button_ajouter_absence = tk.Button(frame_actions, text="Ajouter Absence", command=ajouter_absence)
button_ajouter_absence.grid(row=10, columnspan=2, pady=5)

# Interface graphique pour ajouter un retard
label_id_etudiant_retard = tk.Label(frame_actions, text="ID Étudiant pour Retard:")
label_id_etudiant_retard.grid(row=11, column=0)
entry_id_etudiant_retard = tk.Entry(frame_actions)
entry_id_etudiant_retard.grid(row=11, column=1)

button_ajouter_retard = tk.Button(frame_actions, text="Ajouter Retard", command=ajouter_retard)
button_ajouter_retard.grid(row=12, columnspan=2, pady=5)

# Interface graphique pour générer un bulletin
label_id_etudiant_bulletin = tk.Label(frame_bulletin, text="ID Étudiant pour Bulletin:")
label_id_etudiant_bulletin.grid(row=0, column=0)
entry_id_etudiant_bulletin = tk.Entry(frame_bulletin)
entry_id_etudiant_bulletin.grid(row=0, column=1)

label_format_bulletin = tk.Label(frame_bulletin, text="Format Bulletin (txt/csv):")
label_format_bulletin.grid(row=1, column=0)
entry_format_bulletin = tk.Entry(frame_bulletin)
entry_format_bulletin.grid(row=1, column=1)

button_generer_bulletin = tk.Button(frame_bulletin, text="Générer Bulletin", command=generer_bulletin)
button_generer_bulletin.grid(row=2, columnspan=2, pady=5)

# Lancer l'application Tkinter
root.mainloop()

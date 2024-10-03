Système de Gestion des Notes d'un Établissement Scolaire
Ce projet est un système de gestion des notes d'étudiants conçu pour un établissement scolaire. Il permet aux professeurs d'ajouter et de gérer des notes, aux étudiants de consulter leurs résultats, et fournit une interface web basique via Flask.

Fonctionnalités
Ajout de nouveaux étudiants, matières et professeurs : Les utilisateurs peuvent ajouter des étudiants, des matières et des enseignants à la base de données.
Gestion des notes par matière et par étudiant : Les enseignants peuvent enregistrer et gérer les notes des étudiants pour chaque matière.
Calcul des moyennes : Le système calcule automatiquement les moyennes des étudiants par matière.
Génération de bulletins de notes : Génère des bulletins de notes en format texte ou CSV.
Gestion des absences et retards : Le système permet de suivre les absences et les retards des étudiants.
Sauvegarde et chargement des données : Les données peuvent être sauvegardées et chargées depuis des fichiers JSON ou CSV.
Génération de graphiques de performance : Utilisation de la bibliothèque matplotlib pour visualiser l'évolution des notes des étudiants.
Interface web avec Flask : Une interface web simple permet aux professeurs de saisir des notes et aux étudiants de consulter leurs résultats.
Prérequis
Avant de pouvoir exécuter ce projet, assurez-vous d'avoir installé :

Python 3.8+
Les bibliothèques Python suivantes :
Flask
Matplotlib
JSON (inclus par défaut)

Vous pouvez installer les dépendances via pip :
pip install Flask matplotlib

Installation
Clonez ce dépôt GitHub sur votre machine locale :
git clone https://github.com/ton-utilisateur/ton-repo.git
cd ton-repo

Exécutez le fichier Python principal pour démarrer le système :
python main.py

Pour lancer l'interface web Flask, exécutez :
python app.py

L'interface web sera disponible à l'adresse http://127.0.0.1:5000/.

Utilisation
Ajout d'étudiants, de matières et de professeurs : Accédez à l'interface console ou web pour ajouter des informations.
Gestion des notes : Les enseignants peuvent saisir les notes des étudiants pour chaque matière.
Consultation des résultats : Les étudiants peuvent consulter leurs moyennes et leurs bulletins via l'interface web.
Sauvegarde et Chargement des Données
Les données du système sont automatiquement sauvegardées dans un fichier JSON ou CSV lors de la fermeture. Vous pouvez charger des données existantes au démarrage du système.

Contribution
Les contributions sont les bienvenues ! Si vous souhaitez proposer des améliorations ou corriger des bugs, veuillez ouvrir une issue ou soumettre une pull request.

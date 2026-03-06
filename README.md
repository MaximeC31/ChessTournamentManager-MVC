# Chess Tournament Manager

Application de gestion de tournois d'échecs en ligne de commande.

## Installation

1. Cloner le repository
2. Créer un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Exécution du programme

```bash
python main.py
```

## Utilisation

L'application propose un menu principal avec 4 options :

1. **Gérer les joueurs** - Ajouter, lister, rechercher et supprimer des joueurs
2. **Gérer les tournois** - Créer, lister, jouer et supprimer des tournois
3. **Gérer les rapports** - Générer des rapports HTML sur les joueurs et tournois
4. **Quitter** - Fermer l'application

### Générer un nouveau rapport Flake8

```bash
flake8 --format=html --htmldir=flake8-report --exclude=venv,.git,__pycache__,data,reports .
```

Ouvrir ensuite `flake8-report/index.html` dans un navigateur.

## Structure du projet

```
chess-tournament-manager/
├── controllers/         # Contrôleurs (logique métier)
├── models/             # Modèles (entités et gestionnaires)
│   ├── entities/       # Classes métier
│   └── managers/       # Gestionnaires de données
├── views/              # Vues (interface utilisateur)
├── data/               # Fichiers JSON de stockage
├── reports/            # Rapports HTML générés
├── flake8-report/      # Rapport flake8-html
├── main.py            # Point d'entrée
└── requirements.txt   # Dépendances
```

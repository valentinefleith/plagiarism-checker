# :memo: Guide du Makefile
Ce projet utilise un Makefile pour automatiser plusieurs tâches courantes ! On va détailler juste en dessous desquelles il s'agit.

Les commandes sont associées à des codes couleurs pour améliorer la lisibilité des messages affichés dans le terminal :

🔴 Rouge : Erreur
🟢 Vert : Succès
🟡 Jaune : Avertissement
🔵 Bleu : Information
🔵 Cyan : Action en cours


Il est possible de lister toutes les commandes avec :
```bash
make help
```

## 🧹 Premières étapes
➡️ à faire la première fois qu'on rejoint le projet

### Suppression de l'environnement virtuel
```bash
make clean
```
Il faut en premier lieu supprimer l'environnement virtuel actif pour être sûr d'avoir un environnement propre. Cette commande permet de supprimer le dossier `.venv`.

### Installation des dépendances
```bash
make setup
```
Crée un environnement virtuel (`.venv`), puis met à jour *pip* et installe les dépendances listées dans le `requirements.txt`.

### Lancer le serveur
```bash
make run
```
Lance le serveur FastAPI. Le serveur se recharge automatiquement.

### Télécharger un corpus de données
```bash
make corpus
```

### Exécuter des tests
```bash
make test
```
Lance des tests et s'arrête au bout de la première erreur.

## :art: Modifications esthétiques
### Formater le code
```bash
make format
```
Formate le code avec black sur tout le projet.

### Linter le code
```bash
make lint
```
Analyse et corrige les problèmes de style dans le code avec *ruff*.

## ✅ Vérifications avant commit
```bash
make check
```
Exécute `make format`, `make lint` et `make test` pour être sûre qu'aucune erreur n'est présente dans le code avant de faire un commit.
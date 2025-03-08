## Les objectifs du projet

Ce projet a pour objectif d'aider les professeurs, et plus spécifiquement les professeurs de philosophie (possiblement aussi de littérature ou autres disciplines proches), à détecter la triche dans les rendus d'élèves.

<br>

Le but est de proposer une interface similaire à d'autres outils déjà disponibles en ligne tels que [GPTZero](https://gptzero.me/) ou [ZeroGPT](https://www.zerogpt.com/).
Plus spécialement, son utilisation repose sur:
- L'envoi d'un texte (disseration d'un élève)
- Le retour d'un score de probabilité que le texte ait été généré par IA
- L'affichage des détails de probabilités par paragraphes afin de cibler les passages les plus susceptibles d'avoir été plagiés


<br>

Notre outil se différencie de ceux qui existent déjà pour plusieurs raisons:
- Il est complètement gratuit et n'a pas de limite de nombre de caractères par requête
- Le modèle a été spécifiquement entraîné sur le français
- Le modèle a été fine-tuné sur une corpus de copies d'élèves en philosophie : il est donc parfaitement adapté pour cette tâche.

L'outil est actuellement en version bêta, n'hésitez pas à nous contacter pour d'éventuelles améliorations!


<br>

## Données utilisées pour l'entraînement
### Dissertations écrites par des humains
Les données ont été scrappées depuis le site [20aubac.fr](https://www.20aubac.fr/sujets/philosophie-dissertation), qui met à disposition de tous des copies de qualité rédigées par des élèves et des professeurs.


Certaines dissertations sont en accès premium, nous nous sommes donc contentés de récupérer uniquement les données en libre accès.

De plus, nous avons uniquement récolté les devoirs rédigés par des élèves. Nous en avons obtenus 300, consultables [ici](https://github.com/valentinefleith/plagiarism-checker/tree/main/data/dissertation/human).

<br>

### Dissertations écrites par IA Génératives

Nous avons nous-mêmes générés les textes par IA. Nous avons fait en sorte de varier les textes afin d'augmenter autant que possible la robustesse de notre modèle: plusieurs LLMs différents (chatGPT, le Chat de Mistral, mais aussi quelques unes par Llama etc.) et également de varier les prompts dont voilà un exemple:
*Je veux que tu m'écrives une disseration (sans titre, liste, etc.) de philosophie à partir du sujet que je vais t'envoyer. Cela doit correspondre à un niveau terminale en philosophie. Ecris-la comme l'écrirait un élève de terminale. Je veux la structure suivante: une introduction, qui contient l'annonce du sujet, la définition des termes et l'annonce de plan (rédigée) puis un plan en 2 ou 3 parties avec des sous-parties et une conclusion à la fin. N'hésite pas à citer des références philosophiques. Je ne veux pas que tu fasses apparaître les titres des parties et des sous-parties mais que tu rédiges tout. Les sous-parties doivent être développées.*

Nous avons obtenu également environ 300 textes, consultables [ici](https://github.com/valentinefleith/plagiarism-checker/tree/main/data/dissertation/llm).

<br>

### Statut juridique
Dans les mentions légales du site, il y est écrit que le site ne contient pas de publicité et que les données ne sont ni revendues ni communiquées à des tiers mais il n'y a aucune mention sur l'utilisation de leurs données.


Sans interdiction claire, nous pouvons déduire que l'utilisation de ces données est autorisée pour des fin non-commerciales.


<br>

## Implémentation

### Le modèle

Pour le modèle, nous avons fine-tuné BERT sur une tâche de classification de textes à deux classes (humain / IA).
Le fine-tuning a été réalisé avec le GPU gratuit proposé par Google sur Colab. Le code relatif à l'entraînement du modèle est retrouvable [ici](https://github.com/valentinefleith/plagiarism-checker/blob/main/src/training.py).

**Paramètres d'entraînements:**

- `modèle utilisé: bert-base-uncased`
- `nombre de classes: 2`
- `nombre d'époques : 3`
- `taille du batch: 16`
- `optimiseur: AdamW avec un learning rate de 5e-5`
- `fraction de test: 20% (split train/test 80/20)`
- `fonction de loss: celle implémentée dans BertForSequenceClassification (probablement CrossEntropyLoss)`
- `métrique d'évaluation: accuracy`

Le modèle a été entrainé pour une classification par paragraphes.

<br>

### Le backend

Nous avons réalisé l'api en Python avec FastAPI, qui automatise les appels au modèle pour la classification.

Elle contient une route principale, `/prediction` pour faire la requête d'inférence.

<br>

### Le frontend

Le frontend est écrit en JavaScript et nous avons utilisé le framework Vue.js.


<br>

## Méthodologie
### Répartition du travail

Voici la répartition simplifiée du travail, bien que chacun ait contribué sur l'ensemble des parties:

**Valentine** : L'entraînement du modèle, l'API fastAPI et l'écriture de la documentation.

**Baptiste** : La partie frontend (connexion avec les requêtes API + visuel du site) et le déploiement du site.

**Débora** : Recherches pour le fine-tuning, écriture de la documentation, visuel de la page de documentation.

<br>

### Identification et résolution des problèmes

#### Entraînement du modèle
- **Choix du modèle:** hésitation entre entraînement d'un NN from scratch ou fine-tuning d'un LLM.
Nous avons fait un premier test avec un MLP classique sur `scikit-learn`.

Nous avons cependant vite opté pour le fine-tuning car nous avions trop peu de données et voulions maximiser les performances du modèle.

Toutefois, nous manquions de ressources computationnelles pour fine-tuner un gros modèle comme Llama. Nous avons donc fine-tuné BERT.

- **Choix du format des données:** hésitation sur la longueur des données. Ce n'est pas très pertinent de classer à l'échelle d'un texte, car en réalité peu d'élèves trichent en copiant toute la réponse du LLM. 

Nous avons pensé à classer par phrases, mais cela avait des inconvénients (moins bons résultats, et plus de requêtes API).

Nous avons finalement opté pour un entre-deux: classification par paragraphe (texte `split()` sur le `\n`).

- **Pipeline de tests:** nous avons tenté de mettre en place un workflow github avec automatisation de tests unitaires, mais avons rencontré des problèmes de build à cause des nombreuses dépendances de la librairie `transformers` que nous n'avons pas pris le temps de débugger. Pourrait constituer une amélioration future de projet.

- **Frontend:** nous voulions initialement faire une SPA (*single page application*) afin de ne charger qu'une seule page et afficher les résutats via une modale. Toutefois nous trouvions que cela améliorait l'interface et l'experience utilisateur de pouvoir consulter les résultats sur une page séparée.

<br>

## Les résultats

Sur notre corpus de test, le modèle a une accuracy à 0.8744. L'entraînement a donné les logs suivants:

```
Epoch 0: 100%|██████████| 221/221 [01:23<00:00,  2.64it/s, loss=0.351]
Epoch 0 Loss: 0.56337676281573
Epoch 1: 100%|██████████| 221/221 [01:26<00:00,  2.56it/s, loss=0.133]
Epoch 1 Loss: 0.3198494773644667
Epoch 2: 100%|██████████| 221/221 [01:26<00:00,  2.55it/s, loss=0.172]
Epoch 2 Loss: 0.20889226061490057
```

Durant l'entrainement la loss a diminué convenablement entre chaque époque (pas d'instabilité). Nous nous sommes arrêtés à 3 époques pour éviter l'overfitting.

<br>

### Pistes d'amélioration des résultats

Nous pourrions tester de faire varier le modèle (choisir un autre BERT, voire tester avec GPT-2 ou autre modèle accessible avec nos ressources).

Nous pourrions également varier les hyperparamètres afin de chercher les plus optimaux.

Enfin, il serait interéssant d'augmenter le nombre de données et notamment d'obtenir différentes sources (à partir de vraies copies d'élèves notamment). Il serait également envisageable de ne pas se limiter à l'exercice de la dissertation où à la philosophie mais d'étendre la potentielle utilisation de l'outil aux professeurs de façon générale.
## Les objectifs du projet
L'objectif de ce projet est de présenter un site qui permet à l'utilisateur si une dissertation de philosophie a été générée par IA ou écrite et pensée par un élève de lycée.


C'est un site purement fonctionnel qui pourrait aider de nombreux professeurs, notamment l'amie de Valentine qui est très intéressée par le sujet et qui a pu le tester dans un contexte réel sur une copie d'un élève qu'elle soupçonnait d'avoir triché. Elle nous a envoyé ses remarques et donné des pistes par rapport à son expérience utilisateur, ce qui a été très précieux pour nous orienter dans la suite du projet.


## Les données utilisées
### Dissertations écrites par un humain
Les données d'origine viennent du site [20aubac.fr](https://www.20aubac.fr/sujets/philosophie-dissertation) qui met à disposition de tous des copies de qualité rédigées par des élèves et des professeurs.


Certaines dissertations sont en accès premium et nous n'y avons pas accès, c'est pour cette raison que nous nous sommes contentés de récupérer uniquement les données en libre accès gratuit.


### Dissertations écrites par une IA Générative
Pour pouvoir comparer les dissertations, il nous fallait également des données générées par IA. Nous avons utilisé plusieurs modèles d'IA génératives comme Chat GPT, Mistral AI, ollama ou Gemini.


### Statut juridique
Dans les mentions légales du site, il y est écrit que le site ne contient pas de publicité et que les données ne sont ni revendues ni communiquées à des tiers mais il n'y a aucune mention sur l'utilisation de leurs données.


Comme il n'y a pas d'interdiction et qu'ils sont basés sur une mentalité d'open source en partageant leur code sur gitlab, on peut en déduire que tant qu'on ne propose pas un service payant qui utiliserait leur données, on aura pas de problèmes.


### Traitements opérés dessus


## La méthodologie
### Répartition du travail
Nous avons chacun récolté 100 dissertations générées par un LLM. L’idée était de demander à l’IA de nous rédiger une dissertation de niveau lycée en lui donnant le sujet. 


On a fait beaucoup de réunions pour rassembler nos idées et voir ce qui était possible, globalement on a tous essayé de toucher à tout et on s’est mutuellement expliqués ce qu’on a fait dans notre code.


**Baptiste - frontend** 
Baptiste est un pro en JS donc il a fait toute la structure et il nous a montré comment faire pour le site.


**Valentine - backend**
Valentine a fait toute la partie sur le modèle et a aussi participé à la gestion du site.


**Débora - backend, document** 
Débora a écrit toute la doc et l'a ajouté sur le site. Elle a aussi pu faire des tests et de la recherche au début avec Valentine pour trouver la méthodologie à adopter et quels modèles utiliser. 


### Identification et résolution des problèmes
## Test
chiant et on l’a enlevé au final


## L'implémentation ou les implémentations
### Langages utilisés
Le frontend est écrit en vue JS et le backend avec la partie entraînement du modèle est écrit en python.


### API utilisés


## Les résultats

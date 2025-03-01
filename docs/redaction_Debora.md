### Processus 
Avec la commande :

`git status | egrep ".txt" | wc -l`

Je vérifiais combien j'ai ajouté de fichiers pour faire à peu près le compte 
de fichiers par modèle génératif.

Voici le prompt que j'ai envoyé aux LLM :

``̀ coucou ! j'ai besoin que tu répondes à ma question exactement de cette 
manière : le nom en slug qui finis par un .txt (c'est toi qui génère le slug) 
et ta réponse ! je ne veux pas que tu écrives autre chose que ça ! je vais te 
donner un sujet d'exo de philo pour des lycéens et tu dois me rédiger 
l'exercice tu comprends ? je ne veux pas de listes à puces, je veux un texte 
bien structuré avec un plan clair mais pas apparent. Voici le sujet : 
"{sujet}"```


**Modèles utlisés :** 
* mitral ~33 
* gemini 25 
* gpt ~32 
* llama 1 (pas concluant et le site ne marche pas)


### Liens/sitographie
https://www.lemondeinformatique.fr/actualites/lire-microsoft-met-en-open-source-son-petit-modele-phi-4-95707.html 
https://huggingface.co/microsoft/phi-4 
https://techcommunity.microsoft.com/blog/aiplatformblog/introducing-phi-4-microsoft%E2%80%99s-newest-small-language-model-specializing-in-comple/4357090 
https://medium.com/aihzn/microsofts-phi-4-a-powerful-ai-model-now-freely-accessible-b02add45c0c0


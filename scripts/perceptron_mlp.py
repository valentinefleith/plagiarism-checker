"""Script permettant de prétraiter notre corpus et d'entrainer un modele type perceptron 
mlp pour déterminer si un texte a été écrit avec un llm ou non """

import glob
import spacy
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline



nlp = spacy.load('fr_core_news_sm')

def pretraitement(texte) -> str:

    texte = texte.lower().replace('\n', ' ').strip()
    doc = nlp(texte)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)  



def lecture_fichier(fichiers, label, data) -> None:

    for fichier in fichiers:
        with open(fichier, 'r', encoding='utf-8') as f:
            texte = f.read()  
            texte_pretraite = pretraitement(texte)
            data[fichier] = {"texte": texte_pretraite, "label": label}


def vectoriser_textes(data):
 
    textes = [item['texte'] for item in data.values()]
    vectorizer = CountVectorizer(ngram_range=(1, 2))
    X = vectorizer.fit_transform(textes)
    
    return X, vectorizer


def la_pipeline()-> Pipeline:
    """Pipeline pour combiner les différentes opérations de vectorisation bow -> tfidf -> notre mlp"""

    ## on va combiner un bow suivi d'un tfidf je crois c'est une bonne idée et ensuite on va utiliser le perceptron mlp
    return Pipeline([
        ('bow', CountVectorizer(ngram_range=(1, 2))), ## utilisation de bi-gramme ça donne plus de contexte je pense c'est mieux que juste des ngramme
        ('tfidf', TfidfTransformer()),     
        ('mlp', MLPClassifier(hidden_layer_sizes=(100,), max_iter=300))  
    ])


def evaluer_modele(X_train, y_train, X_test, y_test) -> float:

    pipeline = la_pipeline() ## on setup la pipeline
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)  
    precision = precision_score(y_test, y_pred)  
    recall = recall_score(y_test, y_pred)  
    f1 = f1_score(y_test, y_pred)  
    print(f"Accuracy: {accuracy:.4f}, Précision: {precision:.4f}, Rappel: {recall:.4f}, F-mesure: {f1:.4f}")

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Humain', 'LLM'], yticklabels=['Humain', 'LLM'])
    plt.title("C'est beau")
    plt.xlabel("Prédiction")
    plt.ylabel("La vérité vraie")
    plt.show()

   


def main():
     
    data = {}  
    fichiers_llm = glob.glob('../corpus/dissertation/llm/*.txt') 
    fichiers_humains = glob.glob('../corpus/dissertation/human/*.txt')
    
    lecture_fichier(fichiers_llm, label=1, data=data)
    lecture_fichier(fichiers_humains, label=0, data=data)

    # for fichier, contenu in list(data.items())[:5]:
    #     print(contenu['texte'][:100])
    X, vectorizer = vectoriser_textes(data)
    print(f"{X.shape}")

    ## on va faire deux listes bien distinctes une pour les textes et une pour les labels
    textes = [item['texte'] for item in data.values()]
    labels = [item['label'] for item in data.values()]

    print("c'est long ici courage")
    X_train, X_test, y_train, y_test = train_test_split(textes, labels, test_size=0.3, random_state=0)

    evaluer_modele(X_train, y_train, X_test, y_test) ## on appelle la fonction pour evaluer notre modele
    print(f"{vectorizer.get_feature_names_out()[:10]}...")  ##très bizarre ce print 

if __name__ == '__main__':
    main()



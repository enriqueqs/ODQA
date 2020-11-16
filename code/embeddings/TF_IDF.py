import itertools
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os, sys

cwd = os.getcwd()
with open(cwd + "/data/processed/data.pickle","rb") as file:
    dictionary = pickle.load(file)

sys.path.append(cwd + "/code")
from pre_processing import pre_process

def tfidf_vectors(corpus):    
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
  
    return pd.DataFrame(denselist, columns=feature_names)

def tfidf_embedding(question):
    embeddings = []

    docs = [pre_process(doc, stopwords=True, lemmitize=True, stemming=False) for doc in dictionary[question]['sources'].values()]
    question = pre_process(question, stopwords=True, lemmitize=True, stemming=False)
    
    
    
    corpus = list(itertools.chain(*[[question], docs]))

    df = tfidf_vectors(corpus)
    print(df)

    for _, row in df.iterrows():
        embeddings.append(np.array(row))

    sim_to_quest = []
    for _, emb_i in enumerate(embeddings[1:]):
        sim_to_quest.append(np.dot(emb_i, embeddings[0]))

    print(sim_to_quest, "\n", np.argmin(sim_to_quest), "\n")

    if np.argmin(sim_to_quest) == 0:
        return 1
    else:
        return 0
print(list(dictionary.keys())[0])
tfidf_embedding('Where in England was Dame Judi Dench born?')

dictionary[list(dictionary.keys())[0]]['sources'].values()
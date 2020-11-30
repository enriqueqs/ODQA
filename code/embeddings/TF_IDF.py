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

class TFidf:
    def tfidf_vectors(self, corpus):    
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(corpus)
        feature_names = vectorizer.get_feature_names()
        dense = vectors.todense()
        denselist = dense.tolist()
    
        return pd.DataFrame(denselist, columns=feature_names)

    def tfidf_embedding(self, corpus, true_idx, answer):
        df = self.tfidf_vectors(corpus)
        question = corpus[0]
        passages = corpus[1:]

        for _, row in df.iterrows():
            embeddings.append(np.array(row))

        sim_to_quest = []
        for _, emb_i in enumerate(embeddings[1:]):
            sim_to_quest.append(np.dot(emb_i, embeddings[0]))
        
        if answer in passages[np.argmin(sim_to_quest)]:
            return passages[np.argmin(sim_to_quest)]
        else:
            return None



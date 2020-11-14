import itertools
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf_vectors(corpus):    
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
  
    return pd.DataFrame(denselist, columns=feature_names)

def tfidf_embedding(question):
    embeddings = []

    docs = dictionary[question]
    corpus = list(itertools.chain.from_iterable([question].append(docs)))

    df = tfidf_vectors(corpus)

    for index, row in df.iterrows():
        embeddings.append(np.array(row))

    sim_to_quest = []
    for i, emb_i in enumerate(embeddings[1:]):
        sim_to_quest.append(np.dot(emb_i, embeddings[0]))

    return [np.argmin(sim_to_quest), docs[np.argmin(sim_to_quest)]]

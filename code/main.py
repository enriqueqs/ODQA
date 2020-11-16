import pickle
import os 
import numpy as np
from pre_processing import pre_process
from embeddings.rand_baseline import random_baseline
from embeddings.TF_IDF import tfidf_vectors, tfidf_embedding

cwd = os.getcwd()
with open(cwd + "/data/processed/data.pickle","rb") as file:
    dictionary = pickle.load(file)


def pipeline(questions, model):
    predictions = []
    for question in questions.keys():
        predictions.append(model(question))
        
    return predictions

preds = pipeline(dictionary, tfidf_embedding)

acc = sum(preds) / len(preds)
print(acc)


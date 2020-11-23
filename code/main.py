import pickle
import os 
import random
import numpy as np
from pre_processing import pre_process
from embeddings.rand_baseline import random_baseline
from embeddings.TF_IDF import TFidf
from embeddings.Spacy import SpacyEmbed
from embeddings.triviaData import TriviaQA
import itertools

td = TriviaQA()
BERT = SpacyEmbed()
TFIDF = TFidf()

random.seed(42)

cwd = os.getcwd()
with open(cwd + "/data/processed/dict_idq_paragraphs_answer.pickle","rb") as file:
    dictionary = pickle.load(file)

keys = list(dictionary.keys())
sample = []
while len(sample) < 1000:
    tmp_idx = random.choice(keys)
    if tmp_idx in sample:
        continue
    else:
        sample.append(tmp_idx)

preds = []
for idx in sample:
    qs = dictionary[idx]['question']
    qs_p = dictionary[idx]['paragraphs']
    qs_p_range = len(qs_p)
    
    neg_ex = []
    while len(neg_ex) < 9:
        tmp_idx = random.choice(keys)
        if tmp_idx == idx:
            continue
        else:
            neg_ex.append(tmp_idx)

    neg_ex_p = [dictionary[neg]['paragraphs'] for neg in neg_ex]
    neg_ex_p_flat = list(itertools.chain(*neg_ex_p))

    D = list(itertools.chain(*[[qs], qs_p, neg_ex_p_flat]))

    preds.append(BERT.spacyEmbedding(D, len(qs_p)))




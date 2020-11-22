import pickle
import os 
import random
import numpy as np
from pre_processing import pre_process
from embeddings.rand_baseline import random_baseline
from embeddings.TF_IDF import tfidf_vectors, tfidf_embedding
from embeddings.triviaData import TriviaQA
import itertools

td = TriviaQA()

random.seed(42)

sample = list(set(td.getRandomIndex() for x in range(2000)))

preds = []
for idx in sample[:10]:
    qs = td.getQuestion(idx)
    qs_p = td.getDocBlocks(idx)
    qs_p_range = len(qs_p)

    
    neg_ex = []
    while len(neg_ex) < 9:
        tmp_idx = td.getRandomIndex()
        if tmp_idx == idx:
            continue
        else:
            neg_ex.append(tmp_idx)

    neg_ex_p = [td.getDocBlocks(neg) for neg in neg_ex]
    neg_ex_p_flat = list(itertools.chain(*neg_ex_p))

    D = list(itertools.chain(*[[qs], qs_p, neg_ex_p_flat]))

    preds.append(tfidf_embedding(D, len(qs_p)))
    



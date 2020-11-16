import pickle
import os 
import numpy as np
import random
random.seed(1234)

cwd = os.getcwd()
with open(cwd + "/data/processed/data.pickle","rb") as file:
    dictionary = pickle.load(file)

def random_baseline(question):
    indexes = list(dictionary[question]['ranks'].values())

    rand = random.choice(indexes)

    if rand == dictionary[question]['ranks'][0]:
        return 1
    else:
        return 0
import spacy
import os, sys
import random
from datasets import load_dataset
cwd = os.getcwd()
sys.path.append(cwd + "/code")
from pre_processing import pre_process


def spacy_embedding(text):
    text = pre_process(text, stopwords = True, lemmitize = True, stemming = True)
    ebd = nlp(text)
    return ebd


def get_quest_doc(dataset, doc_only=False):
    idx = random.randint(0, len(dataset)-1)
    context = dataset[idx]['search_results']['search_context']
    if len(context) == 0:
        print(0)
        return get_quest_doc(dataset, doc_only)
    else:
        doc_idx = random.randint(0, len(context)-1)
        doc = context[doc_idx]
        quest = dataset[idx]['question']
        if doc_only == True: 
            return doc
        else:
            return quest, doc


if __name__ == "__main__":
    sims = []
    dataset = load_dataset('trivia_qa', 'rc')['train']
    nlp = spacy.load("en_trf_bertbaseuncased_lg")

    quest, tartget_doc = get_quest_doc(dataset, doc_only=False)
    quest_ebd =  spacy_embedding(quest)
    tartget_doc_ebd = spacy_embedding(tartget_doc)

    sims.append(quest_ebd.similarity(tartget_doc_ebd))

    for i in range(10):
        print(i*10,'%')
        random_doc = spacy_embedding(get_quest_doc(dataset, doc_only=True))
        sims.append(quest_ebd.similarity(random_doc))

    if max(sims) == sims[0]:
        print(sims)
        print('suc')
    else:
        print(sims)
        print('fail')
       

# sentence embeddings
# print('vector: ', question.vector)  # or apple1.tensor.sum(axis=0)
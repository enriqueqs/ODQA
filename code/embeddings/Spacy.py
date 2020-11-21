
import spacy
import os
import sys
from random import randint
from datasets import load_dataset
cwd = os.getcwd()
sys.path.append(cwd + "/code")
from pre_processing import pre_process

class SpacyEmbed:
    def __init__(self):
        self.nlp = spacy.load("en_trf_bertbaseuncased_lg")

    def embed(self, text):
        text = pre_process(text, stopwords=True, lemmitize=True, stemming=True)
        return self.nlp(text)
        

class TriviaQA:
    def __init__(self):
        self.trainData = load_dataset('trivia_qa', 'rc')['train']

    def getRandomIndex(self):
        idx = randint(0, len(self.trainData)-1)
        while len(self.getContext(idx)) == 0:
            idx = randint(0, len(self.trainData))
        return idx
    
    def getRandomDoc(self):
        idx = self.getRandomIndex()
        context = self.getContext(idx)
        return context[randint(0, len(context)-1)]

    def getQuestion(self, idx):
        return self.trainData[idx]['question']

    def getContext(self, idx):
        return self.trainData[idx]['search_results']['search_context']

    def __len__(self):
        return len(self.trainData)


def getSimilarityScore(questIndex, random=True):
    question = triviaQA.getQuestion(questIndex)
    questEmbedding = spacyEmbed.embed(question)

    if not random:
        context = triviaQA.getContext(questIndex)
        doc = context[randint(0,len(context)-1)]
    else:
        doc = triviaQA.getRandomDoc()

    docEmbedding = spacyEmbed.embed(doc)
    return questEmbedding.similarity(docEmbedding)



def getRetriveResult(scores):

    if max(scores) == scores[0]:
        print(scores)
        print('successed')
        return True
    else:
        print(scores)
        print('fail')
        return False

if __name__ == "__main__":
    scores = []
    triviaQA = TriviaQA()
    spacyEmbed = SpacyEmbed()
    idx = triviaQA.getRandomIndex()

    scores.append(getSimilarityScore(idx, random=False))
    for i in range(10):
        print(i*10, '%')
        scores.append(getSimilarityScore(idx))

    getRetriveResult(scores)



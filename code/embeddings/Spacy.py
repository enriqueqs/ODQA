
import spacy
import os
import sys
from random import randint
cwd = os.getcwd()
sys.path.append(cwd + "/code")
from pre_processing import pre_process

class SpacyEmbed:
    def __init__(self):
        self.nlp = spacy.load("en_trf_bertbaseuncased_lg")

    def embed(self, text):
        text = pre_process(text, stopwords=True, lemmitize=True, stemming=True)
        return self.nlp(text)


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
    outputMsg = str(scores) + "success" if max(scores) == scores[0] else str(scores) + "fail" 
    print(outputMsg)
    return True if max(scores) == scores[0] else False

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



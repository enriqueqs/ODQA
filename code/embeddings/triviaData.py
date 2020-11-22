
import os
import sys
from random import randint
from datasets import load_dataset
cwd = os.getcwd()
sys.path.append(cwd + "/code")
from pre_processing import pre_process


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

    def getAnswer(self, idx):
        return self.trainData[idx]['answers']

    def getContext(self, idx):
        return self.trainData[idx]['search_results']['search_context']
    
    def getDividedDoc(self, idx, length=100, stride=40):
        context = self.trainData[idx]['search_results']['search_context']
        context = pre_process(context).split()
        i = 0
        while i < len(context):
        # for i in range(len(context)):
            wordlist = context[i:i+100]
            ' '.join(wordlist)





    def __len__(self):
        return len(self.trainData)
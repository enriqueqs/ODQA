
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
        return pre_process(self.trainData[idx]['question'], stemming=False)

    def getAnswer(self, idx):
        return self.trainData[idx]['answer']['normalized_value']

    def getContext(self, idx):
        return self.trainData[idx]['search_results']['search_context']
    
    def getDocBlocks(self, idx, blockSize=100, stride=20):
        doc = self.getContext(idx)[0]
        doc = pre_process(doc, stemming=False).split()
        i = 0
        docBlocks = []
        while i < len(doc):
            j = i + blockSize
            wordlist = doc[i : j] 
            docBlocks.append(' '.join(wordlist))
            i += stride
        return docBlocks

    def __len__(self):
<<<<<<< HEAD
        return len(self.trainData)
=======
        return len(self.trainData)

<<<<<<< HEAD
#test
t = TriviaQA()
idx = t.getRandomIndex()
docBlocks = t.getDocBlocks(idx)
print(len(docBlocks))
=======
# t = TriviaQA()
# idx = t.getRandomIndex()
# docBlocks = t.getDocBlocks(idx)
# print(len(docBlocks))
>>>>>>> 3f9a24171f43d26c2d702d07695d8bb719cdd41b
>>>>>>> 3321ae95d1f0b09aabb5000d05c94964688def94

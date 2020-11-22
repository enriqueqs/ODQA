import spacy

class SpacyEmbed:
    def __init__(self):
        self.nlp = spacy.load("en_trf_bertbaseuncased_lg")

    def spacyEmbedding(self, corpus, correct_idx):
        # text = pre_process(text, stopwords=True, lemmitize=True, stemming=True)
        scores = []
        question = self.nlp(corpus[0])
        for i in range(1, len(corpus)):
            print(i)
            c = self.nlp(corpus[i]) 
            scores.append(question.similarity(c)) 
        rs_idx = scores.index(max(scores))
        if rs_idx < correct_idx:
            return 1
        else:
<<<<<<< HEAD
            return 0


# def getSimilarityScore(questIndex, random=True):
#     question = triviaQA.getQuestion(questIndex)
#     questEmbedding = spacyEmbed.embed(question)

#     if not random:
#         context = triviaQA.getContext(questIndex)
#         doc = context[randint(0,len(context)-1)]
#     else:
#         doc = triviaQA.getRandomDoc()

#     docEmbedding = spacyEmbed.embed(doc)
#     print(type(docEmbedding))
#     print(type(questEmbedding))

#     return questEmbedding.similarity(docEmbedding)





def getRetriveResult(scores):
    outputMsg = str(scores) + "success" if max(scores) == scores[0] else str(scores) + "fail" 
    print(outputMsg)
    return True if max(scores) == scores[0] else False

if __name__ == "__main__":
    scores = []
    triviaQA = TriviaQA()
    spacyEmbed = SpacyEmbed()
    idx = triviaQA.getRandomIndex()
    # getSimilarityScore(idx, random=True)
    # scores.append(getSimilarityScore(idx, random=False))
    # for i in range(10):
    #     print(i*10, '%')
    #     scores.append(getSimilarityScore(idx))

    # getRetriveResult(scores)


=======
            return 0
>>>>>>> 62f6d8dfa6403407e1475bb6fca47785066c7f5e

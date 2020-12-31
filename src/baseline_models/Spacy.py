import spacy
from spacy.attrs import LOWER, POS, ENT_TYPE, IS_ALPHA

class SpacyEmbed:
    def __init__(self):
        self.nlp = spacy.load("en_trf_bertbaseuncased_lg")

    def spacyEmbedding(self, corpus, correct_idx):
        # text = pre_process(text, stopwords=True, lemmitize=True, stemming=True)
        scores = []

        question = self.nlp(corpus[0])
        # print(type(question.to_array([LOWER, POS, ENT_TYPE, IS_ALPHA])))
        for i in range(1, len(corpus)):
            print(i,':', len(corpus))
            c = self.nlp(corpus[i]) 
            scores.append(question.similarity(c)) 
        rs_idx = scores.index(max(scores))
        if rs_idx < correct_idx:
            return 1
        else:
            return 0


s = SpacyEmbed()
corpus = ['This Date in Central Minnesota History','This Date in Central Minnesota History Jim Maurice December']
s.spacyEmbedding(corpus, 1)
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





# def getRetriveResult(scores):
#     outputMsg = str(scores) + "success" if max(scores) == scores[0] else str(scores) + "fail" 
#     print(outputMsg)
#     return True if max(scores) == scores[0] else False

# if __name__ == "__main__":
#     scores = []
#     triviaQA = TriviaQA()
#     spacyEmbed = SpacyEmbed()
#     idx = triviaQA.getRandomIndex()
    # getSimilarityScore(idx, random=True)
    # scores.append(getSimilarityScore(idx, random=False))
    # for i in range(10):
    #     print(i*10, '%')
    #     scores.append(getSimilarityScore(idx))

    # getRetriveResult(scores)



import spacy

class SpacyEmbed:
    def __init__(self):
        self.nlp = spacy.load("en_trf_bertbaseuncased_lg")

    def spacyEmbedding(self, corpus, correct_idx):
        # text = pre_process(text, stopwords=True, lemmitize=True, stemming=True)
        scores = []
        question = self.nlp(corpus[0])
        for i in range(1, len(corpus)):
            c = self.nlp(corpus[i]) 
            scores.append(question.similarity(c)) 
        rs_idx = scores.index(max(scores))
        if rs_idx < correct_idx:
            return 1
        else:
            return 0
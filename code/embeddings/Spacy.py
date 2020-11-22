import spacy

class SpacyEmbed:
    def __init__(self):
        self.nlp = spacy.load("en_trf_bertbaseuncased_lg")

    def spacyEmbedding(self, corpus, true_idx):
        embeddings = []  

        for idx in corpus:
            embeddings.append(np.array(self.nlp(corpus[i])))

        sim_to_quest = []
        for _, emb_i in enumerate(embeddings[1:]):
            sim_to_quest.append(np.dot(emb_i, embeddings[0]))

        if np.argmin(sim_to_quest) < true_idx:
            return 1
        else:
            return 0        
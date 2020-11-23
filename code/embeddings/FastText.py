import nltk
import numpy as np
from gensim import matutils

class FastText:
  def sentence_emb(self, sentence, normalize = False):
    sentence_sum = []
    words = nltk.word_tokenize(sentence)

    return sentence_sum.append(model.word_vec(tmp_word) for tmp_word in words)

  def FastText(self, corpus, model, true_idx, normalize = False):
    embeddings = []

    if normalize: 
      embeddings.append(self.sentence_emb(paragraph, normalize=True) for paragraph in courpus)
    else:
      embeddings.append(self.sentence_emb(paragraph, normalize=False) for paragraph in courpus)
    average_embedding = [np.average(emb, axis=0) for emb in embeddings]
    if normalize:
      average_embedding = matutils.unitvec(average_embedding)
    
    sim_to_qs = []
    for _, emb_i in enumerate(embeddings):
      sim_to_qs.append(np.dot(emb_i, average_embedding))

    if np.argmin(sim_to_qs) < true_idx:
      return 1
    else:
      return 0
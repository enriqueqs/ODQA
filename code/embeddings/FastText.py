import nltk

def word_embedding(sentence, model, normalize):
    embeddings = []
    words = nltk.word_tokenize(sentence)

    for word in words:

        sentence_sum.append(model.word_vec(tmp_word, use_norm=True))
        if normalize: 
        embeddings.append(matutils.unitvec(np.array(sentence_sum).mean(axis=0)))
        else:
        embeddings.append(np.average(sentence_sum, axis=0))
  average_embedding = np.average(embeddings, axis=0)
  if normalize:
    average_embedding = matutils.unitvec(average_embedding)
  sim_to_mean = []
  for i, emb_i in enumerate(embeddings):
    sim_to_mean.append(np.dot(emb_i, average_embedding))
  print(words[np.argmin(sim_to_mean)],',', sim_to_mean[np.argmin(sim_to_mean)])
  #print("\n")
  #return words[np.argmin(sim_to_mean)], sim_to_mean[np.argmin(sim_to_mean)]
  return words[np.argmin(sim_to_mean)]
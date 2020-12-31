from datasets import load_dataset, ReadInstruction
import random
import pickle
random.seed(42)

# From record 10 (included) to record 20 (excluded) of `train` split.
train_0_200_ds = load_dataset('trivia_qa','rc', split=ReadInstruction('train', from_=1, to=200, unit='abs'))

def search_result_from_question(data, n: int) -> dict:
    out = {}
    for question in data:
        q = question['question']
        qty_orig_source=len(question['search_results']['rank'])
        if (qty_orig_source < 3) :
            continue
        if (n > qty_orig_source):
            q_filling=n-qty_orig_source
            j=0
            sources={}
            ranks = {}
            for i in range(qty_orig_source):
                sources[i]=question['search_results']['search_context'][i]
                ranks[i]=question['search_results']['rank'][i]
            while(q_filling>0):
                l = random.randrange(len(data))
                while(len(data[l]['search_results']['rank'])<3):
                    l = random.randrange(len(data))
                m = random.randrange(len(data[l]['search_results']['rank']))
                sources[j+qty_orig_source]=data[l]['search_results']['search_context'][m]
                ranks[j+qty_orig_source]=-1
                q_filling-=1
                j+=1
        else:
            for i in range(n):
                sources[i]=question['search_results']['search_context'][i]
                ranks[i]=question['search_results']['rank'][i]
        out[q]={"sources": sources,
                "ranks": ranks}
    return out

reduced_dataset = search_result_from_question(train_0_200_ds, 10)
data_path="/Users/enriqueqs/Github_repos/ODQA/data/processed"
with open(data_path + '/data.pickle', 'wb') as f:
    pickle.dump(reduced_dataset, f)


from datasets import list_datasets, load_dataset

#Access datasets from the HuggingFace library
datasets_list = list_datasets()

#Cache the dataset trivia_qa 
trivia = load_dataset('trivia_qa', 'rc')

trivia['train'][8]['search_results']['rank']
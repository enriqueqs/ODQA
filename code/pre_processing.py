import re, string
import nltk
from nltk import tokenize
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english')) 
punctuation = str.maketrans('', '', string.punctuation)
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 
from nltk.stem import PorterStemmer 
porter = PorterStemmer()

def pre_process(document, stopwords = True, lemmitize = True, stemming = True):
    document = re.sub(r'\s+',' ',document)
    document = document.lower()

    tokens = word_tokenize(document)
    if stopwords == True:
        tokens = [token for token in tokens if not token in stop_words]
    if lemmitize == True:
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    if stemming == True:
        tokens = [porter.stem(token) for token in tokens]
    doc = ' '.join(tokens)
    filtered_doc = doc.replace("’",'').replace("‘",'')
    filtered_doc = filtered_doc.translate(punctuation)
    
    return re.sub(' +', ' ', filtered_doc)
        
import pandas as pd
import preprocessing
import pandas as pd
import numpy as np
#import scipy.sparce
import scipy
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from nltk.corpus import stopwords
import joblib
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics.pairwise import linear_kernel

from sklearn.metrics.pairwise import cosine_similarity

def get_results(corpus, txt):
    
    vectorizer = TfidfVectorizer()
    
    #Create a matrix with the following structure 
    #The tuple represents: (document_id, token_id)
    #The value following the tuple represents the tf-idf score of a given token in a given document
    #The tuples that are not there have a tf-idf score of 0
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    #Equivalent to CountVectorizer followed by TfidfTransformer.
    txt_vectorize = vectorizer.transform([txt])
    
    #Perform dot product between tfidf matrix and the txt vectorized
    cosine_similarities = linear_kernel(tfidf_matrix , txt_vectorize).flatten()
    
    #find the top 5 related documents, using some negative array slicing 
    #most related documents have highest cosine similarity values, hence at the end of the sorted indices array
    related_docs_indices = cosine_similarities.argsort()[:-5:-1]
    
    #Exctract similarity values from the array
    similarity_values = cosine_similarities[related_docs_indices]
    
    return related_docs_indices,similarity_values
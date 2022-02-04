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

def compute_score(row, vec):
    sc = 0
    #Gestisci il caso di una riga nulla che in questo contesto ha valore float 
    if (type(row) == float):
        return 0
    row = row.replace("\\", "")
    for w in vec:
        if w[0] in row.split(" "):
            sc += 1

    return sc/len(vec)


def manage_keywords(kwds):
    score = []
    good_match = []
    #df =  pd.read_csv("DB/questions_cleared.csv", sep=",", low_memory = False, encoding='latin-1')
    data = pd.read_csv('DB/Preprocessed_data.csv')
    data = data["processed_title"]
    
    #for i, row in data.iterrows():
    for i, row in data.iteritems():
        tup = str(i), compute_score(row, kwds)
        score.append(tup)
        if score[i][1] != 0.0:
            good_match.append(score[i])

    good_match.sort(key=lambda x: x[1], reverse=True)
    # print(good_match[:5])
    return good_match[:10]

def get_word_count_vec(docs):

    docs = docs.tolist()
    
    #creating an instance of CountVectorizer
    # (useful for converting a collection of text documents to a matrix of token counts)
    count_vec = CountVectorizer(max_df=0.85)
    
    #wc_matrix are the final term-document matrix whit all the terms of the corpus
    wc_matrix = count_vec.fit_transform(docs)
    
    #saving data for unigrams
    scipy.sparse.save_npz('DB/wc_matrix.npz', wc_matrix)
    joblib.dump(count_vec, "DB/count_vec.pkl")
    
    
def tf_idf(count_world, cvec, phrase):
    
    #preprocessing the phrase
    clear_phrase = preprocessing.clear_text(phrase);

    #creation of the TfidfTransformer Object,
    #useful for transform a count matrix to a normalized tf or tf-idf representation
    transformer_weights = TfidfTransformer(smooth_idf=True, use_idf=True)
    
    #fitting
    transformer_weights.fit_transform(count_world)
    tf_idf_vec = transformer_weights.transform(cvec.transform([clear_phrase]))
    
    #computing the final weights for the words
    weights = np.asarray(tf_idf_vec.mean(axis=0)).ravel().tolist()
    weights_df = pd.DataFrame({'term': cvec.get_feature_names(), 'weight': weights})
    result = weights_df.sort_values(by='weight', ascending=False).head(8)
    
    return result.values.tolist()

    '''
    
    allTitleEmb = pd.read_csv('DB/titleEmbeddings.csv').values
    
    vectorSearch = np.array([tf_idf_vec])
    
    similarityCosine = similarityCosine*(1+0.4*data.score)
    
    similarityCosine = pd.Series(cosine_similarity(vectorSearch, allTitleEmb)[0])
    
    '''

#Create a matrix with the following structure 
#The tuple represents: (document_id, token_id)
#The value following the tuple represents the tf-idf score of a given token in a given document
#The tuples that are not there have a tf-idf score of 0
def create_matrix(corpus):
    #Corpus is already preprocessed
    tfidf_matrix = TfidfVectorizer().fit_transform(corpus)
    
    #scipy.sparse.save_npz('DB/tfidf_matrix.npz', tfidf_matrix)
    return tfidf_matrix

def get_results(corpus, txt):
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    #Equivalent to CountVectorizer followed by TfidfTransformer.
    txt_vectorize = vectorizer.transform([txt])
    
    #Perform dot product between tfidf matrix and the txt vectorized
    cosine_similarities = linear_kernel(tfidf_matrix , txt_vectorize).flatten()
    
    #find the top 5 related documents, using some negative array slicing 
    #most related documents have highest cosine similarity values, hence at the end of the sorted indices array
    related_docs_indices = cosine_similarities.argsort()[:-5:-1]
    
    return related_docs_indices
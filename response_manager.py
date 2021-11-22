import tfidf 
#import scipy.sparce
import scipy
import joblib

def gen_response(txt):
    #load wc_matrix presaved
    matr = scipy.sparse.load_npz('DB/wc_matrix.npz')
    cvec = joblib.load("DB/count_vec.pkl")
            
    # Compute tf-idf score on user message
    resp = tfidf.tf_idf(matr, cvec, txt)

    print(resp)
            
    output = tfidf.manage_keywords(resp)
            
    # Setting number of results for the main process
    n_results = 3

    print("\nList of document with high similarity:")
    #Output is a list of tuple lke [["id of the question","similarity score"],...,]
    print(output)
    
    related_results = []
    
    return output
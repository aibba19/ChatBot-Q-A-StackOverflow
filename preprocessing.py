from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import string
import nltk 
import re 

#Da runnare solo la prima volta per scaricare i pacchetti 
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')

#adding personalized stopwords
newStopWords = ['def', 'quot']
stopwords.words('english').extend(newStopWords)

# Passaggio intermedio per pulire il corpo del db dalle parte non utili all'obiettivo 
def remove_tags(df):
    #elimina tutte le parti di codice
    df.replace('((?s)<code>.+?</code>)','',regex= True, inplace= True)
    
    df.replace('((?s)<blockquote>.+?</blockquote>)','',regex= True, inplace= True)
    #La seguente linea elimina tutte le parole dentro i tag a, dove alcuni potrebbero essere necessari
    #da testare
    df.replace('((?s)<a href=.+?>.+?</a>)','',regex= True, inplace = True)
    
    
    #df.replace('(http.+?</a>)', '' , regex= True, inplace = True ) 
    df.replace('(<.*?>)',' ',regex=True, inplace = True)
    #df.replace('(\.?)',' ',regex=True, inplace = True )
    df.replace('(\n)',' ',regex=True,inplace=True)
    
    #df.replace('(\\)',' ',regex=True,inplace=True)
    #df.replace('(/)',' ',regex=True,inplace=True)
    #df.replace('(/)',' ',regex=True,inplace=True)
    #replace everything between parenthesis ( )
    df.replace('(\((.*?)\))',' ',regex=True,inplace=True)
    
    #Remove next word after def, to eliminate personalized name of functions not needed for processing
    df.replace("(^def: (\w+))",' ',regex=True,inplace=True)
    
    #Remove the html keyword quot and def 
    df.replace("(/\b($quot)\b/i)",'',regex=True,inplace=True)
    
    df.replace("(/\b($def)\b/i)",'',regex=True,inplace=True)
    return df




def clear_text(txt, mode):
    
    table = str.maketrans(string.punctuation, " "*len(string.punctuation))
    stripped = [txt.translate(table)]
    
    tokens = word_tokenize(stripped[0])

    # Lowercase conversion
    tokens = [w.lower() for w in tokens]

    # Deleting all non-words
    final_wds = [w for w in tokens if w.isalpha()]

    
    # removing stopwords
    stop_wd = set(stopwords.words('english'))
    final_wds = [w for w in final_wds if w not in stop_wd]
    
    #skipping lemmatize phase if we are cleaning for tf-idf
    if (mode == "tfidf"):
        # Lemmatization process
        lemtz = WordNetLemmatizer()
        final_wds = [lemtz.lemmatize(w) for w in final_wds]
        
    final_text = []

    for term in final_wds:
        final_text.append(term + " ")

    last = ''.join(map(str, final_text))

    return last
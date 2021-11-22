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

# Passaggio intermedio per pulire il corpo del db dalle parte non utili all'obiettivo 
def remove_tags(df):
    #elimina tutte le parti di codice
    df.replace('((?s)<code>.+?</code>)','',regex= True, inplace= True)
    #La seguente linea elimina tutte le parole dentro i tag a, dove alcuni potrebbero essere necessari
    #da testare
    df.replace('((?s)<a href=.+?>.+?</a>)','',regex= True, inplace = True)
    
    
    #df.replace('(http.+?</a>)', '' , regex= True, inplace = True ) 
    df.replace('(<.*?>)',' ',regex=True, inplace = True)
    df.replace('(\.?)','',regex=True, inplace = True )
    df.replace('(\n)',' ',regex=True,inplace=True)
    
    #print(df)
    
    #df.apply(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    #for index, value in df.items():
    #    value = re.sub('<.*?>', '', value)
    #    print(value)

    return df




def clear_text(txt):
    # Tokenization
    tokens = word_tokenize(txt)

    # Lowercase conversion
    tokens = [w.lower() for w in tokens]

    # Removing punctuation
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    # Deleting all non-words
    final_wds = [w for w in stripped if w.isalpha()]

    # removing stopwords
    stop_wd = set(stopwords.words('english'))
    final_wds = [w for w in final_wds if w not in stop_wd]
    
    #skipping lemmatize phase 
    # Lemmatization process
    #lemtz = WordNetLemmatizer()
    #final_wds = [lemtz.lemmatize(w) for w in final_wds]
    final_text = []

    for term in final_wds:
        final_text.append(term + " ")

    last = ''.join(map(str, final_text))

    return last
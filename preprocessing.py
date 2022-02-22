from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import string
import nltk 
import re 

#To run only one time if you getting errors from nltk library 

#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')


#Function to clean the html text from the stack overflow database from the parts that not suit well for our task 
def remove_tags(df):
    
    
    #Remove all the codes part 
    df.replace('((?s)<code>.+?</code>)','',regex= True, inplace= True)
    
    #Remove quote parts 
    df.replace('((?s)<blockquote>.+?</blockquote>)','',regex= True, inplace= True)
    
    #Remove all links 
    df.replace('((?s)<a href=.+?>.+?</a>)','',regex= True, inplace = True)
    
    #Remove all html tags 
    df.replace('(<.*?>)',' ',regex=True, inplace = True)
    
    #Replace all \n with a space
    df.replace('(\n)',' ',regex=True,inplace=True)
    
    #Replace everything between parenthesis ( )
    df.replace('(\((.*?)\))',' ',regex=True,inplace=True)
    
    #Remove next word after def, to eliminate personalized name of functions not needed for processing
    df.replace("(^def: (\w+))",' ',regex=True,inplace=True)
    
    #Remove the html keyword quot and def 
    df.replace("(/\b($quot)\b/i)",'',regex=True,inplace=True)
    df.replace("(/\b($def)\b/i)",'',regex=True,inplace=True)
    
    return df

#Function to clear the ontology data retrivied from rdf files 
def clean_ontology(df):
    
    #From the functions name remove the beginning part related to code ontology
    df.loc[:,'function'].replace('(http://rdf.webofcode.org/woc/)','',regex= True, inplace= True)
    
    #Replace all \n with a space 
    df.replace('(\n)',' ',regex=True,inplace=True)
    
    #Delete everything between < > brackets
    df.replace('(<(.*?)\>)','',regex= True, inplace= True)
    
    #Insert space between lowercase and uppercase character to divide function names as : getAccessibleToken    
    df.loc[:,'description'].replace(r'([a-z])([A-Z])',r"\1 \2",regex = True, inplace = True )
    
    #Delete everything after @ in the function description, since that represent return type and parameter description not utils for our purpouse
    df.loc[:,'description'].replace('(@.*)','',regex= True, inplace= True)
    
    #Delete descrptions where we find a { because from previous steps we have lines to not use with the parenthesis
    df.loc[:,'description'].replace('((?s).*{.*)','',regex= True, inplace= True)
    

#Main function to clean the text with NLP technics, it takes as an argument only a phrase
#The steps followed to process a piece of raw text are:

#Convert raw text into tokens
#Convert tokens to lower case
#Remove punctuations
#Remove Stopwords
#Note: We skipped a 'Stemming/Lemmatization' step because we did not want alter the domain specific terms used in our corpus and risk losing precious information

def clear_text(txt):
    
    #Remove puntuaction
    table = str.maketrans(string.punctuation, " "*len(string.punctuation))
    stripped = [txt.translate(table)]
    
    tokens = word_tokenize(stripped[0])

    # Lowercase conversion
    tokens = [w.lower() for w in tokens]

    # Deleting all non-words
    final_wds = [w for w in tokens if w.isalpha()]
    
    #adding personalized stopwords
    stop_words = stopwords.words('english')
    stop_words.extend(['def', 'quot'])
    
    # removing stopwords
    stop_wd = set(stop_words)
    final_wds = [w for w in final_wds if w not in stop_wd]
    
    #Lemmatization process
    #lemtz = WordNetLemmatizer()
    #final_wds = [lemtz.lemmatize(w) for w in final_wds]
        
    final_text = []

    for term in final_wds:
        final_text.append(term + " ")

    last = ''.join(map(str, final_text))

    return last


# StackBot

StackBot is a telegram bot that allows users to find a possible solution to their problem involving the Python world and a possible corresponding Java function. 

## Setting UP 


### Initialization

0. Run pip install requirements.txt;

### Bot usage 

1. Start the service by running the file main.py;

2. Once the main is running the service is active, on Telegram you need to search for the bot (@StackBot) and start a chat;

3. To get started, type /start, and follow the bot instructions;


## Project information

### Dataset composition

*Stack Overflow data* : downloaded from Google BigQuery services, this dataset includes an archive of Stack Overflow content, including posts, votes, tags, and badges. This dataset is updated to mirror the Stack Overflow content on the Internet archive. More info about the dataset is given at: https://www.kaggle.com/stackoverflow/stackoverflow

From all the data we need:

* Title
* Question body
* Answers for that question
* Votes for each answers

We decide to restrict the query only to questions that has 'python' has a tag, due to the abundance of Q&A in Stack Overflow, to perform better test and try to give more precise answers. However this process can be done over other argument just by changing the LIKE '%python%' word in the query.

*CodeOntology data* : downloaded from codeontology.org, an RDF file containing Java functions names and their description.

### Main  features
NLP features implemented in this project are:

*Preprocessing Data*: data were preprocessed using both regex and NLP helping fucntions from Nltk library, in order to obtain tokens ready for further work, creating two new databases, one for stack overflow data and one for ontology data.

*Tf-idf*: short for term frequency–inverse document frequency, can tell you about the relevant importance of a term based upon a document,here used to rank search results based on relevance, with results which are more relevant to the user having higher TF-IDF scores. Don't consider word context.

*Word2vec*: is an algorithm that uses shallow 2-layer, not deep, neural networks to ingest a corpus and produce sets of vectors.

*Cosine similarity*: measure of similarity used here with both tf-idf and word2vec technics.


### Python libraries

nltk &#x2192; Preprocessing text with NLP technics
numpy &#x2192; Powerful tool for matrix operations
pandas &#x2192; Dataframe management
scipy &#x2192; Managing NLP tools
gensim &#x2192; Word2Vec module
google-api-core &#x2192; Download StackOverflow data
google-auth &#x2192; Download StackOverflow data
jupyterlab &#x2192; IDE 
numpy &#x2192; Powerful tool for matrix operations
regex &#x2192; Cleaning and preprocessing data
telepot &#x2192; Telegram bot
sklearn &#x2192; Vectorizer for TF-IDF 
rdflib &#x2192; Parsing RDF file

### File and project structure

1 **main.py**: is the main project file, which connects the entire system and makes the bot active;

2 **chatbot.ipynb**: this file is the management of the bot in its functions: checking user input, sending messages from the bot to the user and managing the results;

3 **get_results.ipynb**: there are functions that render the results obtained with TF-IDF and Word2Vec using the user input string and data from the stackoverflow db and the codeOntology db;

4 **create_embeddings.ipynb**: create all vector embeddings;

5 **preprocessing.py**: there are all the functions for code cleaning and text tokenization;

6 **Train_Word2Vec.ipynb**: generate word to vec model;

7 **get_ontology_data.ipynb**: get data from comments.nt and processing it;

8 **get_stack_data.ipynb**: get data from Stackoverflow and processing it;

9 **tfidf.py**: find the first 5 related documents with the highest cosine similarity use TF-IDF technology;

10 **requirements.txt**: there are all the libraries you need to install to run the code;



Project for the 2021 AI-NLP course of Università degli Studi di Cagliari.

### ChatBot-Q-A-StackOverflow
@authors: Andrea Ibba and Marco Lilliu
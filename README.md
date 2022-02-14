# ChatBot-Q-A-StackOverflow
@authors: Andrea Ibba and Marco Lilliu

Project for the 2021 AI-NLP course of Università degli Studi di Cagliari.

### Introduction
StackBot is a telegram bot that allows users to find a possible solution to their problem using the Python language and a possible solution in Java. The iteration between the user and the bot takes place via a series of questions administered by the bot. Based on the user's answers, the bot displays possible Stackoverflow posts related to the problem specified as input by the user.

### Main NLP features
The system mainly uses two NLP features:

- Tf-idf (term-frequency / inverse document-frequency);
- Word2vec; 
- Preprocessing Data:
        - StackOverflow Data;
        - CodeOntology Data.

*Preprocessing Data*: In this phase, data were processed in order to obtain tokens ready for further work:

 -   StackOverflow: The data obtained by means of a query, using Google's BigQuery service, were subjected to a cleaning process of the HTML components and then, by using NLP techniques, tokenization of the text.
    - CodeOntology: The data were obtained from a file (comments.nt) on the codeontology.org website. The data was cleaned of RDF components using regex functions and then subjected to text tokenization processes.

*Tf-idf*: 

*Word2vec*: 

### Dataset composition
Updated on a quarterly basis, this BigQuery dataset includes an archive of Stack Overflow content, including posts, votes, tags, and badges. This dataset is updated to mirror the Stack Overflow content on the Internet Archive. More info about the dataset is given at: https://www.kaggle.com/stackoverflow/stackoverflow

To collect the data we need to gather Questions and Answer that were posted on Stack Overflow. Thus what we need are the following:

* Title
* Question body
* Answers for that question
* Votes for each answers

We decide to restrict the query only to questions that has 'python' has a tag, due to the abundance of Q&A in Stack Overflow, to perform better test and try to give more precise answers. However this process can be done over other argument just by changing the LIKE '%python%' word.
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

### Download Data

1. Download the file "credential.json" in the project folder with your Google BigQuery credentials;

2. Download the file "comments.nt" from CodeOntology.org (https://zenodo.org/record/818116#.YgpumO7MK3I);

### Initialization Data

0. Run pip install requirements.txt;

1. Run get_stack_data decommenting the first cell (Google BigQuery);

2. Run get_ontology_data;

3. Run Train_Word2Vec.ipynb;


### Usage of the bot
1. Start the service by running the file main.py;

2. Once the service is active, on Telegram you need to search for the bot (@StackBot) and start a chat;

3. To get started, type /start, and follow the bot instructions;
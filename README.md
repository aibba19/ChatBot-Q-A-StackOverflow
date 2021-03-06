# StackBot

StackBot is a telegram bot that allows users to find a possible solution to their problem involving the Python world and a possible corresponding Java function. 

## Setting UP 

#### Initialization

0. Create a python virtual enviroment following the docs https://docs.python.org/3/library/venv.html (we used python 3.9.10 version)

1. Activate the enviroment from command line typing inside the folder where you just created it: *pipenv shell*

2. Once inside the virtual enviroment Clone the repository with command: *git clone https://github.com/aibba19/ChatBot-Q-A-StackOverflow.git*

3. Inside the repository folder run: *pip install -r requirements.txt*

#### Download data files

0. Go to this drive link: https://drive.google.com/drive/folders/14Ky9gArKWFlVJfyi_7DPkXo44hFrMwAi?usp=sharing

1. Download the folder DB, unzip it, move it to the project directory

#### Bot usage 

0. From terminal inside the project directory open jupyter lab IDE typing: *jupyter lab*

1. Jupyter will open in your browser, here start the service by running the file *main.ipynb*

2. Once the main is running the service is active, on Telegram you need to search for the bot (@StackOverflowNew_bot) and start a chat

3. To get started, type /start, and follow the bot instructions

## Example usage 

With this project you can try to find a solution for your problem among the **Stack Overflow posts** using both tecnologies **'word to vec'** or **'tf-idf'**

Once found a post that is likely to be the solution to your problem a possible Java function that could do the same in the Java world is proposed thanks to the Code Ontology Data. 

The user from the beginning of the interaction with the bot can choose with wich tecnolgy he want to search for the solutions; if among the returned results from the first search the users can't find the one that suits his problem he can repeat the search with the other tecnology.

In any time the bot can be restarted by typing the command '/start' to begin a new interaction from scratch.

Here an interaction example between user and bot:

![bot Example](https://user-images.githubusercontent.com/26245452/156027453-b5fc7286-82f4-44f4-a1ac-65cad038325f.png)

## Project information

Note that we decide to restrict the data only to questions that has **'python'** has a tag, due to the abundance of Q&A in Stack Overflow, to perform better test and try to give more precise answers. However this process can be done over other argument just by changing the LIKE '%python%' word in the query that download the original data.

### Dataset composition

*Stack Overflow data* : downloaded from Google BigQuery services, this dataset includes an archive of Stack Overflow content, including posts, votes, tags, and badges. This dataset is updated to mirror the Stack Overflow content on the Internet archive. More info about the dataset is given at: https://www.kaggle.com/stackoverflow/stackoverflow

From all the data we need:

* Title
* Question body
* Answers for that question
* Votes for each answers


*CodeOntology data* : downloaded from codeontology.org, an RDF file containing Java functions names and their description.

### Main  features

NLP features implemented in this project are:

*Preprocessing Data*: data were preprocessed using both regex and NLP helping fucntions from Nltk library, in order to obtain tokens ready for further work, creating two new databases, one for stack overflow data and one for ontology data.

*Tf-idf*: short for term frequency???inverse document frequency, can tell you about the relevant importance of a term based upon a document,here used to rank search results based on relevance, with results which are more relevant to the user having higher TF-IDF scores. Don't consider word context.

*Word2vec*: is an algorithm that uses shallow 2-layer, not deep, neural networks to ingest a corpus and produce sets of vectors.

*Cosine similarity*: measure of similarity used here with both tf-idf and word2vec technics.


### Considerations

Since this is an **educational project** that aim to learn how to implement the different tecnologies and narrows the field to python by considering only the posts that has this ([python]) has a tag, is limitated and can be hard to find solutions for every problem in this field.

However for simple and popular questions about this field seems work quite good.

In the *get_results* file we can see some tests of both tecnologies. We see that in general the word to vec tecnology seems work slightly better than the tf-idf, since word to vec bases its search also on the **context of the words** trying in this way to look for a syntactic and semantic similarity between the various concepts, while the tf-idf bases its search only on an exact word match between input string and data.

Here some example results:

![exampleResults](https://user-images.githubusercontent.com/26245452/156019186-858c2c0d-2ad7-420b-9a51-d084b8fdd9f0.png)

For this reason W2V has a slight tolerance to grammatical errors in input, being able for example to represent as similar the words 'django' and 'djnago' as we can see in this image:

![similartermsToDjango](https://user-images.githubusercontent.com/26245452/156018647-855c84ef-5e18-446f-81df-52d1bc291ba0.png)


### Python libraries

- **nltk** &#x2192; Preprocessing text with NLP technics;
- **numpy** &#x2192; Powerful tool for matrix operations
- **pandas** &#x2192; Dataframe management
- **scipy** &#x2192; Managing NLP tools
- **gensim** &#x2192; Word2Vec module
- **google-api-core** &#x2192; Download StackOverflow data
- **google-auth** &#x2192; Download StackOverflow data
- **jupyterlab** &#x2192; IDE 
- **numpy** &#x2192; Powerful tool for matrix operations
- **regex** &#x2192; Cleaning and preprocessing data
- **telepot** &#x2192; Telegram bot
- **sklearn** &#x2192; Vectorizer for TF-IDF 
- **rdflib** &#x2192; Parsing RDF file

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

## About

Project for the 2021 AI-NLP course of Universit?? degli Studi di Cagliari.

@authors: Andrea Ibba and Marco Lilliu

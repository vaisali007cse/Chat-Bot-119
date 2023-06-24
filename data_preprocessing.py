#Text Data Preprocessing Lib
import nltk

from nltk.stem import PortStemmer
stemmer= PortStemmer()

import json
import pickle
import numpy as np

words=[]
classes=[]
word_tags_list=[]
ignored_words=['?',"!",",","'s","'m"]

train_data_file = open('intents.json').read()
intents= json.loads(train_data_file)

# function for appending stem words



    
        # Add all words of patterns to list
        
        # Add all tags to the classes list
         

#Create word corpus for chatbot


import re
import spacy
from bs4 import BeautifulSoup
from functions import *

def token_list(m):
    '''
take a string as input, the string is the chat history file path
return a dictionary {token : occurences}
    '''

    nlp = nlp = spacy.load("en_core_web_sm", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
    doc = nlp(msg_list(m))

    f={}

    for ent in doc.ents:
        if 3<=len(ent.text)<=5 and ent.text.isalpha() and ent.text not in spacy.lang.en.stop_words.STOP_WORDS:
            temp=ent.text.upper()
            if temp in f.keys():
                f[temp]=f[temp]+1
            else:
                f[temp]=1
    return f

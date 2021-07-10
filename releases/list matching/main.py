import requests
import re
import json
import spacy
from bs4 import BeautifulSoup
from modules.functions import *
from modules.tokenlists import *


def get_tickers(m, checklist=coingecko_list()):
    '''
take a string as input, the string is the chat history file path
take list as input, a list of tokens ticker
return a dictionary {token : occurences}
    '''

    nlp = nlp = spacy.load("en_core_web_sm", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
    doc = nlp(msg_list(m))

    f={}

    for token in doc:
        if 3<=len(token.text)<=5 and token.text.isalpha() and token.text in checklist:
            temp=token.text.upper()
            if temp in f.keys():
                f[temp]=f[temp]+1
            else:
                f[temp]=1
    return f

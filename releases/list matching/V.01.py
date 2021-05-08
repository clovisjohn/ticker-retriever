import requests
import re
import json

import spacy
from bs4 import BeautifulSoup


def coingecko_list():
    '''
return the latest coingecko tokens list
    '''
    f = requests.get("https://api.coingecko.com/api/v3/coins/list")
    data = json.loads(f.text)
    
    return [i["symbol"].upper() for i in data] + [j["name"] for j in data]


def msg_list(m):
    '''
take a string as input, the string is the chat history file path
return list of messages
    '''
    with open(m, encoding="utf8") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        
    
    l=[]
    
    for i in soup.find_all('div', class_='text'):
        temp=i.get_text()
        temp=re.sub("\\n","",temp)
        temp=temp.rstrip()
        l.append(temp)
        
    return " ".join(l)



def token_list2(m,checklist=coingecko_list()):
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

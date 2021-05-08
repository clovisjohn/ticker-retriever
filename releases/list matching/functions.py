import requests
import re
import json
from bs4 import BeautifulSoup

def default_list(m):
    '''
input: url to a token list a json file
return the latest tokens list
    '''
    f = requests.get(m)
    data = json.loads(f.text)
    
    return [i["symbol"].upper() for i in data]


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

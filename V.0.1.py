import re
import spacy
from bs4 import BeautifulSoup

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



def token_list(m):
    '''
take a string as input, the string is the chat history file path
return a dictionary {token : occurences}
    '''

    nlp = spacy.load("en_core_web_sm")
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

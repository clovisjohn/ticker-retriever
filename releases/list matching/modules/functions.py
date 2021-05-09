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

def query_builder(lastId):
    '''
    take as input a token address
    return a query made suing this address
    '''
    return """{
       tokens(first: 1000, where: { id_gt: \"""" +  lastId + """" } ){
         id
         name
         symbol
       }
     }
    """ 

def query_graph(query, endpoint):
    '''
input: valid uniswap graphql query
output: api response as a dictionary
    '''
    
    r = requests.post(endpoint, json={"query": query})
    if r.status_code == 200:
        parsed_json = json.loads(r.text)
        return parsed_json
    else:
        raise Exception("Query failed to run with a {r.status_code}.")

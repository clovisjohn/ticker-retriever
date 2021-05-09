import requests
import json
import re
from functions import *

def build_uniswap_list():
    l=[] #dummy list to store token data
    k=["1",""] #list of ID , ID=token address
    while k[-1]!=k[-2]:                          #till last id different from previous last Id
        t_query=query_builder(k[-1])  #build a valid uniswap query to retrieve a token list from uniswap
        temp=query_graph(t_query)     #use the previous query to make an api request
        l=l + temp["data"]["tokens"]
        try:
            lastId=temp["data"]["tokens"][-1]["id"] #get Id of the last element of the generated token list
        except IndexError:
            break
        k.append(lastId)                     #add the last Id to the list of ID
    
    f=[i["symbol"].upper() for i in l] + [k[-1]] #extract tickers from the dummy list and add the Id of the last scraped token
    
    with open("uniswap tickers.txt", 'w') as w:
        w.writelines(s + "\n" for s in f)
        
        
def update_uniswap_list():
    with open("uniswap tickers.txt", 'r') as w:
        old_list=w.read().splitlines() 
    l=[] #dummy list to store token data
    
    k=["1",old_list[-1]] #list of ID , ID=token address
    while k[-1]!=k[-2]:                          #till last id different from previous last Id
        t_query=query_builder(k[-1])  #build a valid uniswap query to retrieve a token list from uniswap
        temp=query_graph(t_query)     #use the previous query to make an api request
        l=l + temp["data"]["tokens"]
        try:
            lastId=temp["data"]["tokens"][-1]["id"] #get Id of the last element of the generated token list
        except IndexError:
            break
        k.append(lastId)                     #add the last Id to the list of ID
    
    new_list=[i["symbol"].upper() for i in l] #extract tickers from the dummy list and add the Id of the last scraped token
    f_list=old_list + new_list + [k[-1]]
    with open("uniswap tickers.txt", 'w') as w:
        w.writelines(s + "\n" for s in f_list)

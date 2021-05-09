import requests
import json
import re
from functions import *


def build_pancakeswap_list():
    endpoint="https://api.thegraph.com/subgraphs/name/pancakeswap/pairs"
    l=[] #dummy list to store token data
    k=["1",""] #list of ID , ID=token address
    while k[-1]!=k[-2]:                          #till last id different from previous last Id
        t_query=query_builder(k[-1])  #build a valid uniswap query to retrieve a token list from uniswap
        temp=query_graph(t_query, endpoint)     #use the previous query to make an api request
        l=l + temp["data"]["tokens"]
        try:
            lastId=temp["data"]["tokens"][-1]["id"] #get Id of the last element of the generated token list
        except IndexError:
            break
        k.append(lastId)                     #add the last Id to the list of ID
    
    f=[i["symbol"].upper() for i in l] + [k[-1]] #extract tickers from the dummy list and add the Id of the last scraped token
    
    with open("pancakeswap tickers.txt", 'w') as w:
        w.writelines(s + "\n" for s in f)

def update_pancakeswap_list():

    with open("pancakeswap tickers.txt", 'r') as w:  ##get old list
        old_list=w.read().splitlines() 
        
####### build new list starting from the last element of the old list
    endpoint="https://api.thegraph.com/subgraphs/name/pancakeswap/pairs"
    l=[] 
    k=["1",""] 
    while k[-1]!=k[-2]:                          
        t_query=query_builder(k[-1]) 
        temp=query_graph(t_query, endpoint)    
        l=l + temp["data"]["tokens"]
        try:
            lastId=temp["data"]["tokens"][-1]["id"] 
        except IndexError:
            break
        k.append(lastId)                
    
    new_list=[i["symbol"].upper() for i in l]

    f_list=old_list[:-1] + new_list + [k[-1]]  ### merging the old and new lists
    with open("pancakeswap tickers.txt", 'w') as w:
        w.writelines(s + "\n" for s in f_list) 

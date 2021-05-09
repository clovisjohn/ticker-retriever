from funcions import *

def coingecko_list():
    return default_list("https://api.coingecko.com/api/v3/coins/list")
    
def uniswap_list():
    try:
        with open("unisnwap tickers.txt", 'r') as w:
            temp=w.read().splitlines() 
        return temp
    except FileNotFoundError:
        print("unisnwap tickers.txt not found")
        
 
def pancakeswap_list():
    try:
        with open("pancakeswap tickers.txt", 'r') as w:
            temp=w.read().splitlines() 
        return temp
    except FileNotFoundError:
        print("pancakeswap tickers.txt not found")
    
def full_list()
    temp=coingecko_list() + uniswap_list() + pancakeswap_list()
    return list( dict.fromkeys(temp) )

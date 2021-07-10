import sys
from main import *
from modules.subgraph_list import *


if len(sys.argv) < 2:
    raise ValueError('Please provide arguments')

 ######################
if sys.argv[2]=="uniswap":
  try:
    uniswap=subgraph_list("https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2", "uniswap")
    uniswap.update_list()
    checklist=uniswap.get()
  except FileNotFoundError:
    print("uniswap_tickers.txt not found, it will be created")
    uniswap.build_list()
    checklist=uniswap.get()
        
		
elif sys.argv[2]=="pancakeswap":
  try:
    pancakeswap=subgraph_list("https://api.thegraph.com/subgraphs/name/pancakeswap/pairs", "pancakeswap")
    pancakeswap.update_list()
    checklist=pancakeswap.get()
  except FileNotFoundError:
    print("pancakeswap_tickers.txt not found, it will be created")
    pancakeswap.build_list()
    checklist=pancakeswap.get()	  	  
	  
elif sys.argv[2]=="sushiswap_eth":
  try:
    sushiswap_eth=subgraph_list("https://api.thegraph.com/subgraphs/name/sushiswap/exchange", "sushiswap_eth")
    sushiswap_eth.update_list()
    checklist=sushiswap_eth.get()
  except FileNotFoundError:
    print("sushiswap_eth_tickers.txt not found, it will be created")
    sushiswap_eth.build_list()
    checklist=sushiswap_eth.get()
	
       
elif sys.argv[2]=="coingecko":
    checklist=default_list("https://api.coingecko.com/api/v3/coins/list")
#########################

filepath=sys.argv[1]
    
print(get_tickers(filepath,checklist))

import sys
from main import *
from modules.subgraph_list import *


if len(sys.argv) < 2:
    raise ValueError('Please provide arguments')

 ######################
if sys.argv[2]=="uniswap":
    if "uniswap" in globals():
		try:
			checklist=uniswap.get()
		except FileNotFoundError:
			print("uniswap_tickers.txt not found, it will be created")
			uniswap.update_list()
			checklist=uniswap.get()
	else:	
		uniswap=subgraph_list("https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2", "uniswap")
		uniswap.build_list
		checklist=uniswap.get()
        
elif sys.argv[2]=="pancakeswap":
    if "pancakeswap" in globals():
		try:
			checklist=pancakeswap.get()
		except FileNotFoundError:
			print("pancakeswap_tickers.txt not found, it will be created")
			pancakeswap.update_list()
			checklist=pancakeswap.get()
	else:	
		pancakeswap=subgraph_list("https://api.thegraph.com/subgraphs/name/pancakeswap/pairs", "pancakeswap")
		pancakeswap.build_list
		checklist=pancakeswap.get()	
        
elif sys.argv[2]=="sushiswap_eth":
    if "sushiswap_eth" in globals():
		try:
			checklist=sushiswap_eth.get()
		except FileNotFoundError:
			print("sushiswap_eth_tickers.txt not found, it will be created")
			sushiswap_eth.update_list()
			checklist=sushiswap_eth.get()
	else:	
		sushiswap_eth=subgraph_list("https://api.thegraph.com/subgraphs/name/sushiswap/exchange", "sushiswap_eth")
		sushiswap_eth.build_list
		checklist=sushiswap_eth.get()
       
elif sys.argv[2]=="coingecko":
    checklist=default_list("https://api.coingecko.com/api/v3/coins/list")
#########################

filepath=sys.argv[1]
    
print(get_tickers(filepath,checklist))

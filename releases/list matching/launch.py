from main import *
from modules.uniswap_list import *
from modules.pancakeswap_list import *

if uniswap_list()==None:
    print("Building it...")
    build_uniswap_list()
if pancakeswap_list()==None:
    print("Building it...")
    build_pancakeswap_list()
    

token_list2("messages.html",full_list())

from main import *
from modules.uniswap_list import *
from modules.pancakeswap_list import *

if uniswap_list()==None:
    build_uniswap_list()
if pancakeswap_list()==None:
    build_pancakeswap_list()
    

token_list2("messages.html",full_list())

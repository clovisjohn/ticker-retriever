# Breakdown:

*Identify tokens tickers using a predefined list; accurate results.*

Manually exporting telegram chat history and then processing it using beautifulsoup and regex. Use a predefined list(coingecko or uniswap tokens list for example)
to isolate tokens tickers

To improve: 
Getting live data instead of manually exporting chat history.

Get token lists as files from  a server which will generate them each hour. This will reduce running time.


# How-to-use:
### Uniswap functions
build_uniswap_list(): Create "uniswap tickers.txt" a uniswap tickers list from scratch

update_uniswap_list(): Update "uniswap tickers.txt" with new tickers

### PancakeSwap functions
same set of functions

### token_list2:(input1,input2):
* input1: chat history file
* input2: token list
### Available token lists:
  * uniswap: uniswap_list()
  * pancakeswap: pancakeswap_list()
  * coingecko : coingeclo_list()
  * All in one: full_list()

## how-to-launch
You can try this script by running launch.py but first you need your chat history file saved as "messages.html" in the same folder than "crypto-filter"

## Colab workflow
>!git clone https://github.com/clovisjohn/crypto-filter.git

>!python /content/crypto-filter/releases/list\ matching/launch.py

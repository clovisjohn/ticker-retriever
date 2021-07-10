# Breakdown:

*Identify tokens tickers using a predefined list; accurate results.*

Manually exporting telegram chat history and then processing it using beautifulsoup and regex. Use a predefined list(coingecko or uniswap tokens list for example)
to isolate tokens tickers

To improve: 
Getting live data instead of manually exporting chat history.

Get token lists as files from  a server which will generate them each hour. This will reduce running time.


## Installation
```
git clone https://github.com/clovisjohn/crypto-filter.git
```

## Usage
You can also run this script by using `launch.py <filepath> <tokenlist>`

### Arguments
- filepath : The path of the telegram chat history file(html)
- tokenlist : the token list to use to retrieve tickers. Availabre token lists are :
              * uniswap
              * pancakeswap
              * syshiswap_eth
              * coingecko
### Example
The following line will retrieve token tickers from a telegram chat history using pancakeswap as a source
```
launch.py messages.html pancakeswap
```

**The chat history file can be exported from the telegram desktop app, select export as html**

## Colab workflow
>!git clone https://github.com/clovisjohn/crypto-filter.git

>!python /content/crypto-filter/releases/list\ matching/launch.py <filepath> <tokenlist>

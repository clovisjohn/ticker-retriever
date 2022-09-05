# ticker-retriever

## GOAL:
Get a list of token tickers from a telegram group chat with the number of occurences of each one

Using nlp (spacy or textblob), assign a "hype" value to the token depending of the "sentiment" of the users who wrote about the token

Using pandas, store everything and organize each token with its ticker,number of occurences and "hype" value 

## HOW-TO-USE:
There are two ways to use this tool:

* [NLP matching](https://github.com/clovisjohn/ticker-retriever/blob/V0.2/releases/nlp%20matching/docs.md) : This method use nlp through spaCy to identify tickers.

* [List matching](https://github.com/clovisjohn/ticker-retriever/blob/V0.2/releases/list%20matching/docs.md): This method use spaCy to isolate entities and a predefined list of tickers to identify tickers from the chat.

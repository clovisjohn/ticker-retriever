# crypto-filter

Readme

V0.1 Breakdown: identify tokens tickers using AI, ideal for finding upcoming projects.

Manually exporting telegram chat history and then processing it using beautifulsoup and regex.
Use spacy named entities recognization to isolate tokens tickers

To improve:
Getting live data instead of manually exporting chat history
Build a custom filter or train a model to recognize tokens tickers

Complexity order: n


GOAL:
Get a list of token tickers from a telegram group chats with the number of occurences of each ones
Using nlp (spacy or textblob) assign a "hype" value to the token depending of the sentiment of the users who wrote about the token
Using pandas, store everything and organize each token with its ticker,number of occurences and hype value 

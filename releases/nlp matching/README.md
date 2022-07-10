# Breakdown:

*Identify tokens tickers using AI, ideal for finding upcoming projects.*

Manually exporting telegram chat history and then processing it using beautifulsoup and regex. Use spacy named entities recognization to isolate tokens tickers

To improve: Getting live data instead of manually exporting chat history 

Build a custom filter or train a model to specifically recognize tokens tickers

## Requirements
* Python 3+
* re (regex library)
* Beautiful Soup
* spaCy with the pipeline en_core_web_sm

## how-to-launch
You can try this script by running launch.py but first you need your chat history file saved as "messages.html" in the same folder than "crypto-filter"

**The chat history file can be exported from the telegram desktop app, select export as html**

## Colab workflow
>!git clone https://github.com/clovisjohn/crypto-filter.git

>!python /content/crypto-filter/releases/nlp\ matching/launch.py

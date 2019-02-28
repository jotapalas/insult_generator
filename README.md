# Random insult generator

A simple Python project for learning purposes. The project runs using *run.py*, while *fetch_data.py* is just a module useful for fetching data from a given url.

## What it does?

This program uses the [Codecademy implementation](https://github.com/Codecademy/markov_python.git) for a [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain) to generate random text.

Particularly, it fetches insults and makes a random insult/comeback dialog. Right in the style of [Monkey Island's fights](https://monkeyisland.fandom.com/wiki/Insult_Sword_Fighting)!

## How it does it?
You just have to run ```python run.py``` and enjoy the battle.


### Optional
You can pass an additional parameter to have more than just one insult, like this:
```
python run.py -c 6
python run.py 6
```
# WORDLE GAME IMPLEMENTATION

Python Project for Learning <br>
in Hungarian language<br>
Mihaly Garamvolgyi <br>
2022-09-27

## Overview
Wordle is a popular game for easy implementation in different coding languages.
The code generates a random word in Hungarian and user has 8 tries to guess.
Color hints give feedback to user on correct letters. 
Implementation is in CLI taking advantage of Rich module for coloring.
Basic words are stored in data folder.

## Setting up and running
1. Go to directory
2. Create venv `python -m venv venv`
3. Activate venv source `venv/bin/activate` or `.\venv\Scripts\activate.bat` on Windows
4. Install requirements `pip install -r requirements.txt`

### prerequisities
* Python 3.10.5
* Rich

## Sub modules
### Engine
Holds visuals for graphical feedback on console and engine for game classes
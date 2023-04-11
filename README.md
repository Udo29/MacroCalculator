# MacroCalculator
Simple program that gives you the macro your body needs per day depending on your objectives.

Currently working:
- bulk
- cut  

Different degrees:
- slow (10%)
- medium (15%)
- agressive (25%)

Usage:
```
python3 main.py
usage: main.py [-h] [-s SIZE] [-w WEIGHT] [-a AGE] [-A ACTIVITY] [-S S] [-t TYPEOFDIET] [-d DEGREE]

options:
  -h, --help     show this help message and exit
  -s SIZE        Size of the person.
  -w WEIGHT      Weight of the person.
  -a AGE         Age of the person.
  -A ACTIVITY    Times per week the person does sport.
  -S S           Male or Female.
  -t TYPEOFDIET  Choose the type of diet: cut or bulk.
  -d DEGREE      Choose the degree of agressivity in the diet.
```

Example:
```
python3 main.py -s 1.85 -w 102 -a 23 -A 5 -S male -t cut -d slow
Prots: 183.6
Carbs: 237.99453500000004
Lipids: 86.7
```


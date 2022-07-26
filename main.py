import argparse
from docopt import docopt

usage = """
Usage: 
Calculator.py --add <num1> <num2> 
Calculator.py --divide <num1> <num2>
Calculator.py --multiplication <num1> <num2>
Calculator.py --Rounded_division <num1> <num2>
Calculator.py --subtract <num1> <num2>
Calculator.py --power <num1> <num2>
"""

args = docopt(usage)

if args['--add'] :
    number1 = args['<num1>']
    number2 = args['<num2>']
    print(f"{number1} + {number2} = {number1 + number2}")

elif args['--divide'] : 
    number1 = args['<num1>']
    number2 = args['<num2>']

    print(f"{number1} / {number2} = {number1 / number2}")

elif args['--multiplication']:
    number1 = args['<num1>']
    number2 = args['<num2>']
    print(f"{number1} * {number2} = {number1 / number2}")

elif args['--Rounded_division'] :
    number1 = args['<num1>']
    number2 = args['<num2>']

    print(f"{number1} // {number2} = {number1 // number2}")

elif args['--subtract'] :
    number1 = args['<num1>']
    number2 = args['<num2>']

    print(f"{number1} - {number2} = {number1 - number2}")

elif args['--power']:
    number1 = args['<num1>']
    number2 = args['<num2>']

    print(f"{number1} **  {number2} = {number1 ** number2}")

else : 
    print("Enter Right argument")


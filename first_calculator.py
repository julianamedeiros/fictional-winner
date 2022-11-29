# Building a complex calculator :)
# Defining functions

def soma(n1, n2):
    return n1 + n2


def minus(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multi(n1, n2):
    return n1 * n2


# Defining inputs

number1 = float(input('Enter a number: '))
number2 = float(input('Enter another number: '))

# Defining operations
operations = input('Define an operation. Use + for soma, - for minus, / for division and x for multiplication: ')

# Running tests
if operations == '+':
    print(soma(number1, number2))
elif operations == '-':
    print(minus(number1, number2))
elif operations == '/':
    print(divide(number1, number2))
elif operations == 'x':
    print(multi(number1, number2))
else:
    print('This operations is not valid.')
    
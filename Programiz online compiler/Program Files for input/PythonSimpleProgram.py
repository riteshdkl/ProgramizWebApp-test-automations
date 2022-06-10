# Python program to find random humber and print it

import random

rand = random.randint(0, 9)


def PythonSimpleProgram():
    print("Asking for name")
    name = input("Who are you ")
    print("Hello " + name + " you have been assigned number ")
    print(rand)


PythonSimpleProgram()

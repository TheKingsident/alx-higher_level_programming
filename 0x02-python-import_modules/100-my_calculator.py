#!/usr/bin/python3


from calculator_1 import add, sub, mul, div
from sys import argv, exit


if __name__ == "__main__":
    arguments = argv[1:]
    number_of_args = len(arguments)

    if number_of_args != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(arguments[0])
        b = int(arguments[2])
        operator = arguments[1]

        if operator == "+":
            print(f"{a} {operator} {b} = {add(a, b)}")
            exit(0)
        elif operator == "-":
            print(f"{a} {operator} {b} = {sub(a, b)}")
            exit(0)
        elif operator == "*":
            print(f"{a} {operator} {b} = {mul(a, b)}")
            exit(0)
        elif operator == "/":
            print(f"{a} {operator} {b} = {div(a, b)}")
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

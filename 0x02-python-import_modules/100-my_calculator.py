#!/usr/bin/python3


from calculator_1 import add, sub, mul, div
from sys import argv, exit


arguments = argv[1:]
operator = arguments[1]
number_of_args = len(arguments)

if number_of_args != 3:
    print(f"Usage: ./100-my_calculator.py <a> <operator> <b>\n1")
    exit(1)
else:
    a = int(arguments[0])
    b = int(arguments[2])
    match operator:
        case "+":
            print(f"{a} {operator} {b} = {add(a, b)}\n0")
            exit(0)
        case "-":
            print(f"{a} {operator} {b} = {sub(a, b)}\n0")
            exit(0)
        case "*":
            print(f"{a} {operator} {b} = {mul(a, b)}\n0")
            exit(0)
        case "/":
            print(f"{a} {operator} {b} = {div(a, b)}\n0")
            exit(0)
        case _:
            print("Unknown operator. Available operators: +, -, * and /\n1")
            exit(1)


if __name__ == "__main__":
    main()

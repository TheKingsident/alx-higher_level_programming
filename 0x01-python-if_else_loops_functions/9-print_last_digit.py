#!/usr/bin/python3

def print_last_digit(number):
    lastDigit = number % 10 if number >= 0 else -(-number % 10)
    print(abs(lastDigit), end="")
    return (abs(lastDigit))

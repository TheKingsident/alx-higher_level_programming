#!/usr/bin/python3

import hidden_4

def main():
    strings = dir(hidden_4)
    required_strings = sorted(string for string in strings if not string.startswith("__"))
    for string in required_strings:
        print(string)


if __name__ == "__main__":
    main()

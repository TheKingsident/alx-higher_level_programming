#!/usr/bin/python3

import sys


def main():
    arguments = sys.argv[1:]
    number_of_args = len(sys.argv) - 1
    sum = 0

    for arg in arguments:
        sum += int(arg)

    print(f"{sum}")


if __name__ == "__main__":
    main()

#!/usr/bin/python3


import sys


def main():
    script = sys.argv[0]
    arguments = sys.argv[1:]
    num_of_args = len(sys.argv) - 1

    if (num_of_args == 0):
        print(f"{num_of_args} arguments.")
    elif (num_of_args == 1):
        print(f"{num_of_args} argument:\n1: {arguments[0]}")
    else:
        print(f"{num_of_args} arguments:")
        for num in range(1, (num_of_args + 1)):
            print(f"{num}: {arguments[num - 1]}")


if __name__ == "__main__":
    main()

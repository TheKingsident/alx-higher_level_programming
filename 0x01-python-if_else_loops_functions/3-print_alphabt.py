#!/usr/bin/python3

output = ""
for char_code in range(ord('a'), ord('z') + 1):
    print(chr(char_code), end="")

print("{}".format(output), end="")

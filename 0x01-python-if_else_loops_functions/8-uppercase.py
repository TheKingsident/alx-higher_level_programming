#1/usr/bin/python3

def uppercase(s):
    for character in s:
        if 'a' <= character <= 'z':
            print("{}".format(chr(ord(character) - ord('a') + ord('A'))), end="")
        else:
            print("{}".format(character), end="")
    print()

#!/usr/bin/python3
lower = 122
upper = 89

while lower >= 97 and upper >= 65:
    print("{}".format(chr(lower)), end="")
    print("{}".format(chr(upper)), end="")

    lower -= 2
    upper -= 2

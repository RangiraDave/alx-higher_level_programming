#!/usr/bin/python3
lower = 122
upper = 89

while lower >= 97 and upper >= 65:
    print(chr(lower), end="")
    print(chr(upper), end="")

    lower -= 2
    upper -= 2

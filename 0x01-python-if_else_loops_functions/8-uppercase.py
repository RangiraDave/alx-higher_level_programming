#!/usr/bin/python3
def uppercase(str):
    i = 0
    chr_list = list(str)
    while i < len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            chr_list[i] = chr(ord(str[i]) - 32)
        i += 1
    print("{}".format("".join(chr_list)))

#!/usr/bin/python3

def remove_char_at(str, n):
    array = list(str)
    modified = []
    for i in range(len(array)):
        if i == n:
            continue
#        print("{}".format(array[i]), end="")
        modified.append(array[i])

    return "".join(modified)

#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) == chr(ord(c)):
            return True
        else:
            return False

#!/usr/bin/python3
import dis

def treee():

    height = int(input("Enter the height of the tree: "))

    spaces = height - 1
    hashes = 1
    temp = height - 1
    temp1 = height // 2

    while height != 0:
        for i in range(spaces):
            print(" ", end="")

        for j in range(hashes):
            print("*", end="")

        print()

        spaces -= 1
        hashes += 2
        height -= 1

    for i in range(temp1):
        for t in range(temp):
            print(" ", end="")
        print("#")

treee()

dis.dis(treee)

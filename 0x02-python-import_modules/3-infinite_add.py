#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum1 = 0
    for i in range(1, len(sys.argv)):
        sum1 += int(sys.argv[i])
    print("{:d}".format(sum1))

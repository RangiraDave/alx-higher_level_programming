#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]

        if op == '+':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))

        if op == '-':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))

        if op == '*':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))

        if op == '/':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
        if op != '+' and op != '-' and op != '*' and op != '/':
            print("Unknown operator. ", end="")
            print("{}".format("Available operators: +, -, * and /"))
            exit(1)

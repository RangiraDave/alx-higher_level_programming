#!/usr/bin/python3
a = 89
b = 10
a, b = 10, 89 if a and b else 'Usage: <a =...> and <b = ...>'
print("a={:d} - b={:d}".format(a, b))

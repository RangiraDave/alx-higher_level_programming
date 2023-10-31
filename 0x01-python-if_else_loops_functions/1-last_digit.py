#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
original = number

while number != 0:
    if number < 0:
        number = -(number)
    last = number % 10
    if last > 5:
        state = "and is greater than 5"
    if last == 0:
        state = "and is 0"
    if last < 6 and last != 0:
        state = "and is less than 6 and not 0"
    break

print(f"Last digit of {original} is {last} {state}")

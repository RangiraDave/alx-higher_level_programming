#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_val = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
            }

    num, prev_value = 0, 0
    if roman_string == "":
        return "None"
    if not str(roman_string):
        return 'None'

    for c in reversed(roman_string):
        int_value = roman_val.get(c, 0)

        if int_value >= prev_value:
            num += int_value
        else:
            num -= int_value
        prev_value = int_value

    return num

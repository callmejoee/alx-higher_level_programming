#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for i in roman_string:
        for key, value in roman_dic.items():
            if i in key:
                current = value
                if current > prev:
                    result += current - (2 * prev)
                else:
                    result += value
                prev = current
    return result


#!/usr/bin/python3
def print_last_digit(number):
    while number > 10 or number < -10:
        number = number % 10
    print(number)
    return number

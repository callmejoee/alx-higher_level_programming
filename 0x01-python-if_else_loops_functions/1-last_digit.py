#!/usr/bin/python3
import random

isNegative = False

number = random.randint(-10000, 10000)

print(f"Last digit of {number} is",  end=' ')

if number < 0:
    number = abs(number)
    isNegative = True

while (number >= 10):
    number = number % 10

if isNegative is  True:
    number = -number

print(f"{number} and is", end=' ')


if number > 5:
    print("greater than 5")
elif number == 0:
    print("0")
else:
    print("less than 6 and not 0")

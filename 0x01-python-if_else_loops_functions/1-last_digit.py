#!/usr/bin/python3
import random

bool isNegative = false

number = random.randint(-10000, 10000)

print(f"Last digit of {number} is",  end=' ')

if number < 0:
    number = abs(number)
    isNegative = true

while (number >= 10):
    number = number % 10

if isNegative == true:
    number = -number

print(f"{number} and is", end=' ')


if number > 5:
    print("greater than 5")
elif number == 0:
    print("zero")
else:
    print("less than 6 and not 0")

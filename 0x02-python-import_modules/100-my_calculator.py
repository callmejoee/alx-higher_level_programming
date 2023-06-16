#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

argv = sys.argv


def main():

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if (operator == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))

    if (operator == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))

    if (operator == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))

    if (operator == '/'):
        print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    main()

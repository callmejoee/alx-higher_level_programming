#!/usr/bin/python3
import sys
argv = sys.argv


def main():

    length = len(argv)
    result = 0

    for i in range(1, length):
        result += int(argv[i])
    print("{}".format(result))


if __name__ == "__main__":
    main()

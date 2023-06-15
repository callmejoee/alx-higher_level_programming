#!/usr/bin/python3
def uppercase(str):
    result = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) < 123:
            result += chr(ord(letter) - 32)
        else:
            result += letter
    return result

#!/usr/bin/python3
import sys
import urllib.request
""" This is a code to get header """
if __name__ == "__main__":
    n = (sys.argv[1])
    with urllib.request.urlopen(n) as response:
        var_value = response.getheader('X-Request-Id')
    print(var_value)

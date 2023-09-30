#!/usr/bin/python3
""" This is a code to get header takes in a URL,sends a request to URL displays
the value of the X-Request-Id variable found in the header of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    var_value = response.headers.get('X-Request-Id')
    print(var_value)


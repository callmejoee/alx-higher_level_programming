#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST request
Check if any errors and displays the body of the response (decoded in utf-8)"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":

    url = sys.argv[1]
    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: " e.code)

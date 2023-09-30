#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST request
Check if any errors and displays the body of the response (decoded in utf-8)"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        body = response.text
        print(body)
    except requests.exceptions.HTTPError as e:
        if int(e.response.status_code) >= 400:
            print("Error code: {}".format(e.response.status_code))

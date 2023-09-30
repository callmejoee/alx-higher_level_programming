#!/usr/bin/python3
import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)
body = response.content

print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
print("Body response:")

#!/usr/bin/python3
""" this is to connect to github"""

import requests

username = "callmejoee"
token = "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"

url = 'https://api.github.com/callmejoee'

headers = {
    'Authorization': f'Token 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'
}

response = requests.get(url, headers=headers)
data = response.json()

if 'id' in data:
    print("Your GitHub ID is:", data['id'])
else:
    print("Failed to retrieve your GitHub ID")

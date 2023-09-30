#!/usr/bin/python3
""" this is to connect to github"""

import requests
import sys


def get_github_user_id(username, password):
    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        return user_data["id"]
    else:
        return None


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    user_id = get_github_user_id(username, password)
    print(user_id)

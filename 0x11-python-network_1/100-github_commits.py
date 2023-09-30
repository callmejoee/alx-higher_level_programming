#!/usr/bin/python3
""" this is to connect to github"""

import requests
import sys


def get_github_user_id(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    response = requests.get(url)

    user_data = response.json()
    commits = []
    for commit in user_data[:10]:
        commit_sha = commit['sha']
        commit_author = commit['commit']['author']['name']
        commits.append((commit_sha, commit_author))
    return commits


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    user_id = get_github_user_id(owner, repo)
    if user_id:
        for commit_sha, commit_author in user_id:
            print(f"{commit_sha}: {commit_author}")

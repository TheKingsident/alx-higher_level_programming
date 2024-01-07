#!/usr/bin/python3
'''Lists last 10 commits on a repo'''

import sys
import requests


def last_ten(repo, username):
    '''Lists last 10 commits on a repo'''
    url = f'https://api.github.com/repos/{username}/{repo}/commits?per_page=10'
    response = requests.get(url)

    if response.status_code == 200:
        last_10 = response.json()
        for commit in last_10:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")


if __name__ == "__main__":
    username = sys.argv[2]
    repo = sys.argv[1]
    last_ten(repo, username)

#!/usr/bin/python3
'''Script to display GitHub user id using GitHub API.'''

import sys
import requests
from requests.auth import HTTPBasicAuth


def fetch_github_user_id(username, token):
    '''Fetch and display GitHub user ID.'''
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(username, token))

    if response.status_code == 200:
        user_id = response.json().get('id')
        print(user_id)
    else:
        print("Failed to fetch user details")


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # Personal Access Token
    fetch_github_user_id(username, token)

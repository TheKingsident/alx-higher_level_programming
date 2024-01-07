#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""

import sys
import requests


def error_code(url):
    """Sends a request to the URL and displays the body of the response."""
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    error_code(url)

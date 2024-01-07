#!/usr/bin/python3
"""Script to send a request to a URL and display the response body."""

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys


def error_code(url):
    """sends a request to the URL and displays the body of the response"""
    try:
        with urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    url = sys.argv[1]
    error_code(url)

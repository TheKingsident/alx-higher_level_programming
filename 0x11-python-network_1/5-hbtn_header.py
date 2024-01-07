#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""

import sys
import requests


def fetch_variable(url):
    """Definition of the module"""
    response = requests.get(url)
    x_request = response.headers.get('X-Request-Id')
    print(x_request)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_variable(url)

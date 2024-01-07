#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""

import sys
import urllib.request


def fetch_variable(url):
    """Definition of the module"""
    with urllib.request.urlopen(url) as response:
        x_request = response.getheader('X-Request-Id')
        print(x_request)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_variable(url)

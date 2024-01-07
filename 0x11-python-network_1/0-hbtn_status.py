#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


def fetch_status(url):
    """Definition of this module"""
    with urllib.request.urlopen(url) as response:
        data = response.read()

        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
        print("\t- utf8 content:", data.decode('utf-8'))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)

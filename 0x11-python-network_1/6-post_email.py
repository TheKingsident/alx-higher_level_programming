#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

import sys
import requests


def send_request(url, email):
    """Definition of the module"""
    response = requests.post(url, {'email': email})
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_request(url, email)

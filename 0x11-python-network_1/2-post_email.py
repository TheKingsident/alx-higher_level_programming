#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

import sys
import urllib.parse
import urllib.request


def send_request(url, email):
    """Definition of the module"""
    encoded_email = urllib.parse.urlencode({'email': email})
    encoded_email = encoded_email.encode('ascii')
    post_request = urllib.request.Request(url, encoded_email)

    with urllib.request.urlopen(post_request) as response:
        body = response.read()
        print(body.decode('utf-8'))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_request(url, email)

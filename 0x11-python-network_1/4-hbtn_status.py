#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import requests


def making_requests():
    """script that fetches https://alx-intranet.hbtn.io/status"""
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)


if __name__ == "__main__":
    making_requests()

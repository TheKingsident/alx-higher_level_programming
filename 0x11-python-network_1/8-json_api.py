#!/usr/bin/python3
"""Takes in a letter and sends a POST request to a website"""

import sys
import requests


def main():
    """Send a POST request and handle the response."""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
        
    response = requests.post('http://0.0.0.0:5000/search_user', {'q': q})

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                                json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()

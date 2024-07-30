#!/usr/bin/python3
"""
Python script that retrieves a URL, sends a request, and displays
the value of the X-Request-Id variable from the response header.
"""

import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))

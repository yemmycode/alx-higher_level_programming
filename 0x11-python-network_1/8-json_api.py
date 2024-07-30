#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == '__main__':
    letter = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': letter})
    
    try:
        response_data = response.json()
        if isinstance(response_data, dict) and response_data.get('id') and response_data.get('name'):
            print("[{}] {}".format(response_data['id'], response_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


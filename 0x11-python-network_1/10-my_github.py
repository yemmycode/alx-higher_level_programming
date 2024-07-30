#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    
    url = 'https://api.github.com/users/{}'.format(username)
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    
    try:
        user_data = response.json()
        print(user_data.get('id'))
    except ValueError:
        print("Error: Unable to retrieve data from GitHub API")

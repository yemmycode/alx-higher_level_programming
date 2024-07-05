#!/usr/bin/python3
"""
Python script that takes 2 arguments to retrieve commits from a specified GitHub repository.
"""

import requests
from sys import argv

if __name__ == '__main__':
    repository = argv[1]
    owner = argv[2]
    
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    
    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")

#!/bin/bash
# Bash script that takes a filename and a URL, sends a POST request with the contents of the file as JSON.
# Usage: ./101-post_json.sh <URL> <filename>

curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"

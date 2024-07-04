#!/bin/bash
# Bash script that takes a URL, sends a DELETE request, and displays the response body.
# Usage: ./2-delete.sh <URL>

curl -sX DELETE "$1"

#!/bin/bash
# Bash script that sends a request to a URL and displays only the status code of the response.
# Usage: ./script.sh 0.0.0.0:5000/nop ; echo ""

curl -s -o /dev/null -w "%{http_code}" "$1"

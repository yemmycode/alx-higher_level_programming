#!/bin/bash
# Bash script that takes a URL, sends a GET request, and displays 
#the response body if the response status is 200 OK.
if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d' ' -f2)" = '200' ]; then
    curl -sL "$1"
fi

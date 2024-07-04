#!/bin/bash
# Retrieves and displays the size of the response body.
# Usage: ./0-body_size.sh 0.0.0.0:50

curl_result=$(curl -sI "$1")
content_length=$(echo "$curl_result" | grep "Content-Length:" | cut -d' ' -f 2)
echo "$content_length"

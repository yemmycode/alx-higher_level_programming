#!/bin/bash
# Retrieves and displays the size of the response body.
# Usage: ./script.sh <URL>

size=$(curl -s "$1" | wc -c)
echo "$size"

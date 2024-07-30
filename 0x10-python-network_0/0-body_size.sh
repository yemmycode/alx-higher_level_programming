#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

size=$(curl -s "$url" | wc -c)

echo "$size"

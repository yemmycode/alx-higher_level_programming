#!/bin/bash
# Bash script that takes a URL and displays all accepted HTTP methods.
# Usage: ./3-methods.sh 0.0.0.0:5000/route_4

curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '

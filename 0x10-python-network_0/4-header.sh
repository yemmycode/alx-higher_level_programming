#!/bin/bash
# Bash script that takes a URL, adds a custom header, and displays "Hello School!".
# Usage: ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""

curl -s -H "X-School-User-Id: 98" "$1"

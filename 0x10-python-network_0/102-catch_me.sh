#!/bin/bash
# Bash script that sends a request to trigger a specific response.
# Usage: ./script.sh
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin: You got me!"

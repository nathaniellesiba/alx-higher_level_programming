#!/bin/bash
# This script sends a POST req to a URL and displays the body of the response
# Check if URL is provided as an argument
if [ -z "$1" ]; then
    echo "URL is required"
    exit 1
fi

# Send POST request and display the body of the response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" $1

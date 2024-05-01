#!/bin/bash
# This script sends a request to a URL and displays all HTTP methods the server will accept

# Check if URL is provided as an argument
if [ -z "$1" ]; then
    echo "URL is required"
    exit 1
fi

# Send request and display the HTTP methods accepted by the server
curl -sI -X OPTIONS $1 | grep -i Allow | cut -d ' ' -f 2-

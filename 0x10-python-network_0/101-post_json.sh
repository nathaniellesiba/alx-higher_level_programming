#!/bin/bash
# sends a JSON POST req to URL passed as first args
# and displays the body of the response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

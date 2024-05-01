#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me using curl
# Make a request to the specified URL and cause the server to respond with the message "You got me!"
curl -s -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me

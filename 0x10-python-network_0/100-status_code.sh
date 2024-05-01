#!/bin/bash
# sends req to URL passed as arg and displays only status code response
curl -s -o /dev/null -w "%{http_code}" "$1"

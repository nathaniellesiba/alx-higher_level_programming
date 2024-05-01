#!/bin/bash
# Bash script to take in URL as an args and send a GET req to URL
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"

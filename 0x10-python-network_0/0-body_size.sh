#!/bin/bash
# takes URL, sends request to tht URL then display size of the body of the response
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2

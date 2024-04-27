#!/usr/bin/python3
"""Displays the X-Request-Id header
variable found in the header of response
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
"""fetching the url specified in argv"""
    with urllib.request.urlopen(url) as response:
        html = response.getheader("X-Request-Id")
        print(html)

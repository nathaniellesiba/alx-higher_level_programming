#!/usr/bin/python3
"""Displays the X-Request-Id header variable found in the header of response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

"""fetching the url specified in argv"""
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

#!/usr/bin/python3
"""takes URL Sends a request
to a given URL and displays the response body.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    site = requests.get(url)
    if site.status_code >= 400:
        print("Error code: {}".format(site.status_code))
    else:
        print(site.text)

#!/usr/bin/python3
"""takes URL sends URL to display
the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    site = requests.get(url)
    print(site.headers.get("X-Request-Id"))

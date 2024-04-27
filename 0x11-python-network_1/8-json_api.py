#!/usr/bin/python3
"""takes letter to search and Sends a POST request
to http://0.0.0.0:5000/search_user with a given letter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    site = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = site.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

#!/usr/bin/python3
"""fetches  https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

"""with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
a = type(html)
b = html.decode("utf-8")
print("Body response:")
print("\t- type: {}".format(a))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(b))"""

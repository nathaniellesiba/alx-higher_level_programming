#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status

import requests

if__name__=="__main__":
    html = requests.get('https://intranet.hbtn.io/status')
    a = type(html.text)
    print("Body response:")
    print("\t- type: {}".format(a))
    print("\t- content: {}".format(html.text))"""


import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)
data = response.json()

print("- type: {}".format(type(data)))
print("- content: {}".format(data))

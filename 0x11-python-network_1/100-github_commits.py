#!/usr/bin/python3
"""two req to solve rails by user rails"""
import requests
import sys

if __name__ == "__main__":
        url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))

"""for alternative code

    if len(sys.argv) < 3:
        sys.exit(1)
    else:
        url = 'https://api.github.com/repos/{}/{}/commits'.\
            format(sys.argv[1], sys.argv[2])
        html = requests.get(url)
        my_json = html.json()
        for member_list in my_json[:10]:
            print("{}: {}".format(member_list.get('sha'),
                                  member_list.get('commit').get('author').
                                  get('name')))
"""

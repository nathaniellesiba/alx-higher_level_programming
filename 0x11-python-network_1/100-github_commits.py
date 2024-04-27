#!/usr/bin/python3
"""two req to solve rails by user rails
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    else:
        url = 'https://api.github.com/repos/{}/{}/commits'.\
            format(sys.argv[1], sys.argv[2])
        html = requests.get(url)
        my_json = html.json()
        for member_list in my_json[:10]:
            print("{}: {}".format(member_list.get('sha'),
                                  member_list.get('commit').
                                  get('author').
                                  get('name')))
"""
import requests
import sys

repository_name = sys.argv[1]
owner_name = sys.argv[2]

url = f"https://api.github.com/repos/{owner_name}/{repository_name}"
response = requests.get(url)

if response.status_code == 200:
    repository_info = response.json()
    print(repository_info)
else:
    print("Failed to retrieve repository information.")

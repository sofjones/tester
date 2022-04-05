import requests
import os
from pprint import pprint 

token = os.environ['gh_token']
owner = "sofjones"
repo = 'tester'
query_url = f"https://api.github.com/repos/{owner}/{repo}"
params = {
    "state": "open",
}
headers = {'Authorization': f'token {token}'}
r = requests.get(query_url, headers=headers, params=params)
pprint(r.json())
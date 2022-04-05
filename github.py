import requests
import json

username = 'sofjones'
token = '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'

repos_url = 'https://api.github.com/repos'

gh_session = requests.Session()
gh_session.auth = (username, token)

repos = json.loads(gh_session.get(repos_url).text)

for repo in repos:
	print(repo)

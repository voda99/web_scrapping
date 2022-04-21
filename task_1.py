import requests
import json
from pprint import pprint


def get_github_repos(username: str) -> dict:
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    response_dict = json.loads(response.text)
    return response_dict


username = "voda99"
response = get_github_repos(username)
with open("task_1.json", "w") as f:
    json.dump(response, f, indent=2, ensure_ascii=True)

import requests
import sys


class Api:
    def __init__(self, username, api_token):
        self._username = username
        self._api_token = api_token

    def walk_user_repos(self):
        req_url = "https://api.github.com/user/repos"
        auth = (self._username, self._api_token)
        params = {"affiliation": "owner", "per_page": 100}

        next_page = req_url
        while next_page:
            resp = requests.get(next_page, auth=auth, params=params)
            if not resp.ok:
                print(
                    "Could not retrieve repositories, request failed with",
                    resp.status_code,
                )
                sys.exit(1)

            next_link = resp.links.get("next")
            next_page = None if not next_link else next_link["url"]

            for repo in resp.json():
                yield (repo)

    def list_user_repos(self):
        return [
            repo["name"] for repo in self.walk_user_repos() if self.can_delete(repo)
        ]

    def can_delete(self, repo):
        """ask user if this repo should be deleted"""
        print(
            f'\n{"(forked) " if repo["fork"] else ""}{repo["full_name"]}: {repo["description"]}'
        )
        return input("Delete? (y/N): ").lower() in ["y", "yes"]

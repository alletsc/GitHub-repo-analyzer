import requests
import pandas as pd

def read_token_from_file(filename: str) -> str:
    """Read the first line from a file."""
    with open(filename, 'r') as file:
        return file.readline().strip()

class GitHubRepos:
    API_BASE = 'https://api.github.com'

    def __init__(self, owner: str, access_token: str):
        """Initialize with owner and access token."""
        self.owner = owner
        self.access_token = access_token
        self.headers = {'Authorization': f'Bearer {self.access_token}'}

    def list_repositories(self) -> list:
        """Return a list of repositories for the owner."""
        repos_list = []
        page_num = 1

        while True:
            url = f'{self.API_BASE}/users/{self.owner}/repos?page={page_num}'
            try:
                response = requests.get(url, headers=self.headers)
                if response.status_code != 200:
                    print(f'Error accessing API: {response.status_code}')
                    break

                if not response.json():
                    break

                repos_list.extend(response.json())
                page_num += 1
            except requests.RequestException as e:
                print(f'Request error: {e}')
                break

        return repos_list

    def extract_data_from_repos(self, repos_list: list, key: str) -> list:
        """Extract specific data from a list of repositories."""
        data = []
        for repo in repos_list:
            data.append(repo.get(key, None))
        return data

    def create_dataframe(self) -> pd.DataFrame:
        """Create a DataFrame with repository names and languages."""
        repos = self.list_repositories()
        names = self.extract_data_from_repos(repos, 'name')
        languages = self.extract_data_from_repos(repos, 'language')
        df = pd.DataFrame({'Name': names, 'Language': languages})
        return df


# token = read_token_from_file('token.txt')
# github = GitHubRepos('amzn', token)
# repos = github.list_repositories()
# print(len(repos))
# df = github.create_dataframe()
# df.to_csv('repos.csv', index=False)

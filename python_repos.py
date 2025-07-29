import requests

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

# Headers basically says: "I want the response in GitHub API v3 format, and in JSON."
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary
response_dict = r.json()

# Process the results
print(response_dict.keys())

print(f"Total Repositories: {response_dict['total_count']}")
print(f"Complete results: {response_dict['incomplete_results']}")

# Information about the repositories, "items" here is a list of dictionaries containing data about 1 repo
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repo
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

# print(f"\nSelected information about the first repository:")

sepeartor = "-" * 100
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(sepeartor)
    print(f"Name: P{repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository Link: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}\n")

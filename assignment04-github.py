# assignment04-github.py
# Author: Jake Daly

from github import Github
from config import config as cfg

# Authenticate with github using token
api_key = cfg["key"]
g = Github(api_key)

# repository details
owner = "jakedaly97"
repo_name = "aprivateone"
file_path = "andrew.txt"
commit_message = "Replace Andrew with Jake"

# Get the repository
repo = g.get_user().get_repo(repo_name)

# Get file contents
file = repo.get_contents(file_path)

# Decode and modify the content
content = file.decoded_content.decode("utf-8")

if "Andrew" not in content:
    print("No changes needed.")
else:
    updated_content = content.replace("Andrew", "Jake")

    # update file using pyGithub
    repo.update_file(
        path=file_path,
        message=commit_message,
        content=updated_content,
        sha=file.sha
    )
    print("File updated successfully!")

# Read content of github file, https://python-forum.io/thread-26072.html
# Update file using pygithub, https://stackoverflow.com/questions/40630829/how-to-update-a-file-using-pygithub

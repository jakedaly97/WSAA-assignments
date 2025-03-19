# assignment04-github.py
# Author: Jake Daly

import requests
import json
from config import config as cfg
import base64

# GitHub API credentials
api_key = cfg["key"]
owner = "jakedaly97"
repo = "aprivateone"
file_path = "andrew.txt"  
commit_message = "Replace Andrew with Jake"

# Headers for authentication
headers = {
    "Authorization": f"token {api_key}",
    "Accept": "application/vnd.github.v3+json"
}

# Step 1: Get file details
file_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
response = requests.get(file_url, headers=headers)

if response.status_code == 200:
    file_data = response.json()
    sha = file_data["sha"]  # Needed for updating the file
    content = base64.b64decode(file_data["content"]).decode("utf-8")

    # Step 2: Modify the content
    updated_content = content.replace("Andrew", "Jake")

    # Step 3: Encode and send the updated content
    updated_content_b64 = base64.b64encode(updated_content.encode("utf-8")).decode("utf-8")

    update_data = {
        "message": commit_message,
        "content": updated_content_b64,
        "sha": sha
    }

    update_response = requests.put(file_url, headers=headers, json=update_data)

    if update_response.status_code == 200:
        print("File updated successfully!")
    else:
        print("Failed to update file:", update_response.json())

else:
    print("Failed to fetch file:", response.json())

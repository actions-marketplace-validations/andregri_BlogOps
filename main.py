from cmath import exp
import os
from dotenv import load_dotenv
from github import Github
from pathlib import Path
import pymediumapi
import requests
import base64


def get_last_commit(repo_name):
    """Return last commit from repository `repo_name`"""
    access_token = os.getenv("GH_ACCESS_TOKEN")
    gh = Github(access_token)

    repo = gh.get_user().get_repo(repo_name)
    commit = repo.get_commits()[0]  # latest commit
    return commit


def get_new_files(commit, dir):
    """Return new files in commit that are in dir directory"""
    files = []
    for file in commit.files:
        if Path(dir) in Path(file.filename).parents and file.status == "added":
            files.append(file)
    return files


def main():
    load_dotenv()

    REPO_NAME = os.getenv("REPO_NAME")
    POSTS_DIR = os.getenv("INPUT_POSTS_DIR")

    # Get modified file in the last commit
    last_commit = get_last_commit(REPO_NAME)
    files = get_new_files(last_commit, POSTS_DIR)

    # Create mediumAPI client
    token = os.getenv("MEDIUM_INTEGRATION_TOKEN")
    client = pymediumapi.Client(token)
    client.authenticate()

    my_output = ""

    for file in files:
        # Download file content
        response = requests.get(file.contents_url)
        response_json = response.json()
        content_base64 = response_json["content"]
        content = base64.b64decode(content_base64).decode('utf-8')

        # Find title from parameters at the beginning of the file
        title_start_idx = content.find("title:") + len("title:")
        title_end_idx = content.find('\n', title_start_idx)
        title = content[title_start_idx:title_end_idx].lstrip()

        # Prepare the text body of the post
        text_start_idx = content.find("---\n", title_end_idx) + len("---\n")
        body = content[text_start_idx:]
        
        try:
            client.create_post(
                title=title,
                content_format='markdown',
                content=body
            )
            my_output += f"Published {file.filename}\n"
        except RuntimeError as e:
            my_output.append(f"Could not publish {file.filename}")

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()

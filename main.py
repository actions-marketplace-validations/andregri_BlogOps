import os
from dotenv import load_dotenv
from github import Github
from pathlib import Path


def get_last_commit(repo_name):
    """Return last commit from repository `repo_name`"""
    access_token = os.getenv("GH_ACCESS_TOKEN")
    gh = Github(access_token)

    repo = gh.get_user().get_repo(repo_name)
    commit = repo.get_commits()[0]  # latest commit
    return commit


def main():
    load_dotenv()

    REPO_NAME = os.getenv("REPO_NAME")
    POSTS_DIR = os.getenv("INPUT_POSTS_DIR")

    last_commit = get_last_commit(REPO_NAME)

    my_output = ""
    for file in last_commit.files:
        if Path(POSTS_DIR) in Path(file.filename).parents and file.status == "modified":
            my_output += f" {file.filename}"

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()

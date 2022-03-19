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


def get_files_in(files, dir):
    """Return a subset of `files` in `dir` path"""
    new_files = []
    for file in files:
        if Path(dir) in Path(file.filename).parents:
            new_files.append(file)
    return new_files


def get_new_files(files, status):
    """Return a subset of `files` with this `status`"""
    new_files = []
    for file in files:
        if file.status == status:
            new_files.append(file)
    return new_files


def main():
    load_dotenv()

    REPO_NAME = os.getenv("REPO_NAME")
    POSTS_DIR = os.getenv("INPUT_POSTS_DIR")

    last_commit = get_last_commit(REPO_NAME)
    #new_files = get_files_in(last_commit.files, POSTS_DIR)
    #added_files = get_new_files(new_files, status="added")

    new_files = get_files_in(last_commit.files, ".")
    added_files = get_new_files(new_files, status="modified")

    my_output = f"{len(added_files)} new files in {POSTS_DIR}:"
    for file in added_files:
        my_output += f'\n{file.filename}'

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()

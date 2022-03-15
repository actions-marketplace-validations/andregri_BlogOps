import os
import glob
from dotenv import load_dotenv
from github import Github


def local_posts_state(posts_path='./_posts/'):
    posts = glob.glob(posts_path + "/*.md")
    return posts

def get_last_commit(repo_name):
    #TODO
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    gh = Github(access_token)
    
    repo = gh.get_user().get_repo(repo_name)
    print(repo)


def main():
    load_dotenv()

    get_last_commit("BlogOps")
    
    #posts_path = os.environ["INPUT_POSTSPATH"]
    posts_path = "tests/posts"

    posts = local_posts_state(posts_path)
    my_output = f"Posts path: {posts_path}"
    for post in posts:
        my_output += f'\n{post}'

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()

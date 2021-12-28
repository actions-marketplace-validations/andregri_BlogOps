import os
import glob


def local_posts_state(posts_path='./_posts/'):
    posts = glob.glob(posts_path + "/*.md")
    return posts


def main():
    posts_path = os.environ["INPUT_POSTSPATH"]

    posts = local_posts_state(posts_path)
    my_output = f"Posts path: {posts_path}"
    for post in posts:
        my_output += f'\n{post}'

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()

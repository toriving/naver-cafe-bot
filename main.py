from token import get_token
from post import post_article


def main():
    token = get_token()
    rescode = post_article(token)


if __name__ == "__main__":
    main()
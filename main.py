from login import get_token
from post import post_article


def main():
    token = get_token()
    rescode = post_article(token)
    print(rescode)

if __name__ == "__main__":
    main()
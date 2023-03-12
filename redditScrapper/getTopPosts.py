import praw
from praw.models import MoreComments
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')


def get_reddit_posts(subreddit_name='AskReddit', limit=10):
    reddit_read_only = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)

    subreddit = reddit_read_only.subreddit(subreddit_name)

    posts = subreddit.top(time_filter="day", limit=limit)
    # Scraping the top posts of the current day

    return posts


if __name__ == "__main__":
    top_posts = get_reddit_posts()

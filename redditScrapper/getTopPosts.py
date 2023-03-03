import praw
from praw.models import MoreComments
import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')


reddit_read_only = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)

subreddit = reddit_read_only.subreddit('AskReddit')

posts = subreddit.top(time_filter="month")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)

    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)

    # Unique ID of each post
    posts_dict["ID"].append(post.id)

    # The score of a post
    posts_dict["Score"].append(post.score)

    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)

    # URL of each post
    posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts.to_csv("top_posts.csv", index=True)

url = top_posts['Post URL'][0]
submission = reddit_read_only.submission(url=url)

# Getting the comments of the top post
post_comments = []

for comment in submission.comments:
    if type(comment) == MoreComments:
        continue

    post_comments.append(comment.body)

# creating a dataframe
comments_df = pd.DataFrame(post_comments, columns=['comment'])
comments_df.to_csv("comments.csv", index=True)

# reddit_helpers.py ---
#
# Filename: reddit_helpers.py
# Description:
#
# Author:
# Created: Tue Sep 19 22:11:51 2017 (-0500)
import praw
from secret_settings import r_username, r_password, client_id, client_secret

def init_reddit():
    r = praw.Reddit(user_agent='reddit-sim',
                    client_id=client_id,
                    client_secret=client_secret,
                    username=r_username,
                    password=r_password)

    print("Authenticated to reddit as %s" % r_username)

    return r

def get_submissions(r, subreddit, *args, **kwargs):
    s = r.subreddit(subreddit)

    max_submissions = 50
    submissions = []

    if 'limit' in kwargs:
        max_submissions = kwargs['limit']

    for s in s.hot(limit=max_submissions):
        submissions.append(s)

    return submissions

# sim.py ---
#
# Filename: sim.py
# Description:
#
# Author: Jon Simington
# Created: Tue Sep 19 21:16:45 2017 (-0500)
from reddit_helpers import init_reddit, get_submissions
from db import init_dbs, store_submission, store_comment
from praw.models import MoreComments

if __name__ == "__main__":
    r = init_reddit()

    dbs = init_dbs()

    submissions_store = dbs['submissions']
    comments_store = dbs['comments']

    submissions = get_submissions(r, 'all', limit=30)


    for s in submissions:
        store_submission(submissions_store, s)

        s.comments.replace_more(limit=0)

        for c in s.comments:
            store_comment(comments_store, c)

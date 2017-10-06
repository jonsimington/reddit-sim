# sim.py ---
#
# Filename: sim.py
# Description:
#
# Author: Jon Simington
# Created: Tue Sep 19 21:16:45 2017 (-0500)
from reddit_helpers import init_reddit
from db import init_dbs, get_and_store_submissions
from nlp import mock_comment


if __name__ == "__main__":
    r = init_reddit()

    db = init_dbs()

    print(mock_comment(db, subreddit='pics'))

    # fetch n submissions from reddit, store submissions, comments & redditors in db
    #get_and_store_submissions(r, db, limit=200)

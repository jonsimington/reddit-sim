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
import sys

if __name__ == "__main__":
    r = init_reddit()

    db = init_dbs()

    # fetch n submissions from reddit, store submissions, comments & redditors in db
    if 'fetch' in sys.argv:
        limit = sys.argv[sys.argv.index('fetch') + 1]

        get_and_store_submissions(r, db, int(limit))

    print(mock_comment(db))

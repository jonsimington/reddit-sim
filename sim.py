# sim.py ---
#
# Filename: sim.py
# Description:
#
# Author: Jon Simington
# Created: Tue Sep 19 21:16:45 2017 (-0500)
from reddit_helpers import init_reddit, get_submissions
from db import init_dbs, store_submission, store_comment, store_redditor

if __name__ == "__main__":
    r = init_reddit()

    dbs = init_dbs()

    submissions_store = dbs['submissions']
    comments_store = dbs['comments']
    redditors_store = dbs['redditors']

    submissions = get_submissions(r, 'all', limit=30)

    print('-' * 80)
    for s in submissions:
        store_submission(submissions_store, s)
        store_redditor(redditors_store, s.author)

        s.comments.replace_more(limit=0)

        print('(%s) %s' % (len(s.comments), s.title))
        print('-' * 80)

        for c in s.comments:
            store_comment(comments_store, c)
            store_redditor(redditors_store, c.author)

# sim.py ---
#
# Filename: sim.py
# Description:
#
# Author: Jon Simington
# Created: Tue Sep 19 21:16:45 2017 (-0500)
from reddit_helpers import init_reddit, get_submissions
from db import init_db

if __name__ == "__main__":
    r = init_reddit()

    db = init_db()

    submissions = get_submissions(r, 'all', limit=10)

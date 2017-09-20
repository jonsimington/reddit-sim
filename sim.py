# sim.py ---
#
# Filename: sim.py
# Description:
#
# Author: Jon Simington
# Created: Tue Sep 19 21:16:45 2017 (-0500)
import praw
import requests
from secret_settings import r_username, r_password


r = praw.Reddit(user_agent='reddit-sim')

r.login(r_username, r_password)

print("Authenticated to reddit as %s" % r_username)

# db.py ---
#
# Filename: db.py
# Description:
#
# Author:
# Created: Tue Sep 19 22:25:45 2017 (-0500)
import couchdb
from secret_settings import couch_user, couch_pass, couch_host, couch_port

def init_dbs():
    databases = [
        'submissions',
        'comments',
    ]

    dbs = {}

    try:
        c = couchdb.Server("http://{}:{}@{}:{}".format(couch_user, couch_pass, couch_host, couch_port))
        print("Connected to CouchDB at %s:%s" % (couch_host, couch_port))
    except couchdb.http.Unauthorized:
        print("CouchDB credentials are incorrect.")

    for d in databases:
        try:
            db = c[d]
            print("Loaded DB '%s'." % d)
        except couchdb.http.ResourceNotFound:
            db = c.create(d)
            print("Created DB '%s'." % d)

        dbs.update({d:db})

    return dbs

def store_submission(db, submission):
    doc = {
        '_id': submission.id,
        'title': submission.title,
        'submitter': submission.author.name,
        'subreddit': submission.subreddit.display_name
    }

    try:
        db.save(doc)
        print("Created submission %s." % doc['_id'])
    except couchdb.http.ResourceConflict:
        print("Submission %s already exists." % doc['_id'])

def store_comment(db, comment):
    try:
        doc = {
            '_id': comment.id,
            'words': comment.body,
            'author': comment.author.name,
            'submission': comment.submission.id,
            'subreddit': comment.submission.subreddit.display_name
        }

        try:
            db.save(doc)
            print("Created comment %s." % doc['_id'])
        except couchdb.http.ResourceConflict:
            print("Comment %s already exists." % doc['_id'])
    except:
        pass

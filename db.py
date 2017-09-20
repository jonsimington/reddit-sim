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
    databases = ['submissions',]

    dbs = {}

    try:
        c = couchdb.Server("http://{}:{}@{}:{}".format(couch_user, couch_pass, couch_host, couch_port))
        print("Connected to CouchDB at %s:%s" % (couch_host, couch_port))
    except couchdb.http.Unauthorized:
        print("CouchDB credentials are incorrect.")

    for d in databases:
        try:
            db = c[d]
            print("Loaded DB '%s'" % d)
        except couchdb.http.ResourceNotFound:
            db = c.create(d)
            print("Created DB '%s'" % d)

        dbs.update({d:db})

    return dbs

# nlp.py ---
#
# Filename: nlp.py
# Description:
#
# Author:
# Created: Wed Oct  4 20:34:26 2017 (-0500)
import nltk
import markovify
from db import init_dbs
import logging


def mock_submission_title(db):
    submissions_store = db['submissions']

    titles_view = submissions_store.view('submissionsViews/submission_titles')

    submission_titles = '.'.join([s.key for s in titles_view])

    title_model = markovify.Text(submission_titles)

    mocked_title = title_model.make_short_sentence(2)

    return mocked_title

def mock_comment(db, **kwargs):
    comments_store = db['comments']
    comments_view = comments_store.view('commentsView/comment_words')

    logging.info('Mocking comment based on %s comments' % len(comments_view))

    comments = ' '.join([c.value for c in comments_view])
    comments_model = markovify.Text(comments)

    mocked_comment = comments_model.make_sentence()

    return mocked_comment

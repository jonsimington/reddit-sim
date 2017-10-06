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
    mocked_comment = ""
    filtered = False

    comments_store = db['comments']
    comments_view = comments_store.view('commentsView/comment_words', include_docs=True)

    if 'subreddit' in kwargs:
        filtered = True
        subreddit = kwargs['subreddit']
        comments_view = [c for c in comments_view if c.doc['subreddit']==subreddit]
        print('Mocking comment based on %s comments from /r/%s' % (len(comments_view), subreddit))

    if 'author' in kwargs:
        filtered = True
        author = kwargs['author']
        comments_view = [c for c in comments_view if c.doc['author']==author]
        print('Mocking comment based on %s comments by /u/%s' % (len(comments_view), author))

    if 'submission' in kwargs:
        filtered = True
        submission = kwargs['submission']
        comments_view = [c for c in comments_view if c.doc['submission']==submission]
        print('Mocking comment based on %s comments from submission %s' % (len(comments_view), submission))

    if not filtered:
        print('Mocking comment based on %s comments' % len(comments_view))


    if len(comments_view) > 0:
        comments = ' '.join([c.value for c in comments_view])
        comments_model = markovify.Text(comments)

        mocked_comment = comments_model.make_sentence()
    else:
        logging.error('Filter applied to mock_comment resulted in 0 documents.')

    return mocked_comment

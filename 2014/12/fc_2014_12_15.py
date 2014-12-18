#!/usr/bin/env python3
# imports go here
import os
from wsgiref.simple_server import make_server
import json

import tweepy

#
# Free Coding session for 2014-12-15
# Written by Matt Warren
#

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

PORT = 8970


def tweet_msg(message):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)


def githubping_app(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        try:
            request_body_size = int(environ['CONTENT_LENGTH'])
            request_body = environ['wsgi.input'].read(request_body_size)
        except (TypeError, ValueError):
            request_body = "0"
        try:
            data = json.loads(request_body.decode("utf-8"))
            tweet_msg("GitHub Commit: %s" % data['commits'][-1]['message'])
        except Exception as ex:
            print(ex)
            pass
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    return [b"OK"]


if __name__ == '__main__':
    httpd = make_server("", PORT, githubping_app)
    try:
        print("Starting")
        httpd.serve_forever()
    except:
        print("Stopping")

#!/usr/bin/env python3
# imports go here
import json
import os

import tweepy
from flask import Flask, request
app = Flask(__name__)

#
# Free Coding session for 2014-12-18
# Written by Matt Warren
#


consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


def tweet_msg(message):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)


@app.route("/", methods=['GET', 'POST'])
def gittweet():
    data = json.loads(request.data.decode('utf-8'))
    tweet_msg("Freecoding: %s %s" % (data['commits'][-1]['message'], data['commits'][-1]['url']))
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8970)

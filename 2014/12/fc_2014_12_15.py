#!/usr/bin/env python3
# imports go here
import os
import http.server
import socketserver
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


class GitHubPingHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            length = int(self.headers['content-length'])
            data_string = self.rfile.read(length)
            data = json.loads(data_string)
            tweet_msg("GitHub Commit: %s" % data['commits'][-1]['message'])
        except:
            print(data)
        self.send_response(200)
        self.wfile.write("OK")


if __name__ == '__main__':
    Handler = GitHubPingHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    httpd.serve_forever()

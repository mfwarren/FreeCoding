#!/usr/bin/env python3
# imports go here
import requests
import json

#
# Free Coding session for 2015-05-11
# Written by Matt Warren
#

SLACK_HOOK_URL = 'https://hooks.slack.com/services/Something'

SITES = [
    'http://halotis.com',
    'http://mattwarren.co',
    'http://columfurey.com',
    'http://www.routeburn.co',
    'http://persistenceapp.com'
]


def post_to_slack(message):
    payload = {'channel': '#issues', 'text': message}
    requests.post(SLACK_HOOK_URL, data=json.dumps(payload))


def check_sites(sites):
    for site in sites:
        failed = False
        try:
            status = requests.get(site)
        except requests.exceptions.ConnectionError:
            failed = True
        if failed or not status.ok:
            print("{0} is down!".format(site))
            post_to_slack("[Alert] Site down: {0}".format(site))

if __name__ == '__main__':
    check_sites(SITES)

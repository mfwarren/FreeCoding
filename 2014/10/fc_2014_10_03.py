#!/usr/bin/env python
#imports go here
import os

from github import Github

#
# Free Coding session for 2014-10-03
# Written by Matt Warren
#

hub = Github(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_PASSWORD'])

hub_user = hub.get_user()

for repo in hub_user.get_repos():
    # print repo.name, repo.open_issues_count, repo.description
    if repo.open_issues_count > 0:
        print repo.name, 'has issues'
        for issue in repo.get_issues():
            print issue.title, issue.body


# event = hub_user.get_events()[0]
# print dir(event)
# print event.type
# print event.actor
# print event.payload
# for event in hub_user.get_events():
#     print event

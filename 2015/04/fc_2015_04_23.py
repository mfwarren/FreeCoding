#!/usr/bin/env python3
# imports go here
import os
import datetime
import dateutil.parser

from github import Github
import requests

import plotly.plotly as py
from plotly.graph_objs import *

#
# Free Coding session for 2015-04-23
# Written by Matt Warren
#

hub = Github(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_PASSWORD'])

date_array = [datetime.date.today() + datetime.timedelta(days=-i) for i in range(7)]
timeseries = {d: [] for d in date_array}


def check_commit(commit_url):
    r = requests.get(commit_url)
    data = r.json()
    date = dateutil.parser.parse(data['commit']['committer']['date']).date()
    stats = data['stats']
    timeseries[date].append(stats)


def process_push_event(event):
    for commit in event.payload['commits']:
        check_commit(commit['url'])

user = hub.get_user('mfwarren')
events = user.get_events()
for event in events:
    try:
        if event.type == 'PushEvent':
            process_push_event(event)
    except:
        break

# aggregate time series
for d in timeseries:
    stats = timeseries[d]
    total_stats = {'total': 0, 'additions': 0, 'deletions': 0}
    for stat in stats:
        total_stats['total'] += stat['total']
        total_stats['additions'] += stat['additions']
        total_stats['deletions'] += stat['deletions']
    timeseries[d] = total_stats


total = Bar(
    x=date_array,
    y=[timeseries[d]['total'] for d in date_array],
    name='Total'
)
additions = Bar(
    x=date_array,
    y=[timeseries[d]['additions'] for d in date_array],
    name='Additions'
)
deletions = Bar(
    x=date_array,
    y=[timeseries[d]['deletions'] for d in date_array],
    name='Deletions'
)
data = Data([total, additions, deletions])
layout = Layout(
    barmode='group'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='LOC per day')

#!/usr/bin/env python3
# imports go here
import os
import datetime
import pytz

from github import Github

import plotly.plotly as py
from plotly.graph_objs import Bar, Data, Layout, Figure

#
# Free Coding session for 2015-04-26
# Written by Matt Warren
#

TIMEZONE = pytz.timezone('America/Edmonton')

hub = Github(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_PASSWORD'])

date_array = [datetime.date.today() + datetime.timedelta(days=-i) for i in range(7)]
timeseries = {d: 0 for d in date_array}


def process_issues_event(event):
    # need to convert created_at from UTC to MST
    local_date = event.created_at.replace(tzinfo=pytz.utc).astimezone(TIMEZONE).date()
    timeseries[local_date] += 1


user = hub.get_user('mfwarren')
events = user.get_events()
for event in events:
    try:
        if event.type == 'IssuesEvent':
            process_issues_event(event)
    except:
        break

issue_events = Bar(
    x=date_array,
    y=[timeseries[d] for d in date_array],
    name='Issues Opened or Closed'
)
data = Data([issue_events])
layout = Layout(barmode='stacked')
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Github Issue Activity')

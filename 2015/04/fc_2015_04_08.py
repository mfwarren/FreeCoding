#!/usr/bin/env python3
# imports go here
import datetime
from collections import defaultdict

from github import Github
import os

import plotly.plotly as py
from plotly.graph_objs import Data, Layout, Figure, Bar

#
# Free Coding session for 2015-04-08
# Written by Matt Warren
#


hub = Github(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_PASSWORD'])
r = hub.get_repo('mfwarren/freecoding')
events = r.get_events()


week_ago = datetime.datetime.now() + datetime.timedelta(days=-7)

counts = defaultdict(int)

for event in events:
    if event.created_at < week_ago:
        break
    counts[event.created_at.date()] += 1

# sort the dict
dates = list(counts.keys())
dates.sort()
event_counts = Bar(
    x=dates,
    y=[counts[d] for d in dates],
    name='Github Events'
)

data = Data([event_counts])
layout = Layout(
    barmode='stack'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Github Activity for the week')

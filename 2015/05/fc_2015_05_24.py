#!/usr/bin/env python3
# imports go here
import pandas as pd

import plotly.plotly as py
from plotly.graph_objs import *

#
# Free Coding session for 2015-05-24
# Written by Matt Warren
#

years = list(range(2015, 2045))

YEARS_TO_SIMULATE = 30
INFLATION_RATE = 0.02

KWH_PRICE = 0.10  # 2015 dollars

INSTALL_COST_PER_WATT = 3.00  # in 2015
INSTALL_COST_PER_WATT_2025 = 2.00

cost_per_watt = [INSTALL_COST_PER_WATT]
for i in range(YEARS_TO_SIMULATE):
    if i < 10:
        # linear interpolation
        cost = ((INSTALL_COST_PER_WATT_2025 - INSTALL_COST_PER_WATT) / 10) * i + INSTALL_COST_PER_WATT
    else:
        cost = cost_per_watt[i] * (1+INFLATION_RATE)
    cost_per_watt.append(cost)

data = zip(years, cost_per_watt)

df = pd.DataFrame(data=list(data), columns=['Year', 'Cost Per Watt'])

line = Scatter(x=df['Year'], y=df['Cost Per Watt'])
data = Data([line])
layout = Layout(
    title='Cost per Watt',
    xaxis=XAxis(
        title='Year',
        showgrid=False,
        zeroline=False
    ),
    yaxis=YAxis(
        title='Cost Per Watt',
        showline=False
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Cost Per watt')

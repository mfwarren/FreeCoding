#!/usr/bin/env python3
# imports go here
import itertools
import pandas as pd

import plotly.plotly as py
from plotly.graph_objs import *

#
# Free Coding session for 2015-05-25
# Written by Matt Warren
#


years = list(range(2015, 2045))

YEARS_TO_SIMULATE = 30
INFLATION_RATE = 0.02
INTEREST_RATE = 0.04

KWH_PRICE = 0.15  # 2015 dollars

INSTALL_COST_PER_WATT = 3.00  # in 2015
INSTALL_COST_PER_WATT_2025 = 2.00

INSTALLS_IN_FIRST_YEAR = 200
AVG_INSTALL_SIZE_KW = 3

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

# extend the DataFrame with prices for electricity
def inflate(initial, inflation):
    current = initial
    while True:
        yield current
        current = current * (1+inflation)

price_over_time = list(itertools.islice(inflate(KWH_PRICE, INFLATION_RATE), 0, YEARS_TO_SIMULATE))
df['Price Per KWH'] = pd.Series(price_over_time, index=df.index)

sales_growth_per_year = [1, 0.9, 0.9, 0.9, 0.9, 0.8, 0.8, 0.8, 0.5, 0.5, 0.2] + ([0.01] * (YEARS_TO_SIMULATE-11))

installs_per_year = [INSTALLS_IN_FIRST_YEAR, ]
for i in range(YEARS_TO_SIMULATE-1):
    installs_per_year.append(installs_per_year[i]*(1+sales_growth_per_year[i]))
df['Installs'] = pd.Series(installs_per_year, index=df.index)
df['EOY net new capacity (KW)'] = pd.Series([i * AVG_INSTALL_SIZE_KW for i in installs_per_year], index=df.index)
df['EOY total capacity (KW)'] = pd.Series(list(itertools.accumulate([i * AVG_INSTALL_SIZE_KW for i in installs_per_year])), index=df.index)
df['YOY growth'] = pd.Series(sales_growth_per_year, index=df.index)
#
# Electricty production
PEAK_EFFICIENCY = 0.66  # weather, obstructions, electrical overhead etc
EFFECTIVE_EFFICIENCY = 0.56  # avg % of peak - due to non-direct sunlight
DAYLIGHT_HOURS = 12.0

# avg_install_cost_per_house = INSTALL_COST_PER_WATT * avg_home_install_watts
annual_kwh_per_kw = EFFECTIVE_EFFICIENCY * DAYLIGHT_HOURS * PEAK_EFFICIENCY * 365
df['KWH generated'] = (df['EOY total capacity (KW)']) * annual_kwh_per_kw

df['Revenue'] = df['KWH generated'] * df['Price Per KWH']

df['Capital for installations'] = df['EOY net new capacity (KW)'] * df['Cost Per Watt'] * 1000

# fixed costs
# warehouse per city
# van/truck per install captial_requirements_per_year
df['warehouse costs'] = pd.Series(list(itertools.accumulate([100000] * YEARS_TO_SIMULATE)), index=df.index)
df['vehicles'] = pd.Series(list(itertools.islice(inflate(60000, INFLATION_RATE), 0, YEARS_TO_SIMULATE)), index=df.index)

salaries_per_year = [200000, ]
for i in range(YEARS_TO_SIMULATE-1):
    salaries_per_year.append(salaries_per_year[i]*(1+sales_growth_per_year[i]))

df['salaries'] = pd.Series(salaries_per_year, index=df.index)

# gas, insurance, tooling, computers, servers, hosting, electricity, development
df['gas'] = pd.Series(list(itertools.accumulate(itertools.islice(inflate(2000, INFLATION_RATE), 0, YEARS_TO_SIMULATE))), index=df.index)
# df['insurance']
df['tools'] = pd.Series(list(itertools.islice(inflate(50000, INFLATION_RATE), 0, YEARS_TO_SIMULATE)), index=df.index)
df['computers'] = pd.Series(list(itertools.islice(inflate(6000, INFLATION_RATE), 0, YEARS_TO_SIMULATE)), index=df.index)
df['hosting'] = pd.Series(list(itertools.islice(inflate(5000, INFLATION_RATE), 0, YEARS_TO_SIMULATE)), index=df.index)
df['electricity'] = pd.Series(list(itertools.islice(inflate(3000, INFLATION_RATE), 0, YEARS_TO_SIMULATE)), index=df.index)



df['capital required per year'] = df['Capital for installations'] + df['warehouse costs'] + df['vehicles'] + df['salaries'] + df['gas'] + df['tools'] + df['computers'] + df['hosting'] + df['electricity']

net_new_debt = []
prev_revenue = 0
accum_debt = 0
for i, capital in enumerate(df['capital required per year']):
    new_debt = capital + (accum_debt * INTEREST_RATE) - prev_revenue
    net_new_debt.append(new_debt)
    prev_revenue = df['Revenue'][i]
    accum_debt += new_debt

df['net new debt'] = pd.Series(net_new_debt, index=df.index)
# df['debt servicing'] =

df['accumulated debt'] = pd.Series(list(itertools.accumulate([i for i in df['net new debt']])), index=df.index)

print(df)

line = Scatter(x=df['Year'], y=df['Cost Per Watt'])
line2 = Scatter(x=df['Year'], y=df['Price Per KWH'])
line3 = Scatter(x=df['Year'], y=df['Installs'])
line4 = Scatter(x=df['Year'], y=df['Revenue'])
data = Data([line, line2, line3, line4])
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

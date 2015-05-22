#!/usr/bin/env python3
# imports go here
import plotly.plotly as py
from plotly.graph_objs import *

#
# Free Coding session for 2015-05-18
# Written by Matt Warren
#


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
        cost = cost_per_watt[i-1] * (1+INFLATION_RATE)
    cost_per_watt.append(cost)

revenue_per_kwh = [KWH_PRICE, ]
for i in range(YEARS_TO_SIMULATE):
    revenue_per_kwh.append(revenue_per_kwh[i] * (1+INFLATION_RATE))

EARLY_GROWTH_RATE_YOY = 0.6
LATE_GROWTH_RATE_YOY = 0.1
INSTALLS_IN_FIRST_YEAR = 200

installs_per_year = [INSTALLS_IN_FIRST_YEAR, ]
for i in range(YEARS_TO_SIMULATE):
    if i >= 10:
        installs_per_year.append(installs_per_year[i]*(1+LATE_GROWTH_RATE_YOY))
    else:
        installs_per_year.append(installs_per_year[i]*(1+EARLY_GROWTH_RATE_YOY))

print(installs_per_year)
avg_home_install_watts = 3000.0

expected_efficiency = 0.66  # weather, obstructions, electrical overhead etc
energy_output_avg_per_hour_rate = 0.56  # avg % of peak - due to non-direct sunlight
daylight_hours_per_day = 12.0

avg_install_cost_per_house = INSTALL_COST_PER_WATT * avg_home_install_watts

captial_requirements_per_year = []
for i in range(YEARS_TO_SIMULATE):
    watts_installed = installs_per_year[i] * avg_home_install_watts
    captial_requirements_per_year.append(watts_installed * cost_per_watt[i])

print(captial_requirements_per_year)


daily_output_kwh = energy_output_avg_per_hour_rate * daylight_hours_per_day * expected_efficiency * avg_home_install_watts / 1000
print("Daily output KWH: %s", daily_output_kwh)
monthly_output = (daily_output_kwh * 365) / 12.0
monthly_revenue = monthly_output * KWH_PRICE
roi = (avg_install_cost_per_house / monthly_revenue) / 12.0

kwh_production_per_year = [(INSTALLS_IN_FIRST_YEAR/2)*daily_output_kwh*365]
for i in range(YEARS_TO_SIMULATE):
    prev_year_base = sum(installs_per_year[:i]) * daily_output_kwh * 365
    avg_from_this_year = (installs_per_year[i+1]/2)*daily_output_kwh*365
    total = prev_year_base + avg_from_this_year
    kwh_production_per_year.append(total)

print(kwh_production_per_year)

print("total Install cost: $%s" % avg_install_cost_per_house)
print('Daily output (kWh): %s' % (daily_output_kwh))
print("monthly production (kWh): %s" % (monthly_output / 1000.0))
print("monthly revenue: $%s" % monthly_revenue)
print("ROI (years) %s" % roi)
print('payments under contract: $%s' % (monthly_revenue*12*20))
print("annual revenue: $%s" % (monthly_revenue*12))


# debt financed at x% non-compounding interest each years (bond)
interest_rate = 0.02

debt_principal = [avg_install_cost_per_house, ]
annual_revenue = []
for i in range(YEARS_TO_SIMULATE):
    annual_revenue.append(revenue_per_kwh[i]*kwh_production_per_year[i])
print(annual_revenue)

interest_due = []
for i in range(YEARS_TO_SIMULATE):
    interest = debt_principal[i] * interest_rate
    interest_due.append(interest)
    profit = annual_revenue[i] - interest
    debt_principal.append(debt_principal[i] - profit)

print(debt_principal)


line = Scatter(x=list(range(2015, 2015+YEARS_TO_SIMULATE)), y=annual_revenue)
line2 = Scatter(x=list(range(2015, 2015+YEARS_TO_SIMULATE)), y=installs_per_year)
line3 = Scatter(x=list(range(2015, 2015+YEARS_TO_SIMULATE)), y=kwh_production_per_year)
data = Data([line])
layout = Layout(
    title='Revenue per year under contract',
    xaxis=XAxis(
        title='Year',
        showgrid=False,
        zeroline=False
    ),
    yaxis=YAxis(
        title='Revenue $',
        showline=False
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Revenue from contracts')
print(plot_url)

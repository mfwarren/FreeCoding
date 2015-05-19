#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-05-18
# Written by Matt Warren
#


rate_per_kwh = 0.09005

solar_panel_installed_cost_per_watt = 4.00

avg_home_install_watts = 3000.0

expected_efficiency = 0.66  # weather, obstructions, electrical overhead etc
energy_output_avg_per_hour_rate = 0.56  # avg % of peak - due to non-direct sunlight
daylight_hours_per_day = 12.0

avg_install_cost_per_house = solar_panel_installed_cost_per_watt * avg_home_install_watts

daily_output = energy_output_avg_per_hour_rate * daylight_hours_per_day * expected_efficiency * avg_home_install_watts
monthly_output = (daily_output * 365) / 12.0
monthly_revenue = (monthly_output / 1000.0) * rate_per_kwh
roi = (avg_install_cost_per_house / monthly_revenue) / 12.0

print("total Install cost: $%s" % avg_install_cost_per_house)
print('Daily output (kWh): %s' % (daily_output / 1000.0))
print("monthly production (kWh): %s" % (monthly_output / 1000.0))
print("monthly revenue: $%s" % monthly_revenue)
print("ROI (years) %s" % roi)

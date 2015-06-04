#!/usr/bin/env python3
# imports go here

import pandas as pd

#
# Free Coding session for 2015-06-03
# Written by Matt Warren
#

TAX_RATE = 0.30
INTEREST_RATE = 0.05
MAX_AMOUNT = 10000
INVESTMENT_RETURN_RATE = 0.08


def one_year_with_loan(amount):
    # NOTE: this is approximate.
    total_return = (amount * TAX_RATE) + (amount * INVESTMENT_RETURN_RATE) - (amount * INTEREST_RATE)
    monthly_rate = INTEREST_RATE / 12
    monthly_cashflow_hit = (amount * monthly_rate) / (1 - (1/((1 + monthly_rate)**12)))
    return total_return, monthly_cashflow_hit


def main():
    data = pd.DataFrame(index=range(1, MAX_AMOUNT, 100), columns=['total return', 'monthly cost'])
    for amount in range(1, MAX_AMOUNT, 100):
        total_return, monthly_cost = one_year_with_loan(amount)
        data.loc[amount] = [total_return, monthly_cost]

    data['ratio'] = data['total return'] / data['monthly cost']
    print(data)


if __name__ == '__main__':
    main()

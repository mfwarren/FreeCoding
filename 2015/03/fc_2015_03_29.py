#!/usr/bin/env python3
# imports go here
import plotly.plotly as py
from plotly.graph_objs import *

#
# Free Coding session for 2015-03-29
# Written by Matt Warren


def tax2015(income):
    """
    15% on the first $44,701 of taxable income, +
    22% on the next $44,700 of taxable income (on the portion of taxable income over $44,701 up to $89,401), +
    26% on the next $49,185 of taxable income (on the portion of taxable income over $89,401 up to $138,586), +
    29% of taxable income over $138,586.
    """
    amt = income
    tax_amt = 0

    first_amt = min(44701, amt)
    tax_amt = first_amt * 0.15
    amt = amt - first_amt

    second_amt = min(44700, amt)
    tax_amt = tax_amt + (second_amt * 0.22)
    amt = amt - second_amt

    third_amt = min(49185, amt)
    tax_amt = tax_amt + (third_amt * 0.26)
    amt = amt - third_amt

    tax_amt = tax_amt + (amt * 0.29)

    return tax_amt


if __name__ == '__main__':
    incomes = list(range(20000, 500000, 5000))
    after_tax_amount = [tax2015(amt) for amt in incomes]
    line = Scatter(x=incomes, y=after_tax_amount)
    data = Data([line])
    layout = Layout(
        title='Federal Income Tax Amount - Canada 2015 tax rules',
        xaxis=XAxis(
            title='Income',
            showgrid=False,
            zeroline=False
        ),
        yaxis=YAxis(
            title='Income Tax',
            showline=False
        )
    )
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Federal Tax Amount - Canada 2015 tax rules')
    print(plot_url)

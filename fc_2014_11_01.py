#!/usr/bin/env python
# imports go here
from pandas.io.pytables import HDFStore
from pandas import Series, TimeSeries, rolling_cov, DataFrame
from pandas import date_range
from datetime import datetime
import matplotlib.pyplot as plt

#
# Free Coding session for 2014-11-01
# Written by Matt Warren
#

def chart_stock_close_price(symbol, database):
    store = HDFStore(database)
    data = store[symbol]
    data.Close.plot()
    plt.show()
    store.close()


def compute_returns(hold_period, database='stock_data.h5'):
    # if we held stock for the hold_period number of days
    # and held equal amounts of the num_stocks best stocks for each period
    # get the list of trades and calculate the total return on the portfolio
    # (assuming no transaction costs)

    store = HDFStore(database)

    # compute hold_period returns for each stock
    for stock, _ in store.iteritems():
        data = store[stock]

        # pad out missing values in the time series
        # shift close price back in time by hold_period days

        data['return'] = (data.Close.shift(-hold_period) - data.Open)/data.Open
        # calculate percentage return as (shifted_close - open) / open
        # calculate a hold_period moving variance column
        data['mov_cov'] = rolling_cov(data.Close, window=hold_period)
        store[stock] = data  # save back to file

    store.close()

def best_trades(hold_period, num_stocks=1, database='stock_data.h5'):

    store = HDFStore('stock_data.h5')

    dates = Series(date_range('2011-01-01', '2012-01-01', freq='5B'))
    df = DataFrame(index=dates) #dict(dates=dates))

    i = 0
    for stock, _ in store.iteritems():
        i += 1
        data = store[stock]
        df[stock] = data['return'][dates]

    # for d in dates:
    print df.idxmax(1)

    store.close()

if __name__ == '__main__':
    # chart_stock_close_price('YHOO', 'stock_data.h5')
    # compute_returns(hold_period=5)
    best_trades(hold_period=5, num_stocks=1)

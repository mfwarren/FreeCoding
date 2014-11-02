#!/usr/bin/env python
# imports go here
from fc_2014_11_01 import best_trades
from pandas.io.pytables import HDFStore

#
# Free Coding session for 2014-11-02
# Written by Matt Warren
#
def calc_return_on_trades(trades, database='stock_data.h5'):

    store = HDFStore(database)

    total_return = 0
    for index, t in trades.iteritems():
        if type(t) == float:
            continue
        data = store[t]

        if data['return'][index]:
            total_return += data['return'][index]
    return total_return

if __name__ == '__main__':
    # chart_stock_close_price('YHOO', 'stock_data.h5')
    trades = best_trades(hold_period=5, num_stocks=1)
    print calc_return_on_trades(trades)

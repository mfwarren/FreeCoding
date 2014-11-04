#!/usr/bin/env python
# imports go here

import pandas.io.data as web
from pandas.io.pytables import HDFStore
from datetime import datetime
import csv

#
# Free Coding session for 2014-10-30
# Written by Matt Warren
#

def load_historical_data(start=datetime(2010, 1, 1), end=datetime.today(), filename='stock_data.h5'):
    store = HDFStore(filename)

    with open('companylist.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            print row[0]
            try:
                stock_info = web.DataReader(row[0], "yahoo", start, end)
                store[row[0]] = stock_info
            except:
                print "Error on", row[0]

    store.close()


if __name__ == '__main__':
    load_historical_data()

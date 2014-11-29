#!/usr/bin/env python
# imports go here
from __future__ import print_function

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


#
# Free Coding session for 2014-11-28
# Written by Matt Warren
#

# create a sample set of data - 5 day time series (daily)
dates = pd.date_range('20140101', periods=5)
df = pd.DataFrame(np.random.randn(5, 4), index=dates, columns=list('ABCD'))

# adding  two time series is easy
print(df['A'].add(df['B']))
print(df['A'] + df['B'])


# converts daily rate numbers to average per hour values
converted = df['A'].asfreq('60Min', method='pad')/24
print(converted)

#!/usr/bin/env python
# imports go here
import pandas
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

#
# Free Coding session for 2015-05-15
# Written by Matt Warren
#


canadian_participation = pandas.read_csv('Bfox.csv', index_col=0)
diff = canadian_participation['menwage'] - canadian_participation['womwage']
plot = diff.plot()

plt.show()

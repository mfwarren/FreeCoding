#!/usr/bin/env python3
# imports go here
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state

#
# Free Coding session for 2015-06-07
# Written by Matt Warren
#

n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50. * np.log(1 + np.arange(n))

ir = IsotonicRegression()

y_ = ir.fit_transform(x, y)

segments = [[[i, y[i]], [i, y_[i]]] for i in range(n)]
lc = LineCollection(segments, zorder=0)
lc.set_array(np.ones(len(y)))
lc.set_linewidths(0.5 * np.ones(n))

fig = plt.figure()
plt.plot(x, y, 'r. ', markersize=12)
plt.plot(x, y_, 'g.-', markersize=12)
plt.gca().add_collection(lc)
plt.legend(('Data', 'Isotonic Fit'), loc='lower right')
plt.title('Isotonic regression')
plt.show()

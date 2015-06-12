#!/usr/bin/env python3
# imports go here

import time as time
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import AgglomerativeClustering

#
# Free Coding session for 2015-06-09
# Written by Matt Warren
#

lena = sp.misc.lena()
X = np.reshape(lena, (-1, 1))

connectivity = grid_to_graph(*lena.shape)

st = time.time()
n_clusters = 15  # number of regions
ward = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward', connectivity=connectivity).fit(X)
label = np.reshape(ward.labels_, lena.shape)

plt.figure(figsize=(5, 5))
plt.imshow(lena, cmap=plt.cm.gray)
for l in range(n_clusters):
    plt.contour(label == l, contours=1,
                colors=[plt.cm.spectral(l / float(n_clusters)), ])
plt.xticks(())
plt.yticks(())
plt.show()

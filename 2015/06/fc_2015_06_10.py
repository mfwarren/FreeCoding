#!/usr/bin/env python3
# imports go here

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time

#
# Free Coding session for 2015-06-10
# Written by Matt Warren
#

n_colors = 50

china = load_sample_image("china.jpg")
china = np.array(china, dtype=np.float64) / 255

w, h, d = original_shape = tuple(china.shape)
assert d == 3
image_array = np.reshape(china, (w * h, d))

# grab a sample of pixels to run kmeans on
image_array_sample = shuffle(image_array, random_state=0)[:1000]
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)


labels = kmeans.predict(image_array)
# codebook_random = shuffle(image_array, random_state=0)[:n_colors + 1]
# labels_random = pairwise_distances_argmin(codebook_random,
#                                           image_array,
#                                           axis=0)


def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

plt.figure(1)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Quantized image (50 colors, K-Means)')
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))

plt.show()

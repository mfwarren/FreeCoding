#!/usr/bin/env python3
# imports go here
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

#
# Free Coding session for 2015-06-08
# Written by Matt Warren
#

digits = datasets.load_digits()

images = list(zip(digits.images, digits.target))
for i, (image, label) in enumerate(images[:4]):
    plt.subplot(2, 4, i + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

classifier = svm.SVC(gamma=0.001)
classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])

expected = digits.target[n_samples / 2:]
predicted = classifier.predict(data[n_samples / 2:])

print("report %s\n%s\n" % (classifier, metrics.classification_report(expected, predicted)))
print("confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))
for i, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, i + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()

#!/usr/bin/env python3
# imports go here
import numpy
import theano
import theano.tensor as T


#
# Free Coding session for 2015-06-23
# Written by Matt Warren
#

rng = numpy.random

N = 500
features = 757
D = (rng.randn(N, features), rng.randint(size=N, low=0, high=2))
training_steps = 10000

x = T.matrix('x')
y = T.vector('y')
w = theano.shared(rng.randn(features), name='w')
b = theano.shared(0.0, name='b')

print("Initial State:")
print(w.get_value(), b.get_value())

p_1 = 1 / (1 + T.exp(-T.dot(x, w) - b))  # probability of 1
prediction = p_1 > 0.5
xent = -y * T.log(p_1) - (1 - y) * T.log(1 - p_1)
cost = xent.mean() + 0.01 * (w ** 2).sum()
gw, gb = T.grad(cost, [w, b])

train = theano.function(
        inputs=[x,y],
        outputs=[prediction, xent],
        updates=((w, w - 0.1 * gw), (b, b-0.1 * gb)))  # gradient decent
predict = theano.function(inputs=[x], outputs=prediction)

for i in range(training_steps):
    pred, err = train(D[0], D[1])

print("Final:")
print(w.get_value(), b.get_value())
print("target for D: ", D[1])
print("prediction on D: ", predict(D[0]))

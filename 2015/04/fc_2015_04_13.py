#!/usr/bin/env python3
# imports go here
import factory
import unittest
#
# Free Coding session for 2015-04-13
# Written by Matt Warren
#


class Order(object):
    def __init__(self, amount, status, product_uid):
        self.amount = amount
        self.status = status
        self.product_uid = product_uid

    def __str__(self):
        return '<Order amount=%s status=%s product=%s' % (self.amount, self.status, self.product_uid)


class OrderFactory(factory.Factory):
    class Meta:
        model = Order
    amount = 200
    status = 'PAID'
    product_uid = '9qnt8q23'


class MyTests(unittest.TestCase):

    def test_with_factory_boy(self):
        order = OrderFactory.build()
        print(order)
        self.assertEquals(order.status, 'PAID')

        order = OrderFactory.build(amount=300)
        self.assertEquals(order.amount, 300)

if __name__ == '__main__':
    unittest.main()

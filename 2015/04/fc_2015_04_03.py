#!/usr/bin/env python3
# imports go here
from selenium import webdriver
import unittest

#
# Free Coding session for 2015-04-03
# Written by Matt Warren
#


class MyTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_halotis_homepage(self):

        self.browser.get('http://halotis.com')

        self.assertIn('Halotis', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings=False)

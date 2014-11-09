#!/usr/bin/env python
# imports go here

import gemparser

#
# Free Coding session for 2014-11-08
# Written by Matt Warren
#


gemfile = gemparser.GemFile('''gem "something"
gem "another_gem"
gem "hi"
''')

print gemfile.dependencies.contains("something")

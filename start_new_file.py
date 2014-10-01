#!/usr/bin/env python
import os
import datetime

file_template = """#!/usr/bin/env python
#imports go here

#
# Free Coding session for %s
# Written by Matt Warren
#
"""

if __name__=='__main__':
    today = datetime.date.today()
    filename = today.strftime('fc_%Y_%m_%d.py')
    print filename
    if os.path.isfile(filename):
        print "Today's file is already created"
    else:
        with open(filename, 'w') as file:
            file.write(file_template % today.isoformat())

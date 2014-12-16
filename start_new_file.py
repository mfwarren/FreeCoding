#!/usr/bin/env python3
import os
import datetime

file_template = """#!/usr/bin/env python3
# imports go here

#
# Free Coding session for %s
# Written by Matt Warren
#
"""

if __name__ == '__main__':
    today = datetime.date.today()
    filename = today.strftime('fc_%Y_%m_%d.py')
    path = os.path.join(str(today.year), str(today.month))
    if not os.path.exists(path):
        os.makedirs(path)
    full_path = os.path.join(path, filename)
    print(full_path)
    if os.path.isfile(full_path):
        print("Today's file is already created")
    else:
        with open(full_path, 'w') as file:
            file.write(file_template % today.isoformat())

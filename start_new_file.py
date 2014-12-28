#!/usr/bin/env python3
import os
import datetime
import argparse

file_template = """#!/usr/bin/env python3
# imports go here

#
# Free Coding session for %s
# Written by Matt Warren
#
"""

parser = argparse.ArgumentParser(description="create a new file or package for today's freecoding")
parser.add_argument('--package', action='store_true', help="Create a package instead of a file.")
args = parser.parse_args()

if __name__ == '__main__':
    today = datetime.date.today()
    path = os.path.join(str(today.year), str(today.month))
    if not os.path.exists(path):
        os.makedirs(path)

    if args.package:
        package_name = today.strftime('fc_%d')
        path = os.path.join(path, package_name)
        os.makedirs(path)
        full_path = os.path.join(path, '__init__.py')
    else:
        filename = today.strftime('fc_%Y_%m_%d.py')
        full_path = os.path.join(path, filename)

    print(full_path)
    if os.path.isfile(full_path):
        print("Today's file is already created")
    else:
        with open(full_path, 'w') as file:
            file.write(file_template % today.isoformat())

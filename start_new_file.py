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

swift_template = """#!/usr/bin/env swift
// imports

//
// Free coding session for %s
// Written by Matt Warren
//
"""


def create_file(today, do_package, do_swift):
    path = today.strftime("%Y/%m/")
    if not os.path.exists(path):
        os.makedirs(path)

    if do_package:
        package_name = today.strftime('fc_%d')
        path = os.path.join(path, package_name)
        os.makedirs(path)
        full_path = os.path.join(path, '__init__.py')
    elif do_swift:
        filename = today.strftime('fc_%Y_%m_%d.swift')
        full_path = os.path.join(path, filename)
    else:
        filename = today.strftime('fc_%Y_%m_%d.py')
        full_path = os.path.join(path, filename)

    print(full_path)
    if os.path.isfile(full_path):
        print("Today's file is already created")
    else:
        with open(full_path, 'w') as file:
            if do_swift:
                file.write(swift_template % today.isoformat())
            else:
                file.write(file_template % today.isoformat())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="create a new file or package for today's freecoding")
    parser.add_argument('--package', action='store_true', help="Create a package instead of a file.")
    parser.add_argument('--swift', action='store_true', help="Create a swift script.")
    args = parser.parse_args()

    create_file(datetime.date.today(), args.package, args.swift)

#!/usr/bin/env python3
# imports go here
import subprocess
import re
import pprint
import json

#
# Free Coding session for 2014-12-22
# Written by Matt Warren
#


pp = pprint.PrettyPrinter(indent=4)

def convert_to_json(filename):
    subprocess.call(['pdf2json', filename])  # this didn't produce anything parseable


def convert_to_html(filename):
    # subprocess.call(['pdftohtml', filename])
    return filename[:-4] + 's.html'

bank_fmt = "{:<40}{:>5}".format

def parse_bank_FIs(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith('Routing Numbers /') and not lines[i-2].startswith("<"):
                print(bank_fmt(lines[i-2][:-5], lines[i-1][:-5]))

def parse_branches(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        data = {}
        for i, line in enumerate(lines):
            if line.startswith('Routing Numbers /') and not lines[i-2].startswith("<"):
                bank_key = lines[i-2][:-5]
                data[bank_key] = []
                # print(bank_fmt(lines[i-2][:-5], lines[i-1][:-5]))
            m = re.match("(?P<transit>[0-9]{5})-(?P<fi>[0-9]{3})", line)
            if m:
                # print (m.group('transit'), m.group('fi'))
                data[bank_key].append({'transit': m.group('transit'), 'institution': m.group('fi'), 'address': lines[i+1][:-5]})
        return data


if __name__ == '__main__':
    source = 'MBRBNKSN.pdf'
    # convert_to_json('MBRBNKSN.pdf')
    html_filename = convert_to_html(source)
    # print(html_filename)
    # parse_bank_FIs(html_filename)
    bank_data = parse_branches(html_filename)
    # pp.pprint(bank_data)
    with open("bank_data.json", 'w') as f:
        f.write(json.dumps(bank_data, indent=2))

#!/usr/bin/env python
# imports go here
import sys
import argparse
import os
import json
import shutil
import codecs

import inquirer
import pystache
from dulwich.repo import Repo
from dulwich.client import get_transport_and_path

#
# Free Coding session for 2014-10-31
# Written by Matt Warren
#

# ./fc_2014_10_31.py http

parser = argparse.ArgumentParser(description='Build stuff from templated files.')
# parser.add_argument('--git', metavar='G', type=str,
#                    help='git repo to template files')
parser.add_argument('source', metavar='S', type=str,
                    help='git repo to clone template from')
parser.add_argument('out', type=str,
                    help='output folder name')
args = vars(parser.parse_args())

template_source_path = args['source']
output_root_path = args['out']


def clone_repo(remote_url, local_path):
    # TODO: would like to change to clone with --depth=1
    client, host_path = get_transport_and_path(remote_url)
    r = Repo.init(local_path, mkdir=True)
    remote_refs = client.fetch(host_path, r,
                               determine_wants=r.object_store.determine_wants_all,
                               progress=sys.stdout.write)

    # Update the local head to point at the right object
    r["HEAD"] = remote_refs["HEAD"]

    r._build_tree()


# sanity checks
if os.path.exists(output_root_path):
    print "Output directory already exists.  EXITING"
    sys.exit(1)


clone_repo(args['source'], args['out'])
# Repo(args['source']).clone(args['out'], depth=1)

# remove .git from template project
output_path = args['out']
if os.path.exists(os.path.join(output_path, '.git')):
    shutil.rmtree(os.path.join(output_path, '.git'))

# sane error if questions.json is not in the repo
if not os.path.isfile(os.path.join(output_path, 'questions.json')):
    print ""
    print " TEMPLATE REPOSITORY DOESN'T CONTAIN questions.json"
    print ""
    sys.exit(1)

with open(os.path.join(output_path, 'questions.json')) as fd:
    questions_data = json.loads(fd.read())

questions = [inquirer.load_from_dict(q) for q in questions_data]
answers = inquirer.prompt(questions)

for (dirpath, dirnames, filenames) in os.walk(output_path):
    for filename in filenames:
        with codecs.open(os.path.join(dirpath, filename), "r", "utf-8") as f:
            template = pystache.parse(f.read())
            rendered_text = pystache.render(template, answers)

        # write file with new rendered contents
        with codecs.open(os.path.join(dirpath, filename), 'w', 'utf-8') as f:
            f.write(rendered_text)

        # rename file if filename has template string in it.
        new_filename = pystache.render(filename, answers)
        if filename != new_filename:
            os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_filename))

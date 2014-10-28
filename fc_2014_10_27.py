#!/usr/bin/env python
#imports go here
import pystache
import sys, argparse, os, json
import codecs

#
# Free Coding session for 2014-10-27
# Written by Matt Warren
#

parser = argparse.ArgumentParser(description='Build stuff from templated files.')
# parser.add_argument('--git', metavar='G', type=str,
#                    help='git repo to template files')
parser.add_argument('--source', metavar='S', type=str, required=True,
                   help='path to local template files')
parser.add_argument('--out', type=str, required=True,
                   help='output folder name')
args = vars(parser.parse_args())


#input validation
template_source_path = args['source']
output_root_path = args['out']

if os.path.exists(output_root_path):
    print "Output directory already exists.  EXITING"
    sys.exit(1)
else:
    os.makedirs(output_root_path)


template_args = json.load(open("t_config.json")) # to be replaced by inquirer questions
print template_args

for (dirpath, dirnames, filenames) in os.walk(template_source_path):
    for filename in filenames:
        with codecs.open(os.path.join(dirpath, filename), "r", "utf-8") as f:
            template = pystache.parse(f.read())
        print pystache.render(template, template_args)
        print dirpath

        new_filename = pystache.render(filename, template_args)
        if not os.path.exists(os.path.join(output_root_path, dirpath)):
            os.makedirs(os.path.join(output_root_path, dirpath))
        with codecs.open(os.path.join(output_root_path, dirpath, new_filename), 'w', 'utf-8') as f:
            f.write(pystache.render(template, template_args))

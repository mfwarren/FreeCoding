#!/usr/bin/env python3
# imports go here
import os
import base64
import re

from github import Github
# from fc_2014_11_05 import *


#
# Free Coding session for 2014-12-23
# Written by Matt Warren
#


def get_projects(org, hub):
    organization = hub.get_organization(org)
    repos = organization.get_repos('private')
    return repos


def is_ruby_project(repo, hub):
    root_files = repo.get_dir_contents('.')
    for f in root_files:
        if f.path == 'Gemfile':
            return True
    return False


def gem_version(repo, gem_name, hub):
    content_file = base64.b64decode(repo.get_file_contents('Gemfile').content)
    for line in content_file.decode('utf-8').split('\n'):
        if line.strip().startswith('#'):
            continue
        if re.search('[\'"]{0}[\'"]'.format(gem_name.strip()), line):
            return line
    return None


if __name__ == '__main__':
    hub = Github(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_PASSWORD'])
    projects = get_projects('halotis', hub)
    for project in projects:
        try:
            if is_ruby_project(project, hub):
                gem = gem_version(project, 'rails', hub)
                if gem is not None:
                    print(project.full_name, " ===  ", gem)
        except:
            print("issue with {0}".format(project.full_name))
            continue

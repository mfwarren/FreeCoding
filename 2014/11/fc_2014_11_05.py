#!/usr/bin/env python
# imports go here
from github import Github
import base64
import re

#
# Free Coding session for 2014-11-05
# Written by Matt Warren
#


class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self


def parse_gems(gemfile):
    # read a gemfile and convert to a array of dicts
    gems = Bunch()
    for line in gemfile.splitlines():
        line = line.strip()
        if len(line) == 0 or line.startswith("#"):
            continue

        if line.startswith("source"):
            gems.source = line
        if line.startswith("ruby"):
            gems.ruby_version = line
        if line.startswith("gem"):
            line_split = re.findall(r"[\w\-_\.]+", line)
            gem_name = line_split[1]
            gem_info = line_split[1:]
            # if ',' in line:
            #     gem_info = line.split(',')[1]
            gems[gem_name] = gem_info
    return gems


def list_projects(organization, hub):
    # rip through all projects for the organization and figure out some info about it
    organization = hub.get_organization(organization)
    # print organization.owned_private_repos
    repos = organization.get_repos('private')
    repos_meta = []
    for repo in repos:
        repo_meta = Bunch(full_name=repo.full_name)
        repos_meta.append(repo_meta)
        repo_meta.language = repo.language
        repo_meta.clone_url = repo.clone_url
        repo_meta.raw = repo.raw_data

        print repo.full_name
        is_ruby_project = False
        has_gemfile = False
        has_podfile = False

        root_files = repo.get_dir_contents('.')
        for f in root_files:
            if f.path == '.ruby-version':
                is_ruby_project = True
            if f.path == 'Gemfile':
                has_gemfile = True
            if f.path == 'Podfile':
                has_podfile = True

        if is_ruby_project:
            content_file = repo.get_file_contents('.ruby-version')
            if content_file.encoding == 'base64':
                repo_meta.ruby_version = base64.b64decode(content_file.content).strip()
            else:
                print 'Unknown encoding type:', content_file.encoding

        if has_gemfile:
            content_file = repo.get_file_contents('Gemfile')
            if content_file.encoding == 'base64':
                gems = parse_gems(base64.b64decode(content_file.content).strip())
                repo_meta.gems = gems
                print repo_meta
                return
            else:
                print 'Unknown encoding type:', content_file.encoding

        if has_podfile:
            print 'found podfile'

    return repos_meta


if __name__ == '__main__':
    hub = Github()
    list_projects('halotis', hub)

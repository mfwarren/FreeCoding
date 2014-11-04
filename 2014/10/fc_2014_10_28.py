#!/usr/bin/env python
# imports go here

from dulwich.repo import Repo
from dulwich.objects import Commit, parse_timezone, Tag
import os
import shutil

#
# Free Coding session for 2014-10-28
# Written by Matt Warren
#

# Playing with dulwich

REPO = 'simple_repo'
author = "John Smith"

shutil.rmtree(REPO)

# os.mkdir(REPO)
repo = Repo.init(REPO, mkdir=True)

with open(os.path.join(REPO, 'index.html'), 'w') as f:
    f.write("<html>HI</html>")

print list(repo.open_index())

repo.stage(['index.html'])

print list(repo.open_index())

commit_id = repo.do_commit("first commit")
commit = repo.get_object(commit_id)
print commit


# get tree corresponding to the head commit
# tree_id = repo["HEAD"].tree
# print tree_id
object_store = repo.object_store

tags = repo.refs.subkeys("refs/tags")
print tags

tz = parse_timezone('-0200')[0]

tag_message = "Tag Annotation"
tag = Tag()
tag.tagger = author
tag.message = "message"
tag.name = "v0.1"
tag.object = (Commit, commit.id)
tag.tag_time = commit.author_time
tag.tag_timezone = tz
object_store.add_object(tag)
repo['refs/tags/HI'] = tag.id


tags = repo.refs.subkeys("refs/tags")
print tags

#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-04-28
# Written by Matt Warren
#


WHO_WHAT_WHEN = []


def add_task(who, what, when):
    WHO_WHAT_WHEN.append({'who': who, 'what': what, 'when': when})

def print_tasks():
    print("{:^30}|{:^30}|{:^30}".format("WHO", "WHAT", "WHEN"))
    for t in WHO_WHAT_WHEN:
        print("{who:^30}|{what:^30}|{when:^30}".format(**t))

def del_task(what):
    for i, task in enumerate(WHO_WHAT_WHEN):
        if task['what'] == what:
            del WHO_WHAT_WHEN[i]

if __name__ == '__main__':
    add_task('matt', 'strategy', 'May 25')
    add_task('matt', 'finish app', 'May 30')
    add_task('John', 'QA the app', 'May 23')
    add_task('Jeff', 'eat pizza', 'tomorrow')

    del_task('eat pizza')

    print_tasks()

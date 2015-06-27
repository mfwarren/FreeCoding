#!/usr/bin/env python3
# imports go here
import time

#
# Free Coding session for 2015-06-27
# Written by Matt Warren
#

start_time = time.time()

print('start by launching new EC2 instance')

print("install apache2, php, mysql, python etc.")

# migrate 9 wordpress sites
for site in range(9):
    print("migrate site %s" % site)

# migrate sentry server
print("sentry migrated!")
print("added redis server")

# migrate supervisord
print("migrate supervisord")

print("migrate scripts and crontab config")

print("migrate gitub to twitter posting service")

print("migrate ip address")

print("test")

print("shut down old server")

print("done!")

elapsed_time = time.time() - start_time

print("only took %s seconds - good job" % elapsed_time)

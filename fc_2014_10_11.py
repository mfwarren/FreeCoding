#!/usr/bin/env python
#imports go here
import inquirer
import os
import shutil

#
# Free Coding session for 2014-10-11
# Written by Matt Warren
#
# This script switches out my public keys so I can use two GitHub accounts

PUBLIC_KEY_FILE = '~/.ssh/id_rsa.pub'
PRIVATE_KEY_FILE = '~/.ssh/id_rsa'

print """##
## This script assumes you have multiple keys on the computer
##
## create files ~/.ssh/id_rsa.pub.PERSONAL and ~/.ssh/id_rsa.pub.WORK
## and files ~/.ssh/id_rsa.PERSONAL and ~/.ssh/id_rsa.WORK
##
"""

questions = [
    inquirer.List ('keys',
        message='Choose GitHub Keys',
        choices=["PERSONAL", "WORK"]
    )]

if __name__=='__main__':
    try:
        answers = inquirer.prompt(questions)
        PUBLIC_KEY_FILE = os.path.expanduser(PUBLIC_KEY_FILE)
        PRIVATE_KEY_FILE = os.path.expanduser(PRIVATE_KEY_FILE)
        public_file_to_use = '%s.%s' % (PUBLIC_KEY_FILE, answers['keys'])
        private_file_to_use = '%s.%s' % (PRIVATE_KEY_FILE, answers['keys'])

        print "Switching to %s keys" % answers['keys']

        if os.path.isfile(public_file_to_use) and os.path.isfile(private_file_to_use):
            shutil.copyfile(public_file_to_use, PUBLIC_KEY_FILE)
            shutil.copyfile(private_file_to_use, PRIVATE_KEY_FILE)
            print "You are now using your %s keys" % answers['keys']
        else:
            print "Missing %s keys" % answers['keys']
            print "Download and copy to %s" % public_file_to_use
    except KeyboardInterrupt:
        print "Cancelled"
        pass

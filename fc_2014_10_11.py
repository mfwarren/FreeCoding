#!/usr/bin/env python
#imports go here
import inquirer
import os

#
# Free Coding session for 2014-10-11
# Written by Matt Warren
#
# This script switches out my public keys so I can use two GitHub accounts

PUBLIC_KEY_FILE = '~/.ssh/id_rsa.pub'

print """##
## This script assumes you have multiple public keys on the computer
##
## create files ~/.ssh/id_rsa.pub.PERSONAL and ~/.ssh/id_rsa.pub.WORK
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
        file_to_use = '%s.%s' % (PUBLIC_KEY_FILE, answers['keys'])

        print "Switching to %s keys" % answers['keys']

        if os.path.isfile(file_to_use):
            os.rename(file_to_use, PUBLIC_KEY_FILE)
            print "You are now using your %s keys" % answers['keys']
        else:
            print "Missing %s public key." % answers['keys']
            print "Download and copy to %s" % file_to_use
    except KeyboardInterrupt:
        print "Cancelled"
        pass

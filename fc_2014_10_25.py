#!/usr/bin/env python
#imports go here

#
# Free Coding session for 2014-10-25
# Written by Matt Warren
#

# Snake Case to Camel Case

snake_msg = "hi_there_this_is_awesome"
camel_msg = "iLoveMyCamel"

if __name__=='__main__':
    print snake_msg
    print snake_msg.lower().replace("_", ' ').title().replace(" ", '')

    print camel_msg
    new_str = []
    for c in camel_msg:
        if c.isupper():
            new_str.append('_')
            new_str.append(c.lower())
        else:
            new_str.append(c)
    print ''.join(new_str)

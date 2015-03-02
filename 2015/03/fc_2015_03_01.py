#!/usr/bin/env python3
# imports go here
import logging
import logging.handlers

#
# Free Coding session for 2015-03-01
# Written by Matt Warren
#

smtp_handler = logging.handlers.SMTPHandler(mailhost=('smtp.server.com', 25),
                                            fromaddr='matt.warren@gmail.com',
                                            toaddrs=['matt.warren@gmail.com'],
                                            subject='App error')

logger = logging.getLogger(__name__)
logger.addHandler(smtp_handler)

try:
    asdf
except:
    logger.exception('error happened :(')

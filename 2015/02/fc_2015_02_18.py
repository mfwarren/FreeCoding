#!/usr/bin/env python3
# imports go here
import platform
import logging
from logging.handlers import SysLogHandler

#
# Free Coding session for 2015-02-18
# Written by Matt Warren
#

address = '/dev/log'
if platform.system() == 'Darwin':
    address = "/var/run/syslog"

handler = SysLogHandler(address)
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

logger.addHandler(handler)

logger.critical("this is some info")

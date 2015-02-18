#!/usr/bin/env python3
# imports go here
import logging


#
# Free Coding session for 2015-02-17
# Written by Matt Warren
#


main_logger = logging.getLogger(__name__)

other_logger = logging.getLogger('other')
other_other_logger = logging.getLogger('other.one')

other_logger.debug("debug")
other_logger.info("info")
other_logger.warning('warning')
other_logger.error('error')
other_logger.critical('critical')

assert(not other_logger.isEnabledFor(logging.INFO))
assert(other_logger.isEnabledFor(logging.WARNING))

# default log level is warning


main_logger.setLevel(logging.DEBUG)
main_logger.debug('main debug - still will not log')  # no handler for debug

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
main_logger.addHandler(ch)

main_logger.debug('main debug - will log now that there is a handler')
main_logger.setLevel(logging.ERROR)
main_logger.debug('main debug - not logged - filtered by logger level')


other_logger.debug('other debug - not logged')


try:
    1/0
except ZeroDivisionError as e:
    main_logger.exception("WHAT HAPPENED?")


logging.basicConfig(format='%(asctime)-15s %(clientip)s %(user)-8s %(message)s')
other_logger.warning("HI")
# message doesn't include dict of values to fit formatter

#!/usr/bin/env python3
# imports go here
import logging
import logging.config

#
# Free Coding session for 2015-03-05
# Written by Matt Warren
#

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'log.txt',
            'formatter': 'standard'
        },
        'default_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'log_error.txt',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'default_error'],
            'level': 'INFO',
            'propagate': True
        }
    }
}


logger = logging.getLogger(__name__)
logging.config.dictConfig(logging_config)

if __name__ == '__main__':
    logger.info("only to log.txt")
    logger.error("to both log.txt and log_error.txt")

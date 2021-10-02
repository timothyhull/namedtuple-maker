#!/usr/bin/env python3
''' Perform logging functions for namedtuple_maker.py

    Usage:
        TBD.
'''

# Imports
import logbook
from os import path

# Constants
LOG_FILE_PATH = path.curdir
LOG_FILE_NAME = 'namedtuple-log.log'
LOG_FILE = path.join(LOG_FILE_PATH, LOG_FILE_NAME)
LOG_LEVELS = (
    'FATAL',
    'ERROR',
    'CRITICAL',
    'WARN',
    'WARNING',
    'INFO',
    'NOTICE',
    'DEBUG',
    'TRACE'
)


def initialize_logging(
    log_level: str = None,
    log_file: str = LOG_FILE
) -> None:
    ''' Perform logging initialization functions.

        Args:
            level (str, optional):
                Logging level/verbosity.
    '''

    # If no log level is passed as an argument, set a standard logging level
    if log_level is None:
        log_level = 'DEBUG'

    # If a log level is passed as an argument, format the string
    else:
        log_level = log_level.upper().strip()

    # Confirm log level is valid
        if log_level not in LOG_LEVELS:
            error_message = (
                f'The specified logging level "{log_level}" is invalid.\n'
                f'Use one of the following values:\n'
            )

            for index, evel in enumerate(LOG_LEVELS):
                error_message += (f'{index + 1}. {log_level}\n')

            raise ValueError(
                error_message
            )

    # Initialize logging
    logbook.TimedRotatingFileHandler(
        level=log_level,
        filename=log_file
    ).push_application()

    log_init_log = logbook.Logger('Logging Initializer')
    log_init_log.info(
        f'Initialized {log_level} level logging.'
    )
    log_init_log.info(
        f'Log file path and root name is {log_file}.'
    )

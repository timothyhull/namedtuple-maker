#!/usr/bin/env python3
''' Perform logging functions for namedtuple_maker.py

    Usage:
        TBD.
'''

# Imports
import logbook

# Constants
LOG_FILE_NAME = 'namedtuple-log.log'
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
    level: str = None
) -> None:
    ''' Perform logging initialization functions.

        Args:
            level (str, optional):
                Logging level/verbosity.
    '''

    # If no log level is passed as an argument, set a standard logging level
    if level is None:
        level = 'DEBUG'

    # If a log level is passed as an argument, format the string
    else:
        level = level.upper().strip()

    # Confirm log level is valid
        if level not in LOG_LEVELS:
            error_message = (
                f'The specified logging level "{level}" is invalid.\n'
                f'Use one of the following string values:\n'
            )

            for index, log_level in enumerate(LOG_LEVELS):
                error_message += (f'{index + 1}. {log_level}\n')

            raise ValueError(
                error_message
            )

    ''' Temporary output '''
    print(f'Logging level is {level}.\n')

    # Initialize logging
    filename=LOG_FILE_NAME,
    ''' Needs review to determine where to set the logger
    '''
    logbook.TimedRotatingFileHandler(
        level=level
    )

    filename=LOG_FILE_NAME,
    ''' Needs review to determine where to set the logger
    '''
    logging_log = logbook.Logger('Logging initializer')
    logging_log.log(
        level=level
    )

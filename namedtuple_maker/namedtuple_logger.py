#!/usr/bin/env python3
''' Perform logging functions for namedtuple_maker.py

    Requirements:
        Install Logbook with pip:
            pip install Logbook

        https://pypi.org/project/Logbook/
        https://logbook.readthedocs.io/en/stable/

    Usage:
        # Step 1, import the initialize_logging function into your application:
            from namedtuple_logger import initialize_logging()
            initialize_logging()

        # Step 2, import the logbook module:
            import logbook

        # Step 3, create and name your own logbook.Logger:
            app_log = logbook.Logger('App Log')

        # Step 4, write log events to the log.
            app_log.info('Application logging started.')
'''

# Imports
import logbook
from os import path

# Constants
LOG_FILE_PATH = path.curdir
LOG_FILE_NAME = 'namedtuple-log.log'
LOG_FILE = path.join(LOG_FILE_PATH, LOG_FILE_NAME)
LOG_LEVEL_DEFAULT = 'DEBUG'
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
        log_level = getattr(
            logbook,
            LOG_LEVEL_DEFAULT
        )

    # If a log level is passed as an argument, check validity and set level
    else:

        # Confirm log level is valid
        if log_level not in LOG_LEVELS:
            error_message = (
                f'The specified logging level "{log_level}" is invalid.\n'
                f'Use one of the following values:\n'
            )

            for index, level in enumerate(LOG_LEVELS):
                error_message += (f'{index + 1}. {level}\n')

            raise ValueError(
                error_message
            )

        # Set logging level
        log_level = getattr(
                logbook,
                log_level.upper().strip()
            )

    # Initialize logging
    logbook.TimedRotatingFileHandler(
        level=log_level,
        filename=log_file
    ).push_application()

    log_init_log = logbook.Logger('Logging Initializer')
    log_init_log.info(
        f'Initialized {logbook.get_level_name(log_level)} level logging.'
    )
    log_init_log.info(
        f'Log file path and root name is {log_file}.'
    )

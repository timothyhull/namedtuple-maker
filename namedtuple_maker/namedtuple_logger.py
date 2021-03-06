#!/usr/bin/env python3
""" Perform logging functions for the namedtuple_maker.py module.

    Imports the Logbook module (see 'Requirements' section below),
    initializes application logging to a file or STDOUT, and displays
    the configured log level in STDOUT.

    Requirements:
        Install Logbook with pip:
            pip install Logbook

        https://pypi.org/project/Logbook/
        https://logbook.readthedocs.io/en/stable/

    Usage:
        # Step 1, import the initialize_logging function into your
        # application:
            from namedtuple_logger import initialize_logging()
            initialize_logging()

        # Step 2, import the logbook module:
            import logbook

        # Step 3, create and name your own logbook.Logger:
            app_log = logbook.Logger('App Log')

        # Step 4, write log events to the log.
            app_log.info('Application logging started.')
"""

# Imports - Python Standard Library
from os import path
from sys import stdout

# Imports - Third-Party
import logbook

# Imports - Local
from namedtuple_maker.namedtuple_utils import graceful_exit

# Constants
LOG_FILE_PATH = path.dirname(__file__)
LOG_FILE_NAME = 'namedtuple-log.log'
LOG_FILE = path.join(LOG_FILE_PATH, LOG_FILE_NAME)
LOG_LEVEL_DEFAULT = 'CRITICAL'
LOG_LEVELS = (
    'CRITICAL',
    'ERROR',
    'WARNING',
    'NOTICE',
    'INFO',
    'DEBUG',
    'TRACE',
    'NOTSET'
)


def initialize_logging(
    log_level: str = None,
    log_file: str = LOG_FILE,
    log_to_console: bool = False
) -> None:
    """ Perform logging initialization.

        Starts application logging at a default level or, optionally,
        a specific level by keyword argument.  Log entries write to an
        automatically-named time-rotating file series by default.  A
        specific file name may be set manually by keyword argument.
        Optionally supports logging to STDOUT by keyword argument.

        Raises an exception if the path to a manually set log file is
        not found.

        Args:
            log_level (str, optional):
                Logging level/verbosity.

            log_file (str, optional):
                Path and file name to a target log file.
                Example: ./logs/log-file.log

            log_to_console (bool, optional):
                Display log output to the console, instead of writing
                log output to a file.
    """

    # If no log level is passed as an argument, set a standard logging level
    if log_level is None:
        log_level = getattr(
            logbook,
            LOG_LEVEL_DEFAULT
        )

    # If a log level is passed as an argument, check validity and set level
    else:

        # Confirm log level is valid
        if log_level.upper().strip() not in LOG_LEVELS:

            # Create an error meassage header
            error_message = (
                f'\nThe specified logging level "{log_level}" is invalid.\n'
                f'Use one of the following values:\n'
            )

            # Add valid choice output to the error message
            for index, level in enumerate(LOG_LEVELS):
                error_message += (f'{index + 1}. {level}\n')

            # Display the error message and gracefully exit
            graceful_exit(
                error_message=error_message
            )

        else:
            # Set logging level
            log_level = getattr(
                    logbook,
                    log_level.upper().strip()
                )

    # Display logging level
    log_level_message = (
        f'** Logging level set to {logbook.get_level_name(log_level)} **'
    )
    log_level_message_border = f'\n{"-" * len(log_level_message)}\n'
    print(
        f'{log_level_message_border}'
        f'{log_level_message}'
        f'{log_level_message_border}'
    )

    # Initialize logger and display message
    log_init_log = logbook.Logger('Logging Initializer')

    # Determine logging target
    if log_to_console is False:

        # Initialize logging to log file
        try:

            # Start TimedRotatingFileHandler
            logbook.TimedRotatingFileHandler(
                level=log_level,
                filename=log_file
            ).push_application()

            # Attempt to write message to log file
            log_init_log.info(
                f'Log file path and root name is {log_file}.'
            )

        # Display error and gracefully exit
        except FileNotFoundError as error:
            graceful_exit(
                error_object=error,
            )

    else:
        # Initialize logging to console
        logbook.StreamHandler(
            stream=stdout,
            level=log_level
        ).push_application()

        # Display message to indicate console logging
        log_init_log.info(
            'Initialized logging to console.'
        )

    # Log message to indicate start of logging
    log_init_log.info(
        f'Started {logbook.get_level_name(log_level)} level logging.'
    )

    return None

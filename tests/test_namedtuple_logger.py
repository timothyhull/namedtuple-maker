#!/usr/bin/env pytest
''' Tests for namedtuple_logger.py
    Requires:
        logbook
        requires the pytest be run with the -s option

'''

# Imports
from namedtuple_maker.namedtuple_logger import initialize_logging, \
                                               LOG_LEVELS, LOG_LEVEL_DEFAULT
from logbook import Logger
from pytest import mark

# Constants
LOG_INFO_MESSAGE = 'This is a log entry.'

# Test initialize_logging
    # Different logging levels
    # Detault, manual valid, and manual invalid log files
    # Test file and console logging


def test_initialize_logging_to_console(capfd) -> None:
    ''' Test initialize_logging function for console output.  Writes mock
        log messages to the console and verifies the log messages display
        correctly.

        Args:
            capfd (pytest fixture):
                Reads text in STDOUT.

        Returns:
            None.
    '''

    # Create a logbook Logger
    initialization_log = Logger('Initialization Log')

    # Initialize logging output to console
    initialize_logging(
        log_level='INFO',
        log_to_console=True
    )

    # Write log message to console
    i = initialization_log.info(LOG_INFO_MESSAGE)
    print(i)

    # Validate log output to STDOUT
    log_output = capfd.readouterr().out
    assert LOG_INFO_MESSAGE in log_output

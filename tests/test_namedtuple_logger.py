#!/usr/bin/env pytest
''' Tests for namedtuple_logger.py
    Requires logbook
'''

# Imports
from namedtuple_maker.namedtuple_logger import initialize_logging, \
                                               LOG_LEVELS, LOG_LEVEL_DEFAULT
from pytest import mark
import logbook

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
    initialization_log = logbook.Logger('Initialization Log')

    # Initialize logging output to console
    initialize_logging(
        log_level='INFO',
        log_to_console=True
    )

    # Write log message to console
    initialization_log.warning(LOG_INFO_MESSAGE)

    # Validate log output to STDOUT
    log_output = capfd.readouterr()[0]
    log_output = log_output.replace('\n', ' ')
    print(log_output)

    assert 'entry' in log_output

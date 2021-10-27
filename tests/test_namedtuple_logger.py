#!/usr/bin/env pytest
""" pytest tests for namedtuple_logger.py

    Requires:
        logbook

    Usage:
        pytest -s tests/test_namedtuple_logger.py

    Note:
        Requires the use of the pytest -s option, to capture console
        log output in STDOUT with capfd.

"""

# Imports - Third-Party
from logbook import Logger
# from pytest import raises

# Imports - Local
from namedtuple_maker.namedtuple_logger import initialize_logging

# Constants
LOG_FILE_INVALID = './bad_log_test_dir/log_file.log'
LOG_INFO_MESSAGE = 'This is a log entry.'

# Default, manual valid, and manual invalid log files
# Test file and console logging


def test_initialize_logging_to_console(capfd) -> None:
    ''' Test initialize_logging function for console output.  Writes
        mock log messages to the console and verifies the log messages
        display correctly.

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

    return None


# def test_initialize_logging_invalid_log_file() -> None:
#     ''' Test initialize logging function's ability to handle an invalid
#         log file path level.

#         Args:
#             None.

#         Returns:
#             None.
#     '''

#     with raises(FileNotFoundError):
#         initialize_logging(
#             log_file=LOG_FILE_INVALID
#         )
#     return None

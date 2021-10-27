#!/usr/bin/env python3
""" Utility module with functions for the namedtuple-maker application.

    Usage:
        See individual function docstrings for usage instructions.
"""

# Imports - Python Standard Library
from os import _exit
from sys import exit, stderr
from typing import AnyStr


def graceful_exit(
    error_message: AnyStr = None,
    error_object: Exception = None
):
    ''' Gracefully exit a program after catching an exception.  Call the
    graceful_exit function from within a higher-level except block.
    Instead of using the raise keyword to display a stack trace and
    exit, graceful_exit will display a friendly message, and exit the
    program without displaying full trace stack details.

    The graceful_exit function first attempts to use the sys.exit
    function to exit the application.  If sys.exit raises a
    SystemExit exception, usually as the result of running a program
    within an interactive shell (IDLE, iPython, etc.), graceful_exit
    will use the os._exit function.

    Args:
        error_message (AnyStr, optional):
            String error message to display.

        error_object (Exception):
            Exception object from the source except block.  Write
            the output to STDERR.

    Usage:
        # Step 1, import the graceful_exit() function into your
        # application.
            from graceful_exit import graceful exit.

        # Step 2, define a try/except block to test your code for
        # exceptions.
            try:
                my_function()
            except NameError:
                # TBD

        # Step 3, call the graceful_exit function within the except
        # block
            try:
                my_function()
            except NameError as error:
                graceful_exit(
                    error_message='An error occurred',
                    error_object=error
                )

        Returns:
            N/A.
    '''

    # Display the optional error message
    if error_message is not None:
        print(f'\n{error_message}')

    # Write the error_object to STDERR, use the shorthand for repr(error)
    if error_object is not None:
        print(f'{error_object!r}\n', file=stderr)

    # Graceful exit with status code
    try:

        # Standard sys.exit
        exit(1)

    except SystemExit:

        # Exit from an interactive REPL shell with os._exit
        _exit(1)

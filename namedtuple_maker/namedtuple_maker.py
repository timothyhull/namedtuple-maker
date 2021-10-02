#!/usr/bin/env python3
''' Convert an iterable object into a namedtuple using a decorator.
    Provide the namedtuple attribute names in a kwarg of the decorated
    function, or enter attribute names at prompts.

    Usage:
        from namedtuple_maker.namedtuple_maker import named_tuple_converter

        @named_tuple_converter
        def your_function() -> Iterable:
            # your function code
'''

# Imports
from collections import namedtuple
from typing import Callable, Iterable, NamedTuple
from functools import wraps
from namedtuple_logger import initialize_logging
from re import compile, VERBOSE
import logbook

# Initialize logging
initialize_logging()
application_log = logbook.Logger('Application Log')

# Constants
# Match pattern for allowed first characters in a namedtuple attribute
ATTRIBUTE_INPUT_START_CHARACTER = compile(
    r'''
    ^[^a-zA-Z]+   # Only start with alphabet letters
    ''',
    VERBOSE
)
# Log regex module load
application_log.debug = 'Regex #1 loaded.'
print('loaded regex #1')


# Match pattern for allowed non-first characters in a namedtuple attribute
ATTRIBUTE_INPUT_INVALID_CHARACTERS = compile(
    r'''
    [^\w\s_-]    # Only allow alphabet letters, integers, _, -, and spaces
    ''',
    VERBOSE
)
""" *** Logging Placeholder ***
    Log debug/trace message for 'Constant set...'
"""

# Match pattern to replace space characters in a namedtuple attribute
ATTRIBUTE_INPUT_SPACE_CHARACTERS = compile(
    r'''
    \s            # Any space character
    ''',
    VERBOSE
)
""" *** Logging Placeholder ***
    Log debug/trace message for 'Constant set...'
"""

# Test attribute and value data for the run_make_named_tuple() function
TEST_DATA = {
    'first_name': 'Alex',
    'last_name': 'Smith',
    'age': 45,
    'hair_color': 'brown',
    'eye_color': 'green'
}
""" *** Logging Placeholder ***
    Log debug/trace message for 'Constant set...'
"""


def validate_attribute_input(
    attribute_names: list
) -> list:
    ''' Validate or generate attribute names for a namedtuple.

        Args:
            attribute_names (list):
                Raw list of namedtuple attribute names from user input.

        Returns:
            attribute_names (list):
                Refined list of namedtuple attribute names.
    '''

    # Loop over each attribute name
    for index, _ in enumerate(attribute_names):

        """ *** Logging Placeholder ***
            Log debug/trace message for 'validating attribute # index'
        """
        # Remove leading/trailing spaces and replace invalid start characters
        attribute_names[index] = ATTRIBUTE_INPUT_START_CHARACTER.sub(
            repl='',
            string=attribute_names[index].strip()
        )

        # Replace any invalid characters
        attribute_names[index] = ATTRIBUTE_INPUT_INVALID_CHARACTERS.sub(
            repl='',
            string=attribute_names[index].strip()
        )

        # Replace mid-value spaces with _
        attribute_names[index] = ATTRIBUTE_INPUT_SPACE_CHARACTERS.sub(
            repl='_',
            string=attribute_names[index].strip()
        )

        """ *** Logging Placeholder ***
            Log debug/trace message for 'created name for blank attribute N'
        """
        # Create an attribute name for a blank string
        if attribute_names[index] == '':
            attribute_names[index] = f'index_{index}'

    return attribute_names


def named_tuple_converter(function: Callable) -> Callable:
    ''' Decorator function to convert an iterable into a namedtuple object.

        Args:
            function (Callable):
                Function to decorate.

        Returns:
            convert_to_namedtuple (Callable):
                Decorated function
    '''

    # Use @wraps to preserve the docstring of the function to decorate
    @wraps(function)
    def convert_to_namedtuple(*args, **kwargs) -> namedtuple:
        ''' Perform conversion of an iterable to a namedtuple.

            Args:
                kwargs:
                    iterable_input (Iterable):
                        Optional, any iterable object class including,
                        list, tuple, dict_keys, dict_values, etc.

                    attribute_names (Iterable[str]):
                        Optional kwarg, any iterable object class
                        including, list, tuple, dict_keys, dict_values, etc.
                        with str values.

                    auto_attribute_names (bool):
                        Optional kwarg, automatically name attributes
                        without user input or use of the attribute_names
                        parameter. Default: False

            Returns: named_tuple (namedtuple):
                Class NamedTuple instantiated from collections.namedtuple
        '''

        # Call the decorated function
        iterable_input = function(*args, **kwargs)
        """ *** Logging Placeholder ***
            Log debug/trace message for 'Calling decorated function'
        """

        # Convert the attribute_names argument value to a list object
        if kwargs.get('attribute_names') is not None:
            attribute_names = list(kwargs.get('attribute_names'))
            """ *** Logging Placeholder ***
                Log debug/trace message for 'Attribute names found...'
            """

        # Collect attribute names
        else:
            """ *** Logging Placeholder ***
                Log debug/trace message for 'No attribute names found...'
            """
            attribute_names = []
            for value in iterable_input:

                # Set individual attribute names to a blank string
                # The validate_attribute_input function replaces blank strings
                if kwargs.get('auto_attribute_names') is True:
                    """ *** Logging Placeholder ***
                        Log debug/trace message for 'Auto attribute names set to True...'
                    """
                    attribute_names.append('')

                # Get individual attribute names via input function
                else:
                    """ *** Logging Placeholder ***
                        Log debug/trace message for 'Auto attribute names False...'
                    """
                    """ *** Logging Placeholder ***
                        Log debug/trace message for 'Prompting for input for attribute/value...'
                    """
                    attribute_names.append(
                        input(
                            'Enter an attribute name for the value '
                            f'"{value}": '
                        )
                    )
                    """ *** Logging Placeholder ***
                        Log debug/trace message for 'Collected value N...'
                    """

        # Validate attribute names
        """ *** Logging Placeholder ***
            Log debug/trace message for 'Validate attribute names...'
        """
        attribute_names = validate_attribute_input(
            attribute_names=attribute_names
        )

        # Check for an equal number of attribute names and input values
        """ *** Logging Placeholder ***
            Log debug/trace message for 'Checking for equal attributes/values...'
        """
        if len(iterable_input) == len(attribute_names):
            # Define a namedtuple object
            """ *** Logging Placeholder ***
                Log debug/trace message for 'Creating namedtuple object...'
            """
            NamedTuple = namedtuple(
                typename='NamedTuple',
                field_names=attribute_names
            )

            # Create a namedtuple from the attribute names and source iterable
            """ *** Logging Placeholder ***
                Log debug/trace message for 'Creating namedtuple...'
            """
            named_tuple = NamedTuple(
                *iterable_input
            )

        # Raise an exception for an unequal number of attributes and inputs
        else:
            """ *** Logging Placeholder ***
                Log error/warn message for 'Invalid length...'
            """
            raise ValueError(
                'Length of iterable_input and attribute_names must be equal:\n'
                f'iterable_input length = {len(iterable_input)}\n'
                f'attribute_names length = {len(attribute_names)}'
            )

        """ *** Logging Placeholder ***
            Log debug/trace message for 'Returning named_tuple...'
        """
        return named_tuple

    """ *** Logging Placeholder ***
        Log debug/trace message for 'Returning convert_to_namedtuple...'
    """
    return convert_to_namedtuple


@named_tuple_converter
def make_named_tuple(
    iterable_input: Iterable,
    attribute_names: Iterable[str] = None,
    auto_attribute_names: bool = False
) -> tuple:
    ''' Function to consume the tuple_converter decorator function.

        Args:
            iterable_input (Iterable):
                Any iterable object to convert to a namedtuple.

            attribute_names (Iterable[str]):
                Any iterable object of strings to supply field names for
                a namedtuple.

            auto_attribute_names (bool):
                    Optional kwarg, automatically name attributes
                    without user input or use of the attribute_names
                    parameter. Default: False

        Returns:
            tuple_output (tuple):
                A tuple object of the iterable_input
    '''

    """ *** Logging Placeholder ***
        Log debug/trace message for 'make_name_tuple function called...'
    """

    """ *** Logging Placeholder ***
        Log debug/trace message for 'Display argument values.'
    """

    """ *** Logging Placeholder ***
        Log debug/trace message for 'Converting N to tuple...'
    """
    tuple_output = tuple(iterable_input)

    """ *** Logging Placeholder ***
        Log debug/trace message for 'Returning tuple_output...'
    """
    return tuple_output


def run_make_named_tuple() -> NamedTuple:
    ''' Function to run the decorated make_named_tuple function using
        TEST_DATA as a test iterable.

        Args:
            None.

        Returns:
            named_tuple (NamedTuple):
                NamedTuple class object resulting from the make_named_tuple
                function decorated by the named_tuple_converter function. 
    '''

    """ *** Logging Placeholder ***
        Log debug/trace message for 'run_make_name_tuple function called...'
    """

    """ *** Logging Placeholder ***
        Log debug/trace message for 'Display notification.'
    """

    # Display a notification
    print('\nThis is a sample run of namedtuple-generator.\n')

    """ *** Logging Placeholder ***
        Log debug/trace message for 'Calling make_named_tuple.'
    """
    # Call the make_named_tuple function with test data
    named_tuple = make_named_tuple(
        iterable_input=tuple(TEST_DATA.values())
    )

    """ *** Logging Placeholder ***
        Log debug/trace message for 'Returning named_tuple.'
    """
    return named_tuple

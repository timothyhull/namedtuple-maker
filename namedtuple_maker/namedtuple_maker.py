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
from typing import Callable, Iterable, List, NamedTuple
from functools import wraps
from re import compile, VERBOSE
from namedtuple_maker.namedtuple_logger import initialize_logging
import logbook

# Initialize logging
initialize_logging()

# Log entry
# Log the initialization of logging
application_log = logbook.Logger('Application Log')
application_log.info('Start Application Log.')

# Constants
# Match pattern for allowed first characters in a namedtuple attribute
ATTRIBUTE_INPUT_START_CHARACTER = compile(
    r'''
    ^          # Start at the beginning of the line
    [^a-zA-Z]  # Any non-alphabet character
    +          # One or more repetitions
    ''',
    VERBOSE
)

# Log entry
# Log regex module compilation
application_log.debug(
    'Compiled regular expression with pattern:'
    f'{ATTRIBUTE_INPUT_START_CHARACTER.pattern}'
)

# Match pattern for allowed non-first characters in a namedtuple attribute
ATTRIBUTE_INPUT_INVALID_CHARACTERS = compile(
    r'''
    [^\w\s_-]    # Only allow alphabet letters, integers, _, -, and spaces
    ''',
    VERBOSE
)

# Log entry
# Log regex module compilation
application_log.debug(
    'Compiled regular expression with pattern:'
    f'{ATTRIBUTE_INPUT_INVALID_CHARACTERS.pattern}'
)

# Match pattern to replace space characters in a namedtuple attribute
ATTRIBUTE_INPUT_SPACE_CHARACTERS = compile(
    r'''
    \s            # Any space character
    ''',
    VERBOSE
)

# Log entry
# Log regex module compilation
application_log.debug(
    'Compiled regular expression with pattern:'
    f'{ATTRIBUTE_INPUT_SPACE_CHARACTERS.pattern}'
)

# Test attribute and value data for the run_make_named_tuple() function
TEST_DATA = {
    'first_name': 'Alex',
    'last_name': 'Smith',
    'age': 45,
    'hair_color': 'brown',
    'eye_color': 'green'
}

# Log entry
# Log load of test attribute data
application_log.debug(
    'Loaded test data:'
    f'{TEST_DATA}'
)


def validate_attribute_input(
    attribute_names: List
) -> List:
    ''' Validate or generate attribute names for a namedtuple.

        Args:
            attribute_names (List):
                Raw list of namedtuple attribute names from user input.

        Returns:
            attribute_names (List):
                Refined list of namedtuple attribute names.
    '''

    # Log entry
    # Log start of attribute name validation
    application_log.info(
        'Start namedtuple attribute name validation.'
    )

    # Loop over each attribute name
    for index, _ in enumerate(attribute_names):

        # Log entry
        # Log each attribute validation iteration
        application_log.debug(
            f'Validating attribute index {index} '
            f'with the starting value "{attribute_names[index]}"'
        )

        # Remove leading/trailing spaces and invalid start characters
        attribute_names[index] = ATTRIBUTE_INPUT_START_CHARACTER.sub(
            repl='',
            string=attribute_names[index].strip()
        )

        # Log entry
        # Log leading/trailing space and invalid start character removal
        application_log.debug(
            'Removed leading/trailing spaces and invalid start characters '
            f'in attribute index {index}, '
            f'updated value to "{attribute_names[index]}"'
        )

        # Replace any invalid characters
        attribute_names[index] = ATTRIBUTE_INPUT_INVALID_CHARACTERS.sub(
            repl='',
            string=attribute_names[index].strip()
        )

        # Log entry
        # Log invalid character removal
        application_log.debug(
            f'Removed invalid characters in attribute index {index}, '
            f'updated value to "{attribute_names[index]}"'
        )

        # Replace mid-value spaces with _
        attribute_names[index] = ATTRIBUTE_INPUT_SPACE_CHARACTERS.sub(
            repl='_',
            string=attribute_names[index].strip()
        )

        # Log entry
        # Log mid-value space replacement
        application_log.debug(
            f'Replaced space characters in attribute index {index}, '
            f'updated value to "{attribute_names[index]}"'
        )

        # Create an attribute name for a blank string
        if attribute_names[index] == '':
            attribute_names[index] = f'index_{index}'

            # Log attribute name creation
            application_log.debug(
                f'Attribute {index} is blank, created attribute name '
                f'"{attribute_names[index]}"'
            )

    # Log entry
    # Log return value for attribute_names
    application_log.info(
        'Attribute validation complete. '
        f'Returning "attribute_names" list with the values: {attribute_names}'
    )

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

    # Log entry
    # Log the start of the decorator function
    application_log.info(
        'Start run of the decorator function "named_tuple_converter".'
    )

    # Log entry
    # Log the use of the @wraps decorator
    application_log.debug(
        f'Pass the decorated function "{function.__name__}" in the "function" '
        'parameter to the "@wraps" decorator, to preserve the decorated '
        'function\'s docstring.'
    )

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

        # Log entry
        # Log the start of the function decorated by @wraps
        application_log.info(
            'Start run of the function decorated by at "@wraps" '
            'named "convert_to_namedtuple".'
        )

        # Log entry
        # Log the decorated function call, passed by the function parameter
        application_log.debug(
            f'Calling the decorated function "{function.__name__}" '
            'with the argument values:\n'
            f'*args: {(args)}\n'
            f'**kwargs: {kwargs}'
        )

        # Call the decorated function
        iterable_input = function(*args, **kwargs)

        # Log entry
        # Log the decorated function call result
        application_log.debug(
            f'Call to decorated function "{function.__name__}" returned '
            f'The "iterable_input" value {iterable_input}'
        )

        # Log entry
        # Log a presence check for the attribute_names kwarg
        application_log.info(
            'Checking for presence of the "attribute_names" kwarg using '
            'the "dict.get" method.'
        )

        # Convert the attribute_names argument value to a list object
        if kwargs.get('attribute_names') is not None:
            attribute_names = list(kwargs.get('attribute_names'))

            # Log entry
            # Log a presence check for the attribute_names kwarg
            application_log.info(
                '"attribute_names" kwarg found.'
            )

            # Log entry
            # Log the value of the attribute names kwarg
            application_log.debug(
                '"attribute_names" kwarg contains the values:\n'
                f'{attribute_names}'
            )

        # Collect attribute names
        else:

            # Log entry
            # Log the the result of a None value for the kwarg attribute_names
            application_log.info(
                '"attribute_names" kwarg not found.'
            )

            # Log entry
            # Log setting the attribute_names variable to None
            application_log.debug(
                f'"attribute_names" kwarg set to a value of "{None}".'
            )

            # Log entry
            # Log before setting the attribute_names variable to a blank list
            application_log.debug(
                f'Setting "attribute_names" value to an empty list ({[]}).'
            )

            attribute_names = []

            # Log entry
            # Log setting the attribute_names variable to a blank list
            application_log.debug(
                f'"attribute_names" kwarg value set to "{attribute_names}".'
            )

            # Log entry
            # Log start of loop over iterable_input
            application_log.info(
                'Start loop over the "iterable_input" kwarg, and prompt '
                'for names to assign each namedtuple attribute.'
            )

            for index, value in enumerate(iterable_input):

                # Log entry
                # Log loop iteration information
                application_log.debug(
                    f'Attribute {index} value is "{value}".'
                )

                # Log entry
                # Log a presence check for the auto_attribute_names kwarg
                application_log.info(
                    'Checking for presence of the '
                    '"auto_attribute_names" kwarg.'
                )

                # Set individual attribute names to a blank string
                # The validate_attribute_input function replaces blank strings
                if kwargs.get('auto_attribute_names') is True:

                    # Log Entry
                    # Log the presence of the auto_attribute_names argument
                    application_log.info(
                        f'"auto_attribute_names" is "{True}", auto-naming '
                        f'attribute index {index}.'
                    )

                    # Log Entry
                    # Log setting the current attribute index value to ''
                    application_log.debug(
                        f'Setting name for attribute "{value}" to "\'\'".'
                    )
                    attribute_names.append('')

                # Get individual attribute names via input function
                else:

                    # Log Entry
                    # Log the absence of the auto_attribute_names argument
                    application_log.info(
                        f'"auto_attribute_names" is "{False}", prompting for '
                        f'name to assign the attribute value "{value}".'
                    )

                    # Log Entry
                    # Log input method call, to prompt for attribute name
                    application_log.debug(
                        'Calling "input" method to collect attribute name.'
                    )

                    # Append the input value to the attribute_names list
                    attribute_names.append(
                        input(
                            'Enter an attribute name for the value '
                            f'"{value}": '
                        )
                    )

                    # Log Entry
                    # Log value collected from input method
                    application_log.info(
                        'User input the attribute name '
                        f'"{attribute_names[-1]}" for the value "{value}".'
                    )

        # Log Entry
        # Log start of attribute name validation
        application_log.info(
            'Start attribute name validation.'
        )

        # Log Entry
        # Log function call to validate_attribute_input
        application_log.debug(
            'Calling the "validate_attribute_input" function, sending the '
            'list "attribute_names" as an argument with the value:\n'
            f'{attribute_names}'
        )

        # Validate attribute names
        attribute_names = validate_attribute_input(
            attribute_names=attribute_names
        )

        # Log Entry
        # Log end of attribute name validation
        application_log.info(
            'Attribute name validation complete.'
        )

        # Log Entry
        # Log check for an equal number of attribute names and iterable values
        application_log.info(
            'Check for an equal number of attribute names and values '
            'before constructing namedtuple.'
        )

        # Log Entry
        # Log count of attribute names and iterable values
        application_log.debug(
            f'"attribute_name" length is {len(attribute_names)} and '
            f'"iterable_input" count is {len(iterable_input)}.'
        )

        # Check for an equal number of attribute names and iterable values
        if len(iterable_input) == len(attribute_names):

            # Log Entry
            # Log equal result of attribute name and value count comparision
            application_log.info(
                'Number of attribute names and values is equivalent, '
                'creating namedtuple.'
            )

            # Define a namedtuple object
            NamedTuple = namedtuple(
                typename='NamedTuple',
                field_names=attribute_names
            )

            # Log Entry
            # Log creation of the NamedTuple class
            application_log.debug(
                'Created namedtuple class with the name "NamedTuple" and '
                f'assigned the attribute names:\n{NamedTuple._fields}.'
            )

            # Log Entry
            # Log instantion of namedtuple object from the NamedTuple class
            application_log.info(
                'Instantiating namedtuple object with the name "named_tuple" '
                'from the "NamedTuple class.'
            )

            # Log Entry
            # Log named_tuple instantiation
            application_log.debug(
                f'Passing the values {iterable_input} to the "NamedTuple" '
                'class, and assigning result to the variable "named_tuple".'
            )

            # Create a namedtuple from the attribute names and source iterable
            named_tuple = NamedTuple(
                *iterable_input
            )

            # Log Entry
            # Log result of named_tuple instantiation
            application_log.debug(
                'Created namedtuple object "named_tuple":\n'
                f'{named_tuple}'
            )

        # Raise an exception for an unequal number of attributes and inputs
        else:

            # Log Entry
            # Log unequal result of attribute name and value count comparision
            application_log.info(
                'Number of attribute names and values is not equivalent, '
                'raising exception.'
            )

            # Log Entry
            # Log raise of ValueError for unequal attribute name/value count
            application_log.error(
                f'Raising {ValueError} for due to unequal length of '
                f'"iterable_input" ({len(iterable_input)}) and '
                f'"attribute_names" ({len(attribute_names)}) objects.'
            )

            raise ValueError(
                'Length of iterable_input and attribute_names must be equal:\n'
                f'iterable_input length = {len(iterable_input)}\n'
                f'attribute_names length = {len(attribute_names)}'
            )

        # Log Entry
        # Log return of convert_to_namedtuple function to named_tuple_converter
        application_log.info(
            'Function "convert_to_namedtuple" returning named_tuple object '
            '"named_tuple" to the calling function "named_tuple_converter".'
        )

        # Log Entry
        # Log returned value of convert_to_namedtuple
        application_log.debug(
            'Returning object "named_tuple" with the value:\n'
            f'{named_tuple}'
        )

        return named_tuple

    # Log Entry
    # Log return of named_tuple to named_tuple_converter function
    application_log.info(
        'Function "named_tuple_converter" returning function/Callable object '
        '"convert_to_namedtuple" to calling decorator function '
        '"named_tuple_converter".'
    )

    # Log Entry
    # Log returned value of named_tuple_converter function
    application_log.debug(
        'Returning object "convert_to_namedtuple" with the value:\n'
        f'{convert_to_namedtuple}'
    )

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

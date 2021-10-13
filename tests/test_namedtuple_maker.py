#!/usr/bin/env pytest
''' pytest tests for namedtuple_maker.py

    Usage:
        pytest tests/test_namedtuple_maker.py
'''

# Imports
from namedtuple_maker.namedtuple_maker import named_tuple_converter, \
                                              make_named_tuple, TEST_DATA
from collections import namedtuple
from pytest import mark
from typing import Iterable
from unittest.mock import patch

# Constants
# Create a namedtuple object for synthetic testing
TEST_PERSON_INFO = namedtuple(
    typename='NamedTuple',
    field_names=TEST_DATA.keys()
)

# Instantiate an object from the testing namedtuple, add test data values
TEST_EXPECTED_RESULT = TEST_PERSON_INFO(**TEST_DATA)

# Create a tuple of attribute names with invalid characters
TEST_INVALID_ATTRIBUTE_NAMES_DATA = (
    '_first_name',
    '$1_las*t_nam)(e',
    '+_age',
    'hair color #',
    '  4eye color !@'
)

# Create a test value for a non-iterable object
TEST_INVALID_ITERABLE_OBJECT = 9

# Capture the number of values in the TEST_DATA object
TEST_DATA_LENGTH = len(TEST_DATA.values())

# Create a set of auto-generated attribute names (TEST_DATA_LENGTH # of items)
TEST_AUTO_ATTRIBUTE_NAME_DATA = (f'index_{i}' for i in range(TEST_DATA_LENGTH))


@mark.parametrize(

    # Test data argument names (descriptions in test function docstring)
    argnames=[
        'iter_input',
        'att_names',    # namedtuple attribute names
        'iter_return',  # Expected attribute value names
        'att_return'    # Expected attribute name results
    ],

    # Test data argument values
    argvalues=[

        # Test #1  values, to test normal operation
        [
            TEST_DATA.values(),
            TEST_DATA.keys(),
            TEST_DATA.values(),
            TEST_DATA.keys()
        ],

        # Test #2 values, to test auto-modification of invalid attribute names
        [
            TEST_DATA.values(),
            TEST_INVALID_ATTRIBUTE_NAMES_DATA,
            TEST_DATA.values(),
            TEST_DATA.keys()
        ]
    ]
)
def test_named_tuple_converter(
    iter_input,
    att_names,
    iter_return,
    att_return
) -> None:
    ''' Test of the named_tuple_converter decorator function to determine if
        the function accepts an iterable argument and returns a namedtuple
        with the original iterable data values. Collect the namedtuple field
        names from an iterable of names passed an argument.

        Args:
            iter_input (Iterable):
                Iterable input to be converted to namedtuple attribute values.

            att_names (Iterable):
                Iterable input of namedtuple attribute names.

            iter_return (Iterable):
                Iterable output of expected namedtuple attribute values.

            att_return (Iterable):
                Iterable output of expected namedtuple attribute names.

        Returns:
            None.
    '''

    # Get a namedtuple result to test
    test_result = make_named_tuple(
        iterable_input=iter_input,
        attribute_names=att_names
    )

    # Verify the test result object is of type NamedTuple
    assert 'NamedTuple' in str(test_result.__class__)

    # Verify the iterable input equals the namedtuple attribute values
    assert tuple(iter_return) == tuple(test_result._asdict().values())

    # Verify the attribute names input equals the namedtuple attribute names
    assert tuple(att_return) == test_result._fields


@patch(

    # Create mock namedtuple attribute name data for the input() function
    'builtins.input',
    side_effect=TEST_DATA.keys()
)
def test_named_tuple_converter_input(side_effects) -> None:
    ''' Test of the named_tuple_converter decorator function to determine if
        the function accepts an iterable argument and returns a namedtuple
        with the original iterable data values. Collect the namedtuple
        attribute names with the input() function.

        Args:
            side_effects (unittest.mock.patch):
                namedtuple attribute name mock data for the input() function.

        Returns:
            None.
    '''

    # Get a namedtuple result to test
    test_result = make_named_tuple(
        iterable_input=TEST_DATA.values(),
    )

    # Verify the test result object is of type NamedTuple
    assert 'NamedTuple' in str(test_result.__class__)

    # Verify the iterable input equals the namedtuple attribute values
    assert tuple(TEST_DATA.values()) == tuple(test_result._asdict().values())

    # Verify the attribute names input equals the namedtuple attribute names
    assert tuple(TEST_DATA.keys()) == test_result._fields


@mark.parametrize(

    # Test data argument names (descriptions in test function docstring)
    argnames=[
        'iter_input',
        'iter_return',
        'att_return'
    ],

    # Test #1  values, to test normal operation
    argvalues=[
        [
            TEST_DATA.values(),
            TEST_DATA.values(),
            TEST_AUTO_ATTRIBUTE_NAME_DATA
        ]
    ]
)
def test_named_tuple_converter_custom_function_auto_name_attributes(
    iter_input,
    iter_return,
    att_return
) -> None:
    ''' Test of the named_tuple_converter decorator function using a custom
        function to determine if the function accepts an iterable argument
        and returns a namedtuple with the original iterable data, and if the
        decorator function automatically names the namedtuple attributes
        with the auto_attribute_names parameter set to True. Collect the
        namedtuple field names from an iterable of names passed an argument.

        Args:
            iter_input (Iterable):
                Iterable input to be converted to namedtuple attribute values.

            att_names (Iterable):
                Iterable input of namedtuple attribute names.

            att_return (Iterable):
                Iterable output of expected namedtuple attribute names.

        Returns:
            None.
    '''

    # Create a custom function decorated with named_tuple_converter
    @named_tuple_converter
    def custom_function(
        iterable_input: Iterable,
        auto_attribute_names: bool
    ) -> tuple:
        ''' Test function that accepts an iterable object as input,
            and returns the iterable as a tuple object.

            Args:
                iterable_input (Iterable):
                    Iterable object to convert to a tuple object.

                auto_attribute_names (bool):
                    Boolean to specify whether or not namedtuple attribute
                    names are automatically generated or provided as a
                    separate argument.
        '''

        return tuple(iter_input)

    # Get a namedtuple result to test
    test_result = custom_function(
        iterable_input=iter_input,
        auto_attribute_names=True
    )

    # Verify the test result object is of type NamedTuple
    assert 'NamedTuple' in str(test_result.__class__)

    # Verify the iterable input equals the namedtuple attribute values
    assert tuple(iter_return) == tuple(test_result._asdict().values())

    # Verify the attribute names input equals the namedtuple attribute names
    assert tuple(att_return) == test_result._fields


def test_named_tuple_converter_invalid_iterable_exception(capfd) -> None:
    ''' Test of the named_tuple_converter decorator function for exception
        handling, when the iterable_input argument contains a non-iterable
        object/value.

        Args:
            capsys (pytest fixture):
                Output stream to STDOUT and STDERR.

        Returns:
            None.
    '''

    make_named_tuple(
        iterable_input=TEST_INVALID_ITERABLE_OBJECT,
        auto_attribute_names=True
    )

    print(dir(capfd))

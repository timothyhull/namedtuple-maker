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

    # Get a result to test
    test_result = make_named_tuple(
        iterable_input=iter_input,
        attribute_names=att_names
    )

    # Verify the result is of type NamedTuple
    assert 'NamedTuple' in str(test_result.__class__)

    # Verify the test tuple input data equals the namedtuple attribute values
    assert tuple(iter_return) == tuple(test_result._asdict().values())

    # Verify the field names input data equals the namedtuple attribute names
    assert tuple(att_return) == test_result._fields


@patch(
    'builtins.input',
    side_effect=TEST_DATA.keys()
)
def test_named_tuple_converter_input(side_effects) -> None:
    ''' Test of the named_tuple_converter decorator function to determine if
        the function accepts a tuple argument and returns a namedtuple
        with the original tuple data. Collect the field names with the
        input() function.

        Args:
            None.

        Returns:
            None.
    '''

    # Get a result to test
    test_result = make_named_tuple(
        iterable_input=TEST_DATA.values(),
    )

    # Verify the result is of type NamedTuple
    assert 'NamedTuple' in str(test_result.__class__)

    # Verify the test tuple input data equals the namedtuple attribute values
    assert tuple(TEST_DATA.values()) == tuple(test_result._asdict().values())

    # Verify the field names input data equals the namedtuple attribute names
    assert tuple(TEST_DATA.keys()) == test_result._fields


@mark.parametrize(
    argnames=[
        'iter_input',
        'iter_return',
        'att_return'
    ],
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
        function to determine if the function accepts a tuple argument
        and returns a namedtuple with the original tuple data, and if the
        decorator function automatically names the namedtuple attributes
        with the auto_attribute_names parameter set to True. Pass the
        namedtuple field names as an argument.

        Args:
            None.

        Returns:
            None.
    '''

    # Create a custom function decorated with named_tuple_converter
    @named_tuple_converter
    def custom_function(
        iterable_input: Iterable,
        auto_attribute_names: bool
    ) -> tuple:
        '''
        '''

        return tuple(iter_input)

    # Get a result to test
    test_result = custom_function(
        iterable_input=iter_input,
        auto_attribute_names=True
    )

    # Verify the result is of type NamedTuple
    assert 'NamedTuple' in str(test_result.__class__)

    # Verify the test tuple input data equals the namedtuple attribute values
    assert tuple(iter_return) == tuple(test_result._asdict().values())

    # Verify the field names input data equals the namedtuple attribute names
    assert tuple(att_return) == test_result._fields

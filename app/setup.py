#!/usr/bin/env python3

# Imports
import pathlib
from setuptools import setup

# Constants
# The directory that contains this file
HERE = pathlib.Path(__file__).parent
# The root path of the repository
ROOT = HERE.parent
# README contents
README = (ROOT / 'README.md').read_text()

# Setup
setup(
    name='namedtuple-maker',
    version='1.0.0',
    description='Convert iterable objects to namedtuple objects.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/timothyhull/namedtuple-maker',
    author='Timothy Hull',
    author_email='timothyhull@gmail.com',
    license='Apache 2.0',
    classifiers=[
        'License :: Apache 2.0 License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9'
    ],
    packages=['namedtuple-maker'],
    include_package_data=True,
    install_requires=None,
    entry_points={
        'console_scripts': [
            'namedtuple_maker=namedtuple_maker.__main__:tuple_tester'
        ]
    }
)

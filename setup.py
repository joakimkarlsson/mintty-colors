#!/usr/bin/env python
from setuptools import setup, find_packages


VERSION = '0.0.1'

setup(
    name='mintty-colors',
    version=VERSION,

    packages=find_packages(),

    install_requires=[
        'click>=6.6',
    ],

    entry_points={
        'console_scripts': [
            'mtc = mtc:cli'
        ]
    }
)

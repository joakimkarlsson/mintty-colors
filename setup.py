#!/usr/bin/env python
from setuptools import setup
import os.path as op


VERSION = '1.0.0'


def read(filename):
    return open(op.join(op.dirname(__file__), filename)).read()


setup(
    name='mintty-colors',
    version=VERSION,
    url='https://github.com/joakimkarlsson/mintty-colors',
    author='Joakim Karlsson',
    author_email='joakim@jkarlsson.com',
    description='Switch color themes on the fly in cygwin\'s mintty terminal',
    long_description=read('README.rst'),
    license='MIT',
    keywords='cyginw mintty colors',

    py_modules=['mtc'],

    install_requires=[
        'click>=6.6',
    ],

    entry_points={
        'console_scripts': [
            'mtc = mtc:cli'
        ]
    }
)

#############
mintty-colors
#############

A command line tool for switching colors on the fly in cygwin's mintty terminal.

************
Installation
************

You know this::

    pip install mintty-colors

This installs a command-line tool - `mtc` that let's you control the colors of your mintty session.


*****
Usage
*****

List available themes
=====================

.. code:: bash

    $ mtc list

Change current theme
====================

.. code:: bash

    $ mtc set <theme>

Configuration
=============

You can add your own themes or override the built-in themes by putting a file at :code:`~/.mintty-colors`. This file is a config file where each section describes a mintty color scheme in the format used in mintty's :code:`~/.minttyrc` file.

Example::

    [solarized-light]
    BackgroundColour=253,246,227
    ForegroundColour=88,110,117
    CursorColour=88,110,117
    Black=0,43,54
    BoldBlack=101,123,131
    Red=220,50,47
    BoldRed=220,50,47
    Green=133,153,0
    BoldGreen=133,153,0
    Yellow=181,137,0
    BoldYellow=181,137,0
    Blue=38,139,210
    BoldBlue=38,139,210
    Magenta=108,113,196
    BoldMagenta=108,113,196
    Cyan=42,161,152
    BoldCyan=42,161,152
    White=147,161,161
    BoldWhite=253,246,227

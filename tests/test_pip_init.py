#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from pip_init.templates import setup_line
from pip_init.templates import setup_base_template
from pip_init import input_message


class TestPipInitTemplates(unittest.TestCase):

    def test_setup_line(self):
        self.assertEqual(
            setup_line.substitute(name='author', value='me'),
            '    author="me",\n',
        )

    def test_setup_base_template(self):

        expected_setup = (
            'from setuptools import setup, find_packages\n'
            '\n'
            'try:\n'
            '    long_description = open("README.rst").read()\n'
            'except IOError:\n'
            '    long_description = ""\n'
            '\n'
            'setup(\n'
            '    name="dump-package",\n'
            '    packages=find_packages(),\n'
            '    install_requires=[],\n'
            '    long_description=long_description,\n'
            '    classifiers=[\n'
            '        "Programming Language :: Python",\n'
            '    ]\n'
            ')\n'
        )

        setup_lines = '    name="dump-package",\n'

        self.assertEqual(
            expected_setup,
            setup_base_template.substitute(setup_lines=setup_lines)
        )


class TestUtils(unittest.TestCase):

    def test_input_message(self):
        self.assertEqual(
            input_message('author', 'author name'),
            'author (author name): '
        )

#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from pip_init.templates import setup_line
from pip_init import input_message


class TestPipInitTemplates(unittest.TestCase):

    def test_setup_line(self):
        self.assertEqual(
            setup_line.substitute(name='author', value='me'),
            '    author="me",\n',
        )


class TestUtils(unittest.TestCase):

    def test_input_message(self):
        self.assertEqual(
            input_message('author', 'author name'),
            'author (author name): '
        )

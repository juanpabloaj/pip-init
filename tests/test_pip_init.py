#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from pip_init.templates import setup_line


class TestPipInitTemplates(unittest.TestCase):

    def test_setup_line(self):
        self.assertEqual(
            setup_line.substitute(name='author', value='me'),
            '    author="me",\n',
        )

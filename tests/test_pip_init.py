#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from pip_init.templates import setup_line
from pip_init.templates import setup_base_template
from pip_init.templates import classifiers_line
from pip_init.templates import classifiers_template
from pip_init import input_message
from pip_init import gen_classifiers


class TestPipInitTemplates(unittest.TestCase):

    def test_setup_line(self):
        self.assertEqual(
            setup_line.substitute(name='author', value='me'),
            '    author="me",\n',
        )

    def test_classifiers_line(self):
        self.assertEqual(
            classifiers_line.substitute(classifier='classifier'),
            '        "classifier",\n'
        )

    def test_classifiers_tpl(self):
        classifiers_lines = (
            '        "python 2.7",\n'
            '        "python 3.4",\n'
        )

        self.assertMultiLineEqual(
            classifiers_template.substitute(classifiers=classifiers_lines),
            (
                '    classifiers=[\n'
                '        "python 2.7",\n'
                '        "python 3.4",\n'
                '    ]'
            )
        )

    def test_setup_base_template(self):

        expected_setup = (
            '# -*- coding: utf-8 -*-\n'
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
            '        "Programming Language :: Python :: 2.7"\n'
            '    ]\n'
            ')\n'
        )

        setup_lines = '    name="dump-package",\n'
        classifiers = (
            '    classifiers=[\n'
            '        "Programming Language :: Python",\n'
            '        "Programming Language :: Python :: 2.7"\n'
            '    ]'
        )

        self.assertMultiLineEqual(
            expected_setup,
            setup_base_template.substitute(
                setup_lines=setup_lines,
                classifiers=classifiers
            )
        )


class TestUtils(unittest.TestCase):

    def test_input_message(self):
        self.assertEqual(
            input_message('author', 'author name'),
            'author (author name): '
        )

    def test_gen_classifiers(self):
        self.assertIn(
            '        "Programming Language :: Python",\n',
            gen_classifiers()
        )

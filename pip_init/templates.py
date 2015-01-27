#!/usr/bin/python
# -*- coding: utf-8 -*-
from string import Template

setup_base_template = Template(
    'from setuptools import setup, find_packages\n'
    '\n'
    'try:\n'
    '    long_description = open("README.rst").read()\n'
    'except IOError:\n'
    '    long_description = ""\n'
    '\n'
    'setup(\n'
    '${setup_lines}'
    '    packages=find_packages(),\n'
    '    install_requires=[],\n'
    '    long_description=long_description\n'
    ')\n'
)

setup_line = Template(
    '    ${name}="${value}",\n'
)

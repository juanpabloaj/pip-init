#!/usr/bin/python
# -*- coding: utf-8 -*-
from string import Template

setup_base_template = Template(
    'from setuptools import setup\n'
    '\n'
    'setup(\n'
    '${setup_lines}\n'
    ')\n'
)

setup_line = Template(
    '    ${name}="${value}",\n'
)

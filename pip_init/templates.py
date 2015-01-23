#!/usr/bin/python
# -*- coding: utf-8 -*-
from string import Template

setup_base_template = Template(
    'from setuptools import setup\n'
    'from pip.req import parse_requirements\n'
    'from pip.exceptions import InstallationError\n'
    '\n'
    'try:\n'
    '    requirements = parse_requirements("requirements.txt")\n'
    '    install_requires=[str(r.req) for r in requirements]\n'
    'except InstallationError:\n'
    '    install_requires = []\n'
    '\n'
    'setup(\n'
    '${setup_lines}'
    '    install_requires=install_requires\n'
    ')\n'
)

setup_line = Template(
    '    ${name}="${value}",\n'
)

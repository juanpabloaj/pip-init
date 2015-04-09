#!/usr/bin/python
# -*- coding: utf-8 -*-
from string import Template
from textwrap import dedent

setup_base_template = Template(dedent("""\
    # -*- coding: utf-8 -*-
    from setuptools import setup, find_packages

    try:
        long_description = open("README.rst").read()
    except IOError:
        long_description = ""

    setup(
    ${setup_lines}\
    packages=find_packages(),
        install_requires=[],
        long_description=long_description,
    ${classifiers}
    )
    """))

setup_line = Template(
    '    ${name}="${value}",\n'
)

classifiers_line = Template(
    '        "${classifier}",\n'
)

classifiers_template = Template(
    '    classifiers=[\n'
    '${classifiers}'
    '    ]'
)

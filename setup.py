#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


def read(*paths):
    """ read files """
    with open(os.path.join(*paths), 'r') as filename:
        return filename.read()

setup(
    name="pip-init",
    version="0.1.0",
    description="pip-init to generate a base setup.py file",
    long_description=(read('README.rst')),
    license='MIT',
    author="JuanPablo AJ",
    author_email="jpabloaj@gmail.com",
    url="https://github.com/juanpabloaj/pip-init",
    packages=['pip_init'],
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'pip-init=pip_init:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ]
)

#!/usr/bin/python
# -*- coding: utf-8 -*-
from pip_init.templates import setup_base_template, setup_line
from pip_init.templates import classifiers_line, classifiers_template
from sys import version_info
from subprocess import Popen, PIPE
from getpass import getuser
import os


def input_message(field_name, default_value):
    return u'{} ({}): '.format(field_name, default_value)


def gen_classifiers():
    mayor, minor = version_info[:2]
    python = "Programming Language :: Python"
    local = "Programming Language :: Python :: {}.{}".format(mayor, minor)
    classifiers = [python, local]

    classifiers_lines = ''
    for cls in classifiers:
        classifiers_lines += classifiers_line.substitute(classifier=cls)

    return classifiers_template.substitute(classifiers=classifiers_lines)


def get_username():
    '''Get git config values.'''
    username = ''

    # use try-catch to prevent crashes if user doesn't install git
    try:
        # run git config --global <key> to get username
        git_command = ['git', 'config', '--global', 'user.name']
        p = Popen(git_command, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()

        # turn stdout into unicode and strip it
        username = output.decode('utf-8').strip()

        # if user doesn't set global git config name, then use getuser()
        if not username:
            username = getuser()
    except OSError:
        # if git command is not found, then use getuser()
        username = getuser()

    return username


def default_values(field_name):
    if field_name == 'name':
        return os.path.relpath('.', '..')
    if field_name == 'version':
        return '0.1.0'
    elif field_name == 'description':
        return 'A pip package'
    elif field_name == 'license':
        return 'MIT'
    elif field_name == 'author':
        return get_username()


def main():
    fields = ['name', 'version', 'description', 'license', 'author']
    setup_lines = ''

    for field_name in fields:
        default_value = default_values(field_name)
        input_msg = input_message(field_name, default_value)

        if version_info >= (3, 0):
            input_value = input(input_msg)
        else:
            input_value = raw_input(input_msg.encode('utf8'))

        if input_value == '':
            input_value = default_value

        setup_lines += setup_line.substitute(
            name=field_name, value=input_value
        )

    setup_content = setup_base_template.substitute(
        setup_lines=setup_lines,
        classifiers=gen_classifiers()
    )

    with open('setup.py', 'w') as setup_file:
        if version_info >= (3, 0):
            setup_file.write(setup_content)
        else:
            setup_file.write(setup_content.encode('utf8'))


if __name__ == '__main__':
    main()

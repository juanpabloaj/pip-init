#!/usr/bin/python
# -*- coding: utf-8 -*-
from pip_init.templates import setup_base_template, setup_line
from subprocess import Popen, PIPE


def git_config(key):
    '''Get git config values.'''

    # run git config --global <key> to get global git config value
    p = Popen(['git', 'config', '--global', key], stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()

    # turn stdout into unicode and strip it
    output = output.decode('utf-8').strip()

    return output


def default_values(field_name):
    if field_name == 'name':
        return 'package-name'
    if field_name == 'version':
        return '0.1.0'
    elif field_name == 'description':
        return 'A pip package'
    elif field_name == 'license':
        return 'MIT'
    elif field_name == 'author':
        return git_config('user.name')


def main():
    fields = ['name', 'version', 'description', 'license', 'author']
    setup_lines = ''

    for field_name in fields:
        default_value = default_values(field_name)
        input_msg = '{} ({}): '.format(field_name, default_value)

        input_value = raw_input(input_msg)
        if input_value == '':
            input_value = default_value

        setup_lines += setup_line.substitute(
            name=field_name, value=input_value
        )

    setup_content = setup_base_template.substitute(setup_lines=setup_lines)

    with open('setup.py', 'w') as setup_file:
        setup_file.write(setup_content)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup

required = [line for line in open('requirements.txt').read().split("\n") if not line.startswith("http")]
dependency_links = [line for line in open('requirements.txt').read().split("\n") if line.startswith("http")]
required_dev = [line for line in open('requirements_dev.txt').read().split("\n") if not line.startswith("-r")]
fbinit = open('fitbit/__init__.py').read()
author = re.search("__author__ = '([^']+)'", fbinit).group(1)
version = re.search("__version__ = '([^']+)'", fbinit).group(1)

setup(
    name='fitbit',
    version=version,
    description='Fitbit API Wrapper.',
    long_description=open('README.rst').read(),
    author=author,
    author_email='issac@kellycreativetech.com',
    url='https://github.com/issackelly/python-fitbit',
    packages=['fitbit'],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=["distribute"] + required,
    dependency_links=dependency_links,
    license='Apache 2.0',
    test_suite='tests.all_tests',
    tests_require=required_dev,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache 2.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)

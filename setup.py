#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, command
import os
import sys
import json

def download_lda_package():



setup(
    name='PythonSLDA',
    version='0.1.0',
    author='Manojit Nandi',
    author_email='mnandi92@gmail.com',
    packages=['pythonslda', 'pythonslda.test'],
    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/PythonSLDA/',
    license='LICENSE.txt',
    description='Python wrapper for sLDA method in R \"lda\" package.',
    long_description=open('README.txt').read(),
    install_requires=[
        "pyper",
    ],
)

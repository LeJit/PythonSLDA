#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, command
import os
import sys
import json

def download_lda_package():



setup(
    name="PythonSLDA",
    packages=['PythonSLDA'],
    install_requires=[
        'pyper',
    ]
)

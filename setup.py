# coding: utf-8

import os
import sys
from setuptools import setup, find_packages


setup(
    name='apex_wsgi_sample',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)

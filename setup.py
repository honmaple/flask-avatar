#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: setup.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-07-02 16:12:02 (CST)
# Last Update: Saturday 2018-03-03 21:38:50 (CST)
#          By:
# Description:
# **************************************************************************
from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Flask-Avatar',
    version='0.1.3',
    url='https://github.com/honmaple/flask-avatar',
    license='BSD',
    author='honmaple',
    author_email='xiyang0807@gmail.com',
    description='To generate avatar for flask',
    long_description=read('README.rst'),
    packages=['flask_avatar'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'Pillow'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])

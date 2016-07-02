#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: setup.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-07-02 16:12:02 (CST)
# Last Update:星期六 2016-7-2 18:31:25 (CST)
#          By:
# Description:
# **************************************************************************
from setuptools import setup


setup(
    name='Flask-Avatar',
    version='0.1.0',
    url='https://github.com/honmaple/flask-avatar',
    license='BSD',
    author='honmaple',
    author_email='xiyang0807@gmail.com',
    description='To generate avatar for flask',
    long_description='Please visit https://github.com/honmaple/flask-avatar',
    packages=['flask_avatar'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Pillow'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

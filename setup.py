#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "May 19, 2015"

from setuptools import setup, find_packages
import os
import catalog

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mfs-catalog',
    version=catalog.__version__,
    packages=find_packages(),
    # package_data={'setlinks.templates': ['*']},
    install_requires=[
        'django>=1.7', 'django-polymorphic==0.7.1', 'django-polymorphic-tree==1.1',
        'django-mptt==0.7.3', 'easy-thumbnails==2.2'
    ],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to conduct Web-based catalog.',
    long_description=README,
    url='http://www.example.com/',
    author=catalog.__author__,
    author_email=catalog.__email__,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
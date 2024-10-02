#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import io
from setuptools import setup, find_packages


BASE_DIR = os.path.join(os.path.dirname(__file__))

with io.open(os.path.join(BASE_DIR, 'README.md'), encoding='utf-8') as f:
    README = f.read()

VERSION = __import__('spirit').__version__

with io.open(os.path.join(BASE_DIR, 'requirements.txt'), encoding='utf-8') as fh:
    REQUIREMENTS = fh.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-spirit',
    version=VERSION,
    description='Spirit is a Python based forum powered by Django.',
    author='Esteban Castro Borsani',
    author_email='ecastroborsani@gmail.com',
    long_description=README,
    long_description_content_type='text/markdown',
    url='http://spirit-project.com/',
    packages=find_packages(),
    test_suite="runtests.start",
    entry_points="""
[console_scripts]
spirit=spirit.extra.bin.spirit:main
""",
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    extras_require={
        'files': [
            # the two requirements below simplify to the single requirement "python-magic==0.4.28" when cross-platform python-magic gets released: https://github.com/ahupp/python-magic/pull/294
            "python-magic-bin~=0.4.14 ; sys_platform == 'win32'",
            # for python-magic to work, either install libmagic on your system or install cross-platform python-magic (containing pre-compiled libmagic) by running 'pip install python-magic==0.4.28 --find-links=https://github.com/ddelange/python-magic/releases/expanded_assets/0.4.28.post7'
            "python-magic~=0.4.27 ; sys_platform != 'win32'",
        ],
        'huey': 'huey == 2.4.5',
        'celery': 'celery[redis] == 4.4.7'},
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

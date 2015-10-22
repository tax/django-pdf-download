# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='django-pdf-download',
    version='0.1.0',
    author='Paul Tax',
    author_email='paultax@gmail.com',
    include_package_data=True,
    install_requires=['PyVirtualDisplay==0.1.5', 'selenium==2.47.3', 'Django>=1.8.0'],
    py_modules=['pdfdownload'],
    entry_points={
        'console_scripts': ['activate_headless_print=pdfdownload:activate_headless_print'],
    },
    url='https://github.com/tax/django-pdf-download',
    license='BSD licence, see LICENCE.txt',
    description='',
    long_description=open('README.md').read(),
)

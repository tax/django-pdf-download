# -*- coding: utf-8 -*-
import os
import sys
from setuptools.command.install import install
from setuptools import setup


class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        install.run(self)
        print "Print activating headless printing"
        from pdfdownload import activate_headless_print
        activate_headless_print()


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='django-pdf-download',
    version='0.0.3',
    author='Paul Tax',
    author_email='paultax@gmail.com',
    include_package_data=True,
    install_requires=['PyVirtualDisplay==0.1.5', 'selenium==2.47.3', 'Django>=1.8.0'],
    py_modules=['pdfdownload'],
    cmdclass={
        'install': CustomInstallCommand,
    },
    url='https://github.com/tax/django-pdf-download',
    license='BSD licence, see LICENCE.txt',
    description='',
    long_description=open('README.md').read(),
)

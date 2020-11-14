# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in custom_css/__init__.py
from custom_css import __version__ as version

setup(
	name='custom_css',
	version=version,
	description='Custom Css',
	author='bharath',
	author_email='bharathjinka09@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

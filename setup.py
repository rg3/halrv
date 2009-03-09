#!/usr/bin/env python

from distutils.core import setup

setup(
	name='halrv',
	version='3',
	description='HAL Removable Volumes Manager',
	author='Ricardo Garcia',
	url='http://github.com/rg3/halrv/tree/master',
	data_files = [
		('man/man1', ['halrv.1']),
	],
	scripts = [
		'halrv',
	],
)

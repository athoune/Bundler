#!/usr/bin/env python
# -*- coding: utf8 -*-

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(name='imageBundler',
      version='0.2.1',
      license='GPL-3',
      description='Image bundler',
      author='Mathieu Lecarme',
      author_email='mathieu@garambrogne.net',
      url='https://admin.garambrogne.net/projets/bundler',
      packages=[''],
      package_dir={'': 'src/'},
      scripts=['src/bundler'],
      install_requires=["PIL"]
     )

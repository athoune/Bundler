#!/usr/bin/env python
# -*- coding: utf8 -*-

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(name='imageBundler',
      version='0.2.2',
      license='GPL-3',
      description='Image bundler',
      author='Mathieu Lecarme',
      author_email='mathieu@garambrogne.net',
      url='http://github.com/athoune/Bundler',
      packages=['bundler'],
      package_dir={'': 'src'},
      scripts=['bin/bundler'],
      install_requires=["PIL==1.1.7"],
     )

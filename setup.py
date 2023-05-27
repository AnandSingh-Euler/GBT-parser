#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages
import re


def find_version():
    return re.search(r"^__version__ = '(.*)'$",
                     open('cantools/version.py', 'r').read(),
                     re.MULTILINE).group(1)


setup(name='GBT_parser',
      version=find_version(),
      description='GBT CAN bus parser.',
      long_description=open('README.rst', 'r').read(),
      long_description_content_type='text/x-rst',
      author='Anand Singh',
      author_email='anandsingh16898@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      keywords=['can', 'can bus', 'dbc', 'kcd', 'automotive'],
      url='https://github.com/AnandSingh-Euler/GBT-parser',
      packages=find_packages(exclude=['tests']),
      package_data={"GBT-parser": ["py.typed"]},
      python_requires='>=3.8',
      install_requires=[
          'bitstruct>=8.16.1',
          'python-can>=3.3.4',
          'textparser>=0.21.1',
          'diskcache',
          'argparse_addons',
          'typing_extensions>=3.10.0.0',
          'crccheck',
          'windows-curses',
      ],
      extras_require={
          'plot': ['matplotlib'],
          'windows-all': ["windows-curses;platform_system=='Windows'"],
      },
      test_suite="tests",
      entry_points={
          'console_scripts': ['cantools=cantools.__init__:_main']
      })

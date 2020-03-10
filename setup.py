#!/usr/bin/env python3

#from distutils.core import setup
from setuptools import setup, find_packages

setup(
      name='revwho',  
      version='0.1',
      scripts=['src/revwho'] ,
      description='A simple python tool to reverse search whois by name and email from free services',
      author='aggr3ssor',
      author_email='aggr3ssor@pm.me',
      url='https://github.com/aggr3ssor/Reverse-Whois',
      install_requires=['lxml'],
      packages=find_packages(where='src'),
      classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
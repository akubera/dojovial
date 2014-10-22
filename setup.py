#
# setup.py
#

import sys

from setuptools import setup, find_packages

install_requires = ['growler', 'asyncio_mongo']

long_description = """
Growler application providing web access to a sandboxed python environment
allowing (authorized) friends to connect to the server and run/share python
code.

Inspired by the lack of collaboration available in iPython (with good reason)
mixed with the want to share/run code at python meetings (dojos).

Pronounced doe-joe-vee-all.
"""


setup(
  name= "Dojovial",
  version= "0.0.1",
  author= "Andrew Kubera",
  license= "Apache v2.0",
  url= "https://github.com/akubera/dojovial",
  author_email= "andrew.kubera@gmail.com",
  description= "Growler application for collaborative python.",
  long_description= long_description,
  classifiers= [
    "Development Status :: 2 - Pre-Alpha",
    # "Framework :: Growler",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Internet :: WWW/HTTP",
    "Natural Language :: English"
  ],
  install_requires = install_requires,
  packages= find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)

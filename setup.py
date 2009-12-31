#!/usr/bin/env python
# -*- coding: latin-1 -*-
#
# Copyright (c) 2007 Thomas Lotze
# See also LICENSE.txt

"""Access to Google page ranks similar to what the Google toolbar does.

It contains a Python package, tl.googlepagerank, and a command line tool,
googlepagerank, exercising the package's functionality. The script takes a
number of URLs as parameters and prints their page ranks to standard output.
"""

import os, os.path
from setuptools import setup, find_packages

desc, longdesc = __doc__.split("\n\n", 1)

scripts = [
    "bin/googlepagerank",
    ]

data_files = [
    ("share/doc/tl.googlepagerank", [
        "LICENSE.txt",
        "COPYRIGHT.txt",
        "README.txt",
        ]),
    ]

provides = [
    "tl.googlepagerank",
    ]

setup(name="tl.googlepagerank",
      version="trunk",
      description=desc,
      long_description=longdesc,
      author="Thomas Lotze",
      author_email="thomas@thomas-lotze.de",
      url="http://www.thomas-lotze.de/en/software/",
      license="ZPL 2.1",
      packages=find_packages(),
      include_package_data=True,
      scripts=scripts,
      data_files=data_files,
      provides=provides,
      namespace_packages=["tl"],
      )

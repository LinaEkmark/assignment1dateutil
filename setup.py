#!/usr/bin/python
from os.path import isfile
import os

from setuptools import setup

from dateutil._version import VERSION

if isfile("MANIFEST"):
    os.unlink("MANIFEST")

setup(name="python-dateutil",
      version=VERSION,
      description="Extensions to the standard Python datetime module",
      author="Paul Ganssle",
      author_email="dateutil@python.org",
      url="https://dateutil.readthedocs.io",
      license="BSD 3-Clause",
      long_description="""
The dateutil module provides powerful extensions to the
datetime module available in the Python standard library.
""",
      packages=["dateutil", "dateutil.zoneinfo", "dateutil.tz"],
      package_data={"dateutil.zoneinfo": ["dateutil-zoneinfo.tar.gz"]},
      zip_safe=True,
      requires=["six"],
      install_requires=["six >=1.5"],  # XXX fix when packaging is sane again
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
      ],
      test_suite="dateutil.test"
      )

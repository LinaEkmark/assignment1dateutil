#!/usr/bin/env python
from os.path import isfile
import os

import setuptools
from setuptools import setup
from setuptools import Command

from distutils.version import LooseVersion
import warnings

import io
import sys

if isfile("MANIFEST"):
    os.unlink("MANIFEST")

if LooseVersion(setuptools.__version__) <= LooseVersion("24.3"):
    warnings.warn("python_requires requires setuptools version > 24.3",
                  UserWarning)


class Unsupported(Command):
    """Unsupported command class.
    """
    def run(self):
        """The overridden run method of the parent class.
        """
        sys.stderr.write("Running 'test' with setup.py is not supported. "
                         "Use 'pytest' or 'tox' to run the tests.\n")
        sys.exit(1)


###
# Load metadata

def readme():
    """Function to read and return the updated README.rst file.

    Returns:
        str: The modified contents of README.rst.
    """
    with io.open('README.rst', encoding='utf-8') as f:
        readme_lines = f.readlines()

    # The .. doctest directive is not supported by PyPA
    lines_out = []
    for line in readme_lines:
        if line.startswith('.. doctest'):
            lines_out.append('.. code-block:: python3\n')
        else:
            lines_out.append(line)

    return ''.join(lines_out)


README = readme()


setup(
      use_scm_version={
          'write_to': 'src/dateutil/_version.py',
      },
      # Needed since doctest not supported by PyPA.
      long_description=README,
      cmdclass={
          "test": Unsupported
      }
      )

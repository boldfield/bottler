"""
bottler
========

This is bottler, a private python package index built on Python-Flask.
It is responsible for authorizing downloads and proxying content from s3.
"""

from setuptools import setup, find_packages
import sys

py = sys.version_info[:2]

if py > (2, 7) or py < (2, 7):
    raise RuntimeError('Python 2.7 is required')


required = [
    'boto==2.6.0',
    'gunicorn==0.14.6',
    'flask==0.9',
]

meta = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers'
]

setup(name='bottler',
      version='0.1dev',
      description='The bottler private python package index',
      long_description=__doc__,
      keywords='website',
      author='Collin Watson',
      author_email='watson.collin@gmail.com',
      url='',
      license='PRIVATE',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      extras_require=dict(),
      install_requires=required,
      entry_points=dict(),
      scripts=[],
      classifiers=meta)

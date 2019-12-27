# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='osfile',
    version='1.2',
    description='module for file operation.',
    long_description='module for file operation.',
    author='Takeki Shikano',
    author_email='',
    url=None,
    license='MIT',
    packages=find_packages(exclude=('docs',))
)


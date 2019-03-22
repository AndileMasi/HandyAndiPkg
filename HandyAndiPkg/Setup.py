#!/usr/bin/env python
# coding: utf-8

# In[1]:


from setuptools import setup, find_packages

setup(
    name='HandyAndi',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Handy Andi is a python project that Andi created for school.',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/AndileMasi/HandyAndyPackage',
    author='Andile Skosana',
    author_email='msikamhlanga@gmail.com'
)


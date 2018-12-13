
#!/usr/bin/env python

"""
A simple setup file to point to the flask module
"""

from setuptools import find_packages, setup

setup(
    name='creative_calculations',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

#!/usr/bin/env python
from setuptools import find_packages
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

VERSION = '1.0.0'

setup_args = generate_distutils_setup(
    name='hyperion-ui',
    packages=find_packages(),

    version=VERSION,
    install_requires=[
        'urwid==2.0.1',
    ],

    description='User interfaces for the Hyperion Launch Engine',
    author='David Leins',
    author_email='dleins@techfak.uni-bielefeld.de',
    url='https://github.com/DavidPL1/hyperion-start/hyperion-ui.git',
    keywords=['hyperion'],
    classifiers=[],
    entry_points={
            'hyperion.user_interfaces': [
                'urwid = hyperion_user_interfaces.interactiveCLI',
                'pyqt = hyperion_user_interfaces.hyperGUI'
            ]
    }
)

setup(**setup_args)

#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = '1.0.0'

setup(
    name='hyperion-ui',
    packages=find_packages(),

    version=VERSION,
    install_requires=[
        'urwid',
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
    },
    include_package_data=True,
    zip_safe=False
)

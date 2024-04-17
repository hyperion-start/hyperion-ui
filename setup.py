#!/usr/bin/env python
IS_CATKIN = False

try:
    from catkin_pkg.python_setup import generate_distutils_setup
    import selectors
    from setuptools import setup, find_packages
    IS_CATKIN = True
except ImportError:
    from setuptools import setup, find_packages
    pass

VERSION = '1.0.0'

setup_args = dict(
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

if IS_CATKIN:
    setup_args = generate_distutils_setup(
        **setup_args
    )

setup(**setup_args)

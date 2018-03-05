"""aurman AUR dependency solver

see: https://github.com/polygamma/aurman
"""

from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aurmansolver',

    version='2.6',  # do not forget to change this

    description='Arch Linux AUR dependency solver',

    long_description=long_description,

    url='https://github.com/polygamma/aurman',

    author='Jonni Westphalen',

    author_email='jonny.westphalen@googlemail.com',

    packages=find_packages('src', exclude=['unit_tests']),
    package_dir={'': 'src'},

    entry_points={
        'console_scripts': [
            'aurmansolver=aurman.main_solver:main',
        ]
    },

    install_requires=['requests']
)
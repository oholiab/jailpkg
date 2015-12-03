from setuptools import find_packages
from setuptools import setup

setup(
        name='jailpkg',
        description='Script for managing packages in jails',
        version='0.1.0',
        platforms='freebsd',
        packages=find_packages(exclude=('tests*')),
        entry_points={
            'console_scripts': [
                'jailpkg = jailpkg:main',
            ],
        },
)

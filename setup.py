"""Setup for JSH"""

from setuptools import setup
from platform import system
from jsh.version import __VERSION__

setup(
    name='jsh',
    version=__VERSION__,
    description='Junos-like shell library for Python',
    author='InfDev',
    author_email='infdev@ocado.com',
    packages=['jsh'],
    install_requires=['readline'] if system() == 'Darwin' else [],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

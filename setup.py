from setuptools import setup, find_packages
import sys
import os

wd = os.path.dirname(os.path.abspath(__file__))
os.chdir(wd)
sys.path.insert(1, wd)

name = 'slack_kanbanize_formatter_plugin'
pkg = __import__('slack_kanbanize_formatter_plugin')

author, email = pkg.__author__.rsplit(' ', 1)
email = email.strip('<>')

version = pkg.__version__
classifiers = pkg.__classifiers__

readme = open(os.path.join(wd, 'README.md'),'r').readlines()
description = readme[1]
long_description = ''.join(readme)

try:
    reqs = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read()
except (IOError, OSError):
    reqs = ''

setup(
    name=name,
    version=version,
    author=author,
    author_email=email,
    url='https://github.com/mportela/slack_kanbanize_formatter_plugin',
    maintainer=author,
    maintainer_email=email,
    description=description,
    long_description=long_description,
    classifiers=classifiers,
    install_requires = reqs,
    package_dir={'': 'slack_kanbanize_formatter_plugin'},
    packages=[''] + find_packages('slack_kanbanize_formatter_plugin'),
    license = 'GNU GPL V2',
    keywords ='formatter plugin to be used to extend slack notificator from kanbanize, https://github.com/mportela/slack_kanbanize',
    zip_safe=False
)

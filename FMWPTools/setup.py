import py2exe
import sys

from distutils.core import setup

setup(
    options = {'py2exe': {
        'bundle_files': 1,
        'compressed': True,
        "includes" : ['sip','fmwp_mainwindow']
    }},
    windows = [{'script': 'FMWPModel.py'}],
    zipfile = None
)

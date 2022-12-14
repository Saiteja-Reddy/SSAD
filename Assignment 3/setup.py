"""Writing Setup.py for TOX"""
from distutils.core import setup

from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    """PyTest Class"""
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)

setup(
    #...,
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    )

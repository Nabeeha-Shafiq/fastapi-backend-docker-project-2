# common/setup.py
from setuptools import setup, find_packages

setup(
    name='common', # The name of your common package
    version='0.1.0',
    packages=find_packages(), # This will find the 'config' package inside 'common'
    # If you added any install_requires, make sure they are within the list and correctly formatted.
    # Example: install_requires=['some-package'],
)
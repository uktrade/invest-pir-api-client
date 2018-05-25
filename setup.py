"""
Export Directory API client
"""
import ast
import pip.download
from pip.req import parse_requirements
import re
from setuptools import setup, find_packages


def get_requirements():
    return [str(r.req) for r in list(parse_requirements(
        'requirements.txt',
        session=pip.download.PipSession()
    ))]


setup(
    name='pir_client',
    version="0.0.1",
    license='MIT',
    author='Department for International Trade',
    description='API client for PIR',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements()
)

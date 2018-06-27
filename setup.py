"""
Invest PIR API client
"""
from setuptools import setup, find_packages


setup(
    name='pir_client',
    version="0.0.1",
    license='MIT',
    author='Department for International Trade',
    description='API client for PIR',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['directory-client-core'],
    test_suite='nose.collector',
    tests_require=['nose', 'httpretty'],
)

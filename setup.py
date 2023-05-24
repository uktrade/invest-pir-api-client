"""
Invest PIR API client
"""
from setuptools import setup, find_packages


setup(
    name='pir_client',
    version='1.2.0',
    url='https://github.com/uktrade/invest-pir-api-client',
    license='MIT',
    author='Department for International Trade',
    description='API client for PIR',
    packages=find_packages(),
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'directory_client_core>=6.1.0,<=7.2.2',
    ],
    extras_require={
        'test': [
            'pytest==5.4.0',
            'pytest-codecov',
            'pytest-cov',
            'GitPython',
            'pytest-sugar==0.9.5',
            'flake8==5.0.4',
            'requests_mock==1.1.0',
            'twine',
            'wheel>=0.31.0,<1.0.0',
            'setuptools',
            'httpretty'
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 4.2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

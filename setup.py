"""
Invest PIR API client
"""
from setuptools import setup, find_packages


setup(
    name='pir_client',
    version='1.1.0',
    url='https://github.com/uktrade/invest-pir-api-client',
    license='MIT',
    author='Department for International Trade',
    description='API client for PIR',
    packages=find_packages(),
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'directory_client_core>=6.1.0,<7.0.0',
    ],
    extras_require={
        'test': [
            'pytest==3.0.2',
            'pytest-cov==2.3.1',
            'pytest-sugar==0.8.0',
            'flake8==3.0.4',
            'requests_mock==1.1.0',
            'codecov==2.0.16',
            'twine>=1.11.0,<2.0.0',
            'wheel>=0.31.0,<1.0.0',
            'setuptools>=38.6.0,<39.0.0',
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
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

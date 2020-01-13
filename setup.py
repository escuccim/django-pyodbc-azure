try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: BSD License',
    'Framework :: Django',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Internet :: WWW/HTTP',
]

setup(
    name='django-pyodbc-azure-2019',
    version='2.1.0.0',
    description='Django backend for Microsoft SQL Server and Azure SQL Database using pyodbc, compatible with SQL Server 2019',
    long_description=open('README.rst').read(),
    author='Michiya Takahashi, updated by Eric A Scuccimarra (skooch@gmail.com)',
    author_email='michiya.takahashi@gmail.com',
    url='https://github.com/escuccim/django-pyodbc-azure',
    license='BSD',
    packages=['sql_server', 'sql_server.pyodbc'],
    install_requires=[
        'Django>=2.1.0',
        'pyodbc>=3.0',
    ],
    classifiers=CLASSIFIERS,
    keywords='azure django',
)

django-teradata
===============

.. image:: https://secure.travis-ci.org/kpn-digital/django-teradata.svg?branch=master
    :target:  http://travis-ci.org/kpn-digital/django-teradata?branch=master

.. image:: https://img.shields.io/codecov/c/github/kpn-digital/django-teradata/master.svg
    :target: http://codecov.io/github/kpn-digital/django-teradata?branch=master

.. image:: https://img.shields.io/pypi/v/django-teradata.svg
    :target: https://pypi.python.org/pypi/django-teradata

.. image:: https://readthedocs.org/projects/django-teradata/badge/?version=latest
    :target: http://django-teradata.readthedocs.org/en/latest/?badge=latest

Features
--------

WIP

Installation
------------

.. code-block:: bash

    $ pip install django-teradata

Usage
-----

Add to your `settings.py` file.

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django_teradata',
            'AUTOCOMMIT': False,
            'NAME': 'database_name',
            'USER': 'database_user',
            'PASSWORD': 'database_password',
            'HOST': 'database_host',
            'APP_NAME': 'teradata_app_name',
            'LOG_CONSOLE': False,
            'DEFAULT_VERSION': '1.0',
            'CONNECTION_TYPE': 'odbc',
            'ODBC_LIB_PATH': 'path_to_odbc_library',
            'CHARSET': 'UTF8',
        }
    }

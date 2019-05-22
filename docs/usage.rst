========
Usage
========

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

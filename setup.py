
from setuptools import setup
setup(**{'author': 'KPN Digital Team',
 'author_email': 'gustavo.cunha@kpn.com',
 'classifiers': ['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Internet :: WWW/HTTP'],
 'description': 'Django Teradata Engine',
 'include_package_data': True,
 'install_requires': ['django<2', 'teradata'],
 'long_description': 'django-teradata\n'
                     '===============\n'
                     '\n'
                     '.. image:: '
                     'https://secure.travis-ci.org/kpn-digital/django-teradata.svg?branch=master\n'
                     '    :target:  '
                     'http://travis-ci.org/kpn-digital/django-teradata?branch=master\n'
                     '\n'
                     '.. image:: '
                     'https://img.shields.io/codecov/c/github/kpn-digital/django-teradata/master.svg\n'
                     '    :target: '
                     'http://codecov.io/github/kpn-digital/django-teradata?branch=master\n'
                     '\n'
                     '.. image:: '
                     'https://img.shields.io/pypi/v/django-teradata.svg\n'
                     '    :target: '
                     'https://pypi.python.org/pypi/django-teradata\n'
                     '\n'
                     '.. image:: '
                     'https://readthedocs.org/projects/django-teradata/badge/?version=latest\n'
                     '    :target: '
                     'http://django-teradata.readthedocs.org/en/latest/?badge=latest\n'
                     '\n'
                     'Features\n'
                     '--------\n'
                     '\n'
                     'WIP\n'
                     '\n'
                     'Installation\n'
                     '------------\n'
                     '\n'
                     '.. code-block:: bash\n'
                     '\n'
                     '    $ pip install django-teradata\n'
                     '\n'
                     'Usage\n'
                     '-----\n'
                     '\n'
                     'Add to your `settings.py` file.\n'
                     '\n'
                     '.. code-block:: python\n'
                     '\n'
                     '    DATABASES = {\n'
                     "        'default': {\n"
                     "            'ENGINE': 'de.db.teradata',\n"
                     "            'AUTOCOMMIT': False,\n"
                     "            'NAME': 'database_name',\n"
                     "            'USER': 'database_user',\n"
                     "            'PASSWORD': 'database_password',\n"
                     "            'HOST': 'database_host',\n"
                     "            'APP_NAME': 'teradata_app_name',\n"
                     "            'LOG_CONSOLE': False,\n"
                     "            'DEFAULT_VERSION': '1.0',\n"
                     "            'CONNECTION_TYPE': 'odbc',\n"
                     "            'ODBC_LIB_PATH': 'path_to_odbc_library',\n"
                     '        }\n'
                     '    }\n',
 'name': 'django-teradata',
 'packages': ['de', 'de.db', 'de.db.teradata'],
 'tests_require': ['tox'],
 'url': 'https://github.com/kpn-digital/django-teradata',
 'version': None,
 'zip_safe': False})

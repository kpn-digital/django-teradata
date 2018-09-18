# -*- coding: utf-8 -*-

import django
from django.conf import global_settings, settings

settings.configure(
    # Minimal django settings
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'unittest.sqlite',
            # 'TEST_NAME': ':memory:',
        },
    },
    MIDDLEWARE_CLASSES=global_settings.MIDDLEWARE_CLASSES,
    ROOT_URLCONF=None,
    INSTALLED_APPS=['de.db.teradata'],
)
if hasattr(django, 'setup'):
    django.setup()

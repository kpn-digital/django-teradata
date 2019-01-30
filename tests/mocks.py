# -*- coding: utf-8 -*-


class UdaExecConnectionMock:
    def __init__(self, side_effect_commit=None, side_effect_execute=None):
        self.settings_dict = {
            'ENGINE': 'django_teradata',
            'AUTOCOMMIT': False,
            'NAME': 'database',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'APP_NAME': 'teradata',
            'LOG_CONSOLE': False,
            'DEFAULT_VERSION': '',
            'CONNECTION_TYPE': 'odbc',
            'ODBC_LIB_PATH': '',
            'CHARSET': 'UTF8',
        }
        self.side_effect_commit = side_effect_commit
        self.side_effect_execute = side_effect_execute
        self.executed_statements = []
        self.connect_called_count = 0

    def connect(self, externalDSN=None, dataTypeConverter=None, **kwargs):
        self.connect_called_count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

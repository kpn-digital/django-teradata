# -*- coding: utf-8 -*-

from unittest import skip

import mock
from django.db import connection
from django.db.backends.utils import CursorWrapper
from django.test import TestCase
from django_teradata.base import DatabaseWrapper
from tests.mocks import UdaExecConnectionMock


class TestsDatabaseWrapper(TestCase):
    def setUp(self):
        settings_dict = self.settings_dict()
        self.database = DatabaseWrapper(settings_dict)
        self.database.connection = connection

    def settings_dict(self):
        return {
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

    def test_set_autocommit(self):
        self.database._set_autocommit(True)
        assert self.database.connection.autocommit is True

    @skip('method is empty')
    def test_init_connection_state(self):
        pass

    @skip('method is empty')
    def test_get_connection_params(self):
        pass

    def test_create_cursor(self):
        cursor = self.database.create_cursor()
        assert isinstance(cursor, CursorWrapper) is True

    def test_get_new_connection(self):
        with mock.patch('django_teradata.base.Database.UdaExec') as uda_exec_mock:
            connection_mock = UdaExecConnectionMock()
            uda_exec_mock.return_value = connection_mock
            self.database.get_new_connection({})
        assert connection_mock.connect_called_count == 1

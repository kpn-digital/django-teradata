# -*- coding: utf-8 -*-

from django.db.backends.base.base import BaseDatabaseWrapper
from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection

import teradata as Database

from .operations import DatabaseOperations


class DatabaseWrapper(BaseDatabaseWrapper):
    Database = Database
    # Classes instantiated in __init__().
    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations

    # TODO: update to have all possible SQL operators. Currently only supporting exact matching
    # Operators sample can be found in
    # https://github.com/django/django/blob/1.11.13/django/db/backends/sqlite3/base.py#L123
    operators = {
        'exact': '= %s',
        'gte': '>= %s',
    }

    def _set_autocommit(self, autocommit):
        self.connection.autocommit = autocommit

    def init_connection_state(self):
        pass

    def get_connection_params(self):
        pass

    def create_cursor(self, name=None):
        return self.connection.cursor()

    def get_new_connection(self, conn_params):
        settings_dict = self.settings_dict
        uda_exec = Database.UdaExec(appName=settings_dict['APP_NAME'],
                                    logConsole=settings_dict['LOG_CONSOLE'],
                                    version=settings_dict['DEFAULT_VERSION'],
                                    odbcLibPath=settings_dict['ODBC_LIB_PATH'])

        return uda_exec.connect(autoCommit=settings_dict['AUTOCOMMIT'],
                                method=settings_dict['CONNECTION_TYPE'],
                                database=settings_dict['NAME'],
                                username=settings_dict['USER'],
                                password=settings_dict['PASSWORD'],
                                DBCName=settings_dict['HOST'],
                                charset=settings_dict['CHARSET'])

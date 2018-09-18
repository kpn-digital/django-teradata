# -*- coding: utf-8 -*-

from de.db.teradata.operations import DatabaseOperations
from django.db import connection
from django.test import TestCase


class TestsDatabaseOperations(TestCase):
    def test_quoted_name(self):
        # '%' chars are escaped for query execution.
        ops = DatabaseOperations(connection)
        name = '"SOME%NAME"'
        expected = '"SOME%NAME"'
        quoted_name = ops.quote_name(name)
        assert quoted_name == expected

    def test_unquote_name(self):
        ops = DatabaseOperations(connection)
        name = "SOME%NAME"
        expected = '"SOME%NAME"'
        quoted_name = ops.quote_name(name)
        assert quoted_name == expected

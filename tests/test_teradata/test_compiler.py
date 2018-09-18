# -*- coding: utf-8 -*-

from de.db.teradata.compiler import SQLCompiler
from django.db import connection
from django.db.models.sql.query import Query
from django.test import TestCase
from tests.models import OrderedSampleModel, SampleModel


class TestsSQLCompiler(TestCase):
    def setUp(self):
        model = OrderedSampleModel()
        self._set_compiler(model)

    def _set_compiler(self, model):
        query = Query(model=model)
        using = {}
        self.compiler = SQLCompiler(query, connection, using)

    def _set_pagination_marks(self):
        self.compiler.query.high_mark = 10
        self.compiler.query.low_mark = None

    def test_as_sql_with_range_and_order(self):
        self._set_pagination_marks()
        sql, params = self.compiler.as_sql(with_limits=True)
        assert ('BETWEEN 1 AND 10' in sql) is True
        assert params == ()

    def test_as_sql_with_range_and_without_order(self):
        model = SampleModel()
        self._set_compiler(model)
        self._set_pagination_marks()
        sql, params = self.compiler.as_sql(with_limits=True)
        assert ('BETWEEN 1 AND 10' in sql) is True
        assert params == ()

    def test_as_sql_without_range(self):
        sql, params = self.compiler.as_sql(with_limits=True)
        assert ('BETWEEN 1 AND 10' in sql) is False
        assert params == ()

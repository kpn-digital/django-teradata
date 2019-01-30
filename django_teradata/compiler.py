# -*- coding: utf-8 -*-

from django.db.models.sql import compiler


class SQLCompiler(compiler.SQLCompiler):
    def as_sql(self, with_limits=True, with_col_aliases=False):
        sql, params = super(SQLCompiler, self).as_sql(with_limits=False, with_col_aliases=with_col_aliases)
        do_offset = with_limits and (self.query.high_mark is not None or self.query.low_mark)
        order_by = self.get_order_by()
        ranking = []
        if order_by:
            for _, (o_sql, _, _) in order_by:
                ranking.append(o_sql)
        else:
            ranking.append(self.query.model._meta.pk.attname)

        if do_offset:
            low_mark = self.query.low_mark
            high_mark = self.query.high_mark
            if low_mark is None:
                low_mark = 1
            limit_query = ' QUALIFY RANK(%s) BETWEEN %s AND %s;' % (', '.join(ranking), low_mark, high_mark)
            sql = sql + limit_query

        # Teradata package is expecting question marks instead of %s to prepare SQL
        sql = sql.replace('%s', '?')
        return sql, params


class SQLInsertCompiler(compiler.SQLInsertCompiler, SQLCompiler):
    pass


class SQLDeleteCompiler(compiler.SQLDeleteCompiler, SQLCompiler):
    pass


class SQLUpdateCompiler(compiler.SQLUpdateCompiler, SQLCompiler):
    pass


class SQLAggregateCompiler(compiler.SQLAggregateCompiler, SQLCompiler):
    pass

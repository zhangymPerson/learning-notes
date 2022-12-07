#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@file : py_pgsql.py
@desc : 脚本运行方式 [python3 py_pgsql.py]
        脚本说明: python操作 pgsql
@date : 2022-10-13 17:45:20
@auth : danao
@version : 1.0
"""

import psycopg2
import psycopg2.extras


class DB():
    """
    类的作用是:
        构造一个连接

    Attributes:
        params: type
    """

    def __init__(self, host='localhost', port="5432", db_name='', user='root', passwd='root'):
        # 建立连接
        self.conn = psycopg2.connect(
            database=db_name, user=user, password=passwd, host=host, port=port)
        # 创建游标，操作设置为字典类型 pgsql 的指定方式  其中 psycopg2.extras 需要单独 import
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


def exec_sql(db_conn, table_name):
    """
    查数据 获取当前库下的表
    """
    # 游标执行返回的是数量
    sql = """
    select
        c.relname 表名,
        cast(obj_description(relfilenode, 'pg_class') as varchar) 名称,
        a.attname 字段,
        d.description 字段备注,
        concat_ws('', t.typname, SUBSTRING(format_type(a.atttypid, a.atttypmod) from '\(.*\)')) as 列类型
    from
        pg_class c,
        pg_attribute a,
        pg_type t,
        pg_description d
    where
        a.attnum>0
        and
        a.attrelid = c.oid
        and
        a.atttypid = t.oid
        and
        d.objoid = a.attrelid
        and
        d.objsubid = a.attnum
        and
        c.relname in (
            select
            tablename
            from
            pg_tables
            where
            schemaname = 'public'
            and
                position('_2' in tablename)= 0
            and
                tablename = '%s'
        )
    order by
        c.relname,
        a.attnum;
    """
    db_conn.execute(sql % (table_name))
    # 获取数据库名
    # 需要调用 fetchall() 函数获取结果
    results = db_conn.fetchall()
    if len(results) < 1:
        return
    print(f"- **{table_name} - {results[0][1]}**")
    print("")
    print(f"  |字段名|字段类型|字段备注|")
    print(f"  |---|---|---|")
    for row in results:
        print(f"  |{row[2]}|{row[4]}|{row[3]}|")
    print("")


def get_all_table(db_conn):
    sql = """
    select
        tablename
    from
        pg_tables
    where
        schemaname = 'public'
        and
            position('_2' in tablename)= 0
    """
    db_conn.execute(sql)
    # 获取数据库名
    # 需要调用 fetchall() 函数获取结果
    results = db_conn.fetchall()
    list = []
    for row in results:
        # print(f"row = [{row}]")
        list.append(row[0])
    return list


def main():
    """
    主要是处理
    """
    print("hello world!")
    db_name = "pgsql"
    with DB(host='127.0.0.1', user='root', passwd='123456', db_name=db_name) as db_conn:
        # 获取所有表名
        tables = get_all_table(db_conn=db_conn)
        for table in tables:
            # print(f"table = [{table}]")
            exec_sql(db_conn=db_conn, table_name=table)


if __name__ == "__main__":
    main()

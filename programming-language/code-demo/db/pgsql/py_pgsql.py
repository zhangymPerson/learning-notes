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
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor()

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


def exec_sql(db_conn):
    """
    查数据 获取当前库下的表
    """
    # 游标执行返回的是数量
    db_conn.execute("select * from table_name;")
    # 获取数据库名
    print(db_conn.name)
    # 需要调用 fetchall() 函数获取结果
    results = db_conn.fetchall()
    for row in results:
        print("row=[%s]" % (str(row)))


def main():
    """
    主要是处理
    """
    print("hello world!")
    db_name = "pgsql"
    with DB(host='127.0.0.1', user='root', passwd='123456', db_name=db_name) as db_conn:
        # 获取所有表名
        exec_sql(db_conn=db_conn)


if __name__ == "__main__":
    main()

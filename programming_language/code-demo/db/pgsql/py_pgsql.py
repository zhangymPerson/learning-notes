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
import logging
# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s-%(name)s][%(filename)s:%(lineno)d][%(funcName)s][%(levelname)s]%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


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
        self._cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def __enter__(self):
        # 返回
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self._cur.close()
        # 关闭数据库连接
        self.conn.close()

    def get_conn(self):
        """函数的作用是: 获取数据库连接，删除等操作需要手动提交时使用
        Args:
            params:type
        Returns:
            return res
        Raises:
            列出与接口有关的所有异常.
        """
        return self.conn

    def get_cur(self):
        """函数的作用是: 获取操作数据库的游标
        Args:
            params:type
        Returns:
            return res
        Raises:
            列出与接口有关的所有异常.
        """
        return self._cur


def create_table(cur, table_name):
    try:
        sql = f"""
drop table IF EXISTS {table_name};
create TABLE {table_name}(
    id SERIAL NOT NULL,
    ip VARCHAR(25),
    time VARCHAR(255),
    method VARCHAR(25),
    url VARCHAR(255),
    ctime timestamp,
    mtime timestamp,
    request jsonb,
    response jsonb,
    exception TEXT,
    remark jsonb,
    other jsonb,
    other_msg TEXT,
    PRIMARY KEY (id)
);
comment on table {table_name} is '系统记录表';
comment on column {table_name}.ip is '请求 ip';
comment on column {table_name}.time is '耗时';
comment on column {table_name}.method is '请求方式';
comment on column {table_name}.url is '请求路由';
comment on column {table_name}.ctime is '创建时间';
comment on column {table_name}.request is '请求参数';
comment on column {table_name}.response is '返回参数';
comment on column {table_name}.exception is '异常信息';
comment on column {table_name}.remark is '备注信息';
comment on column {table_name}.other is '其他扩展';
comment on column {table_name}.other_msg is '其他扩展字符串';
        """
        cur.execute(sql)
        logging.info(f"建表[{table_name}]成功")
    except Exception as e:
        logging.info(f"处理异常,e = [{e}]")


def exec_sql(cur, table_name):
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
    cur.execute(sql % (table_name))
    # 获取数据库名
    # 需要调用 fetchall() 函数获取结果
    results = cur.fetchall()
    if len(results) < 1:
        return
    print(f"- **{table_name} - {results[0][1]}**")
    print("")
    print(f"  |字段名|字段类型|字段备注|")
    print(f"  |---|---|---|")
    for row in results:
        print(f"  |{row[2]}|{row[4]}|{row[3]}|")
    print("")


def get_all_table(cur):
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
    cur.execute(sql)
    # 获取数据库名
    # 需要调用 fetchall() 函数获取结果
    results = cur.fetchall()
    list = []
    for row in results:
        # print(f"row = [{row}]")
        list.append(row[0])
    return list


def clear_table(table_name, cur):
    sql = f"delete from {table_name};"
    try:
        cur.execute(sql)
        logging.info(f"删除表[{table_name}]中数据成功")
    except Exception as e:
        logging.info(f"处理异常,e = [{e}]")


def main():
    """
    主要是处理
    """
    print("hello world!")
    db_name = "db_name"
    table_name = "test"
    with DB(host='127.0.0.1', user='user', passwd='123456', db_name=db_name) as db:
        cur = db.get_cur()
        create_table(cur, table_name)
        # 获取所有表名
        # tables = get_all_table(cur=cur)
        exec_sql(cur=cur, table_name=table_name)
        clear_table(table_name, cur)


if __name__ == "__main__":
    main()

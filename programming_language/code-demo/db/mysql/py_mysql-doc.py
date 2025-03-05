#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@file : py_mysql-doc.py
@desc : 脚本运行方式 [python3 py_mysql-doc.py -h]
        脚本说明:获取数据库指定表的表结构文档
@date : 2022-08-03 14:34:43
@auth : danao
@version : 1.1
@update : 2024-09-04 
"""

import argparse
import datetime
import json
import os
import traceback

import pymysql


class DB():
    """
    类的作用是:
        连接数据库

    Attributes:
        params: type
    """

    def __init__(self, host='localhost', port=3306, db='',
                 user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(
            host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

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


def get_mysql_version(db):
    db.execute("SELECT VERSION()")
    rows = db.fetchall()
    for row in rows:
        return row.get('VERSION()')


def get_all_table_from_db(db, db_name):
    """
    查数据 获取当前库下的表
    """
    # 游标执行返回的是数量
    sql = f"""
    SELECT
        TABLE_NAME AS table_name,
        TABLE_COMMENT AS table_comment
    FROM
        information_schema.TABLES
    WHERE
        TABLE_SCHEMA = '{db_name}'
    ORDER BY
        TABLE_NAME;
    """
    db.execute(sql)
    # 需要调用 fetchall() 函数获取结果
    results = db.fetchall()
    return results


def get_create_table_sql(db, table_name=None):
    """获取单个表的建表语句
    Args:
        params:db 数据库连接对象
               db_name 库名
               table_name 表名
    Returns:
        return res
    Raises:
        列出与接口有关的所有异常.
    """
    sql = "show create table %s" % (table_name)
    db.execute(sql)
    # 需要调用 fetchall() 函数获取结果
    results = db.fetchall()
    res = ""
    createTableSql = ""
    for row in results:
        # print(row.get('Table'))
        createTableSql = row.get('Create Table')
    strs = createTableSql.split("\n")
    for line in strs:
        res = res + "%s\n" % (line)
    return res


def get_table_info(db, db_name, table_name):
    """
    获取单个表的所有字段信息
    """
    sqlStr = """
SELECT
    TABLE_SCHEMA AS '库名',
    TABLE_NAME AS '表名',
    COLUMN_NAME AS '列名',
    ORDINAL_POSITION AS '列的排列顺序',
    COLUMN_DEFAULT AS '默认值',
    IS_NULLABLE AS '是否为空',
    DATA_TYPE AS '数据类型',
    CHARACTER_MAXIMUM_LENGTH AS '字符最大长度',
    NUMERIC_PRECISION AS '数值精度(最大位数)',
    NUMERIC_SCALE AS '小数精度',
    COLUMN_TYPE AS 列类型,
    COLUMN_KEY 'KEY',
    EXTRA AS '额外说明',
    COLUMN_COMMENT AS '注释'
FROM
    information_schema.`COLUMNS`
WHERE
    TABLE_SCHEMA = '%s'
    and TABLE_NAME = '%s'
ORDER BY
    TABLE_NAME,
    ORDINAL_POSITION;
    """

    sql = sqlStr % (db_name, table_name)
    # print(sql)
    db.execute(sql)
    rows = db.fetchall()
    # for row in rows:
    #     print(row, end='')
    # print()
    # [{'库名': 'test', '表名': 'user', '列名': 'username', '列的排列顺序': 1, '默认值': None, '是否为空': 'NO', '数据类型': 'char', '字符最大长度': 20, '数值精度(最大位数)': None, '小数精度': None, '列类型': 'char(20)', 'KEY': '', '额外说明': '', '注释': ''}]
    return rows


def get_doc_from_row(rows):
    """
    根据查询到的字段信息生成表的 markdown 文档
    返回文档数据
    """
    doc_tpl = """
| 序号 | 字段名      | 数据类型            | 非空 | 键类型   | 默认值 | 注释                     |
| ---- | ----------- | ------------------- | ---- | -------- | ------ | ------------------------ |
"""
    num = 1
    for row in rows:
        rowStr = "|%s|%s|%s|%s|%s|%s|%s|\n" % (num, row.get('列名'), row.get(
            '数据类型'), row.get('是否为空'), row.get('KEY'), row.get('默认值'), row.get('注释'))
        doc_tpl = doc_tpl + rowStr
        num = num + 1
    # print(doc_tpl)
    return doc_tpl


def get_insert_into_sql(table_name, rows):
    """
    获取sql insert into 模板语句
    """
    columnNames = []
    values = []
    for row in rows:
        columnNames.append(row.get('列名'))
        values.append(row.get('数据类型'))
    sql = "insert into %s (%s) values (%s)" % (table_name, columnNames, values)
    # print(sql)
    return sql


def all_table(db, db_name):
    """
    获取所有表的介绍和文档
    Args:
        params: db_name 数据库名
    Returns:
        return res
    Raises:
        列出与接口有关的所有异常.
    """
    doc_version = '0.0.1'
    author = 'danao'
    version = get_mysql_version(db)
    print(f"""
# 数据库 **{db_name}** 说明文档

- 文档创建日期: {datetime.datetime.now().strftime('%Y-%m-%d')}

- 数据库版本: {version}

- 文档版本号: {doc_version}

- 文档编写者: {author}

## 目录

|编号|表名|备注|
|----|----|----|""")
    # 获取所有表名
    results = get_all_table_from_db(db=db, db_name=db_name)
    i = 1
    tables = {}
    for row in results:
        tables[row.get('table_name')] = row.get('table_comment')
        # 去掉换行符
        name = row.get('table_name').replace("\r\n", "\n").replace("\n", "")
        comment = row.get('table_comment').replace(
            "\r\n", "\n").replace("\n", "")
        print(f"|{i}|[{name}](#{name})|{comment}|")
        i = i + 1
    print()
    print(f"## 单个表结构说明")
    # 获取表名创建文档
    for table_name in tables.keys():
        get_table(db, db_name, table_name)


def get_table(db, db_name, table_name):
    """获取单个表信息
    Args:
        params:db 数据库连接对象
               db_name 数据库名
               table_name 表名
    Returns:
        return res
    Raises:
        列出与接口有关的所有异常.
    """
    rows = get_table_info(db, db_name, table_name)
    doc = get_doc_from_row(rows)
    table_sql = get_create_table_sql(db, table_name)
    insert_sql = get_insert_into_sql(table_name, rows)
    doc_tpl = """
### %s

#### %s 表-结构说明

%s

#### %s 表-建表语句

```sql
%s
```

"""
    print(doc_tpl % (table_name, table_name, doc,
                     table_name, table_sql))


def run(conf_dict: dict):
    db_name = conf_dict.get('db_name')
    table_name = conf_dict.get('table_name')
    host = conf_dict.get("host")
    port = conf_dict.get("port")
    user = conf_dict.get("user")
    password = conf_dict.get("password")
    try:
        with DB(host=host, port=port, user=user, passwd=password, db=db_name) as db:
            if table_name == "test":
                all_table(db=db, db_name=db_name)
                # get_table(db, db_name, table_name)
            else:
                get_table(db, db_name, table_name)
    except Exception as e:
        print(e)
        error_info()
        # traceback.print_exc()


def init_args():
    argp = argparse.ArgumentParser(
        description=f"""
        获取mysql数据库表的一个说明文档,执行如下命令
        python {os.path.basename(__file__)} -ip 127.0.0.1 -P 3306 -u root -p 123456 -d db_name 
        """, epilog='结束')
    argp.add_argument("-ip", "--host", type=str, dest="host",
                      default="127.0.0.1", help="host")
    argp.add_argument("-P", "--port", type=int,
                      default=3306, dest="port", help="port")
    argp.add_argument("-u", "--user", type=str,
                      default="root", dest="user", help="user")
    argp.add_argument("-p", "--password", type=str,
                      default="123456", dest="password", help="password")
    argp.add_argument("-d", "--dbname", type=str,
                      dest="db_name", default="test", help="dbname")
    argp.add_argument("-t", "--table", type=str, default="test", dest="table_name",
                      help="table_name")
    parse_args = argp.parse_args()  # 返回一个命名空间,如果想要使用变量,可用args.attr

    return parse_args.__dict__


def error_info():
    current_script_path = os.path.abspath(__file__)
    command = f"python {current_script_path} -ip 127.0.0.1 -P 3306 -u root -p 123456 -d db_name"
    print(f"start command = [{command}]")


if __name__ == '__main__':
    args = init_args()
    jsons = json.dumps(args, ensure_ascii=False, default=str, indent=2)
    # print(jsons)
    run(args)

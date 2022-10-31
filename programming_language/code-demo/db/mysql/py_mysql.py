#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@file : py-mysql.py
@desc : 脚本运行方式 [python3 py-mysql.py]
        脚本说明: 数据库相关常用脚本
@date : 2022-03-22 20:38:38
@author : danao
@version : 1.0
'''

# 需要安装
# pip install pymssql
import pymysql


def is_empty(obj):
    """
    判断字符串为空
    None , '' ,'  ' 都是空字符串
    """
    if obj is None:
        return True
    if not isinstance(obj, str):
        return False
    if len(obj.strip()) == 0:
        return True
    return False


class DB():
    """
    类的作用是:
        获取 mysql 连接
    Attributes:
        params: type
    """

    def __init__(self, host='localhost', port=3306, db_name='', user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(
            host=host, port=port, db=db_name, user=user, passwd=passwd, charset=charset)
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


def get_all_table_from_db(db_conn, db_name):
    """
    查数据 获取当前库下的表
    """
    # 游标执行返回的是数量
    db_conn.execute("show tables;")
    # 获取数据库名
    print(db_name)
    tables = []
    # 需要调用 fetchall() 函数获取结果
    results = db_conn.fetchall()
    for row in results:
        for table in row:
            tables.append(row.get(table))
    print("数据库[%s]中有[%s]张表,\n分别是%s" % (db_name, len(tables), tables))
    return tables


def get_create_table_sql(db_conn, dbname=None):
    """
    获取指定库中的所有表的建表语句
    """
    tables = []
    sql = "show tables;"
    db_conn.execute(sql)
    for rows in db_conn.fetchall():
        for key in rows:
            tables.append(rows.get(key))

    print("数据库[%s]中有[%s]张表,\n分别是%s" % (dbname, len(tables), tables))

    split_str = "==============================================================="
    for table_name in tables:
        sql = "show create table %s" % table_name
        db_conn.execute(sql)
        # 需要调用 fetchall() 函数获取结果
        results = db_conn.fetchall()
        for row in results:
            print(row.get('Table'))
            print(row.get('Create Table'))
            print(split_str)


def delete_table(table_name):
    """
    delete
    删除表
    """
    if not is_empty(table_name):
        # delete from tableName where id = 1
        # 可以添加清理条件
        sql = "delete from %s" % table_name
        db.execute(sql)
        print("清理表[%s]完成" % table_name)


def truncate_table(db_conn, table_name):
    """
    清空表 
    Args:
        params:tableName 表名
    Returns:
        return res
    Raises:
        列出与接口有关的所有异常.
        有外键约束时，需要 SET FOREIGN_KEY_CHECKS=0; 之后执行后在 SET FOREIGN_KEY_CHECKS=1
    """
    if not is_empty(table_name):
        sql = "truncate table %s" % table_name
        db_conn.execute(sql)
        print("清理表[%s]完成" % table_name)


def change_foreignkey_check(db_conn, status):
    """修改外键状态 
    解决有外键表不能 truncate 问题
    Args:
        params:status
    Returns:
        return res
    Raises:
        列出与接口有关的所有异常.
    """
    if status == 0 or status == 1:
        check_sql = "SELECT @@FOREIGN_KEY_CHECKS;"
        db_conn.execute(check_sql)
        # 需要调用 fetchall() 函数获取结果
        results = db_conn.fetchall()
        for row in results:
            print("修改前状态是%d" % row.get('@@FOREIGN_KEY_CHECKS'))
        sql = "SET FOREIGN_KEY_CHECKS=%d;" % status
        db_conn.execute(sql)
        db_conn.execute(check_sql)
        # 需要调用 fetchall() 函数获取结果
        results = db_conn.fetchall()
        for row in results:
            print("修改后状态是%d" % row.get('@@FOREIGN_KEY_CHECKS'))
    else:
        return


if __name__ == '__main__':
    db_name = "mysql"
    with DB(host='127.0.0.1', user='root', passwd='123456', db_name=db_name) as db:
        # 获取所有表名
        tables = get_all_table_from_db(db_conn=db, db_name=db_name)
        # 修改外键状态
        # changeForeignKeyCheck(db, 0)
        # 批量清理表
        # for tableName in tables:
        #     truncateTable(db, tableName=tableName)
        # 获取库中所有表的建表sql
        # getCreateTableSql(db=db, dbname=dbName)
        # deleteTable('user')

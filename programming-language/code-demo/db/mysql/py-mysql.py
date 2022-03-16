#!/usr/bin/python3

import pymysql


class DB():
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
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


def getAllTableFromDb(db, dbName):
    """
    查数据 获取当前库下的表
    """
    # 游标执行返回的是数量
    db.execute("show tables;")
    # 获取数据库名
    print(dbName)
    tables = []
    # 需要调用 fetchall() 函数获取结果
    results = db.fetchall()
    for row in results:
        for table in row:
            tables.append(row.get(table))
    print("数据库[%s]中有[%s]张表,\n分别是%s" % (dbName, len(tables), tables))
    return tables


def getCreateTableSql(db, dbname=None):
    """
    获取指定库中的所有表的建表语句
    """
    tables = []
    sql = "show tables;"
    db.execute(sql)
    for rows in db.fetchall():
        for key in rows:
            tables.append(rows.get(key))

    print("数据库[%s]中有[%s]张表,\n分别是%s" % (dbname, len(tables), tables))

    splitStr = "==============================================================="
    for tableName in tables:
        sql = "show create table %s" % (tableName)
        db.execute(sql)
        # 需要调用 fetchall() 函数获取结果
        results = db.fetchall()
        for row in results:
            print(row.get('Table'))
            print(row.get('Create Table'))
            print(splitStr)


if __name__ == '__main__':
    dbName = "test"
    with DB(host='127.0.0.1', user='root', passwd='123456', db=dbName) as db:
        # 获取所有表名
        getAllTableFromDb(db=db, dbName=dbName)
        # 获取库中所有表的建表sql
        getCreateTableSql(db=db, dbname=dbName)

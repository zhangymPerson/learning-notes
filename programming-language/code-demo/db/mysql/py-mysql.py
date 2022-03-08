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


def queryTest(db):
    """
    查数据
    """
    # 游标执行返回的是数量
    count = db.execute("select * from EMPLOYEE")
    print("count is %s" % (count))
    # 需要调用 fetchall() 函数获取结果
    results = db.fetchall()
    for row in results:
        print("row is %s" % (row))
    # 取值 row.get('id')


def getTable(db):
    """
    获取表结构
    """
    tableName = "EMPLOYEE"
    sql = "show create table %s" % (tableName)
    count = db.execute(sql)
    print("count is %s" % (count))
    # 需要调用 fetchall() 函数获取结果
    results = db.fetchall()
    for row in results:
        print("row is %s" % (row))


if __name__ == '__main__':
    with DB(host='127.0.0.1', user='root', passwd='123456', db='test') as db:
        queryTest(db=db)
        getTable(db=db)

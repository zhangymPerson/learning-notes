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


def getCreateTableSql(db, dbname=None, tableName=None):
    """获取单个表的建表语句 
    Args:
        params:db 数据库连接对象
               dbname 库名
               tableName 表名 
    Returns:
        return res
    Raises:
        列出与接口有关的所有异常.
    """
    sql = "show create table %s" % (tableName)
    db.execute(sql)
    # 需要调用 fetchall() 函数获取结果
    results = db.fetchall()
    res = ""
    for row in results:
        print(row.get('Table'))
        res = row.get('Create Table')
    return res


def getTableInfo(db, dbName, tableName):
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

    sql = sqlStr % (dbName, tableName)
    # print(sql)
    db.execute(sql)
    rows = db.fetchall()
    # for row in rows:
    #     print(row, end='')
    # print()
    # [{'库名': 'test', '表名': 'user', '列名': 'username', '列的排列顺序': 1, '默认值': None, '是否为空': 'NO', '数据类型': 'char', '字符最大长度': 20, '数值精度(最大位数)': None, '小数精度': None, '列类型': 'char(20)', 'KEY': '', '额外说明': '', '注释': ''}]
    return rows


def getDocFromRow(tableName, rows):
    """
    根据查询到的字段信息生成表的 markdown 文档
    返回文档数据
    """
    docTpl = """
- %s

    | 序号 | 字段名      | 数据类型            | 非空 | 键类型   | 默认值 | 注释                     |
    | ---- | ----------- | ------------------- | ---- | -------- | ------ | ------------------------ |
""" % (tableName)
    num = 1
    for row in rows:
        rowStr = "    |%s|%s|%s|%s|%s|%s|%s|\n" % (num, row.get('列名'), row.get(
            '数据类型'), row.get('是否为空'), row.get('KEY'), row.get('默认值'), row.get('注释'))
        docTpl = docTpl + rowStr
        num = num + 1
    # print(docTpl)
    return docTpl


def getInsertIntoSql(tableName, rows):
    """
    获取sql insert into 模板语句
    """
    columnNames = []
    values = []
    for row in rows:
        columnNames.append(row.get('列名'))
        values.append(row.get('数据类型'))
    sql = "insert into %s (%s) values (%s)" % (tableName, columnNames, values)
    # print(sql)
    return sql


def allTable(db, dbName):
    """
    获取所有表的介绍和文档 
    Args:
        params: dbname 数据库名
    Returns:
        return res
    Raises:
        列出与接口有关的所有异常.
    """
    # 获取所有表名
    tables = getAllTableFromDb(db=db, dbName=dbName)
    # 获取表名创建文档
    for tableName in tables:
        getTable(db, dbName, tableName)


def getTable(db, dbName, tableName):
    """获取单个表信息 
    Args:
        params:db 数据库连接对象
               dbName 数据库名
               tableName 表名
    Returns:
        return res
    Raises:
        列出与接口有关的所有异常.
    """
    rows = getTableInfo(db, dbName, tableName)
    doc = getDocFromRow(tableName, rows)
    tableSql = getCreateTableSql(db, dbName, tableName)
    insertSql = getInsertIntoSql(tableName, rows)
    docTpl = """
%s
```sql
%s
```
%s
    """
    print(docTpl % (doc, tableSql, insertSql))


if __name__ == '__main__':
    dbName = "test"
    tableName = "test"
    with DB(host='127.0.0.1', user='root', passwd='123456', db=dbName) as db:
        # allTable(db, dbName)
        getTable(db, dbName, tableName)

# 常用的 MySQL 特殊作用的 sql

- 查询物理文件位置

  `show global variables like "%datadir%";`

- mysql 服务器状态变量

- mysql 各个参数随着时间的变化的值的变化

  `mysqladmin -uroot -p extended-status -ri60`

- 查看 mysql 参数

- 查看数据库状态

  `show status;`

  `show status like '%table%';`

- 查看数据库参数配置情况

  `show variables;`

  `show global variables like 'sql_mode';`

- 查询配置文件参数

  `show variables like '%参数名%';`

- 导出到文件中

  `mysql -u user -p password -e "show variables;" > data`

- 查看 MySQL 服务进程情况

- 进程查看

  `show processlist;`

  `show full processlist;`

- 主节点查询

  `show master status; #从节点查询`

  `show slave status;`

- 数据库数据表数据量查询

  `select table_name,table_rows from information_schema.tables where TABLE_SCHEMA = '库名' order by table_rows desc;`

- 查看用户

  `desc mysql.user;`

  `select host,user from mysql.user;`

- 查看用户详细信息

  `select \* from mysql.user where user='用户名'\G;`

  `drop user test;`

- 查询制指定库中所有表的注释

  `SELECT table_name NAME, TABLE_COMMENT VALUE FROM INFORMATION_SCHEMA. TABLES WHERE table_type = 'base table' AND table_schema = 'boyi_data' ORDER BY table_name ASC;`

- 查询数据库中所有表的字段信息

  `select \* from information_schema.COLUMNS where table_schema = '库名';`

- 查询某个库所有表

  `select \* from information_schema.TABLES where table_schema = '数据库'`

- 查询所有表的注释和字段注释

  ```sql
  SELECT
      a.table_name 表名,
      a.table_comment 表说明,
      b.COLUMN_NAME 字段名,
      b.column_comment 字段说明,
      b.column_type 字段类型,
      b.column_key 约束
  FROM
      information_schema. TABLES a
  LEFT JOIN information_schema. COLUMNS b ON
      a.table_name = b.TABLE_NAME
  WHERE
      a.table_name LIKE '%user%'
  ORDER BY
      a.table_name
  ```

- 查询单个表的信息

- 查询所有表的注释和字段注释

  ```sql
  SELECT
      a.table_name 表名,
      a.table_comment 表说明,
      b.COLUMN_NAME 字段名,
      b.column_comment 字段说明,
      b.column_type 字段类型,
      b.column_key 约束
  FROM
      information_schema. TABLES a
  LEFT JOIN information_schema. COLUMNS b ON
      a.table_name = b.TABLE_NAME
  WHERE
      a.table_schema = '库名'
      and a.table_name = '表名'
  ORDER BY
      a.table_name
  ```

  ```sql
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
      TABLE_SCHEMA = '库名'
      and TABLE_NAME = '表名'
  ORDER BY
      TABLE_NAME,
      ORDINAL_POSITION;
  ```

- MySQL 获取表名 + 列名

  `select TABLE_NAME,GROUP_CONCAT(`COLUMN_NAME`) from information_schema.COLUMNS where table_schema = '库' GROUP BY TABLE_NAME;`

- 查看数据库表，列，列说明

  `select TABLE_NAME,GROUP_CONCAT(`COLUMN_NAME`),GROUP_CONCAT(`column_comment`) from information_schema.COLUMNS where table_schema = '库名' GROUP BY TABLE_NAME;`

- 跳过一个事务；

  `SET GLOBAL SQL_SLAVE_SKIP_COUNTER = 1`

- mysql 创建数据库语句

  `CREATE DATABASE IF NOT EXISTS dbname DEFAULT CHARSET utf8 COLLATE utf8_general_ci;`

- 创建编码格式为 utf8mb4

  `create database databasesName default character set utf8mb4 collate utf8mb4_unicode_ci;`

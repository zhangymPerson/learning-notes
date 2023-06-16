# PostgreSQL

## 基本说明

## 基本使用

- 登录

  `psql -h IP地址 -p 端口 -U 数据库名 `

  `psql -U user -d dbname -W 密码`

- 常用库 sql

  | 执行操作                   | sql                          | 备注            |
  | -------------------------- | ---------------------------- | --------------- |
  | 列举数据库：               | \l                           | show databases; |
  | 选择数据库：               | \c 数据库名                  | use databases   |
  | 查看该某个库中的所有表：   | \dt                          | show tables;    |
  | 切换数据库：               | \c interface                 |                 |
  | 查看某个库中的某个表结构： | \d 表名                      |                 |
  | 查看某个库中某个表的记录： | select \* from apps limit 1; |                 |
  | 显示字符集：               | \encoding                    |                 |
  | 退出 psgl：                | \q                           |                 |
  | 查询结果 行转列展示        | \x                           |                 |

- 查看单表信息

  ```sql
  SELECT
      a.attname as 字段名,
      format_type(a.atttypid,a.atttypmod) as 类型,
      a.attnotnull as 非空, col_description(a.attrelid,a.attnum) as 注释
  FROM
      pg_class as c,pg_attribute as a
  where
      a.attrelid = c.oid
      and
      a.attnum>0
      and
      c.relname = '你的表名';
  ```

- 查看带注释的表信息

  ```sql
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
      )
  order by
    c.relname,
    a.attnum;
  ```

- 删除库 需要先手动关闭连接

  `drop database databasename;`

  断开连接

  `select pg_terminate_backend(pid) from (select pid from pg_stat_activity where datname = 'databasename' ) a;`

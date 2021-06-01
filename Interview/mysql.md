# mysql

## 事务相关

- ACID 原则

- MVCC

  MVCC 是 Multi Version Concurrency Control 的简称，代表多版本并发控制。

## 存储引擎 innerdb

- 数据结构

## sql 优化

## 索引分类

### 从数据结构角度

- B+树索引

- hash 索引：

  a 仅仅能满足"=","IN"和"<=>"查询，不能使用范围查询

  b 其检索效率非常高，索引的检索可以一次定位，不像 B-Tree 索引需要从根节点到枝节点，最后才能访问到页节点这样多次的 IO 访问，所以 Hash 索引的查询效率要远高于 B-Tree 索引

  c 只有 Memory 存储引擎显示支持 hash 索引

- FULLTEXT 索引（现在 MyISAM 和 InnoDB 引擎都支持了）

- R-Tree 索引（用于对 GIS 数据类型创建 SPATIAL 索引）

### 从物理存储角度

- 聚簇索引（clustered index）

- 非聚簇索引（non-clustered index）

### 从逻辑角度

- 主键索引：主键索引是一种特殊的唯一索引，不允许有空值

- 普通索引或者单列索引

- 多列索引（复合索引）：复合索引指多个字段上创建的索引，只有在查询条件中使用了创建索引时的第一个字段，索引才会被使用。使用复合索引时遵循最左前缀集合

- 唯一索引或者非唯一索引

- 空间索引：空间索引是对空间数据类型的字段建立的索引，MYSQL 中的空间数据类型有 4 种，分别是 GEOMETRY、POINT、LINESTRING、POLYGON。 MYSQL 使用 SPATIAL 关键字进行扩展，使得能够用于创建正规索引类型的语法创建空间索引。创建空间索引的列，必须将其声明为 NOT NULL，空间索引只能在存储引擎为 MYISAM 的表中创建

### 索引失效问题

- 排查方法

  `explain` 预执行

- 最左匹配原则 like 联合索引

- 聚合函数

## 日志的作用

- undo log 数据回滚

- redo log 宕机 数据恢复

- big log 数据库主从

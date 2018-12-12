# 物理文件简单分析

- 查看物理文件位置
```sh
#sql 中的datadir 为物理文件所在位置
mysql> show global variables like '%dir%';
+-----------------------------------------+----------------------------+
| Variable_name                           | Value                      |
+-----------------------------------------+----------------------------+
| basedir                                 | /usr/                      |
| binlog_direct_non_transactional_updates | OFF                        |
| character_sets_dir                      | /usr/share/mysql/charsets/ |
| datadir                                 | /data/mysql/data/          |
| ignore_db_dirs                          |                            |
| innodb_data_home_dir                    |                            |
| innodb_log_group_home_dir               | ./                         |
| innodb_max_dirty_pages_pct              | 75.000000                  |
| innodb_max_dirty_pages_pct_lwm          | 0.000000                   |
| innodb_tmpdir                           |                            |
| innodb_undo_directory                   | ./                         |
| lc_messages_dir                         | /usr/share/mysql/          |
| plugin_dir                              | /usr/lib64/mysql/plugin/   |
| slave_load_tmpdir                       | /tmp                       |
| tmpdir                                  | /tmp                       |
+-----------------------------------------+----------------------------+
15 rows in set (0.00 sec)
```
 - 物理文件简单分析

 ```conf
#事务日志文件,是确保事务的REDO和UNDO，主要是确保事务的前滚和后滚，不是用来恢复用
ib_logfile0 
#事务日志文件,是确保事务的REDO和UNDO，不是用来恢复用
ib_logfile1
#临时表空间
ibtmp1
#记录mysql数据库实例的server_uuid，安装的时候初始化,master和slave的server_uuid不能一样
auto.cnf
# 主从之间的二进制文件
mysql-bin.001069

#在关闭MySQL时，会把内存中的热数据保存在磁盘里ib_buffer_pool文件中，位于数据目录下。
#在关闭时把热数据dump到本地磁盘。
innodb_buffer_pool_dump_at_shutdown = 1
#采用手工方式把热数据dump到本地磁盘。
innodb_buffer_pool_dump_now = 1
#在启动时把热数据加载到内存。
innodb_buffer_pool_load_at_startup = 1
#采用手工方式把热数据加载到内存。
innodb_buffer_pool_load_now = 1
ib_buffer_pool
注：只有在正常关闭MySQL服务，或者pkill mysql时，会把热数据dump到内存。机器宕机或者pkill -9 mysql，是不会dump。
```



- 数据库目录下的数据文件简介

```
db.opt存放这数据库编码等相关的配置信息

还有很多数据库同名的数据库文件夹
mysql两种常用存储引擎myisam和innodb
myisam不支持事务；innodb支持事务，当前作为插件来安装
 
myisam的数据库的物理文件结构为：
.frm文件：与表相关的元数据信息都存放在frm文件，包括表结构的定义信息等。各种存储引擎都需要frm文件，并且存放于数据库名目录下。
.myd文件：myisam存储引擎专用，用于存储myisam表的数据
.myi文件：myisam存储引擎专用，用于存储myisam表的索引相关信息
 
innodb的数据库的物理文件结构为：
.frm文件
.ibd文件和.ibdata文件：
这两种文件都是存放innodb数据的文件，之所以用两种文件来存放innodb的数据，是因为innodb的数据存储方式能够通过配置来决定是使用共享表空间存放存储数据，还是用独享表空间存放存储数据。
独享表空间存储方式使用.ibd文件，并且每个表一个ibd文件
共享表空间存储方式使用.ibdata文件，所有表共同使用一个ibdata文件

```
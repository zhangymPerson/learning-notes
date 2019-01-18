# 下载 安装

- 安装依赖包

    yum install perl-IO-Socket-SSL perl-DBD-MySQL perl-Time-HiRes perl perl-DBI -y

    rpm -ivh percona-toolkit-2.2.7-1.noarch.rpm


# 使用教程


- pt-table-checksum 是 Percona-Toolkit的组件之一，用于检测MySQL主、从库的数据是否一致。

    其原理是在主库执行基于statement的sql语句来生成主库数据块的checksum，把相同的sql语句传递到从库执行，并在从库上计算相同数据块的checksum，最后，比较主从库上相同数据块的checksum值，由此判断主从数据是否一致。检测过程根据唯一索引将表按row切分为块（chunk），以为单位计算，可以避免锁表。检测时会自动判断复制延迟、 master的负载， 超过阀值后会自动将检测暂停，减小对线上服务的影响。

    pt-table-checksum 默认情况下可以应对绝大部分场景，官方说，即使上千个库、上万亿的行，它依然可以很好的工作，这源自于设计很简单，一次检查一个表，不需要太多的内存和多余的操作；必要时，pt-table-checksum 会根据服务器负载动态改变 chunk 大小，减少从库的延迟。


    为了减少对数据库的干预，pt-table-checksum还会自动侦测并连接到从库，当然如果失败，可以指定--recursion-method选项来告诉从库在哪里。它的易用性还体现在，复制若有延迟，在从库 checksum 会暂停直到赶上主库的计算时间点（也通过选项--设定一个可容忍的延迟最大值，超过这个值也认为不一致）。

- 注意

    第一次运行的时候需要加上--create-replicate-table参数，生成checksums表！！如果不加这个参数，那么就需要在对应库下手工添加这张表了,表结构SQL如下：

    ```sql
    CREATE TABLE checksums (
    db             char(64)     NOT NULL,
    tbl            char(64)     NOT NULL,
    chunk          int          NOT NULL,
    chunk_time     float            NULL,
    chunk_index    varchar(200)     NULL,
    lower_boundary text             NULL,
    upper_boundary text             NULL,
    this_crc       char(40)     NOT NULL,
    this_cnt       int          NOT NULL,
    master_crc     char(40)         NULL,
    master_cnt     int              NULL,
    ts             timestamp    NOT NULL,
    PRIMARY KEY (db, tbl, chunk),
    INDEX ts_db_tbl (ts, db, tbl)
    ) ENGINE=InnoDB;

    ```
- 常用参数解释:

    --nocheck-replication-filters : 不检查复制过滤器，建议启用。后面可以用--databases来指定需要检查的数据库。
  
    --no-check-binlog-format : 不检查复制的binlog模式，要是binlog模式是ROW，则会报错。
  
    --replicate-check-only : 只显示不同步的信息。
  
    --replicate= : 把checksum的信息写入到指定表中，建议直接写到被检查的数据库当中。
  
    --databases= : 指定需要被检查的数据库，多个则用逗号隔开。
  
    --tables= : 指定需要被检查的表，多个用逗号隔开
  
    h= : Master的地址
  
    u= : 用户名
  
    p=：密码
  
    P= : 端口

- 最重要的一点就是：

    要在主库上授权，能让主库ip访问。这一点不能忘记！（实验证明从库上可以不授权，但最好还是从库也授权）

- 注意:
    
    1）**根据测试，需要一个即能登录主库，也能登录从库的账号**

    2）只能指定一个host，必须为主库的IP；
    
    3）在检查时会向表加S锁；
    
    4）运行之前需要从库的同步IO和SQL进程是YES状态。


- 在主库执行授权用户

    **（一定要对主库ip授权，授权的用户名和密码可以自行定义，不过要保证这个权限能同时登陆主库和从库）**

    ```sql
    mysql> GRANT SELECT, PROCESS, SUPER, REPLICATION SLAVE,CREATE,DELETE,INSERT,UPDATE ON *.* TO 'pt-table'@'%' identified by 'PtTable123456.';
    mysql> flush privileges;

    在从库上执行授权
    mysql> GRANT SELECT, PROCESS, SUPER, REPLICATION SLAVE ON *.* TO 'pt-table'@'%' IDENTIFIED BY 'PtTable123456.';
    mysql> flush privileges;

- eg

    ```sh
    pt-table-checksum --nocheck-replication-filters --no-check-binlog-format --replicate=huanqiu.checksums --databases=huanqiu --tables=haha h=192.168.1.101,u=root,p=123456,P=3306

    ```

            TS ERRORS  DIFFS     ROWS  CHUNKS SKIPPED    TIME TABLE
        01-08T04:11:03      0      0        4       1       0   1.422 huanqiu.haha
    参数解释:

        TS : 完成检查的时间。
        ERRORS : 检查时候发生错误和警告的数量。
        DIFFS : 0表示一致，1表示不一致。当指定--no-replicate-check时，会一直为0，当指定--replicate-check-only会显示不同的信息。
        ROWS : 表的行数。
        CHUNKS : 被划分到表中的块的数目。
        SKIPPED : 由于错误或警告或过大，则跳过块的数目。
        TIME : 执行的时间。
        TABLE : 被检查的表名。

- 参考地址

    [percona-toolkit工具（数据一致性监测、延迟监控）使用梳理](https://www.cnblogs.com/kevingrace/p/6261091.html)
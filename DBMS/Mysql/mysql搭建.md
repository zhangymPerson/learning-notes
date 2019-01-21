# MySQL 主从搭建

## 先分别搭建好单独的主从数据库

- 关闭防火墙
    ```sh
    $ systemctl stop firewalld.service
    ```
- 搭建mysql

    使用yum源搭建

## 主库上配置好二进制日志


- 配置 Master 以使用基于二进制日志文件位置的复制

    必须启用二进制日志记录并建立唯一的服务器ID,否则则无法进行主从复制。

    停止MySQL服务。
    ```sh
    $ service mysql.server stop
    ```
    开启binlog ，每台设置不同的 server-id

    - master服务器
        ```sh
        $ vim /etc/my.cnf
        [mysqld]
        log-bin=mysql-bin
        server-id=1
        ```
    - slave 服务器
        ```sh
        $ service mysql.server stop
        $ vim /etc/my.cnf
        [mysqld]
        server-id=2
        ```
## 查看主从日志起始位置

- master服务位置查看
    ```sql
    show master status;
    mysql>  show master status;
    +------------------+----------+--------------+------------------+-------------------+
    | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
    +------------------+----------+--------------+------------------+-------------------+
    | mysql-bin.000001 |      629 |              |                  |                   |
    +------------------+----------+--------------+------------------+-------------------+
    ```
## 指定日志位置启动

- slave 服务器上

    - 配置主从日志的读取位置

        ```sql
        mysql> CHANGE MASTER TO
            -> MASTER_HOST='192.168.252.123',
            -> MASTER_USER='replication',
            -> MASTER_PASSWORD='mima',
            -> MASTER_LOG_FILE='mysql-bin.000001',
            -> MASTER_LOG_POS=629;
        Query OK, 0 rows affected, 2 warnings (0.02 sec)

        change master to master_host='104.199.171.116',master_user='slave',master_password='slave',master_log_file='mysql-bin.000001',master_log_pos=107;
        #一行上参数修改成自己的
        CHANGE MASTER TO MASTER_HOST='192.168.252.123', MASTER_USER='replication', MASTER_PASSWORD='mima', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=629;
        ```
    - 启动主从
        ```sql
        mysql> START SLAVE;
        Query OK, 0 rows affected (0.00 sec)
        ```
    - 主从状态查看
        ```sql
        show slave status;

        Slave_IO_State #从站的当前状态 
        Slave_IO_Running： Yes #读取主程序二进制日志的I/O线程是否正在运行 
        Slave_SQL_Running： Yes #执行读取主服务器中二进制日志事件的SQL线程是否正在运行。与I/O线程一样 
        Seconds_Behind_Master #是否为0，0就是已经同步了
        ```


## 监控主从

- 通过建表，添加数据测试

- 可以通过脚本测试
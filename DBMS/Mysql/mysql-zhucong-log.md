# 查询主从二进制文件

- 进入MySQL查询

    ```sql

    # 进入mysql以后 查看日志文件
    show binlog events in 'mysql-bin.000002';

    # 查看当前主库的二进制日志文件位置 
    show master status\G;
    #获取当前二进制文件的列表
    show binary logs;

    # 上面这条语句可以将指定的binlog日志文件，分成有效事件行的方式返回，并可使用limit指定pos点的起始偏移，查询条数！
    如下操作示例：
    #查询第一个(最早)的binlog日志：
    mysql> show binlog events\G;

    #指定查询 mysql-bin.000002这个文件：
    mysql> show binlog events in 'mysql-bin.000002'\G;

    #指定查询 mysql-bin.000002这个文件，从pos点:624开始查起：
    mysql> show binlog events in 'mysql-bin.000002' from 624\G;

    #指定查询 mysql-bin.000002这个文件，从pos点:624开始查起，查询10条（即10条语句）
    mysql> show binlog events in 'mysql-bin.000002' from 624 limit 10\G;

    e）指定查询 mysql-bin.000002这个文件，从pos点:624开始查起，偏移2行（即中间跳过2个），查询10条
    mysql> show binlog events in 'mysql-bin.000002' from 624 limit 2,10\G;

    ```

- mysqlbinlog工具的使用

    ```sql
    mysqlbinlog --no-defaults mysql-bin.000985 | grep last_committed

    #根据开始时间和结束时间查找
    mysqlbinlog --no-defaults --start-datetime='2018-12-06 14:00:00' --stop-datetime='2018-12-06 14:30:01' -d boyi_data mysql-bin.000985

    # 查询格式
    mysqlbinlog --no-defaults --start-datetime='2018-12-06 14:00:00' --stop-datetime='2018-12-06 14:30:01' -d 数据库名 /*/*/mysql-bin.000***

    #此命令需配合 grep 命令使用  也可以通过管道写入其他文件中进行分析


    #按照偏移量来查询日志
    mysqlbinlog --no-defaults --start-position=471 --stop-position=875 --database=ops /var/lib/mysql/mysql-bin.000003


    # 查看日志文件  根据日志偏移量
    mysqlbinlog --no-defaults –v –v --base64-output=decode-rows /usr/local/mysql/data/master-bin.000010 | grep –A '10' 920578920

    ```
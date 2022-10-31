# sqoop导入

- 概念

    数据从 数据源导入到大数据平台 

## sqoop基本原理


## sqoop常用命令

```sh

    #帮助命令  导入
    sqoop import --help

    #Demo (以mysql导入到hdfs为例)
    sqoop import -Dmapreduce.job.queuename=hive2 -Dhadoop.security.credential.provider.path=jceks://hdfs/user/password/old_mysql_huizongceng.pwd.jceks --connect "$URL" --username $UNAME --password-alias old_mysql_huizongceng --table $MYSQL_TABLE   --mysql-delimiters --target-dir /user/test/${MYSQL_TABLE}  --split-by 'day' --where 'day < "2018-12-06"' -m 5
    # 参数解析
    - Dmapreduce.job.queuename 参数指的是yarn中的队列名 
    - Dhadoop.security.credential.provider.path hadoop生成的密钥文件位置
    - connect 数据源的JDBC配置;("jdbc:mysql://ip:3306/库名?tinyInt1isBit=false&zeroDateTimeBehavior=round&autoReconnect=true")
    - username 数据库用户名
    - password-alias 密码对应的别名
    - table 指定要导入的数据表
    - mysql-delimiters 数据分割方式
    - target-dir 数据在hdfs上的存储位置
    - split-by 指定无主键的多map时需指定数据分割列的字段
    - where指定数据导入时数据需要满足的条件
    - m 指定sqoop job 中的map数;

    



```


# mysql权限

- MySQL用户权限说明

|权限|权限级别|权限说明
|-|-|-|
CREATE|数据库、表或索引|创建数据库、表或索引权限
|DROP|数据库或表|删除数据库或表权限
|GRANT OPTION|数据库、表或保存的程序|赋予权限选项
|REFERENCES|数据库或表 
|ALTER|表|更改表，比如添加字段、索引等
|DELETE|表|删除数据权限
|INDEX|表|索引权限
|INSERT|表|插入权限
|SELECT|表|查询权限
|UPDATE|表|更新权限
|CREATE VIEW|视图|创建视图权限
|SHOW VIEW|视图|查看视图权限
|ALTER ROUTINE|存储过程|更改存储过程权限
|CREATE ROUTINE|存储过程|创建存储过程权限
|EXECUTE|存储过程|执行存储过程权限
|FILE|服务器主机上的文件访问|文件访问权限
|CREATE TEMPORARY TABLES|服务器管理|创建临时表权限
|LOCK TABLES|服务器管理|锁表权限
|CREATE USER|服务器管理|创建用户权限
|PROCESS|服务器管理|查看进程权限
|RELOAD|服务器管理|执行flush-hosts, flush-logs, flush-privileges, flush-status,|flush-tables, flush-threads, refresh, reload等命令的权限
|REPLICATION CLIENT|服务器管理|复制权限
|REPLICATION SLAVE|服务器管理|复制权限
|SHOW DATABASES|服务器管理|查看数据库权限
|SHUTDOWN|服务器管理|关闭数据库权限
|SUPER|服务器管理|执行kill线程权限

    
MYSQL的权限如何分布，就是针对表可以设置什么权限，针对列可以设置什么权限等等，这个可以从官方文档中的一个表来说明：

权限分布|可能的设置的权限
|-|-|
|表权限|'Select', 'Insert', 'Update', 'Delete', 'Create', 'Drop','Grant', 'References', 'Index', 'Alter'
|列权限|'Select', 'Insert', 'Update', 'References'
|过程权限|'Execute', 'Alter Routine', 'Grant'

- MySQL权限经验原则：

    权限控制主要是出于安全因素，因此需要遵循一下几个经验原则：

    1、只授予能满足需要的最小权限;

    2、创建用户的时候限制用户的登录主机，一般是限制成指定IP或者内网IP段。

    3、初始化数据库的时候删除没有密码的用户。安装完数据库的时候会自动创建一些用户，这些用户默认没有密码。
    
    4、为每个用户设置满足密码复杂度的密码。
    
    5、定期清理不需要的用户。回收权限或者删除用户。

### 权限相关的sql

- 创建用户并且授权

    ```sql
    grant all privileges on *.* to username@'ip' identified by "password" with grant option;
    #授权完成后，必须要刷新权限，否则创建用户 不生效
    flush privileges;
    ```
    GRANT命令说明：
    
        ALL PRIVILEGES 是表示所有权限，你也可以使用select、update等权限。

        ON 用来指定权限针对哪些库和表。

        *.* 中前面的*号用来指定数据库名，后面的*号用来指定表名。

        TO 表示将权限赋予某个用户。

        username@'ip' 表示usernaem用户，@后面接限制的主机，可以是IP、IP段、域名以及%，%表示任何地方。注意：这里%有的版本不包括本地，以前碰到过给某个用户设置了%允许任何地方登录，但是在本地登录不了，这个和版本有关系，遇到这个问题再加一个localhost的用户就可以了。

        IDENTIFIED BY 指定用户的登录密码。

        WITH GRANT OPTION 这个选项表示该用户可以将自己拥有的权限授权给别人。注意：经常有人在创建操作用户的时候不指定WITH GRANT OPTION选项导致后来该用户不能使用GRANT命令创建用户或者给其它用户授权。

    **备注**：可以使用GRANT重复给用户添加权限，权限叠加，比如你先给用户添加一个select权限，然后又给用户添加一个insert权限，那么该用户就同时拥有了select和insert权限。

    多个库授权:

    ```sql
    #授权db1库的权限
    Grant all privilegs on db1.* to‘用户名’@‘ip地址’ 
    #授权db2库的权限
    Grant all privilegs on db2.* to‘用户名’@‘ip地址’
    ```
- 查看当前用户授权

    ```sql
    #查看当前用户的授权情况
    mysql> show grants;+---------------------------------------------------------------------+
    | Grants for root@localhost                                           |
    +---------------------------------------------------------------------+
    | GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION |
    | GRANT PROXY ON ''@'' TO 'root'@'localhost' WITH GRANT OPTION        |
    +---------------------------------------------------------------------+
    2 rows in set (0.00 sec)

    #查看某个用户的权限
    show grants for 'boyi'@'%';
    +-------------------------------------------------------------+
    | Grants for boyi@%                                           |
    +-------------------------------------------------------------+
    | GRANT ALL PRIVILEGES ON *.* TO 'boyi'@'%' WITH GRANT OPTION |
    +-------------------------------------------------------------+
    1 row in set (0.00 sec)

    ```
- 回收授权

    ```sql

    #回收授权
    revoke 权限名 on 库.表 from username@'ip';
    #收回全部权限
    revoke all privileges,grant option from 'username'@'ip';
    
    #TODO 下一步研究
    测试发现库表名要与创建时保持一致

    ```
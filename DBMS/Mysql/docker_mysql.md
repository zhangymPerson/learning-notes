# docker 安装 mysql

> 查询 - 拉取 - 配置 - 安装

## docker 远程仓库查询

- 查看可用版本
  `docker search mysql`

## 拉取

- 拉取 mysql 镜像

  `docker pull mysql:latest`

## 配置-运行

- 直接启动命令,不带挂载和自定义的相关配置

  `docker run -d -p 3307:3306 --name mysql -e MYSQL_ROOT_PASSWORD=123456 mysql:latest`

  这个启动命令是不指定指定配置文件和数据文件的

  其中 `-d` 是后台运行 `-p` 指定端口 **主机:容器** `-e MYSQL_ROOT_PASSWORD=` 指定密码 `--name` 指定运行名称

  **重点:3307 是主机的 ip 地址**

  可以启动多个实例

- 链接 mysql

  报错 : **出现 2059 错误**

  - 原因

    mysql8 之前的版本中加密规则是 **mysql_native_password**,而在 mysql8 之后,加密规则是 **caching_sha2_password**

  - 解决

    更改加密规则：

    ```sh
    #登录
    mysql -uroot -ppassword

    #选择数据库
    use mysql;

    #更改加密方式
    # 远程连接请将'localhost'换成'%'
    ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER;

    ALTER USER 'root'@'%' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER;
    #更新用户密码
  ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
    
    ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
    #刷新权限
    FLUSH PRIVILEGES;
    ```

- 启动带**自定义配置文件和数据路径**的mysql服务

  - 创建要自定义的文件夹
    `mkdir -p /opt/docker/mysql/3307`
  - 创建本地配置文件

    `mkdir conf`
    `vim my.cnf`

    ```conf
    [mysqld]
    character-set-server=utf8
    [client]
    default-character-set=utf8
    [mysql]
    default-character-set=utf8
    ```

  - 创建本地数据目录
    mkdir data

  - 指定挂载内容启动

    `docker run --name mysql07 -p 3307:3306 -e MYSQL_ROOT_PASSWORD=123456 -v /opt/docker/mysql/3307/conf:/etc/mysql/conf.d -v /opt/docker/mysql/3307/data:/var/lib/mysql -d mysql:latest`

- 参数说明
  - -p 3307:3306：将容器的 3306 端口映射到主机的 3307 端口。(主机:容器)
  - -v -v /opt/docker/mysql/3307/conf:/etc/mysql/conf.d：将主机目录下的 /opt/docker/mysql/3307/conf 挂载到容器的 /etc/mysql/my.cnf。
  - -v /opt/docker/mysql/3307/data:/var/lib/mysql ：将主机目录下的 /opt/docker/mysql/3307/data 目录挂载到容器的 /var/lib/mysql 。
  - -e MYSQL_ROOT_PASSWORD=123456：初始化 root 用户的密码。
  - -d 后台运行
  - --name 运行容器名称
  - -v 挂载宿主机的一个目录。冒号":" **前面的目录是宿主机目录**，**后面的目录是容器内目录**。


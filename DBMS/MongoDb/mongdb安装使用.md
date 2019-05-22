# mongdb 安装使用

- 下载

  [官网](https://www.mongodb.com/) 

- 安装

- 使用

- 报错

    [ftdc] Unclean full-time diagnostic data capture shutdown detected, found interim file, some metrics may have been lost.

- mongdb的 配置文件

    ```xml
    #日志文件位置
    #(这些都是可以自定义修改的） 配置到具体的文件
    logpath=/data/db/journal/mongodb.log　　

    # 以追加方式写入日志
    logappend=true

    # 是否以守护进程方式运行
    fork = true

    # 默认27017
    #port = 27017

    # 数据库文件位置
    dbpath=/data/db

    # 启用定期记录CPU利用率和 I/O 等待
    #cpu = true

    # 是否以安全认证方式运行，默认是不认证的非安全方式
    #noauth = true
    #auth = true

    # 详细记录输出
    #verbose = true

    # Inspect all client data for validity on receipt (useful for
    # developing drivers)用于开发驱动程序时验证客户端请求
    #objcheck = true

    # Enable db quota management
    # 启用数据库配额管理
    #quota = true
    # 设置oplog记录等级
    # Set oplogging level where n is
    #   0=off (default)
    #   1=W
    #   2=R
    #   3=both
    #   7=W+some reads
    #diaglog=0

    # Diagnostic/debugging option 动态调试项
    #nocursors = true

    # Ignore query hints 忽略查询提示
    #nohints = true
    # 禁用http界面，默认为localhost：28017
    #nohttpinterface = true

    # 关闭服务器端脚本，这将极大的限制功能
    # Turns off server-side scripting.  This will result in greatly limited
    # functionality
    #noscripting = true
    # 关闭扫描表，任何查询将会是扫描失败
    # Turns off table scans.  Any query that would do a table scan fails.
    #notablescan = true
    # 关闭数据文件预分配
    # Disable data file preallocation.
    #noprealloc = true
    # 为新数据库指定.ns文件的大小，单位:MB
    # Specify .ns file size for new databases.
    # nssize =

    # Replication Options 复制选项
    # in replicated mongo databases, specify the replica set name here
    #replSet=setname
    # maximum size in megabytes for replication operation log
    #oplogSize=1024
    # path to a key file storing authentication info for connections
    # between replica set members
    #指定存储身份验证信息的密钥文件的路径
    #keyFile=/path/to/keyfile
    ```

- mongodb将开启远程授权

    ```xml
    #可以访问的地址. 127.0.0.1表示自己访问,  
    #0.0.0.0 表示所有人都能访问
    bind_ip = 0.0.0.0
    auth=true
    ```



- mongodb 的启动和关闭

    ```
    cd $MONGODB_HOME/bin
    #启动  mongodb的配置文件 需要自己创建
    ./mongdb -f mongodb.conf  

    # 安全关闭mongodb

    use admin
    db.shutdownServer() 

    ```
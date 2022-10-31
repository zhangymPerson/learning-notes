### mongodb的权限

- 注意 先创建用户和相关权限 后开启权限登陆模式 (auth=true)



### mongodb默认的库
        
-  admin

    admin库主要存放有数据库帐号相关信息。
 
- local
 
    local数据库永远不会被复制到从节点，可以用来存储限于本地单台服务器的任意集合副本集的配置信息、oplog就存储在local库中。 

    注意：重要的数据不要存储在local库，因为没有冗余副本，如果这个节点故障，存储在local库的数据就无法正常使用了。
 
- config
    config数据库用于分片集群环境，存放了分片相关的元数据信息。
 - test

    MongoDB默认创建的一个测试库，连接mongod服务时，如果不指定连接的具体数据库，默认就会连接到test库。

- mongodb创建用户

    ```sh
    #先切换到admin库
    use admin
    #创建用户 旧版本的创建
    db.addUser("root","pwd");
    #新版本的创建
    db.createUser(user, writeConcern)

    #创建超级管理员
    db.createUser({user:'root',pwd:'pwd',roles:[{ role: "root", db: "admin" }]})


    #创建单个库的用户 读写权限 如测试库
    db.createUser({user:"test",pwd:"test",roles:[{role:"readWrite",db:"test"}]})

    #查看单个库下的用户
    use dbname
    show users

    #查看所有用户
    use admin
    db.system.users.find().pretty()

    #修改密码
    use dbname
    db.changeUserPassword('username','newpassword');  

    #用户登陆
    ```
    **用户只能在用户所在数据库登录，管理员需要通过admin认证后才能管理其他数据库**

    先进入admin库登陆在转到别的库，不然提示没有权限

- 创建语法的说明

    定义：

    创建一个数据库新用户用db.createUser()方法，如果用户存在则返回一个用户重复错误。


    语法：

        db.createUser(user, writeConcern)
        user这个文档创建关于用户的身份认证和访问信息；
        writeConcern这个文档描述保证MongoDB提供写操作的成功报告。
        
- user文档，定义了用户的以下形式：

    ```json
    { user: "<name>",
      pwd: "<cleartext password>",
      customData: { <any information> },
      roles: [
    { role: "<role>", db: "<database>" } | "<role>",
    ...
      ]
    }
    ```

- user文档字段介绍：

    user字段，为新用户的名字；

    pwd字段，用户的密码；

    cusomData字段，为任意内容，例如可以为用户全名介绍；

    roles字段，指定用户的角色，可以用一个空数组给新用户设定空角色；

    在roles字段,可以指定内置角色和用户定义的角色。

- Built-In Roles（内置角色）:

    Read：允许用户读取指定数据库

    readWrite：允许用户读写指定数据库

    dbAdmin：允许用户在指定数据库中执行管理函数，如索引创建、删除，查看统计或访问system.profile

    userAdmin：允许用户向system.users集合写入，可以找指定数据库里创建、删除和管理用户

    clusterAdmin：只在admin数据库中可用，赋予用户所有分片和复制集相关函数的管理权限。

    readAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的读权限

    readWriteAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的读写权限

    userAdminAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的userAdmin权限

    dbAdminAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的dbAdmin权限。

    root：只在admin数据库中可用。超级账号，超级权限

 - writeConcern文档（官方说明）

     w选项：允许的值分别是 1、0、大于1的值、"majority"、<tag set>；

    j选项：确保mongod实例写数据到磁盘上的journal（日志），这可以确保mongd以外关闭不会丢失数据。设置true启用。

    wtimeout：指定一个时间限制,以毫秒为单位。wtimeout只适用于w值大于1。

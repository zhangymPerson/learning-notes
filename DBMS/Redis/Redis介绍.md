# Redis 

## Nosql简介

- 概念

    NoSQL(NoSQL = Not Only SQL)，泛指非关系型的数据库。
    [Nosql-百度百科](https://baike.baidu.com/item/NoSQL/8828247)    
## Resid简介

### redis 中的数据结构

- String 类型

- Hash数据类型

- List数据类型

- Set数据类型

- zset 数据类型

    zset（sorted set 有序集合


## 应用场景

### 集群搭建的模式

- 主从模式

    一主多从
- 哨兵模式

    Redis 的 Sentinel 系统用于管理多个 Redis 服务器（instance）， 该系统执行以下三个任务：

    监控（Monitoring）： Sentinel 会不断地检查你的主服务器和从服务器是否运作正常。
    
    提醒（Notification）： 当被监控的某个 Redis 服务器出现问题时， Sentinel 可以通过 API 向管理员或者其他应用程序发送通知。
    
    自动故障迁移（Automatic failover）： 当一个主服务器不能正常工作时， Sentinel 会开始一次自动故障迁移操作， 它会将失效主服务器的其中一个从服务器升级为新的主服务器， 并让失效主服务器的其他从服务器改为复制新的主服务器； 当客户端试图连接失效的主服务器时， 集群也会向客户端返回新主服务器的地址， 使得集群可以使用新主服务器代替失效服务器。
    
    Redis Sentinel 是一个分布式系统， 你可以在一个架构中运行多个 Sentinel 进程（progress）， 这些进程使用流言协议（gossip protocols)来接收关于主服务器是否下线的信息， 并使用投票协议（agreement protocols）来决定是否执行自动故障迁移， 以及选择哪个从服务器作为新的主服务器。

    虽然 Redis Sentinel 释出为一个单独的可执行文件 redis-sentinel ， 但实际上它只是一个运行在特殊模式下的 Redis 服务器， 你可以在启动一个普通 Redis 服务器时通过给定 --sentinel 选项来启动 Redis Sentinel 。

    - 参考:
    
        [Redis 的 Sentinel 系统](http://doc.redisfans.com/topic/sentinel.html)

        [英文版本](https://redis.io/topics/sentinel)
- 集群模式


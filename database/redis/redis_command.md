# Redis 常用命令

## 打开客服端-连接服务

- redis-cli

  ```sh
  #打开本地
  redis-cli
  #打开远程
  redis-cli -h host -p port -a password
  ```

- 中文乱码

  ```sh
  #要在 redis-cli 后面加上 --raw
  redis-cli --raw
  ```

- 登陆

  ```sh
  # 没有登陆则操作报错
  (error) NOAUTH Authentication required.
  #密码登陆
  redis-cli -h 127.0.0.1 -p 6379 -a myPassword
  ```

- 集群登陆

  ```sh
  # -c参数代表集群登陆
  redis-cli -c -h 127.0.0.1 -p 6379 -a myPassword
  ```

- 退出

  `exit` 或者 `quit`

- 命令查询网站[redis-命令参考](http://doc.redisfans.com/)

## 常用命令

> [reids 查询手册](http://redisdoc.com/index.html)

- 获取命令帮助

  ```sh
  #连接成功后，去查询命令使用帮助
  help commandName
  ```

- 库信息命令

  `dbsize` 查看当前数据库中的 key 的数量

  `config get *` 查看服务器参数信息

- 数据持久化

  `save` : 保存到磁盘

  `bgsave` ： 异步保存到磁盘

  `info` : 查看数据库信息

- 对 value 的常用操作

  | 命令                     | 含义                                 |
  | ------------------------ | ------------------------------------ |
  | `keys pattern`           | 返回匹配指定模式的所有 key           |
  | `keys *`                 | 获取 redis 中所有 key                |
  | `keys key1*`             | 获取 redis 中以 key1 开头的 key      |
  | `exists key`             | 指定 key 是否存在                    |
  | `del key1 key2 ... keyN` | 删除指定 key                         |
  | `type key`               | 返回指定 key 的 value 类型           |
  | `randomkey`              | 返回从当前数据库中随机的一个 key     |
  | `rename oldkey newkey`   | 重命名                               |
  | `dbsize`                 | 返回当前数据库的 key 数量            |
  | `expire key seconds`     | 为指定 key 设置剩余秒数              |
  | `ttl key`                | 返回 key 的剩余秒数                  |
  | `select index`           | 选择数据库(一共 16 个,0-15,默认是 0) |
  | `move key index`         | 把 key 从当前数据库移动到指定数据库  |
  | `flushdb`                | 删除当前数据库中所有 key             |
  | `flushall`               | 删除当前所有数据库中的所有 key       |

- String 类型的操作命令

  | 命令                                           | 含义                      |
  | ---------------------------------------------- | ------------------------- |
  | `set key value`                                | 设置 key 的值             |
  | `get key`                                      | 获取 key 的值             |
  | `mset key1 value1 key2 value2 ... keyN valueN` | 一次设置多个 key 的值     |
  | `mget key1 key2 ... keyN`                      | 一次获取多个 key 的值     |
  | `incr key`                                     | 对 key 的值做++操作       |
  | `decr key`                                     | 对 key 的值做--操作       |
  | `incrby key integer`                           | 把 key 的值加上指定值     |
  | `decrby key integer`                           | 把 key 的值减去指定值     |
  | `append key value`                             | 把 key 的值追加一个字符串 |
  | `substr key start end`                         | 截取 key 的值             |

- Hash 类型

  | 命令                                        | 含义                                         |
  | ------------------------------------------- | -------------------------------------------- |
  | `hset key field value`                      | 给字段赋值,如果不存在则先创建,如果存在则更新 |
  | `hget key field`                            | 获取 hash 中指定字段的值                     |
  | `hmset key field1 value1 ... fieldN valueN` | 给 hash 多个字段赋值                         |
  | `hmget key field1 ... fieldN`               | 获取 hash 中多个指定字段的值                 |
  | `hincrby key field integer`                 | 给 hash 中指定字段加上指定值                 |
  | `hexists key field`                         | hash 中指定字段是否存在                      |
  | `hdel key field`                            | 删除 hash 中指定字段                         |
  | `hlen key`                                  | 获取 hash 中字段数量                         |
  | `hkeys key`                                 | 获取 hash 中所有的字段                       |
  | `hvals key`                                 | 获取 hash 中所有的值                         |
  | `hgetall key`                               | 获取 hash 中所有的字段和值                   |

- List 类型

  | 命令                          | 含义                                                                      |
  | ----------------------------- | ------------------------------------------------------------------------- |
  | `lpush key value [value ...]` | 在 list 的头部(左边)添加元素                                              |
  | `rpush key value [value ...]` | 在 list 的尾部(右边)添加元素                                              |
  | `llen key`                    | 返回 list 的长度,key 不存在返回 0,key 对应的值不是 list 类型则返回错误    |
  | `lrange key start end`        | 返回指定区间内的元素,下标从 0 开始                                        |
  | `ltrim key start end`         | 截取 list,保留指定区间内元素                                              |
  | `lset key index value`        | 设置 list 中指定下标的元素值                                              |
  | `lrem key count value`        | 从 key 对应 list 中删除 count 个和 value 相同的元素.count 为 0 时删除全部 |
  | `lpop key`                    | 从 list 头部删除元素,并返回删除元素                                       |
  | `rpop key`                    | 从 list 尾部删除元素,并返回删除元素                                       |
  | `lindex key index`            | 获取 list 中指定索引的值                                                  |

- Set 类型

  | 命令                                    | 含义                                                            |
  | --------------------------------------- | --------------------------------------------------------------- |
  | `sadd key member [member ...]`          | 添加一个 string 元素到 set 集合中,成功返回 1,元素已经存在返回 0 |
  | `srem key member [member ...]`          | 从 set 中移出给定元素,成功返回 1                                |
  | `smove p1 p2 member`                    | 从 p1 对应 set 中移出 member 并添加到 p2 对应 set 中            |
  | `scard key`                             | 返回 set 中元素的个数                                           |
  | `sismember key member`                  | 判断 member 是否在 set 中                                       |
  | `sinter key1 key2 [key ...]`            | 返回指定 list 的交集                                            |
  | `sinterstore p1 key1 key2 [key ...]`    | 同 sinter,但是会同时把交集存在 p1 中                            |
  | `sunion key1 key2 [key ...]`            | 返回指定 list 的并集                                            |
  | `sunionstore p1 key1 key2 [key ...]`    | 同 sunion,并同时把并集保存到 p1 中                              |
  | `sdiff key1 key2 [key ...]`             | 返回指定 list 的差集                                            |
  | `sdiffstore dstkey key1 key2 [key ...]` | 同 sdiff,并同时把差集保存到 dstkey 中                           |
  | `smembers key`                          | 返回 set 的所有元素,结果是无序的                                |

- SortedSet 类型

  | 命令                           | 含义                                                         |
  | ------------------------------ | ------------------------------------------------------------ |
  | `zadd key score member`        | 添加元素到集合,元素在集合中存在则更新对应 score              |
  | `zrem key member`              | 删除指定元素,1 表示成功,如果元素不存在则返回 0               |
  | `zincrby key incr member`      | 按照 incr 幅度增加对应 member 的 score 值,返回 score 值      |
  | `zrank key member`             | 返回指定元素在集合中的排名,集合元素是按 score 从小到大排序的 |
  | `zrevrank key member`          | 同上, 但是集合中元素是按 score 逆序的                        |
  | `zrange key start end`         | 从集合中取出指定区间元素,返回有序结果                        |
  | `zrevrange key start end`      | 同上,返回结果是按 socre 逆序                                 |
  | `zrangebyscore key min max`    | 返回集合中 score 在给定区间的元素                            |
  | `zcount key min max`           | 返回集合中 score 在给定区间的数量                            |
  | `zcard key`                    | 返回集合中元素个数                                           |
  | `zscore key element`           | 返回给定元素对应的 score                                     |
  | `zremrangebyrank key min max`  | 删除集合中排名在给定区间的元素                               |
  | `zremrangebyscore key min max` | 删除集合中 score 在给定区间的元素                            |

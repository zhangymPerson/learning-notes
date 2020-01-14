# Redis 相关笔记

- Redis介绍

    [官网](https://redis.io/)

    [百度百科](https://baike.baidu.com/item/Redis/6549233)

    [GitHub地址](https://github.com/antirez/redis)

    [社区](http://www.redis.cn/)

    [简单教程](http://www.runoob.com/redis/redis-tutorial.html)

- Redis中的数据类型

- String（字符串）

    结构存储的值
    
    可以是字符串、整数或者浮点数。

    结构的读写能力：

    对整个字符串或者字符串的其中一部分执行操作，对象和浮点数执行自增(increment)或者自减(decrement)。

- List（列表）

    结构存储的值：

    一个链表，链表上的每个节点都包含了一个字符串。

    结构的读写能力：
    
    从链表的两端推入或者弹出元素，根据偏移量(offset)对链表进行修剪(trim)，读取单个或者多个元素，根据值来查找或者移除元素。

- Set（集合）
    
    结构存储的值：
    
    包含字符串的无序收集器(unOrderedCollection)，并且被包含的每个字符串都是独一无二的、各不相同。

    结构的读写能力：
    
    添加、获取、移除单个元素，检查一个元素是否存在于某个集合中，计算交集、并集、差集，从集合里面随机获取元素。

- Hash（散列）

    结构存储的值：
    
    包含键值对的无序散列表。

    结构的读写能力：
    
    添加、获取、移除单个键值对，获取所有键值对。

- zSet（有序集合）
    
    结构存储的值：
    
    字符串成员(member)与浮点数分值(score)之间的有序映射，元素的排列顺序由分值(score)的大小决定。

    结构的读写能力：
    
    添加、获取、删除单个元素，根据分值(score)范围(range)或者成员来获取元素。
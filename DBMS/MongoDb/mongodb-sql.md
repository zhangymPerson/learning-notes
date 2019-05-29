## mongodb的操作sql

### 库相关的操作 database

- 帮助命令查看

    shell下执行help命令
    
```
#进入某个库
use dbname

#查看当前库
db

#创建数据库 
use testdb 

#创建集合 
db.tableName.insert({name:"test",test:"testInfo"}) 

# 查询集合
db.tableName.find() 
db.tableName.findOne() 

#修改
#不会影响其他属性列 ，主键冲突会报错
db.tableName.update({name:"test"},{$set:{test:"alterInfo"}})

#第三个参数为 true 则执行 insertOrUpdate 操作，查询出则更新，没查出则插入，
db.tableName.update({name:"test"},{$set:{testOne:18}},true) #

#删除
#删除满足条件的第一条 只删除数据 不删除索引
db.tableName.remove({testOne:1})

#删除集合
db.tableName.drop();

#删除数据库
db.dropDatabase(); 

# 查看集合 
show collections 

#查看数据库 
show dbs 

#插入数据 

#不允许键值重复 
db.tableName.insert()

#若键值重复，可改为插入操作 
db.tableName.save() 

#批量更新 
db.tableName.update({name:"test"},{$set:{name:"zhanmin11"}},false,t rue);
#批量操作需要和选择器同时使用，第一个 false 表示不执行 insertOrUpdate 操作，第二个 true 表示 执行批量 

#删库

```

### 表相关的操作 collection


```
#建立集合

#操作集合

#查询所有数据
db.tablename.find()

db.tablename.find({})

# 添加数据
db.tablename.insert({})

# 修改更新数据
db.tablename.save({})



#删除集合


```

### 索引操作
- 基础索引

    在字段age 上创建索引，1(升序);-1(降序)：

        db.tablename.ensureIndex({age:1})

    _id 是创建表的时候自动创建的索引，此索引是不能够删除的。当系统已有大量数据时，创建索引就是个非常耗时的活，我们可以在后台执行，只需指定“backgroud:true”即可。

        db.tablename.ensureIndex({age:1} , {backgroud:true})

- 组合索引

        db.tablename.ensureIndex( { "addr" : 1, "state" : 1 } );

- 删除索引

    删除tablename 表中的所有索引
        
        db.tablename.dropIndexes()

    删除tablename 表中的firstname 索引

        db.tablename.dropIndex({firstname: 1})

- 设置时间TTL 索引


        db.tablename.createIndex( { "字段名": 1 },{ "name":'idx_字段名',expireAfterSeconds: 定义的时间,background:true} )
    
        #给表 tablename 的createdate字段添加TTL索引  数据消失时间 60s 60s后删除
        db.tablename.createIndex({"createdate": 1},{expireAfterSeconds: 60})
    
    说明 ：expireAfterSeconds为过期时间（单位秒） 

    只能在时间字段上进行添加该索引

     索引关键字段必须是 Date 类型。
    
     非立即执行：扫描 Document 过期数据并删除是独立线程执行，默认 60s 扫描一次，删除也不一定是立即删除成功。
 
    单字段索引，混合索引不支持。
### 行相关的操作 document
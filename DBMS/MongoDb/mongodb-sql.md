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

#删除集合

```

### 行相关的操作 document
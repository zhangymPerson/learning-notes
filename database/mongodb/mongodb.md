## mongodb 概念的学习

### mongodb 的模型与关系型数据库概念对比

| 数据库概念      | mysql       | mongodb                                   |
| --------------- | ----------- | ----------------------------------------- |
| 数据库 database | database    | database                                  |
| 数据库表/集合   | 表（table） | 集合（collection）                        |
| 行/文档         | 行（row）   | 文档对象（document）                      |
| 数据列/数据字段 | Column      | Field                                     |
| 索引            | Index       | Index                                     |
| 主键            | Primary Key | Object ID 主键/MongoDB 将\_id 设置为 主键 |

一个 mongod 实例中允许创建多个数据库。

一个数据库中允许创建多个集合（集合相当于关系型数据库的表）。

一个集合则是由若干个文档构成（文档相当于关系型数据库的行，是 MongoDB 中数据的基本单元）。

### mongo 支持的数据类型

| 数据类型     | 说明       | 解释                                                                                      | 举例                    |
| ------------ | ---------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Null         | 空值       | 表示空值或者未定义的 对象                                                                 | {“x”:null}              |
| Boolean      | 布尔值     | 真或者假：true 或者 false                                                                 | {“x”:true}              |
| Integer      | 整数       | 整型数值。用于存储数 值。根据你所采用的服务 器，可分为 32 位或 64 位。                    |
| Double       | 浮点数     | 双精度浮点值。                                                                            | {“x”：3.14，”y”： 3}    |
| String       | 字符串     | UTF-8 字符串                                                                              |
| Symbol       | 符号       | 符号。该数据类型基本上 等同于字符串类型，但不 同的是，它一般用于采用 特殊符号类型的语言。 |
| ObjectID     | 对象 ID    | 对象 ID。用于创建文档 的 ID。                                                             | {“id”: ObjectId()}      |
| Date         | 日期       | 日期时间。用 UNIX 时 间格式来存储当前日期 或时间。                                        | {“date”:newDate()}      |
| Timestamp    | 时间戳     | 从标准纪元开始的毫秒 数                                                                   |
| Regular      | 正则表达式 | 文档中可以包含正则表 达式，遵循 JavaScript 的语法                                         | {“foo”:/testdb/i}       |
| Code         | 代码       | 可 以 包 含 JavaScript 代码                                                               | { “x”： function(){}}   |
| Undefined    | 未定义     | 已废弃 Array 数组 值的集合或者列表                                                        | {“arr”:[“a”,”b” ]}      |
| Binary Data  | 二进制     | 用于存储二进制数据。                                                                      |
| Object       | 内嵌文档   | 文档可以作为文档中某个 key 的 value                                                       | {“x” :{“foo” :” bar” }} |
| Min/Max keys | 最小/大值  | 将一个值与 BSON（二进 制的 JSON）元素的最低 值和最高值相对比。                            |

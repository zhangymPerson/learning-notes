# XXX 项目数据库设计说明书

- 文档变更

  | **序号** | **变更日期** | **版本** | **变更位置** | **变更原因** | **修订人** | **审核人** | **批准人** |
  | -------- | ------------ | -------- | ------------ | ------------ | ---------- | ---------- | ---------- |
  | 1        |              |          |              |              |            |            |            |
  |          |              |          |              |              |            |            |            |
  |          |              |          |              |              |            |            |            |
  |          |              |          |              |              |            |            |            |

- 说明：“变更原因”主要是分为：

  - 建立初稿
  - 内容修订
  - 正式发布

## 文档介绍

### 1.1. 编写目的

说明文档的编写目的

### 1.2. 文档范围

说明文档的主要内容

### 1.3. 读者对象

说明文档的读者对象

### 1.4. 术语与缩写解释

| **术语或缩写** | **解释** |
| -------------- | -------- |
|                |          |
|                |          |

### 1.5. 参考资料

| **序号** | **文档名称** | **文档编号** | **版本** | **发布日期** |
| -------- | ------------ | ------------ | -------- | ------------ |
| 1        |              |              |          |              |
| 2        |              |              |          |              |

## 2. 数据库环境说明

### 2.1. 数据库系统

### 2.2. 设计工具

### 2.3. 数据库配置

| **表空间**           |     |
| -------------------- | --- |
| **表空间初始化大小** |     |
| **自增量**           |     |
| **用户名**           |     |
| **密码**             |     |

## 3. 数据库的命名规则

### 3.1. 数据表名称规范

### 3.2. 数据项名称规范

### 3.3. 数据表结构定义

## 4. 数据库设计

### 4.1. 逻辑设计

### 4.2. 物理设计

### 数据库

- 数据库名：project

- 数据库说明：项目数据库

| 序号 | 表名 | 说明   |
| ---- | :--- | ------ |
| 1    | user | 用户表 |

## 数据库中单表信息

### demo 表

- 表名:demo

- 字符集:utf-8

- 引擎:InnoDB

- 字段介绍

  | 序号 | 字段名 | 数据类型  | 非空 | 键类型 | 默认值            | 注释                                      |
  | ---- | ------ | --------- | ---- | ------ | ----------------- | ----------------------------------------- |
  | 1    | id     | bigint    | NO   | PRI    | None              |                                           |
  | 2    | name   | varchar   | YES  |        | None              | 姓名                                      |
  | 3    | status | int       | YES  |        | None              | 数据状态，-1 为逻辑删除，0，>0 为可用状态 |
  | 4    | ctime  | timestamp | YES  |        | CURRENT_TIMESTAMP | 创建时间                                  |
  | 5    | mtime  | timestamp | YES  |        | None              | 修改时间                                  |
  | 6    | remark | varchar   | YES  |        | None              | 备注                                      |

- 建表 sql

  ```sql
  CREATE TABLE `demo` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '姓名',
    `status` int DEFAULT NULL COMMENT '数据状态，-1为逻辑删除，0，>0 为可用状态',
    `ctime` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `mtime` timestamp NULL DEFAULT NULL COMMENT '修改时间',
    `remark` varchar(1024) DEFAULT NULL COMMENT '备注',
    PRIMARY KEY (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='demo 表';
  ```

### user 表

- 表名:user

- 字符集:utf-8

- 引擎:InnoDB

- 字段介绍

  | 序号 | 字段名      | 数据类型            | 非空 | 键类型   | 默认值 | 注释                     |
  | ---- | ----------- | ------------------- | ---- | -------- | ------ | ------------------------ |
  | 1    | id          | bigint(20) unsigned | Y    | PRI 主键 |        | 自增 id                  |
  | 2    | userid      | bigint(20)          | Y    | MUL      |        | 用户 userid，普通索引    |
  | 3    | status      | tinyint(3)          |      | PRI      |        | 用户状态，0 注册 -1 注销 |
  | 4    | username    | varchar(50)         |      | PRI      |        | 用户名                   |
  | 5    | nickname    | varchar(50)         |      | PRI      |        | 昵称                     |
  | 6    | age         | tinyint(3)          |      | PRI      |        | 年龄                     |
  | 7    | sex         | varchar(5)          |      | PRI      |        | 性别                     |
  | 8    | info        | varchar(500)        |      | PRI      |        | 个人介绍                 |
  | 9    | create_time | int(11)             |      | PRI      |        | 注册时间                 |
  | 10   | update_time | int(11)             |      | PRI      |        | 修改时间                 |

- sql

  ```sql
    CREATE TABLE `user` (
        `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '自增 id',
        `userid` bigint(20) UNSIGNED NOT NULL COMMENT '用户 userid，普通索引',
        `status` tinyint(3) UNSIGNED NOT NULL DEFAULT '0' COMMENT '用户状态，0 注册 -1 注销',
        `username` varchar(50) NOT NULL DEFAULT '' COMMENT '用户名',
        `nickname` varchar(50) NOT NULL DEFAULT '' COMMENT '昵称',
        `age` tinyint(3) NOT NULL DEFAULT '0' COMMENT '年龄',
        `sex` varchar(5) NOT NULL DEFAULT '' COMMENT '性别',
        `info` varchar(500) NOT NULL DEFAULT '' COMMENT '个人介绍',
        `create_time` int(11) UNSIGNED NOT NULL DEFAULT '0' COMMENT '注册时间',
        `update_time` int(11) UNSIGNED NOT NULL DEFAULT '0' COMMENT '修改时间',
        PRIMARY KEY (`id`),
        KEY `userid` (`userid`)
    ) ENGINE = InnoDB CHARSET = utf8;
  ```

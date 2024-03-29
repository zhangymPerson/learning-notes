# 开发文档

- 日期:2022-11-30 18:31:22

- 编写人员:danao (email_name@163.com)

- 版本:1.0

| 文档编号 | 题目     | 作者/修改 | 创建/修改时间       | 最新版本号 | 摘要说明       |
| -------- | -------- | --------- | ------------------- | ---------- | -------------- |
| 1-1-001  | 开发文档 | danao     | 2022-12-01 09:49:17 | 1.0        | 开发文档第一版 |

## 概要

（编写目的，项目背景，定义，参考资料）

## 需求分析

\*\*项目主要是解决什么问题。

### 需求分析

### 需求分析报告的编制者

### 需求报告审评

### 需求报告格式

## 概要设计

项目的主要技术方案

### 设计目标

需求的简要描述，为完成需求要做一个什么东西 / 实现一个什么功能

### 设计方案

### 核心逻辑

描述如何实现，包括核心逻辑的执行流程、重要数据流向、模块之间工作方式等，复杂逻辑用图表加强说明

### 技术选型

使用的编程语言、设计模式、框架、中间件、第三方组件、数据库、RPC 等

## 详细设计

### 主要模块

本项目分位几个模块，主要有
模块划分
从逻辑上拆分为哪些模块，模块各自的功能以及模块间的交互形态；涉及模块重构，需要做哪些调整

#### 子模块 1

子模块 1 主要实现了\*\*功能

- 数据模型

  描述所用到、需要调整的数据结构，包括：

  数据库表结构

  内存数据结构

#### 子模块 2

子模块 2 主要实现了\*\*功能

### 数据库表结构设计

（E-R 图：实体-联系图 Entity Relationship Diagram）

#### 数据库基本信息

| 序号 | 表名 | 说明   |
| ---- | :--- | ------ |
| 1    | user | 用户表 |

##### user 表的说明

| 序号 | 字段名  | 数据类型  | 可以非空 | 键类型 | 默认值            | 注释                                      |
| ---- | ------- | --------- | -------- | ------ | ----------------- | ----------------------------------------- |
| 1    | id      | bigint    | NO       | PRI    |                   | id 一般为自增                             |
| 2    | name    | varchar   | YES      |        |                   | 姓名                                      |
| 3    | status  | int       | YES      |        |                   | 数据状态，-1 为逻辑删除，0，>0 为可用状态 |
| 4    | ctime   | timestamp | YES      |        | CURRENT_TIMESTAMP | 创建时间                                  |
| 5    | mtime   | timestamp | YES      |        |                   | 修改时间                                  |
| 6    | remark  | varchar   | YES      |        |                   | 备注                                      |
| 7    | type    | varchar   | YES      |        |                   | 类型                                      |
| 8    | version | varchar   | YES      |        |                   | 版本                                      |

### 图例

#### 业务流程图、时序图-用户

（按照人操作的维度）

#### 程序流程图、时序图-代码

（按照代码执行的维度）

### 接口约定

（对外公开的方法、api 接口等）

#### 接口文档的链接

### 其他

（伪代码、类图、思维导图、泳道流程图，对安全、性能、边界情况、性价比的思考）

- 可用性：考虑极端情况下是否能够正常工作、会展现出什么样的行为

- 可扩展性：问题规模上升时的性能变化；模块是否需要一定通用性，设计上满足后续需求

- 可部署性：部署复杂程度、不同部署平台支持；不同部署模式下功能取舍

- 可维护性：代码组织直观的功能代码分布与隔离；代码复用要求，划分基础功能代码（可复用）与业务逻辑代码（不可复用），复杂逻辑的

- 抽象与封装；其他扩展功能

- 兼容性：现有版本升级后可能出现的问题；模块之间版本不一致是否可以兼容

- 分模块复杂度预估

- 代码量（精确到量级即可），及实现所需人天估算

## 软件的编码说明

### 软件编码

### 软件编码的要求

### 编码的评审

## 参考资料

（附加的解释和说明、引用资料）

## 评审情况

# \*\*项目接口说明文档

- 日期:2022-11-30 18:31:22

- 编写人员:danao (email_name@163.com)

- 版本:1.1

| 文档编号 | 题目     | 作者/修改 | 创建/修改时间       | 最新版本号 | 摘要说明       |
| -------- | -------- | --------- | ------------------- | ---------- | -------------- |
| 1-1-001  | 开发文档 | danao     | 2022-12-01 09:49:17 | 1.0        | 开发文档第一版 |
| 1-1-002  | 开发文档 | danao     | 2024-02-26 10:34:03 | 1.1        | 开发文档 修改  |

## 概述

- 项目主要是处理:

  1.\*\*\*

  2.\*\*\*

### 相关概念

- 项目涉及的一些概念说明:

  1.模块 1 \*\*\*

  2.模块 2 \*\*\*

### 环境说明

- 服务器环境

  host:127.0.0.1

  port:8080

- 请求地址

  http:127.0.0.1:8080/

### 接口概览

- 版本控制

  如果需要版本控制，则所有请求添加版本前缀

  如: `http://127.0.0.1:8080/v1/`

- 接口权限说明

  需要加权限访问的接口,通过结构后面的\*表示，带\*的接口说明需要添加权限访问

- 接口列表

  | 名称                                      | 地址             | 请求方式 | 说明             | 备注         |
  | ----------------------------------------- | ---------------- | -------- | ---------------- | ------------ |
  | [测试项目是否启动](#get-测试项目是否启动) | /ping            | get      | 检查项目是否启动 | success 成功 |
  | [用户注册](#post-注册接口)                | /v1/api/register | post     | 用户进行注册     |              |
  | [用户登录](#post-登录接口)                | /v1/api/login    | post     | 用户进行登录     |              |
  | [获取单个用户信息](#get-获取用户信息)\*   | /v1/api/user     | get      | 获取单个信息     |              |
  | [获取用户列表](#get-获取用户列表)\*       | /v1/api/users    | get      | 获取用户列表     |              |

### 权限说明

### 全局错误码定义

| 错误码 | 说明         | 备注 |
| ------ | ------------ | ---- |
| 200    | 请求成功     |      |
| 500    | 请求失败     |      |
| 500100 | 用户已经存在 |      |
| 500101 | 用户不存在   |      |

### 对象结构概览

| 名称 | 说明                  | 备注 |
| ---- | --------------------- | ---- |
| user | [用户结构](#用户结构) |      |

## 接口说明

## GET 测试项目是否启动

GET /ping

> 请求示例

```shell
curl -X GET "http://127.0.0.1:8080/ping"
```

### 请求参数

空

> 返回示例
> 200 Response

### 返回数据

```json
{
  "message": "success"
}
```

## POST 注册接口

POST /v1/api/register

> 请求示例

```shell
curl -X POST "http://127.0.0.1:8080/v1/api/register" -d '{"username":"zhangsan","password":"123456"}'
```

### 请求参数

> Body 请求参数示例

```json
{
  "username": "zhangsan",
  "password": "123456"
}
```

| 名称       | 位置 | 类型   | 必选 | 说明   |
| ---------- | ---- | ------ | ---- | ------ |
| body       | body | object | 是   | none   |
| » username | body | string | 是   | 用户名 |
| » password | body | string | 是   | 密码   |

### 返回数据

> 返回示例

> 200 Response

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "userid": "123456",
    "token": "123456"
  }
}
```

状态码 **200**

| 名称      | 类型    | 必选 | 约束 | 中文名  | 说明 |
| --------- | ------- | ---- | ---- | ------- | ---- |
| » code    | integer | true | none |         | none |
| » msg     | string  | true | none |         | none |
| » data    | object  | true | none |         | none |
| »» userid | string  | true | none | 用户 id | none |
| »» token  | string  | true | none | token   | none |

## POST 登录接口

POST /v1/api/register

> 请求示例

```shell
curl -X POST "http://127.0.0.1:8080/v1/api/register" -d '{"username":"zhangsan","password":"123456"}'
```

### 请求参数

> Body 请求参数示例

```json
{
  "username": "string",
  "password": "string"
}
```

| 名称       | 位置 | 类型   | 必选 | 说明   |
| ---------- | ---- | ------ | ---- | ------ |
| body       | body | object | 否   | none   |
| » username | body | string | 是   | 用户名 |
| » password | body | string | 是   | 密码   |

### 返回数据

> 返回示例

> 200 Response

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "userid": "123456",
    "token": "123456"
  }
}
```

> 结构

状态码 **200**

| 名称      | 类型    | 必选 | 约束 | 中文名  | 说明 |
| --------- | ------- | ---- | ---- | ------- | ---- |
| » code    | integer | true | none |         | none |
| » msg     | string  | true | none |         | none |
| » data    | object  | true | none |         | none |
| »» userid | string  | true | none | 用户 id | none |
| »» token  | string  | true | none | token   | none |

## GET 获取用户信息

GET /v1/api/user

> 请求示例

```shell
curl -X GET "http://127.0.0.1:8080/v1/api/user?user_id=123456"
```

### 请求参数

| 名称    | 位置  | 类型   | 必选 | 说明    |
| ------- | ----- | ------ | ---- | ------- |
| user_id | query | string | No   | 用户 id |

### 返回结果

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "id": 0,
    "updated_at": 0,
    "created_at": 0,
    "user_id": "string",
    "username": 0,
    "info": 0
  }
}
```

| 名称          | 类型    | 必选  | 约束 | 中文名 | 说明     |
| ------------- | ------- | ----- | ---- | ------ | -------- |
| » code        | integer | true  | none |        | none     |
| » msg         | string  | true  | none |        | none     |
| » data        | object  | true  | none |        | none     |
| »» user_id    | string  | false | none |        | 用户 id  |
| »» updated_at | integer | false | none |        | 更新时间 |
| »» created_at | integer | false | none |        | 创建时间 |
| »» username   | string  | false | none |        | 用户名   |
| »» info       | string  | false | none |        | 其他信息 |

## GET 获取用户列表

GET /v1/api/users

> 请求示例

```shell
curl -X GET "http://127.0.0.1:8080/v1/api/users?offset=0&limit=10&sort=desc&sort_key=id&create_time[]=1597520000&create_time[]=1597520000&update_time[]=1597520000&update_time[]=15975200"
```

### 请求参数

| 名称          | 位置  | 类型          | 必选 | 说明          |
| ------------- | ----- | ------------- | ---- | ------------- |
| offset        | query | string        | 否   | none          |
| limit         | query | string        | 否   | none          |
| sort          | query | string        | 否   | 排序方式 升降 |
| sort_key      | query | array[string] | 否   | 排序字段      |
| create_time[] | query | array[string] | 否   | 起止时间戳    |
| update_time[] | query | array[string] | 否   | 起止时间戳    |

### 返回结果

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "total": 0,
    "List": [
      {
        "id": 0,
        "updated_at": 0,
        "created_at": 0,
        "user_id": "string",
        "username": 0,
        "info": 0
      }
    ]
  }
}
```

状态码 **200**

| 名称           | 类型    | 必选  | 约束 | 中文名 | 说明     |
| -------------- | ------- | ----- | ---- | ------ | -------- |
| » code         | integer | true  | none |        | none     |
| » msg          | string  | true  | none |        | none     |
| » data         | object  | true  | none |        | none     |
| »» total       | integer | true  | none |        | 总数     |
| »»» user_id    | string  | false | none |        | 用户 id  |
| »»» updated_at | integer | false | none |        | 更新时间 |
| »»» created_at | integer | false | none |        | 创建时间 |
| »»» username   | string  | false | none |        | 用户名   |
| »»» info       | string  | false | none |        | 其他信息 |

## 对象结构说明

### 用户结构

| 字段名   | 字段类型 | 字段说明 | 默认值       | 可能为空/null | 备注 |
| -------- | -------- | -------- | ------------ | ------------- | ---- |
| username | string   | 用户名   | admin        | no            |
| password | string   | 密码     | \*\*\*\*\*\* | no            |

## GET Get 请求示例

GET /v1/api/get

> 请求示例

```shell
curl -X GET "http://127.0.0.1:8080/v1/api/get?key=value"
```

### 请求参数

| 名称 | 位置  | 类型   | 必选 | 说明 |
| ---- | ----- | ------ | ---- | ---- |
| key  | query | string | 否   |      |

### 返回结果

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "info": "string"
  }
}
```

| 名称   | 类型    | 必选 | 约束 | 中文名 | 说明 |
| ------ | ------- | ---- | ---- | ------ | ---- |
| » code | integer | true | none |        | none |
| » msg  | string  | true | none |        | none |
| » data | object  | true | none |        | none |
| »»info |         |      |      |        | none |

## POST Post 请求示例

POST /v1/api/post

> 请求示例

```shell
curl -X POST "http://127.0.0.1:8080/v1/api/post" -H "Content-Type: application/json" -d '{"key":"value"}'
```

### 请求参数

> 请求示例

```json
{
  "key": "value"
}
```

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| key  | body | string | 否   |      |

### 返回结果

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "info": "string"
  }
}
```

| 名称   | 类型    | 必选 | 约束 | 中文名 | 说明 |
| ------ | ------- | ---- | ---- | ------ | ---- |
| » code | integer | true | none |        | none |
| » msg  | string  | true | none |        | none |
| » data | object  | true | none |        | none |
| »»info |         |      |      |        | none |

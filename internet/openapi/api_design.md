# api 接口设计

## 接口参数设计

- 接口设计规范

  [openapi](https://www.openapis.org/)

  [openapi-中文规范](https://openapi.apifox.cn/)

  [openapi-github](https://github.com/OAI)

  [OpenAPITools](https://github.com/OpenAPITools)

## RESTful 请求

## 异常处理/错误码

- 服务器向用户返回的状态码和提示信息，常见的有以下一些（方括号中是该状态码对应的 HTTP 动词）。

  | 状态码 | 请求方式                               | 说明                                                                       |
  | ------ | -------------------------------------- | -------------------------------------------------------------------------- |
  | 200    | OK - [GET]                             | 服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。               |
  | 201    | CREATED - [POST/PUT/PATCH]             | 用户新建或修改数据成功。                                                   |
  | 202    | Accepted - [*]                         | 表示一个请求已经进入后台排队（异步任务）                                   |
  | 204    | NO CONTENT - [DELETE]                  | 用户删除数据成功。                                                         |
  | 400    | INVALID REQUEST - [POST/PUT/PATCH]     | 用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。 |
  | 401    | Unauthorized - [*]                     | 表示用户没有权限（令牌、用户名、密码错误）。                               |
  | 403    | Forbidden - [*]                        | 表示用户得到授权（与 401 错误相对），但是访问是被禁止的。                  |
  | 404    | NOT FOUND - [*]                        | 用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。   |
  | 406    | Not Acceptable - [GET]                 | 用户请求的格式不可得（比如用户请求 JSON 格式，但是只有 XML 格式）。        |
  | 410    | Gone -[GET]                            | 用户请求的资源被永久删除，且不会再得到的。                                 |
  | 422    | Unprocesable entity - [POST/PUT/PATCH] | 当创建一个对象时，发生一个验证错误。                                       |
  | 500    | INTERNAL SERVER ERROR - [*]            | 服务器发生错误，用户将无法判断发出的请求是否成功。                         |

## vscode 下使用 openapi 需要使用插件

- `OpenAPI (Swagger) Editor`

- 编写 openapi 对应的 yaml 文件

# curl 中常用的命令

## 常用参数说明

| 参数         | 说明                     | 备注                                                                                      |
| ------------ | ------------------------ | ----------------------------------------------------------------------------------------- |
| -X/--request | 请求方式                 | 如 GET POST                                                                               |
| -d/--data    | HTTP POST 方式传送数据   | `--data-raw '{"key":"value"}'` 这种格式发送 json 数据                                     |
| -H/--header  | 自定义头信息传递给服务器 | `-H 'token:GGXKskdfksfl='`这种方式传递 token 如果是多个可以使用 `-H 'a:b' -H 'key:value'` |

- 直接 get 请求

  `curl https://baidu.com`

- 带 token 的 get 请求

  ```sh
  curl -X GET -H 'token:aaa' http://baidu.com
  ```

- post 中的 json 请求

  `curl -H "Content-type: application/json" -X POST -d '{"username":"username","password":"password"}' https://baidu.com`

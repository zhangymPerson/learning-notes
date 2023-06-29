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

  `curl -X GET -H 'token:aaa' http://baidu.com`

- post 表单参数

  除了 post json，我们还常常需要 post 表单的键值对参数

  `curl -X POST -d 'nam=bin&content=hello' https://www.example.com/hello`

- post 中的 json 请求

  `curl -H "Content-type: application/json" -X POST -d '{"username":"username","password":"password"}' https://www.example.com`

- curl 下载 wget 下载失败或者报错时

  `curl -O -L https://spacevim.org/cn/install.sh`

- curl cookie

  使用 `--cookie 'cookie值'`

  `curl -H 'Content-Type: application/json; charset=UTF-8' --cookie "admin_token=00000763aZQ8GP5U" -X POST -d '{"name":"binecy","content":"hello"}' https://www.example.com`

  使用 `-b` 参数

  `curl -b 'foo=bar' https://www.example.com`

  使用 `-c` 参数
  -c 参数将服务器设置的 Cookie 写入一个文件。

  `curl -c cookies.txt https://www.example.com`

- 调试

  `-v` 参数输出通信的整个过程，用于调试。

  `curl -v https://www.example.com`

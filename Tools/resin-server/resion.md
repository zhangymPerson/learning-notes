# Resin 服务器

## 目录

## 其他

- [官网](https://caucho.com/)

- [官方文档](https://caucho.com/resin-4.0/admin/config.xtp)

### 安装启动

- 官网找到下载源文件

- 解压到指定目录

- 启动方式

  `linux` 下执行

  ```sh
  # 到解压后的bin目录下
  cd ~/resin/bin/

  # 先不加载自己的 war 包
  # 执行启动命令
  sh resin.sh start
  # 执行关闭命令
  sh resin.sh stop
  # 查看日志
  #进入日志目录
  cd ~/resin/log/
  # 查看日志 主日志文件
  tail -f jvm-app-0.log
  ```

- 加载自己的 `war` 包

  拷贝自己的 `web.war` 包 到 `~/resin/webapps/` 目录下

  按照上文进行启动，查看日志看是否启动成功

### 配置文件说明

- 说明 resin 项目启动一般有 3 个接口

  - WatchDog 的端口，默认 6600
  - Server 监控端口，默认 6800
  - 应用的 HTTP 端口，默认 8080

- resin.properties

  常见的服务配置信息都在这个位置，这里定义的变量可以用在 `resin.xml` 文件中
  |属性 key|说明|
  |-|-|
  |app_servers|集群应用服务器层的 IP 地址列表，每个 IP 对于一个服务器|
  |app.http|每个应用服务器层的 HTTP 端口号|
  |jvm_args|配置 Resin 实体的 Java 参数|

- resin.xml

# elasticsearch 的学习使用

## 目录

- [返回总目录](../../README.md#项目目录)
- [返回大数据目录](../README.md)
- [基础介绍.md](./基础介绍.md)

## 其他

- [Elasticsearch 权威指南-github 版本](https://github.com/looly/elasticsearch-definitive-guide-cn)
- [中文官网](https://www.elastic.co/cn/)
- [Elasticsearch: 权威指南-官网版](https://www.elastic.co/guide/cn/elasticsearch/guide/current/index.html)

## 安装测试

- 下载

  [中文官网](https://www.elastic.co/cn/elasticsearch/)

- 启动

  解压安装包，直接打开 `~/bin` 目录，启动文件 `elasticsearch` windows 下 `elasticsearch.bat` 启动

  **注意：在启动时，权限问题，windows 下需要右键单击管理员权限启动，否则不能正确创建索引，请求无响应，但不报错**

  启动运行依赖 `jvm`

- 启动查看

  ```sh
  curl localhost:9200
  curl 127.0.0.1.9200
  #windows 下
  curl.exe 127.0.0.1:9200
  ```

  返回结果

  ```json
  {
    "name": "DESKTOP-2FRSCJO",
    "cluster_name": "elasticsearch",
    "cluster_uuid": "1LlGxlFVR92t09wJOy-OaQ",
    "version": {
      "number": "7.6.0",
      "build_flavor": "default",
      "build_type": "zip",
      "build_hash": "7f634e9f44834fbc12724506cc1da681b0c3b1e3",
      "build_date": "2020-02-06T00:09:00.449973Z",
      "build_snapshot": false,
      "lucene_version": "8.4.0",
      "minimum_wire_compatibility_version": "6.8.0",
      "minimum_index_compatibility_version": "6.0.0-beta1"
    },
    "tagline": "You Know, for Search"
  }
  ```

## web 可视化支持

- GitHub 项目

  依赖开源项目 **[https://github.com/mobz/elasticsearch-head](https://github.com/mobz/elasticsearch-head)**

- 需要 nodejs 环境的支持

  [安装 nodejs](../../programming-language/JavaScript/node/nodejs.md)

- 安装 nodejs 的一个构建工具 `grunt`

  安装命令 `npm install -g grunt-cli`

- 下载安装启动该开源项目

  ```sh
  #下载
  git clone https://github.com/mobz/elasticsearch-head.git
  #在源码目录构建
  npm install
  #在源码目录启动
  grunt server
  ```

  浏览器打开 http://127.0.0.1:9100 连接 es 集群 127.0.0.01:9200

  **注意 es 集群需要配置跨域服务。配置内容如下，配置完成后重启服务**

  配置文件在 es 安装目录下的 `~/conf/elasticsearch.yml` 添加如下配置

  ```yml
  #允许elasticsearch跨越访问
  http.cors.enabled: true
  http.cors.allow-origin: "*"
  ```

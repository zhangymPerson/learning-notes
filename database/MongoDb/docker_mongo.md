# docker 中安装 mongodb

> 查询 - 拉取 - 配置 - 安装

## 查询

- 查询命令
  `docker search mongo`

## 拉取

- 拉取镜像
  `docker pull mongo:latest`

## 配置-运行

- 指定端口

  `docker run -p 27018:27017 mongo:latest`

- 用户名密码

  `docker run -p 27018:27017 --auth mongo:latest`

- 指定数据目录

  ```sh
  #创建数据目录
  mkdir  -p /opt/docker/mongo/12017/data
  #指定数据目录启动
  docker run -p 27017:27017 -v /opt/docker/mongo/12017/data:/data/db --name mongodb -d mongo:latest
  ```

- 其他复杂配置和启动方式参考 https://hub.docker.com/_/mongo

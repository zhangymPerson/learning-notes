# 使用 docker 安装 elasticsearch

> 查询 - 拉取 - 配置 - 安装

## 查询

- 查询命令
  `docker search elasticsearch`

## 拉取

- 拉取镜像
  `docker pull elasticsearch:latest`

## 配置-运行

- 指定端口

  `docker run -p 9200:9200 elasticsearch:latest`

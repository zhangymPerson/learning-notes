# docker-compose

- [官方文档](https://docs.docker.com/compose/)

- [github](https://github.com/docker/compose)

- [使用样例](https://github.com/docker/awesome-compose)

- [菜鸟教程](https://m.runoob.com/docker/docker-compose.html)

## 简介

- Docker Compose 是一个用来定义和运行复杂应用的 Docker 工具。一个使用 Docker 容器的应用，通常由多个容器组成。使用 Docker Compose 不再需要使用 shell 脚本来启动容器。

## 使用

- 编写 docker-compose.yml 文件

- 检查 docker-compose 配置
  
  `docker-compose config`

  可以在 docker-compose.yml 文件目录中配置 .env 文件夹 添加变量，然后在 docker_compose 文件中使用 `${}` 中引用

- 启动

  `docker-compose up`

- 后台启动

  `docker-compose up -d`

- 关闭

  `docker-compose stop`

- 关闭并删除

  `docker-compose down`

- 关闭并删除镜像信息

  `docker-compose down -v`

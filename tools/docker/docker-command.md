# docker 常用命令

- [返回](./README.md)

- 查询某个镜像文件

  ```sh
  docker search ***
  ```

  查询网址:

  [https://hub.docker.com/](https://hub.docker.com/)

- 常用仓库命令

  | 操作   | 命令                                                  | 说明                                                                     |
  | ------ | ----------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------- |
  | 检索   | docker search                                         | 关键字如：docker search redis                                            | 经常会去 docker hub 上检索镜像的详细信息 |
  | 拉取   | docker pull 镜像名:tag                                | :tag 是可选的，tag 表示标签，通常是软件的版本号，默认是 latest(即最新版) |
  | 列表   | docker images                                         | 查看所有本地镜像                                                         |
  | 删除   | docker rmi image-id                                   | 删除指定的本地镜像                                                       |
  | 传文件 | docker cp /home/work/path containerid:/home/work/path | 传本地文件到 docker 容器内部                                             |

- 常用操作

  停止已经退出的容器 `docker stop $(docker ps -a | grep "Exited" | awk '{print $1 }')`

  删除已经退出的容器 `docker rm $(docker ps -a | grep "Exited" | awk '{print $1 }')`

  删除 none 的镜像 `docker rmi $(docker images | grep "none" | awk '{print $3}')`

## docker 进入容器 修改配置文件

- docker 中没有 vi vim 等编辑器时 需要复制文件/或者安装 vi/vim

- 复制容器内文件到宿主机，修改后复制回去

  docker 复制文件到宿主机 -> 修改相关内容 -> 从宿主机到容器

  ```sh
  # dockername 指容器名
  # docker cp 容器名:要拷贝的文件在容器里面的路径 要拷贝到宿主机的相应路径
  docker cp dockername:/data/test.log /home/main/log/
  # docker cp 要拷贝到宿主机的相应路径 容器名:要拷贝的文件在容器里面的路径
  docker cp /home/main/log/test.log dockername:/data/test.log
  ```

## docker 查看仓库镜像版本

- 网址上查询 (需要科学上网)

  <https://hub.docker.com/>

- 命令

  以查询 mysql 版本号为例

  `curl https://registry.hub.docker.com/v1/repositories/mysql/tags`

  返回的是 json

  ```json
  [
    { "layer": "", "name": "latest" },
    { "layer": "", "name": "5" },
    ...
    { "layer": "", "name": "8.0.4" },
    { "layer": "", "name": "8.0.4-rc" }
  ]
  ```

## docker 查看所有本地镜像

- `docker images | grep -v TAG | awk '{print $1":"$2}'`

## docker 导出保存镜像

- `docker save $image_name -o ${dir}/${tar_name}.tar`

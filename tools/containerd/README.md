# Containerd 容器

- 官网
  [containerd](https://containerd.io/)

## containerd 容器相关的命令

### 命名空间

ctr 是 containerd 自带的 CLI 命令行工具，ctr 命令运行的默认 命名空间 是在：default

- ctr 查看命名空间

  `ctr ns ls`

### 镜像相关

- 拉取远程镜像

  ctr 比较严格，需要完整的 URL 路径：docker.io/library/[镜像名称]:[tag]

  `ctr image pull docker.io/library/redis:latest` 这个 crictl 查询不到镜像

  指定 命名空间 拉取镜像 指定命名空间后 crictl 可以查到

  `ctr -n k8s.io image pull docker.io/library/redis:latest`

crictl image ls

- 查看镜像情况（查不到上面拉取的镜像）

  `crictl image ls`

- 命令 ctr 查看镜像情况（可以查到上面拉取的镜像）

  `ctr image ls`

### 容器相关的命令

- 查看容器运行信息

  `ctr container ls`

- 运行一个新的容器

  `ctr run -t -d docker.io/library/image:tag container_name` 需指定容器名称

  使用宿主机网络

  `ctr run --net-host -t -d docker.io/library/image:tag container_name ` 需指定容器名称

### 启动后 task 相关的

- 查看容器运行状态(其实是查看任务，这个跟 ctr container ls 是分开的)

  `ctr task ls`

- 进入容器中

  进入容器

  注意:**--exec-id 必须指定进入容器时的一个名称，是唯一不能重复使用的**

  如果发送断开再用这个名称就报错了，只能用另外一个名称

  `ctr t exec --exec-id datax -t datax1 /bin/bash`

- 停止容器

  `ctr t ls |grep name` 查找到容器

  `ps -ef |grep pid` 查找容器对应的 pid 然后 `kill -0 pid` 掉那个进程 可以看到容器处于 stop 状态

  `ctr t rm name` 移除掉运行中的容器 
  
  `ctr c rm name` 删除掉静态的容器

## 与 docker 的比较和在 k8s 下的一些命令

- command 比较
  | 命令                 | Docker         | crictl（kubernetes） | ctr (Containerd)                                  |
  | -------------------- | -------------- | -------------------- | ------------------------------------------------- |
  |                      | docker         | crictl（推荐）       | ctr                                               |
  | 查看容器列表         | docker ps      | crictl ps            | ctr -n k8s.io c ls / ctr task ls/ctr container ls |
  | 查看容器详情         | docker inspect | crictl inspect       | ctr -n k8s.io c info                              |
  | 查看容器日志         | docker logs    | crictl logs          | 无                                                |
  | 容器内执行命令       | docker exec    | crictl exec          | 无                                                |
  | 挂载容器             | docker attach  | crictl attach        | 无                                                |
  | 显示容器资源使用情况 | docker stats   | crictl stats         | 无                                                |
  | 创建容器             | docker create  | crictl create        | ctr -n k8s.io c create                            |
  | 启动容器             | docker start   | crictl start         | ctr -n k8s.io run                                 |
  | 停止容器             | docker stop    | crictl stop          | 无                                                |
  | 删除容器             | docker rm      | crictl rm            | ctr -n k8s.io c del                               |
  | 查看镜像列表         | docker images  | crictl images        | ctr -n k8s.io i ls /ctr image ls                  |
  | 查看镜像详情         | docker inspect | crictl inspecti      | 无                                                |
  | 拉取镜像             | docker pull    | crictl pull          | ctr -n k8s.io i pull                              |
  | 推送镜像             | docker push    | 无 ctr               | -n k8s.io i push                                  |
  | 删除镜像             | docker rmi     | crictl rmi           | ctr -n k8s.io i rm                                |
  | 查看 Pod 列表        | 无             | crictl pods          | 无                                                |
  | 查看 Pod 详情        | 无             | crictl inspectp      | 无                                                |
  | 启动 Pod             | 无             | crictl runp          | 无                                                |
  | 停止 Pod             | 无             | crictl stopp         | 无                                                |
  | 运行一个新的容器     | docker run     | 无（最小单元为 pod） | ctr run                                           |
  | 导入镜像             | docker load    | 无                   | ctr image import                                  |
  | 导出镜像             | docker save    | 无                   | ctr image export                                  |

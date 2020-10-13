# docker 常用命令

- 查询某个镜像文件

  ```sh
  docker search ***
  ```

  查询网址:

  [https://hub.docker.com/](https://hub.docker.com/)

- 常用仓库命令

  | 操作 | 命令                   | 说明                                                                     |
  | ---- | ---------------------- | ------------------------------------------------------------------------ |
  | 检索 | docker search          | 关键字如：docker search redis                                            | 经常会去 docker hub 上检索镜像的详细信息 |
  | 拉取 | docker pull 镜像名:tag | :tag 是可选的，tag 表示标签，通常是软件的版本号，默认是 latest(即最新版) |
  | 列表 | docker images          | 查看所有本地镜像                                                         |
  | 删除 | docker rmi image-id    | 删除指定的本地镜像                                                       |

  ```sh
  > docker --help
  Usage:	docker [OPTIONS] COMMAND

  A self-sufficient runtime for containers

  Options:
        --config string      Location of client config files (default "/root/.docker")
    -D, --debug              Enable debug mode
    -H, --host list          Daemon socket(s) to connect to
    -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
        --tls                Use TLS; implied by --tlsverify
        --tlscacert string   Trust certs signed only by this CA (default "/root/.docker/ca.pem")
        --tlscert string     Path to TLS certificate file (default "/root/.docker/cert.pem")
        --tlskey string      Path to TLS key file (default "/root/.docker/key.pem")
        --tlsverify          Use TLS and verify the remote
    -v, --version            Print version information and quit

  Management Commands:
    builder     Manage builds
    config      Manage Docker configs
    container   Manage containers
    engine      Manage the docker engine
    image       Manage images
    network     Manage networks
    node        Manage Swarm nodes
    plugin      Manage plugins
    secret      Manage Docker secrets
    service     Manage services
    stack       Manage Docker stacks
    swarm       Manage Swarm
    system      Manage Docker
    trust       Manage trust on Docker images
    volume      Manage volumes

  Commands:
    attach      Attach local standard input, output, and error streams to a running container
    build       Build an image from a Dockerfile
    commit      Create a new image from a container's changes
    cp          Copy files/folders between a container and the local filesystem
    create      Create a new container
    diff        Inspect changes to files or directories on a container's filesystem
    events      Get real time events from the server
    exec        Run a command in a running container
    export      Export a container's filesystem as a tar archive
    history     Show the history of an image
    images      List images
    import      Import the contents from a tarball to create a filesystem image
    info        Display system-wide information
    inspect     Return low-level information on Docker objects
    kill        Kill one or more running containers
    load        Load an image from a tar archive or STDIN
    login       Log in to a Docker registry
    logout      Log out from a Docker registry
    logs        Fetch the logs of a container
    pause       Pause all processes within one or more containers
    port        List port mappings or a specific mapping for the container
    ps          List containers
    pull        Pull an image or a repository from a registry
    push        Push an image or a repository to a registry
    rename      Rename a container
    restart     Restart one or more containers
    rm          Remove one or more containers
    rmi         Remove one or more images
    run         Run a command in a new container
    save        Save one or more images to a tar archive (streamed to STDOUT by default)
    search      Search the Docker Hub for images
    start       Start one or more stopped containers
    stats       Display a live stream of container(s) resource usage statistics
    stop        Stop one or more running containers
    tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
    top         Display the running processes of a container
    unpause     Unpause all processes within one or more containers
    update      Update configuration of one or more containers
    version     Show the Docker version information
    wait        Block until one or more containers stop, then print their exit codes
  ```

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

  https://hub.docker.com/

- 命令

  以查询 mysql 版本号为例

  `curl https://registry.hub.docker.com/v1/repositories/mysql/tags`

  返回的是 json

  ```json
  [
    { "layer": "", "name": "latest" },
    { "layer": "", "name": "5" },
    { "layer": "", "name": "5.5" },
    { "layer": "", "name": "5.5.40" },
    { "layer": "", "name": "5.5.41" },
    { "layer": "", "name": "5.5.42" },
    { "layer": "", "name": "5.5.43" },
    { "layer": "", "name": "5.5.44" },
    { "layer": "", "name": "5.5.45" },
    { "layer": "", "name": "5.5.46" },
    { "layer": "", "name": "5.5.47" },
    { "layer": "", "name": "5.5.48" },
    { "layer": "", "name": "5.5.49" },
    { "layer": "", "name": "5.5.50" },
    { "layer": "", "name": "5.5.51" },
    { "layer": "", "name": "5.5.52" },
    { "layer": "", "name": "5.5.53" },
    { "layer": "", "name": "5.5.54" },
    { "layer": "", "name": "5.5.55" },
    { "layer": "", "name": "5.5.56" },
    { "layer": "", "name": "5.5.57" },
    { "layer": "", "name": "5.5.58" },
    { "layer": "", "name": "5.5.59" },
    { "layer": "", "name": "5.5.60" },
    { "layer": "", "name": "5.5.61" },
    { "layer": "", "name": "5.5.62" },
    { "layer": "", "name": "5.6" },
    { "layer": "", "name": "5.6.17" },
    { "layer": "", "name": "5.6.20" },
    { "layer": "", "name": "5.6.21" },
    { "layer": "", "name": "5.6.22" },
    { "layer": "", "name": "5.6.23" },
    { "layer": "", "name": "5.6.24" },
    { "layer": "", "name": "5.6.25" },
    { "layer": "", "name": "5.6.26" },
    { "layer": "", "name": "5.6.27" },
    { "layer": "", "name": "5.6.28" },
    { "layer": "", "name": "5.6.29" },
    { "layer": "", "name": "5.6.30" },
    { "layer": "", "name": "5.6.31" },
    { "layer": "", "name": "5.6.32" },
    { "layer": "", "name": "5.6.33" },
    { "layer": "", "name": "5.6.34" },
    { "layer": "", "name": "5.6.35" },
    { "layer": "", "name": "5.6.36" },
    { "layer": "", "name": "5.6.37" },
    { "layer": "", "name": "5.6.38" },
    { "layer": "", "name": "5.6.39" },
    { "layer": "", "name": "5.6.40" },
    { "layer": "", "name": "5.6.41" },
    { "layer": "", "name": "5.6.42" },
    { "layer": "", "name": "5.6.43" },
    { "layer": "", "name": "5.6.44" },
    { "layer": "", "name": "5.6.45" },
    { "layer": "", "name": "5.6.46" },
    { "layer": "", "name": "5.6.47" },
    { "layer": "", "name": "5.6.48" },
    { "layer": "", "name": "5.6.49" },
    { "layer": "", "name": "5.7" },
    { "layer": "", "name": "5.7.10" },
    { "layer": "", "name": "5.7.11" },
    { "layer": "", "name": "5.7.12" },
    { "layer": "", "name": "5.7.13" },
    { "layer": "", "name": "5.7.14" },
    { "layer": "", "name": "5.7.15" },
    { "layer": "", "name": "5.7.16" },
    { "layer": "", "name": "5.7.17" },
    { "layer": "", "name": "5.7.18" },
    { "layer": "", "name": "5.7.19" },
    { "layer": "", "name": "5.7.20" },
    { "layer": "", "name": "5.7.21" },
    { "layer": "", "name": "5.7.22" },
    { "layer": "", "name": "5.7.23" },
    { "layer": "", "name": "5.7.24" },
    { "layer": "", "name": "5.7.25" },
    { "layer": "", "name": "5.7.26" },
    { "layer": "", "name": "5.7.27" },
    { "layer": "", "name": "5.7.28" },
    { "layer": "", "name": "5.7.29" },
    { "layer": "", "name": "5.7.30" },
    { "layer": "", "name": "5.7.31" },
    { "layer": "", "name": "5.7.4" },
    { "layer": "", "name": "5.7.4-m14" },
    { "layer": "", "name": "5.7.5" },
    { "layer": "", "name": "5.7.5-m15" },
    { "layer": "", "name": "5.7.6" },
    { "layer": "", "name": "5.7.6-m16" },
    { "layer": "", "name": "5.7.7" },
    { "layer": "", "name": "5.7.7-rc" },
    { "layer": "", "name": "5.7.8" },
    { "layer": "", "name": "5.7.8-rc" },
    { "layer": "", "name": "5.7.9" },
    { "layer": "", "name": "8" },
    { "layer": "", "name": "8.0" },
    { "layer": "", "name": "8.0.0" },
    { "layer": "", "name": "8.0.1" },
    { "layer": "", "name": "8.0.11" },
    { "layer": "", "name": "8.0.12" },
    { "layer": "", "name": "8.0.13" },
    { "layer": "", "name": "8.0.14" },
    { "layer": "", "name": "8.0.15" },
    { "layer": "", "name": "8.0.16" },
    { "layer": "", "name": "8.0.17" },
    { "layer": "", "name": "8.0.18" },
    { "layer": "", "name": "8.0.19" },
    { "layer": "", "name": "8.0.2" },
    { "layer": "", "name": "8.0.20" },
    { "layer": "", "name": "8.0.21" },
    { "layer": "", "name": "8.0.3" },
    { "layer": "", "name": "8.0.4" },
    { "layer": "", "name": "8.0.4-rc" }
  ]
  ```

# 安装

- [docker 中文社区](http://www.docker.org.cn/)

- [docker-菜鸟教程](http://www.runoob.com/docker/docker-tutorial.html)

- [docker-中文文档](http://www.dockerinfo.net/document)

## 安装步骤

### 检查

- 检查内核

  uname -a

### 安装

- 安装必要工具

  sudo yum install -y yum-utils device-mapper-persistent-data lvm2

- 添加 yum 源 (阿里云)

  sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

* 更新 yum 源

  sudo yum makecache fast

* 安装 Docker-ce

  sudo yum -y install docker-ce

* 启动 Docker 后台服务
  **Docker 安装后必须启动，不然很多命令没法使用**

  sudo systemctl start docker

* 配置 docker 镜像

  mkdir /etc/docker/
  vim /etc/docker/daemon.json（Linux）
  添加以下内容
  ```json
  {
  "registry-mirrors": ["http://hub-mirror.c.163.com"]
  }
  ```

- 启动一个 ubuntu

  docker run -it ubuntu bash

- docker 镜像启动查看

  docker ps

- docker 查看镜像

  docker images

- docker 启动报错，在不好排错的情况下

  可以更新系统的依赖库执行一下以下命令

  yum update

- docker 运行报错 **connect to the Docker daemon at unix:///var/run/docker.sock. Is**

  docker 是 cs 架构，运行先需要启动`daemon Process` 守护线程

  执行命令 `systemctl start docker` 然后 `docker stats`

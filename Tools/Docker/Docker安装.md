# 安装

- [docker中文社区](http://www.docker.org.cn/)

- [docker-菜鸟教程](http://www.runoob.com/docker/docker-tutorial.html)

- [docker-中文文档](http://www.dockerinfo.net/document)
## 安装步骤

### 检查

- 检查内核

    uname -a 
### 安装

- 安装必要工具

        sudo yum install -y yum-utils device-mapper-persistent-data lvm2

- 添加yum源 (阿里云)

        sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo


- 更新yum源

        sudo yum makecache fast

- 安装 Docker-ce

        sudo yum -y install docker-ce

- 启动 Docker 后台服务
**Docker安装后必须启动，不然很多命令没法使用**

        sudo systemctl start docker

- 配置docker镜像

        mkdir /etc/docker/
    
        vim /etc/docker/daemon.json（Linux）
    
        #添加以下内容

        
        {
            "registry-mirrors": ["http://hub-mirror.c.163.com"]
        }
        

- 启动一个ubuntu

        docker run -it ubuntu bash

- docker镜像启动查看

        docker ps

- docker 查看镜像

        docker images



# 搭建远程maven仓库

## 使用docker版本的

- 安装
```sh
# 检测是否安装docker
docker -v
#查看仓库中是否有该镜像
docker search nexus
#拉取该镜像
docker pull docker.io/sonatype/nexus3

# 配置存储位置
mkdir -p /usr/local/nexus3/nexus-data
#授权 必须有 这一步
chown -R 200 /usr/local/nexus3/nexus-data
#启动
docker run -tid -p 8081:8081 --name nexus -e NEXUS_CONTEXT=nexus -v /usr/local/nexus3/nexus-data:/nexus-data  docker.io/sonatype/nexus3
```
- 使用
  
   访问：http://ip:8081/nexus  使用默认管理员身份登录，帐号：admin，密码：在文件中

                    

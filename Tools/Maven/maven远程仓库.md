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

## 发布本地项目到远程仓库中

- 发布到远程仓库
   
   mvn install 会将项目生成的构件安装到本地Maven仓库；
   
   mvn deploy 用来将项目生成的构件分发到远程Maven仓库。
   
   本地Maven仓库的构件只能供当前用户使用，在分发到远程Maven仓库之后，所有能访问该仓库的用户都能使用你的构件。

   我们需要配置POM的distributionManagement来指定Maven分发构件的位置；

   例如 在项目的pom.xml文件中添加如下内容

   需要在maven的安装目录下的 ~/conf/settings.xml 文件中配置远程仓库中的账户和密码

   ```xml
   <servers>
      <server>
         <id>id</id>
         <username>username</username>
         <password>password</password>
      </server>
   </servers>
   ```

   在要远程发布的项目中配置pom.xml文件 添加以下配置
   ```xml
   <!--指定要发布的内容仓库-->
   <distributionManagement>
      <repository>
         <id>id</id>
         <url>http://127.0.0.1:8081/nexus/repository/maven/</url>
      </repository>
   </distributionManagement>

   <plugins>
      <!--发布使用插件-->
      <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-deploy-plugin</artifactId>
            <version>2.8.2</version>
      </plugin>
   </plugins>
   ```

   **注意：**
   
   **1.pom.xml中的 仓库 id 要和 setting.xml 中的用户名和密码的id保持一致**

   **2.idea中的maven的配置可能不是安装包的conf/setting.xml 而是 ${USERPath}/.m2/setting.xml 如 C:\Users\Administrator\.m2\setting.xml ;**
# Java 项目和 docker

- [返回](./README.md)

## springboot 打包 - 发布到 docker

- 创建好普通 springboot 项目 可以单独 发布的项目

- 添加 mvn - docker 插件

  修改 pom.xml 的配置

  在 `<build> <plugins>` 标签下添加下面的插件

  ```xml
  <!--打包docker的插件-->
  <plugin>
      <groupId>com.spotify</groupId>
      <artifactId>docker-maven-plugin</artifactId>
      <version>1.0.0</version>
      <configuration>
      <!-- 在docker运行时要用的，只是一个前缀而已，就像包名一样,可自己任意定义此名称 -->
          <imageName>${docker.image.prefix}/${project.artifactId}</imageName>
          <!--docker docker的Dockerfile文件所在的文件夹位置  不要放到 target中 因为mvn clean 会清理 Dockerfile文件 这个文件需自己创建 -->
          <dockerDirectory>${basedir}/docker</dockerDirectory>
          <!--配置docker读取的jar的位置,运行docker打包命令会自动复制配置好的源码jar包到指定的Dockerfile位置-->
          <resources>
              <resource>
                  <targetPath>/</targetPath>
                  <directory>${project.build.directory}</directory>
                  <include>${project.build.finalName}.jar</include>
              </resource>
          </resources>
      </configuration>
  </plugin>
  ```

- 打包命令
  ```sh
  mvn clean package docker:build -Dmaven.test.skip=true
  ```
- 注意事项

  配置文件中的各个参数可以百度自行理解

  Dockerfile 文件需要和`<dockerDirectory>${basedir}/docker</dockerDirectory>`配置一致,且手动创建 否则会报错

  Dockerfile 文件内容 可自行修改

  ```dockerfile
  #基础镜像文件
  FROM frolvlad/alpine-oraclejdk8:slim
  VOLUME /tmp
  ADD springbootlearingone-1.0-SNAPSHOT.jar app.jar
  ENTRYPOINT ["java","-jar","app.jar"]
  ```

  在实践中，基础镜像可以根据实际情况自己调整 通过一下命令查找基础镜像

  `docker search ***`

  其他内容含义见[Dockerfile_note.md](Dockerfile_note.md)
